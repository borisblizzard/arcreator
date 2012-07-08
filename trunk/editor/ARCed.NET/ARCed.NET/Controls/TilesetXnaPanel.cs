using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Windows.Forms;
using ARCed.Database.Tilesets;
using ARCed.Helpers;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Image = System.Drawing.Image;

namespace ARCed.Controls
{
	/// <summary>
	/// Flags used for determining display mode for the tileset panel.
	/// </summary>
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
		private static Color _currentColor;
		private static RPG.Tileset _tileset;
		private static Texture2D _tilesetTexture;
		private static SpriteBatch _batch;
		private static bool _mouseDown, _selectionEnabled, _selectionActive, _displayIcons;
		private static TilesetMode _mode = TilesetMode.Passage;
		private static Point _originPoint, _endPoint;
		private static Color _semiTransparent = Color.White * 0.7f;

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
		public Rectangle SelectionRectangle
		{
			get
			{
				int sx = Math.Min(_originPoint.X, _endPoint.X).RoundFloor(Constants.TILESIZE);
				int ex = Math.Max(_originPoint.X, _endPoint.X).RoundCeil(Constants.TILESIZE);
				int sy = Math.Min(_originPoint.Y, _endPoint.Y).RoundFloor(Constants.TILESIZE);
				int ey = Math.Max(_originPoint.Y, _endPoint.Y).RoundCeil(Constants.TILESIZE);
				return new Rectangle(Math.Max(0, sx), Math.Max(0, sy),
					ex - sx + 1, ey - sy + 1);
			}
		}

		/// <summary>
		/// Gets or sets the settings used for drawing on the panel.
		/// </summary>
		[Browsable(false)]
		public ARCed.Settings.ImageColorSettings Settings
		{ 
			get { return Editor.Settings.ImageColorSettings; } 
		}
		
		/// <summary>
		/// Gets or sets the enabled status of batch selection.
		/// </summary>
		[Browsable(false)]
		public bool SelectionEnabled
		{
			get { return _selectionEnabled; }
			set
			{
				_selectionEnabled = value;
				if (!value)
					ResetPoints();
				Invalidate();
			}
		}

