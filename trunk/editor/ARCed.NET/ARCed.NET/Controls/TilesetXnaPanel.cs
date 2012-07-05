using System;
using System.ComponentModel;
using System.Drawing;
using ARCed.Database.Tilesets;
using System.Linq;
using ARCed.Helpers;
using System.Collections.Generic;
using Microsoft.Xna.Framework.Graphics;
using System.Windows.Forms;
using Vector2 = Microsoft.Xna.Framework.Vector2;
using XnaColor = Microsoft.Xna.Framework.Color;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace ARCed.Controls
{
	public enum TilesetMode
	{
		Passage,
		Passage4Dir,
		Priority,
		Bush,
		Counter,
		Terrain
	}

	/// <summary>
	/// Control for configuring tileset configurations.
	/// </summary>
	public partial class TilesetXnaPanel : GraphicsDeviceControl
	{
		#region Private Fields

		private static int _currentId;
		private static Texture2D _rectTexture;
		private static XnaColor _currentColor;
		RPG.Tileset _tileset;
		Texture2D _tilesetTexture;
		SpriteBatch _batch;
		bool _mouseDown, _ctrlDown;
		TilesetMode _mode = TilesetMode.Passage;
		Point _originPoint, _endPoint;
		private static XnaColor _semiTransparent = new XnaColor(160, 160, 160, 160);

		#endregion

		#region Events

		public delegate void OnSelectHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised whenever the selected status of a sprite is changed.
		/// </summary>
		[Category("ARCed"), Description("Raised whenever the selected status tiles are changed.")]
		public event OnSelectHandler OnSelectionChanged;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the total number of tiles of the current tileset.
		/// </summary>
		[Browsable(false)]
		public int TileCount
		{
			get
			{
				return (Constants.MAXWIDTH / Constants.TILESIZE) * 
				(_tilesetTexture.Height / Constants.TILESIZE); 
			}
		}

		/// <summary>
		/// Gets or sets the current display mode of the tileset editor.
		/// </summary>
		[Browsable(false)]
		public TilesetMode TilesetMode 
		{
			get { return _mode; }
			set { _mode = value; Invalidate(); }
		}

		/// <summary>
		/// Gets the rectangle of the selector
		/// </summary>
		[Browsable(false)]
		public XnaRect SelectionRectangle
		{
			get
			{
				int sx = Math.Min(_originPoint.X, _endPoint.X).RoundFloor(Constants.TILESIZE);
				int ex = Math.Max(_originPoint.X, _endPoint.X).RoundCeil(Constants.TILESIZE);
				int sy = Math.Min(_originPoint.Y, _endPoint.Y).RoundFloor(Constants.TILESIZE);
				int ey = Math.Max(_originPoint.Y, _endPoint.Y).RoundCeil(Constants.TILESIZE);
				return new XnaRect(Math.Max(0, sx), Math.Max(0, sy),
					Math.Min(Constants.MAXWIDTH, ex - sx + 1), Math.Min(ey - sy, Height) + 1);
			}
		}

		/// <summary>
		/// Gets or sets the settings used for drawing on the panel.
		/// </summary>
		[Browsable(false)]
		public ARCed.Settings.TilesetSettings Settings { get; set; }
		
		/// <summary>
		/// Gets or sets the enabled status of batch selection.
		/// </summary>
		[Browsable(false)]
		public bool SelectionEnabled 
		{
			get { return _ctrlDown; }
			set
			{
				_ctrlDown = value;
				if (value)
				{
					ResetPoints();
					Invalidate();
				}
			}
		}


		public RPG.Tileset Tileset
		{
			get { return _tileset; }
			set
			{
				if (value != null)
				{
					_tileset = value;
					Image image = Cache.Tileset(value.tileset_name);
					if (image == null)
					{
						GraphicsDevice.Clear(XnaColor.White);
						_tilesetTexture = null;
						this.Size = new Size(0, 0);
						Refresh();
					}
					else
					{
						_tilesetTexture = image.ToTexture(GraphicsDevice);
						this.Size = image.Size;
						Invalidate();
					}
				}
			}
		}

		#endregion

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public TilesetXnaPanel()
		{
			InitializeComponent();
			ResetPoints();
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Gets the ID of the tile at the specified X and Y.
		/// </summary>
		/// <param name="x">X-coordinate value, in pixels.</param>
		/// <param name="y">Y-coordinate value, in pixels.</param>
		/// <returns>ID of the tile that contains the coordinates.</returns>
		public int GetTileAtPoint(int x, int y)
		{
			int row = x / Constants.TILESIZE;
			int column = y / Constants.TILESIZE;
			return Constants.AUTO_IDS + (row + (column * Constants.TILEWIDTH));
		}

		/// <summary>
		/// Gets the ID of the tile at the specified Point.
		/// </summary>
		/// <param name="point">Coordinates to check, in pixels.</param>
		/// <returns>ID of the tile that contains the coordinates.</returns>
		public int GetTileAtPoint(Point point)
		{
			return GetTileAtPoint(point.X, point.Y);
		}

		#endregion

		#region Protected Methods

		/// <summary>
		/// Creates the context and prepares for drawing
		/// </summary>
		protected override void Initialize()
		{
			IconCache.GraphicsDevice = GraphicsDevice;
			Settings = Editor.Settings.TilesetSettings;
			_batch = new SpriteBatch(GraphicsDevice);
			GraphicsDevice.Clear(XnaColor.Gray);
			_rectTexture = new Texture2D(GraphicsDevice, 1, 1);
			_rectTexture.SetData(new[] { XnaColor.White });
			Disposed += new EventHandler(TroopXnaPanel_Disposed);
			this.MouseDown += new MouseEventHandler(TroopXnaPanel_MouseDown);
			this.MouseUp += new MouseEventHandler(TroopXnaPanel_MouseUp);
			this.MouseMove += new MouseEventHandler(TroopXnaPanel_MouseMove);
			this.MouseLeave += new EventHandler(TilesetXnaPanel_MouseLeave);
			this.MouseEnter += new EventHandler(TilesetXnaPanel_MouseEnter);
		}

		void TilesetXnaPanel_MouseLeave(object sender, EventArgs e)
		{
			_currentId = -1;
			Invalidate();
			Editor.StatusBar.Items[2].Text = "";
		}

		void TilesetXnaPanel_MouseEnter(object sender, EventArgs e)
		{
			Editor.StatusBar.Items[2].Text = "Use mouse buttons to edit. Hold Ctrl to batch select.";
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			if (_tilesetTexture != null)
			{
				GraphicsDevice.Clear(Settings.BackgroundColor);
				_batch.Begin();
				_batch.Draw(_tilesetTexture, new Vector2(0, 0), XnaColor.White);

				if (Settings.ShowGrid)
				{
					int h = _tilesetTexture.Height;
					for (int x = Constants.TILESIZE; x < Constants.MAXWIDTH; x += Constants.TILESIZE)
						_batch.Draw(_rectTexture, new XnaRect(x, 0, 1, h), Settings.GridColor);
					for (int y = Constants.TILESIZE; y < h; y += Constants.TILESIZE)
						_batch.Draw(_rectTexture, new XnaRect(0, y, Constants.MAXWIDTH, 1), Settings.GridColor);
				}
				switch (TilesetMode)
				{
					case TilesetMode.Passage: RefreshPassage(); break;
					case TilesetMode.Passage4Dir: RefreshPassage4Dir(); break;
					case TilesetMode.Priority: RefreshPriority(); break;
					case TilesetMode.Counter: RefreshCounter(); break;
					case TilesetMode.Bush: RefreshBush(); break;
					case TilesetMode.Terrain: RefreshTerrain(); break;
				}
				if (_originPoint != _endPoint)
				{
					XnaRect rect = SelectionRectangle;
					DrawRectangle(rect, XnaColor.Black, 3);
					XnaRect innerRect = new XnaRect(rect.X + 1, rect.Y + 1, 
						rect.Width - 2, rect.Height - 2);
					DrawRectangle(innerRect, Settings.SelectorColor, 1);
				}
				_batch.End();
			}
		}

		#endregion

		#region Private Methods

		private void RefreshPassage()
		{
			int x, y, passage;
			for (int i = Constants.AUTO_IDS; i < Tileset.passages.xsize; i++)
			{
				x = (i - Constants.AUTO_IDS) % Constants.TILEWIDTH * Constants.TILESIZE;
				y = (i - Constants.AUTO_IDS) / Constants.TILEWIDTH * Constants.TILESIZE;
				passage = Tileset.passages[i];
				_currentColor = (_currentId == i) ? XnaColor.White : _semiTransparent;
				_batch.Draw(IconCache.Passage(passage), new Vector2(x, y), _currentColor);
			}
		}

		private void RefreshPassage4Dir()
		{
			int x, y, passage;
			for (int i = Constants.AUTO_IDS; i < Tileset.passages.xsize; i++)
			{
				x = (i - Constants.AUTO_IDS) % Constants.TILEWIDTH * Constants.TILESIZE;
				y = (i - Constants.AUTO_IDS) / Constants.TILEWIDTH * Constants.TILESIZE;
				passage = Tileset.passages[i];
				if (_currentId != i)
					_batch.Draw(IconCache.Passage4Dir(passage), new Vector2(x, y), _semiTransparent);
				else
					_batch.Draw(IconCache.Passage4Dir(passage), new Vector2(x, y), XnaColor.White);
			}
		}

		private void RefreshPriority()
		{
			int x, y, priority;
			for (int i = Constants.AUTO_IDS; i < Tileset.priorities.xsize; i++)
			{
				x = (i - Constants.AUTO_IDS) % Constants.TILEWIDTH * Constants.TILESIZE;
				y = (i - Constants.AUTO_IDS) / Constants.TILEWIDTH * Constants.TILESIZE;
				priority = Tileset.priorities[i];
				_currentColor = (_currentId == i) ? XnaColor.White : _semiTransparent;
				_batch.Draw(IconCache.Priority(priority), new Vector2(x, y), _currentColor);
			}
		}

		private void RefreshBush()
		{
			int x, y, passage;
			for (int i = Constants.AUTO_IDS; i < Tileset.passages.xsize; i++)
			{
				x = (i - Constants.AUTO_IDS) % Constants.TILEWIDTH * Constants.TILESIZE;
				y = (i - Constants.AUTO_IDS) / Constants.TILEWIDTH * Constants.TILESIZE;
				passage = Tileset.passages[i];
				_currentColor = (_currentId == i) ? XnaColor.White : _semiTransparent;
				_batch.Draw(IconCache.Bush(passage), new Vector2(x, y), _currentColor);
			}
		}

		private void RefreshCounter()
		{
			int x, y, passage;
			for (int i = Constants.AUTO_IDS; i < Tileset.passages.xsize; i++)
			{
				x = (i - Constants.AUTO_IDS) % Constants.TILEWIDTH * Constants.TILESIZE;
				y = (i - Constants.AUTO_IDS) / Constants.TILEWIDTH * Constants.TILESIZE;
				passage = Tileset.passages[i];
				_currentColor = (_currentId == i) ? XnaColor.White : _semiTransparent;
				_batch.Draw(IconCache.Counter(passage), new Vector2(x, y), _currentColor);
			}
		}

		private void RefreshTerrain()
		{
			int x, y, terrain;
			for (int i = Constants.AUTO_IDS; i < Tileset.terrain_tags.xsize; i++)
			{
				x = (i - Constants.AUTO_IDS) % Constants.TILEWIDTH * Constants.TILESIZE;
				y = (i - Constants.AUTO_IDS) / Constants.TILEWIDTH * Constants.TILESIZE;
				terrain = Tileset.terrain_tags[i];
				_currentColor = (_currentId == i) ? XnaColor.White : _semiTransparent;
				_batch.Draw(IconCache.Terrain(terrain), new Vector2(x, y), _currentColor);
			}
		}

		private void ResetPoints()
		{
			_originPoint = _endPoint = new Point(-1, -1);
		}

		/// <summary>
		/// Draw a rectangle.
		/// </summary>
		/// <param name="rect">The rectangle to draw.</param>
		/// <param name="color">The draw color.</param>
		/// <param name="border">Thickness of the border, in pixels.</param>
		private void DrawRectangle(XnaRect rect, XnaColor color, int border = 1)
		{
			_batch.Draw(_rectTexture, new XnaRect(rect.Left, rect.Top, rect.Width, border), color);
			_batch.Draw(_rectTexture, new XnaRect(rect.Left, rect.Bottom - border, rect.Width, border), color);
			_batch.Draw(_rectTexture, new XnaRect(rect.Left, rect.Top, border, rect.Height), color);
			_batch.Draw(_rectTexture, new XnaRect(rect.Right - border, rect.Top, border, rect.Height - border), color);
		}

		private void sprite_OnSelectionChanged(object sender, EventArgs e)
		{
			if (OnSelectionChanged != null)
				OnSelectionChanged(sender, e);
		}

		private void TroopXnaPanel_Disposed(object sender, EventArgs e)
		{
			if (_tilesetTexture != null)
				_tilesetTexture.Dispose();
			_rectTexture.Dispose();
			_batch.Dispose();
		}

		private void TroopXnaPanel_MouseMove(object sender, MouseEventArgs e)
		{
			_currentId = GetTileAtPoint(e.X, e.Y);
			if (SelectionEnabled && _mouseDown)
			{
				_endPoint.X = e.X;
				_endPoint.Y = e.Y;
			}
			Invalidate();
		}

		private void TroopXnaPanel_MouseUp(object sender, MouseEventArgs e)
		{
			_mouseDown = false;
		}

		private void TroopXnaPanel_MouseDown(object sender, MouseEventArgs e)
		{
			_mouseDown = true;
			_originPoint.X = _endPoint.X = e.X;
			_originPoint.Y = _endPoint.Y = e.Y;
			if (SelectionEnabled)
				Invalidate();
			else
				ChangeData(e);
		}

		/// <summary>
		/// Performs logic for changing tileset data during mouse events.
		/// </summary>
		/// <param name="e">Mouse event arguments.</param>
		private void ChangeData(MouseEventArgs e)
		{
			if (e.Button != MouseButtons.Left && e.Button != MouseButtons.Right)
				return;
			int id = GetTileAtPoint(e.X, e.Y);
			if (TilesetMode == TilesetMode.Passage)
			{
				if ((_tileset.passages[id] & ~0x40 & ~0x80) == 0)
					_tileset.passages[id] |= 0x01 | 0x02 | 0x04 | 0x08;
				else
					_tileset.passages[id] &= ~(0x01 | 0x02 | 0x04 | 0x08);
			}
			else if (TilesetMode == TilesetMode.Passage4Dir)
			{
				int half = Constants.TILESIZE / 2;
				int x = 1 + e.X % Constants.TILESIZE;
				int y = 1 + e.Y % Constants.TILESIZE;
				List<double> dist = new List<double>
				{
					Math.Pow(half - x, 2) + Math.Pow(Constants.TILESIZE - y, 2), // Bottom
					Math.Pow(x, 2) + Math.Pow(half - y, 2),            // Left
					Math.Pow(Constants.TILESIZE - x, 2) + Math.Pow(half - y, 2), // Right
					Math.Pow(half - x, 2) + Math.Pow(y, 2)             // Top
				};
				int index = dist.IndexOf(dist.Min());
				int bit = new[] { 0x01, 0x02, 0x04, 0x08 }[index];
				if ((_tileset.passages[id] & bit) == bit)
					_tileset.passages[id] &= ~bit;
				else
					_tileset.passages[id] |= bit;
			}
			else if (TilesetMode == TilesetMode.Priority)
			{
				if (e.Button == MouseButtons.Left)
					_tileset.priorities[id] = (_tileset.priorities[id] + 1) % Constants.PRIORITIES;
				else 
				{
					_tileset.priorities[id]--;
					if (_tileset.priorities[id] < 0)
						_tileset.priorities[id] = Constants.PRIORITIES - 1;
				}
			}
			else if (TilesetMode == TilesetMode.Bush)
			{
				if ((_tileset.passages[id] & 0x40) == 0x40)
					_tileset.passages[id] &= ~0x40;
				else
					_tileset.passages[id] |= 0x40;
			}
			else if (TilesetMode == TilesetMode.Counter)
			{
				if ((_tileset.passages[id] & 0x80) == 0x80)
					_tileset.passages[id] &= ~0x80;
				else
					_tileset.passages[id] |= 0x80;
			}
			else if (TilesetMode == TilesetMode.Terrain)
			{
				if (e.Button == MouseButtons.Left)
					_tileset.terrain_tags[id] = (_tileset.terrain_tags[id] + 1) % Constants.TERRAINS;
				else
				{
					_tileset.terrain_tags[id]--;
					if (_tileset.terrain_tags[id] < 0)
						_tileset.terrain_tags[id] = Constants.TERRAINS - 1;
				}
			}
			Invalidate(); 
		}

		#endregion
	}
}
