using System;
using System.ComponentModel;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;
using ARCed.Database.Tilesets;
using Microsoft.Xna.Framework.Graphics;
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

		private float planeSx, planeSy;
		private int _cx, _cy, _sx, _sy, _zoom, _blendMode;
		private bool _advanced, _mouseDown;
		private Timer _timer;
		private static Texture2D _rectTexture;
		private Image _image;
		private Texture2D _texture;
		private SpriteBatch _batch;
		private Point _originPoint, _endPoint;
		private static XnaColor _blendColor = XnaColor.White;
		private static XnaColor _semiTransparent = new XnaColor(160, 160, 160, 160);

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the image that will be displayed.
		/// </summary>
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
					this.Size = new Size(0, 0);
				}
				else
				{
					_texture = value.ToTexture(GraphicsDevice);
					if (!AdvancedEnabled)
						this.Size = value.Size;
				}
				Invalidate(); 
			}
		}

		/// <summary>
		/// Gets or sets the opacity of the image. Full opacity is used unless 
		/// "AlphaPreview" is true.
		/// </summary>
		[Browsable(false)]
		public int ImageOpacity 
		{
			get { return _blendColor.A; }
			set 
			{
				int opp = 255 - value;
				//_blendColor = new XnaColor(opp, opp, opp, value.Clamp(0, 255));
				//_blendColor = new XnaColor(255, 255, 255, value.Clamp(0, 255)); 
				_blendColor = XnaColor.White * (value / 255.0f);
				Invalidate(); 
			}
		}

		/// <summary>
		/// Gets or sets the flag to show alpha transparency in the preview window.
		/// </summary>
		[Browsable(false)]
		public bool AlphaPreview { get; set; }

		/// <summary>
		/// Gets or sets the speed at which the image scrolls on the X-Axis.
		/// </summary>
		[Browsable(false)]
		public int ScrollX 
		{
			get { return _sx; }
			set { _sx = value; planeSx = value / 8.0f; Invalidate(); }
		}

		/// <summary>
		/// Gets or sets the speed at which the image scrolls on the Y-Axis.
		/// </summary>
		[Browsable(false)]
		public int ScrollY
		{
			get { return _sy; }
			set { _sy = value; planeSy = value / 8.0f;  Invalidate(); }
		}

		/// <summary>
		/// Gets or sets the zoom factor to apply to the image.
		/// </summary>
		[Browsable(false)]
		public int Zoom 
		{
			get { return _zoom; }
			set { _zoom = value; Invalidate(); }
		}

		/// <summary>
		/// Gets or sets the blend mode of the image.
		/// </summary>
		[Browsable(false)]
		public int BlendMode
		{
			get { return _blendMode; }
			set { _blendMode = value; Invalidate(); }
		}

		/// <summary>
		/// Gets or sets the flag to use advanced drawing techniques such as alpha and scrolling.
		/// </summary>
		[Browsable(false)]
		public bool AdvancedEnabled 
		{
			get { return _advanced; }
			set 
			{
				_advanced = value;
				if (value)
				{
					this.Dock = DockStyle.Fill;
					if (_timer == null)
					{
						_timer = new Timer();
						_timer.Tick += new EventHandler(_timer_Tick);
						if (components == null)
						{
							components = new Container();
							this.components.Add(_timer);
						}
					}
					_timer.Interval = 1000 / Constants.FRAMERATE;
					_timer.Start();
				}
				else
				{
					this.Dock = DockStyle.None;
					if (_image != null)
						this.Size = _image.Size;
				}
			}
		}

		/// <summary>
		/// Gets or sets the flag to allow selection of tiles on the image.
		/// </summary>
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
				int sx = Math.Min(_originPoint.X, _endPoint.X).RoundFloor(Constants.TILESIZE);
				int ex = Math.Max(_originPoint.X, _endPoint.X).RoundCeil(Constants.TILESIZE);
				int sy = Math.Min(_originPoint.Y, _endPoint.Y).RoundFloor(Constants.TILESIZE);
				int ey = Math.Max(_originPoint.Y, _endPoint.Y).RoundCeil(Constants.TILESIZE);
				return new XnaRect(Math.Max(0, sx), Math.Max(0, sy),
					Math.Min(Constants.MAXWIDTH, ex - sx + 1), Math.Min(ey - sy, Height) + 1);
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
			_batch = new SpriteBatch(GraphicsDevice);
			GraphicsDevice.Clear(XnaColor.DarkGray);
			_rectTexture = new Texture2D(GraphicsDevice, 1, 1);
			_rectTexture.SetData(new[] { XnaColor.White });
			this.Disposed += new EventHandler(imageSelectXnaPanel_Disposed);
			this.MouseDown += new MouseEventHandler(imageXnaPanel_MouseDown);
			this.MouseUp += new MouseEventHandler(imageXnaPanel_MouseUp);
			this.MouseMove += new MouseEventHandler(imageXnaPanel_MouseMove);
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			if (_texture != null)
			{
				if (AdvancedEnabled)
				{
					_batch.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend,
						SamplerState.LinearWrap, null, null);
					XnaColor color = AlphaPreview ? _blendColor : XnaColor.White;
					GraphicsDevice.Clear(XnaColor.White);
					for (int x = 0; x < Width + _texture.Width; x += _texture.Width)
					{
						for (int y = 0; y < Height + _texture.Height; y += _texture.Height)
						{
							XnaRect destRect =
								new XnaRect(x, y, _texture.Width, _texture.Height);
							XnaRect srcRect = new XnaRect(
								Convert.ToInt32((-_cx - planeSx) / 4), 
								Convert.ToInt32((-_cy - planeSy) / 4), 
								_texture.Width, _texture.Height);
							_batch.Draw(_texture, destRect, srcRect, color);
						}
					}
					_cx %= _texture.Width * 8;
					_cy %= _texture.Height * 8;
				}
				else
				{
					_batch.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend);
					GraphicsDevice.Clear(XnaColor.DarkGray);
					FillRectangle(0, 0, _texture.Width, _texture.Height, XnaColor.White);
					_batch.Draw(_texture, new Vector2(0, 0), XnaColor.White);
				}
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

		private void imageSelectXnaPanel_Disposed(object sender, EventArgs e)
		{
			if (_image != null)
				_image.Dispose();
			if (_texture != null)
				_texture.Dispose();
			_rectTexture.Dispose();
			_batch.Dispose();
		}

		private void _timer_Tick(object sender, EventArgs e)
		{
			if (_texture != null)
			{
				_cx+= _sx;
				_cy+= _sy;
				Invalidate();
			}
		}

		private void ResetPoints()
		{
			_originPoint = _endPoint = new Point(-1, -1);
		}

		private void FillRectangle(int x, int y, int width, int height, XnaColor color)
		{
			Texture2D rectangleTexture = new Texture2D(GraphicsDevice, width, height);
			XnaColor[] colors = Enumerable.Repeat(color, width * height).ToArray();
			rectangleTexture.SetData(colors);
			_batch.Draw(rectangleTexture, new Vector2(x, y), XnaColor.White);
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

		private void imageXnaPanel_MouseMove(object sender, MouseEventArgs e)
		{
			if (SelectionEnabled && _mouseDown)
			{
				_endPoint.X = e.X;
				_endPoint.Y = e.Y;
				Invalidate();
			}
		}

		private void imageXnaPanel_MouseUp(object sender, MouseEventArgs e)
		{
			_mouseDown = false;
		}

		private void imageXnaPanel_MouseDown(object sender, MouseEventArgs e)
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
