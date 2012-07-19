#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Drawing.Design;
using System.IO;
using System.Windows.Forms;
using System.Windows.Forms.Design;

#endregion

namespace ARCed.Controls
{
    /// <summary>
	/// PictureBox control with automatic scroll functions.
    /// </summary>
	[Description("PictureBox control with automatic scroll functions.")]
	[ToolboxBitmap(typeof(PictureBox))]
    public partial class CharSelectionControl : Panel
	{
		#region Constants

		const int COLUMNS = 4;
		const int ROWS = 4;

		#endregion

		#region Private Fields

        readonly PictureBox picBox = new PictureBox();
		Image _image;
		private string _picturePath = "";
		private bool _selectable;
		private int _x, _y, _tWidth, _tHeight;
		private readonly Pen _innerPen = new Pen(Color.White, 2);
        private readonly Pen _outerPen = new Pen(Color.Black, 4);

        #endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the color used for the outline of the selection rectangle
		/// </summary>
		[Category("ARCed"), Description("Defines the color used for the outline of the selection rectangle.")]
		[DefaultValue(typeof(Color), "Black")]
		public Color SelectorOutlineColor
		{
			get { return this._outerPen.Color; }
			set
			{
				if (this._outerPen.Color != value)
				{
					this._outerPen.Color = value;
					this.RefreshImage();
				}
			}
		}

		/// <summary>
		/// Gets or sets the inner color used for the selection rectangle
		/// </summary>
		[Category("ARCed"), Description("Defines the color used for the inner portion of the selection rectangle.")]
		[DefaultValue(typeof(Color), "White")]
		public Color SelectorInnerColor
		{
			get { return this._innerPen.Color; }
			set
			{
				if (this._innerPen.Color != value)
				{
					this._innerPen.Color = value;
					this.RefreshImage();
				}
			}
		}

		/// <summary>
		/// Gets or sets the property to enable the selection of individual tiles
		/// </summary>
		[Category("ARCed"), Description("Defines the property that allows ability to select individual tiles.")]
		[DefaultValue(true)]
		public bool SelectionEnabled
		{
			get { return this._selectable; }
			set { this._selectable = value; this.RefreshImage(); }
		}

		/// <summary>
		/// Gets or sets the background color of the _srcTexture area
		/// </summary>
		[Category("ARCed"), Description("Defines the background color of the image area.")]
		[DefaultValue(typeof(Color), "LightGray")]
		public Color ImageBackColor
		{
			get { return this.picBox.BackColor; }
			set { this.picBox.BackColor = value; }
		}

		/// <summary>
		/// Gets or sets the path to the _srcTexture file used in the panel
		/// </summary>
		[Category("ARCed"), Description("Define path to image file.")]
		[Editor(typeof(FileNameEditor), typeof(UITypeEditor))]
		[DefaultValue("")]
		public string PictureFile
		{
			get { return this._picturePath; }
			set
			{
				if (!String.IsNullOrEmpty(value) && File.Exists(value))
				{
					this._picturePath = value;
					this._image = Image.FromFile(value);
					this.RefreshImage();
				}
			}
		}

		/// <summary>
		/// Gets or sets the coordinate relative to tiles of the selected tile
		/// </summary>
		[Category("ARCed"), Description("Sets the initial coordinate of the tile selection rectangle")]
		[DefaultValue(typeof(Point), "0, 0")]
		public Point SelectionCoordinate
		{
			get { return new Point(this._x, this._y); }
			set
			{
				if (this._x != value.X || this._y != value.Y)
				{
					this._x = value.X;
					this._y = value.Y;
					this.RefreshImage();
				}
			}
		}

		/// <summary>
		/// Gets or sets the _srcTexture used in the control
		/// </summary>
		[Category("ARCed"), Description("Set the image used by the control")]
		public Image Image
		{
			get { return this._image; }
			set
			{
				this._image = value;
				this.RefreshImage();
			}
		}

		/// <summary>
		/// Gets a image copied from the main _srcTexture file that was contained in the selection rectangle
		/// </summary>
		[Browsable(false)]
		public Image SelectionImage
		{
			get
			{
				var rect = new Rectangle(this._x, this._y, this._tWidth, this._tHeight);
				Image image = new Bitmap(rect.Width, rect.Height);
				using (Graphics g = Graphics.FromImage(image))
					g.DrawImage(this._image, rect);
				return image;
			}
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor.
		/// </summary>
        public CharSelectionControl()
        {
            this.InitializeComponent();
			this._selectable = true;
            this.picBox.Top = 0;
            this.picBox.Left = 0;
			this._x = this._y = 0;
			this.picBox.Visible = false;
            this.picBox.SizeMode = PictureBoxSizeMode.Normal;
			this.picBox.BorderStyle = BorderStyle.None;
            Controls.Add(this.picBox);
			this.picBox.MouseClick += this.picBox_MouseClick;
        }

		#endregion

		#region Private Methods

		private void RefreshImage()
		{
			if (this._image != null)
			{
				this.picBox.Visible = true;
				this.picBox.Image = new Bitmap(this._image);
				this.picBox.Size = this.picBox.Image.Size;
				this._tWidth = this._image.Width / COLUMNS;
				this._tHeight = this._image.Height / ROWS;

				if (this._selectable)
				{
					using (Graphics g = Graphics.FromImage(this.picBox.Image))
					{
						int x = this._x * this._tWidth;
						int y = this._y * this._tHeight;
						g.DrawRectangle(this._outerPen, x + 2, y + 2, this._tWidth - 4, this._tHeight - 4);
						g.DrawRectangle(this._innerPen, x + 2, y + 2, this._tWidth - 4, this._tHeight - 4);
					}
				}
			}
			else
				this.picBox.Visible = false;
		}

		private void picBox_MouseClick(object sender, MouseEventArgs e)
		{
			Point pnt = this.picBox.PointToClient(MousePosition);
			if (pnt.X < this.picBox.Image.Width && pnt.Y < this.picBox.Image.Height)
			{
				int x = pnt.X / this._tWidth;
				int y = pnt.Y / this._tHeight;
				if (x != this._x || y != this._y)
				{
					this._x = x;
					this._y = y;
					this.RefreshImage();
				}
			}
		}

		#endregion
	}
}