		/// <summary>
		/// Gets or sets the associated tileset of the panel.
		/// </summary>
		[Browsable(false)]
		public RPG.Tileset Tileset
		{
			get { return _tileset; }
			set
			{
				ResetPoints();
				if (value != null)
				{
					_tileset = value;
					Image image = Cache.Tileset(value.tileset_name);
					if (image == null)
					{
						GraphicsDevice.Clear(Color.White);
						_tilesetTexture = null;
						this.Size = System.Drawing.Size.Empty;
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

		/// <summary>
		/// Gets the IDs of all tiles that are within the selection rectangle.
		/// </summary>
		[Browsable(false)]
		public List<int> SelectedTileIds
		{
			get
			{
				Rectangle rect = SelectionRectangle;
				rect.Width--;
				rect.Height--;
				int size = (rect.Width / Constants.TILESIZE) * (rect.Height / Constants.TILESIZE);
				if (size > 0)
				{
					List<int> tiles = new List<int>(size);
					for (int x = rect.X; x < rect.X + rect.Width; x += Constants.TILESIZE)
					{
						for (int y = rect.Y; y < rect.Y + rect.Height; y += Constants.TILESIZE)
						{
							tiles.Add(GetTileAtPoint(x, y));
						}
					}
					return tiles;
				}
				return new List<int>();
			}
		}

		/// <summary>
		/// Gets or sets the flag to draw the icon overlay on the panel.
		/// </summary>
		[Browsable(false)]
		public bool DisplayIcons
		{
			get { return _displayIcons; }
			set { _displayIcons = value; Invalidate(); }
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

		public Vector2 GetTileVector(int tileId)
		{
			int x = (tileId - Constants.AUTO_IDS) % Constants.TILEWIDTH * Constants.TILESIZE;
			int y = (tileId - Constants.AUTO_IDS) / Constants.TILEWIDTH * Constants.TILESIZE;
			return new Vector2(x, y);
		}

		#endregion

		#region Protected Methods

		/// <summary>
		/// Creates the context and prepares for drawing
		/// </summary>
		protected override void Initialize()
		{
			IconCache.GraphicsDevice = GraphicsDevice;
			_batch = new SpriteBatch(GraphicsDevice);
			
			_displayIcons = true;
			GraphicsDevice.Clear(Color.Gray);
			Disposed += new EventHandler(TroopXnaPanel_Disposed);
			this.MouseDown += new MouseEventHandler(TroopXnaPanel_MouseDown);
			this.MouseUp += new MouseEventHandler(TroopXnaPanel_MouseUp);
			this.MouseMove += new MouseEventHandler(TroopXnaPanel_MouseMove);
			this.MouseLeave += new EventHandler(TilesetXnaPanel_MouseLeave);
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			GraphicsDevice.Clear(Settings.BackgroundColor);
			if (_tilesetTexture != null)
			{
				_batch.Begin();
				_batch.Draw(_tilesetTexture, new Vector2(0, 0), Color.White);

				if (Settings.ShowGrid)
				{
					int h = _tilesetTexture.Height;
					for (int x = Constants.TILESIZE; x < Constants.MAXWIDTH; x += Constants.TILESIZE)
						_batch.DrawRectangle(new Rectangle(x, 0, 1, h), Settings.GridColor);
					for (int y = Constants.TILESIZE; y < h; y += Constants.TILESIZE)
						_batch.DrawRectangle(new Rectangle(0, y, Constants.MAXWIDTH, 1), Settings.GridColor);
				}
				if (_displayIcons)
				{
					switch (TilesetMode)
					{
						case TilesetMode.Passage: RefreshPassage(); break;
						case TilesetMode.Passage4Dir: RefreshPassage4Dir(); break;
						case TilesetMode.Priority: RefreshPriority(); break;
						case TilesetMode.Counter: RefreshCounter(); break;
						case TilesetMode.Bush: RefreshBush(); break;
						case TilesetMode.Terrain: RefreshTerrain(); break;
					}
				}
				if (SelectionEnabled && _originPoint != _endPoint)
					_batch.DrawSelectionRect(SelectionRectangle, Settings.SelectorColor, 2);
				_batch.End();
			}
		}

		#endregion

		#region Private Methods

		#region Icon Refreshing

		private void RefreshPassage()
		{
			int passage;
			for (int i = Constants.AUTO_IDS; i < Tileset.passages.xsize; i++)
			{
				passage = Tileset.passages[i];
				_currentColor = (_currentId == i) ? Color.White : _semiTransparent;
				_batch.Draw(IconCache.Passage(passage), GetTileVector(i), _currentColor);
			}
		}

		private void RefreshPassage4Dir()
		{
			int passage;
			for (int i = Constants.AUTO_IDS; i < Tileset.passages.xsize; i++)
			{
				passage = Tileset.passages[i];
				if (_currentId != i)
					_batch.Draw(IconCache.Passage4Dir(passage), GetTileVector(i), _semiTransparent);
				else
					_batch.Draw(IconCache.Passage4Dir(passage), GetTileVector(i), Color.White);
			}
		}

		private void RefreshPriority()
		{
			int priority;
			for (int i = Constants.AUTO_IDS; i < Tileset.priorities.xsize; i++)
			{
				priority = Tileset.priorities[i];
				_currentColor = (_currentId == i) ? Color.White : _semiTransparent;
				_batch.Draw(IconCache.Priority(priority), GetTileVector(i), _currentColor);
			}
		}

		private void RefreshBush()
		{
			int passage;
			for (int i = Constants.AUTO_IDS; i < Tileset.passages.xsize; i++)
			{
				passage = Tileset.passages[i];
				_currentColor = (_currentId == i) ? Color.White : _semiTransparent;
				_batch.Draw(IconCache.Bush(passage), GetTileVector(i), _currentColor);
			}
		}

		private void RefreshCounter()
		{
			int passage;
			for (int i = Constants.AUTO_IDS; i < Tileset.passages.xsize; i++)
			{
				passage = Tileset.passages[i];
				_currentColor = (_currentId == i) ? Color.White : _semiTransparent;
				_batch.Draw(IconCache.Counter(passage), GetTileVector(i), _currentColor);
			}
		}

		private void RefreshTerrain()
		{
			int terrain;
			for (int i = Constants.AUTO_IDS; i < Tileset.terrain_tags.xsize; i++)
			{
				terrain = Tileset.terrain_tags[i];
				_currentColor = (_currentId == i) ? Color.White : _semiTransparent;
				_batch.Draw(IconCache.Terrain(terrain), GetTileVector(i), _currentColor);
			}
		}

		#endregion

		private void ResetPoints()
		{
			_originPoint = _endPoint = new Point(-1, -1);
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
			_batch.Dispose();
		}

		#region Mouse Events

		private void TroopXnaPanel_MouseMove(object sender, MouseEventArgs e)
		{
			if (_tilesetTexture != null)
			{
				int x = e.X.Clamp(0, _tilesetTexture.Width);
				int y = e.Y.Clamp(0, _tilesetTexture.Height);
				_currentId = GetTileAtPoint(x, y);
				if (SelectionEnabled && _mouseDown && _selectionActive)
				{
					_endPoint.X = x;
					_endPoint.Y = y;
				}
				Invalidate();
			}
		}

		private void TroopXnaPanel_MouseUp(object sender, MouseEventArgs e)
		{
			_mouseDown = false;
			_selectionActive = false;
		}

		private void TroopXnaPanel_MouseDown(object sender, MouseEventArgs e)
		{
			_mouseDown = true;
			if (SelectionEnabled && _originPoint.X < 0 && _originPoint.Y < 0)
			{
				_originPoint.X = _endPoint.X = e.X;
				_originPoint.Y = _endPoint.Y = e.Y;
				_selectionActive = true;
				Invalidate();
			}
			else if (!SelectionEnabled)
				ChangeData(e);
			else if (SelectionRectangle.Contains(e.X, e.Y))
			{
				foreach (int id in SelectedTileIds)
				{
					Vector2 vector = GetTileVector(id);
					ChangeData(new MouseEventArgs(e.Button, 1, 
						(int)vector.X + (e.X % Constants.TILESIZE),
						(int)vector.Y + (e.Y % Constants.TILESIZE), 
						0));
				}
			}
		}

		private void TilesetXnaPanel_MouseLeave(object sender, EventArgs e)
		{
			_currentId = -1;
			Invalidate();
		}

		#endregion

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
