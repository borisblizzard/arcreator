using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using ARCed.Helpers;
using Microsoft.Xna.Framework.Graphics;
using ARCed.Database.Tilesets;
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

	public enum Passages
	{
		None = 0x00,
		CannotMoveDown = 0x01,
		CannotMoveLeft = 0x02,
		CannotMoveRight = 0x04,
		CannotMoveUp = 0x08,
		BushFlag = 0x40,
		CounterFlag = 0x80,
		All = 0x01 | 0x02 | 0x04 | 0x08
	}


	/// <summary>
	/// Control for configuring Troop layouts
	/// </summary>
	public partial class TilesetXnaPanel : GraphicsDeviceControl
	{
		#region Private Fields

		private const int TILESIZE = 32;
		private const int MAXWIDTH = 256;
		private const int TILEWIDTH = 8;
		private const int AUTOPASSAGES = 384;

		private static Texture2D _rectTexture;
		private static XnaColor _hiddenColor;
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
			get { return (MAXWIDTH / TILESIZE) * (_tilesetTexture.Height / TILESIZE); }
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
				int sx = Math.Min(_originPoint.X, _endPoint.X).RoundFloor(TILESIZE);
				int ex = Math.Max(_originPoint.X, _endPoint.X).RoundCeil(TILESIZE);
				int sy = Math.Min(_originPoint.Y, _endPoint.Y).RoundFloor(TILESIZE);
				int ey = Math.Max(_originPoint.Y, _endPoint.Y).RoundCeil(TILESIZE);

				return new XnaRect(sx, sy, ex - sx + 1, ey - sy + 1);
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
				_tileset = value;
				Image image = Cache.Tileset(value.tileset_name);
				_tilesetTexture = image.ToTexture(GraphicsDevice);
				this.Size = image.Size;
				Invalidate();
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
			_hiddenColor = new XnaColor(80, 80, 80, 60); ;
			Disposed += new EventHandler(TroopXnaPanel_Disposed);
			this.MouseDown += new System.Windows.Forms.MouseEventHandler(TroopXnaPanel_MouseDown);
			this.MouseUp += new System.Windows.Forms.MouseEventHandler(TroopXnaPanel_MouseUp);
			this.MouseMove += new System.Windows.Forms.MouseEventHandler(TroopXnaPanel_MouseMove);
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
					for (int x = TILESIZE; x < MAXWIDTH; x += TILESIZE)
						_batch.Draw(_rectTexture, new XnaRect(x, 0, 1, h), Settings.GridColor);
					for (int y = TILESIZE; y < h; y += TILESIZE)
						_batch.Draw(_rectTexture, new XnaRect(0, y, MAXWIDTH, 1), Settings.GridColor);
				}
				// *************************************************************
				if (TilesetMode == TilesetMode.Passage)
					RefreshPassage();
				else if (TilesetMode == TilesetMode.Passage4Dir)
					RefreshPassage4Dir();
				else if (TilesetMode == TilesetMode.Priority)
					RefreshPriority();
				else if (TilesetMode == TilesetMode.Counter)
					RefreshCounter();
				else if (TilesetMode == TilesetMode.Bush)
					RefreshBush();
				else if (TilesetMode == TilesetMode.Terrain)
					RefreshTerrain();

				// *************************************************************
				XnaRect rect = SelectionRectangle;
				if (rect != XnaRect.Empty)
				{
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
			int x, y;
			XnaRect rect;
			int passage;
			for (int i = AUTOPASSAGES; i < Tileset.passages.xsize; i++)
			{
				x = (i - AUTOPASSAGES) % TILEWIDTH * TILESIZE;
				y = (i - AUTOPASSAGES) / TILEWIDTH * TILESIZE;
				rect = new XnaRect(x, y, 32, 32);
				passage = Tileset.passages[i];
				_batch.Draw(IconCache.Passage(passage), new Vector2(x, y), _semiTransparent);
			}
		}

		private void RefreshPassage4Dir()
		{
			int x, y;
			XnaRect rect;
			int passage;
			for (int i = AUTOPASSAGES; i < Tileset.passages.xsize; i++)
			{
				x = (i - AUTOPASSAGES) % TILEWIDTH * TILESIZE;
				y = (i - AUTOPASSAGES) / TILEWIDTH * TILESIZE;
				rect = new XnaRect(x, y, 32, 32);
				passage = Tileset.passages[i];
				_batch.Draw(IconCache.Passage4Dir(passage), new Vector2(x, y), _semiTransparent);
			}
		}

		private void RefreshPriority()
		{
			int x, y;
			XnaRect rect;
			int priority;
			for (int i = AUTOPASSAGES; i < Tileset.priorities.xsize; i++)
			{
				x = (i - AUTOPASSAGES) % TILEWIDTH * TILESIZE;
				y = (i - AUTOPASSAGES) / TILEWIDTH * TILESIZE;
				rect = new XnaRect(x, y, 32, 32);
				priority = Tileset.priorities[i];
				_batch.Draw(IconCache.Priority(priority), new Vector2(x, y), _semiTransparent);
			}
		}

		private void RefreshBush()
		{
			int x, y;
			XnaRect rect;
			int passage;
			for (int i = AUTOPASSAGES; i < Tileset.passages.xsize; i++)
			{
				x = (i - AUTOPASSAGES) % TILEWIDTH * TILESIZE;
				y = (i - AUTOPASSAGES) / TILEWIDTH * TILESIZE;
				rect = new XnaRect(x, y, 32, 32);
				passage = Tileset.passages[i];
				_batch.Draw(IconCache.Bush(passage), new Vector2(x, y), _semiTransparent);
			}
		}

		private void RefreshCounter()
		{
			int x, y;
			XnaRect rect;
			int passage;
			for (int i = AUTOPASSAGES; i < Tileset.passages.xsize; i++)
			{
				x = (i - AUTOPASSAGES) % TILEWIDTH * TILESIZE;
				y = (i - AUTOPASSAGES) / TILEWIDTH * TILESIZE;
				rect = new XnaRect(x, y, 32, 32);
				passage = Tileset.passages[i];
				_batch.Draw(IconCache.Counter(passage), new Vector2(x, y), _semiTransparent);
			}
		}

		private void RefreshTerrain()
		{
			int x, y;
			XnaRect rect;
			int terrain;
			for (int i = AUTOPASSAGES; i < Tileset.terrain_tags.xsize; i++)
			{
				x = (i - AUTOPASSAGES) % TILEWIDTH * TILESIZE;
				y = (i - AUTOPASSAGES) / TILEWIDTH * TILESIZE;
				rect = new XnaRect(x, y, 32, 32);
				terrain = Tileset.terrain_tags[i];
				_batch.Draw(IconCache.Terrain(terrain), new Vector2(x, y), _semiTransparent);
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
			
		}

		private void TroopXnaPanel_MouseMove(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			if (SelectionEnabled && _mouseDown)
			{
				_endPoint.X = e.X;
				_endPoint.Y = e.Y;
				Invalidate();
			}
		}

		private void TroopXnaPanel_MouseUp(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			_mouseDown = false;

		}

		private void TroopXnaPanel_MouseDown(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			_mouseDown = true;
			_originPoint.X = _endPoint.X = e.X;
			_originPoint.Y = _endPoint.Y = e.Y;
			if (SelectionEnabled)
				Invalidate();
		}






		#endregion
	}
}
