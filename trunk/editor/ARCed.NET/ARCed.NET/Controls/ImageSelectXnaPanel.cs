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
	/// <summary>
	/// Control for configuring tileset configurations.
	/// </summary>
	public partial class ImageSelectXnaPanel : GraphicsDeviceControl
	{
		#region Private Fields

		private const int TILESIZE = 32;
		private const int MAXWIDTH = 256;
		private const int TILEWIDTH = 8;
		private const int AUTO_IDS = 384;


		private int _sx, _sy, _zoom, _blendMode;

		private static Texture2D _rectTexture;
		Image _image;
		Texture2D _texture;
		SpriteBatch _batch;
		bool _mouseDown;
		Point _originPoint, _endPoint;
		private static XnaColor _semiTransparent = new XnaColor(160, 160, 160, 160);

		#endregion

		#region Public Properties

		[Browsable(false)]
		public Image Image 
		{
			get { return _image; }
			set 
			{
				_image = value; 
				if (value == null)
				{
					_texture = null;
					this.Size = Size.Empty;
				}
				else
				{
					_texture = value.ToTexture(GraphicsDevice);
					this.Size = value.Size;
				}
				Invalidate(); 
			}
		}

		[Browsable(false)]
		public int ScrollX 
		{
			get { return _sx; }
			set { _sx = value; Invalidate(); }
		}

		[Browsable(false)]
		public int ScrollY
		{
			get { return _sy; }
			set { _sy = value; Invalidate(); }
		}

		[Browsable(false)]
		public int Zoom 
		{
			get { return _zoom; }
			set { _zoom = value; Invalidate(); }
		}

		[Browsable(false)]
		public int BlendMode
		{
			get { return _blendMode; }
			set { _blendMode = value; Invalidate(); }
		}

		[Browsable(false)]
		public bool SelectionEnabled { get; set; }

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
				return new XnaRect(Math.Max(0, sx), Math.Max(0, sy), 
					Math.Min(MAXWIDTH, ex - sx + 1), Math.Min(ey - sy, Height) + 1);
			}
		}

		#endregion

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public ImageSelectXnaPanel()
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
			int row = x / TILESIZE;
			int column = y / TILESIZE;
			return AUTO_IDS + (row + (column * TILEWIDTH));
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
			_batch = new SpriteBatch(GraphicsDevice);
			GraphicsDevice.Clear(XnaColor.Gray);
			_rectTexture = new Texture2D(GraphicsDevice, 1, 1);
			_rectTexture.SetData(new[] { XnaColor.White });
			this.MouseDown += new MouseEventHandler(TroopXnaPanel_MouseDown);
			this.MouseUp += new MouseEventHandler(TroopXnaPanel_MouseUp);
			this.MouseMove += new MouseEventHandler(TroopXnaPanel_MouseMove);
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			if (_texture != null)
			{
				GraphicsDevice.Clear(XnaColor.DarkGray);
				_batch.Begin();
				_batch.Draw(_texture, new Vector2(0, 0), XnaColor.White);

				if (_originPoint != _endPoint)
				{
					XnaRect rect = SelectionRectangle;
					DrawRectangle(rect, XnaColor.Black, 3);
					XnaRect innerRect = new XnaRect(rect.X + 1, rect.Y + 1, 
						rect.Width - 2, rect.Height - 2);
					DrawRectangle(innerRect, XnaColor.White, 1);
				}
				_batch.End();
			}
		}

		#endregion

		#region Private Methods

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

		private void TroopXnaPanel_MouseMove(object sender, MouseEventArgs e)
		{
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
		}

		public void UpdateScroll()
		{
			if (_sx != 0 || _sy != 0)
			{

			}
		}

		#endregion
	}
}
