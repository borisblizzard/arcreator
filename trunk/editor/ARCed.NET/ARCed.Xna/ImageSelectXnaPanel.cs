#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Point = System.Drawing.Point;
using XnaColor = Microsoft.Xna.Framework.Color;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Control for configuring tileset configurations.
	/// </summary>
	public partial class ImageSelectXnaPanel : GraphicsDeviceControl
	{
		#region Private Fields

		private float planeSx, planeSy;
		private int _cx, _cy, _sx, _sy, _zoom, _blendMode, _opacity;
		private bool _advanced, _mouseDown, _alphaPreview;
		private Timer _timer;
		private Image _image;
		private Texture2D _texture;
		private SpriteBatch _batch;
		private Point _originPoint, _endPoint;

		private static XnaColor _blendColor;
		private static XnaColor _backColor;

		private static BlendState _subBlend;
		private static BlendState _addBlend;

		#endregion

		#region Public Properties

		public BlendState CurrentBlendState
		{
			get
			{
				switch (this._blendMode)
				{
					case 1: return _addBlend;
					case 2: return _subBlend;
					default: return BlendState.AlphaBlend;
				}
			}
		}

		/// <summary>
		/// Gets or sets the background color in the image preview.
		/// </summary>
		[Browsable(false)]
		public XnaColor ImageBackColor
		{
			get { return _backColor; }
			set { _backColor = value; Invalidate(); }
		}

		/// <summary>
		/// Gets or sets the image that will be displayed.
		/// </summary>
		[Browsable(false)]
		public Image Image 
		{
			get { return this._image; }
			set 
			{
				this._image = value; 
				if (value == null)
				{
					this._texture = null;
					Size = new Size(0, 0);
				}
				else
				{
					this._texture = value.ToTexture(GraphicsDevice);
					if (!this.AdvancedEnabled)
						Size = value.Size;
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
			get { return this._opacity; }
			set 
			{
				this._opacity = value;
				if (this._alphaPreview)
				{
					_blendColor = XnaColor.White * (value / 255.0f);
					Invalidate();
				}
			}
		}

		/// <summary>
		/// Gets or sets the flag to show alpha transparency in the preview window.
		/// </summary>
		[Browsable(false)]
		public bool AlphaPreview 
		{
			get { return this._alphaPreview; }
			set
			{
				this._alphaPreview = value;
				_blendColor = value ? XnaColor.White * (this._opacity / 255.0f) : XnaColor.White;
				Invalidate();
			}
		}

		/// <summary>
		/// Gets or sets the speed at which the image scrolls on the X-Axis.
		/// </summary>
		[Browsable(false)]
		public int ScrollX 
		{
			get { return this._sx; }
			set { this._sx = value; this.planeSx = value / 8.0f; Invalidate(); }
		}

		/// <summary>
		/// Gets or sets the speed at which the image scrolls on the Y-Axis.
		/// </summary>
		[Browsable(false)]
		public int ScrollY
		{
			get { return this._sy; }
			set { this._sy = value; this.planeSy = value / 8.0f;  Invalidate(); }
		}

		/// <summary>
		/// Gets or sets the zoom factor to apply to the image.
		/// </summary>
		[Browsable(false)]
		public int Zoom 
		{
			get { return this._zoom; }
			set { this._zoom = value; Invalidate(); }
		}

		/// <summary>
		/// Gets or sets the blend mode of the image.
		/// </summary>
		[Browsable(false)]
		public int BlendMode
		{
			get { return this._blendMode; }
			set { this._blendMode = value; Invalidate(); }
		}

		/// <summary>
		/// Gets or sets the flag to use advanced drawing techniques such as alpha and scrolling.
		/// </summary>
		[Browsable(false)]
		public bool AdvancedEnabled 
		{
			get { return this._advanced; }
			set 
			{
				this._advanced = value;
				if (value)
				{
					Dock = DockStyle.Fill;
					if (this._timer == null)
					{
						this._timer = new Timer();
						this._timer.Tick += this._timer_Tick;
						if (this.components == null)
						{
							this.components = new Container();
							this.components.Add(this._timer);
						}
					}
					this._timer.Interval = 1000 / Constants.FRAMERATE;
					this._timer.Start();
				}
				else
				{
					Dock = DockStyle.None;
					if (this._image != null)
						Size = this._image.Size;
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
				int sx = Math.Min(this._originPoint.X, this._endPoint.X).RoundFloor(Constants.TILESIZE);
				int ex = Math.Max(this._originPoint.X, this._endPoint.X).RoundCeil(Constants.TILESIZE);
				int sy = Math.Min(this._originPoint.Y, this._endPoint.Y).RoundFloor(Constants.TILESIZE);
				int ey = Math.Max(this._originPoint.Y, this._endPoint.Y).RoundCeil(Constants.TILESIZE);
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
			this.InitializeComponent();
			this.ResetPoints();
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
			return this.GetTileAtPoint(point.X, point.Y);
		}

		#endregion

		#region Protected Methods

		/// <summary>
		/// Creates the context and prepares for drawing
		/// </summary>
		protected override void Initialize()
		{
			_addBlend = new BlendState
			{
				ColorDestinationBlend = Blend.One,
				ColorSourceBlend = Blend.One,
				AlphaDestinationBlend = Blend.One,
				AlphaSourceBlend = Blend.One,
				ColorBlendFunction = BlendFunction.Add,
				AlphaBlendFunction = BlendFunction.Add
			};
			_subBlend = new BlendState
			{
				ColorSourceBlend = Blend.InverseBlendFactor,
				ColorDestinationBlend = Blend.One | Blend.InverseSourceColor,
				ColorBlendFunction = BlendFunction.Add,
				AlphaSourceBlend = Blend.InverseBlendFactor,
				AlphaDestinationBlend = Blend.One | Blend.InverseSourceAlpha,
				AlphaBlendFunction = BlendFunction.Add
			};
            _backColor = XnaColor.White;
			IconCache.GraphicsDevice = GraphicsDevice;
			this._batch = new SpriteBatch(GraphicsDevice);
			GraphicsDevice.Clear(XnaColor.DarkGray);
			Disposed += this.imageSelectXnaPanel_Disposed;
			MouseDown += this.imageXnaPanel_MouseDown;
			MouseUp += this.imageXnaPanel_MouseUp;
			MouseMove += this.imageXnaPanel_MouseMove;
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			GraphicsDevice.Clear(XnaColor.DarkGray);
			if (this._texture != null)
			{
				GraphicsDevice.Clear(_backColor);
				if (this.AdvancedEnabled)
				{
					this._batch.Begin(SpriteSortMode.Immediate, this.CurrentBlendState,
						SamplerState.LinearWrap, null, null);
					int zw = this._texture.Width;
					int zh = this._texture.Height;
					XnaRect destRect, srcRect;
					if (this._zoom > 100)
					{
						float factor = this._zoom / 100.0f;
						zw = (int)(zw * factor);
						zh = (int)(zh * factor);
					}
					for (int x = 0; x < Width + zw; x += zw)
					{
						for (int y = 0; y < Height + zh; y += zh)
						{
							destRect = new XnaRect(x, y, zw, zh);
							srcRect = new XnaRect(
								Convert.ToInt32((-this._cx - this.planeSx) / 4), 
								Convert.ToInt32((-this._cy - this.planeSy) / 4), 
								this._texture.Width, this._texture.Height);
							this._batch.Draw(this._texture, destRect, srcRect, _blendColor);
						}
					}
					this._cx %= this._texture.Width * 8;
					this._cy %= this._texture.Height * 8;
				}
				else
				{
					this._batch.Begin();
					this._batch.FillRectangle(0, 0, this._texture.Width, this._texture.Height, _backColor);
					this._batch.End();
					this._batch.Begin(SpriteSortMode.Immediate, this.CurrentBlendState);
					this._batch.Draw(this._texture, new Vector2(0, 0), _blendColor);
				}

				if (this._originPoint != this._endPoint)
					this._batch.DrawSelectionRect(this.SelectionRectangle, XnaColor.White, 2);
				this._batch.End();
			}
		}

		#endregion

		#region Private Methods

		private void imageSelectXnaPanel_Disposed(object sender, EventArgs e)
		{
			if (this._image != null)
				this._image.Dispose();
			if (this._texture != null)
				this._texture.Dispose();
			this._batch.Dispose();
		}

		private void _timer_Tick(object sender, EventArgs e)
		{
			if (this._texture != null)
			{
				this._cx+= this._sx;
				this._cy+= this._sy;
				Invalidate();
			}
		}

		private void ResetPoints()
		{
			this._originPoint = this._endPoint = new Point(-1, -1);
		}

		private void imageXnaPanel_MouseMove(object sender, MouseEventArgs e)
		{
			if (this.SelectionEnabled && this._mouseDown)
			{
				this._endPoint.X = e.X;
				this._endPoint.Y = e.Y;
				Invalidate();
			}
		}

		private void imageXnaPanel_MouseUp(object sender, MouseEventArgs e)
		{
			this._mouseDown = false;
		}

		private void imageXnaPanel_MouseDown(object sender, MouseEventArgs e)
		{
			this._mouseDown = true;
			this._originPoint.X = this._endPoint.X = e.X;
			this._originPoint.Y = this._endPoint.Y = e.Y;
			if (this.SelectionEnabled)
				Invalidate();
		}

		#endregion
	}
}
