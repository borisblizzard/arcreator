using System;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

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

		PictureBox picBox = new PictureBox();
		Image _image;
		private string picturePath = "";
		private bool _selectable;
		private int _x, _y, _tWidth, _tHeight;
		private Pen _innerPen = new Pen(Color.White, 2), _outerPen = new Pen(Color.Black, 4);

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the color used for the outline of the selection rectangle
		/// </summary>
		[Category("ARCed"), Description("Defines the color used for the outline of the selection rectangle.")]
		[DefaultValue(typeof(Color), "Black")]
		public Color SelectorOutlineColor
		{
			get { return _outerPen.Color; }
			set
			{
				if (_outerPen.Color != value)
				{
					_outerPen.Color = value;
					RefreshImage();
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
			get { return _innerPen.Color; }
			set
			{
				if (_innerPen.Color != value)
				{
					_innerPen.Color = value;
					RefreshImage();
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
			get { return _selectable; }
			set { _selectable = value; RefreshImage(); }
		}

		/// <summary>
		/// Gets or sets the background color of the _srcTexture area
		/// </summary>
		[Category("ARCed"), Description("Defines the background color of the image area.")]
		[DefaultValue(typeof(Color), "LightGray")]
		public Color ImageBackColor
		{
			get { return picBox.BackColor; }
			set { picBox.BackColor = value; }
		}

		/// <summary>
		/// Gets or sets the path to the _srcTexture file used in the panel
		/// </summary>
		[Category("ARCed"), Description("Define path to image file.")]
		[Editor(typeof(System.Windows.Forms.Design.FileNameEditor), typeof(System.Drawing.Design.UITypeEditor))]
		[DefaultValue("")]
		public string PictureFile
		{
			get { return picturePath; }
			set
			{
				if (!String.IsNullOrEmpty(value) && File.Exists(value))
				{
					picturePath = value;
					_image = Image.FromFile(value);
					RefreshImage();
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
			get { return new Point(_x, _y); }
			set
			{
				if (_x != value.X || _y != value.Y)
				{
					_x = value.X;
					_y = value.Y;
					RefreshImage();
				}
			}
		}

		/// <summary>
		/// Gets or sets the _srcTexture used in the control
		/// </summary>
		[Category("ARCed"), Description("Set the image used by the control")]
		public Image Image
		{
			get { return _image; }
			set
			{
				_image = value;
				RefreshImage();
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
				Rectangle rect = new Rectangle(_x, _y, _tWidth, _tHeight);
				Image image = new Bitmap(rect.Width, rect.Height);
				using (Graphics g = Graphics.FromImage(image))
					g.DrawImage(_image, rect);
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
            InitializeComponent();
			_selectable = true;
            picBox.Top = 0;
            picBox.Left = 0;
			_x = _y = 0;
			picBox.Visible = false;
            picBox.SizeMode = PictureBoxSizeMode.Normal;
			picBox.BorderStyle = BorderStyle.None;
            Controls.Add(picBox);
			picBox.MouseClick += new MouseEventHandler(picBox_MouseClick);
        }

		#endregion

		#region Private Methods

		private void RefreshImage()
		{
			if (_image != null)
			{
				picBox.Visible = true;
				picBox.Image = new Bitmap(_image);
				picBox.Size = picBox.Image.Size;
				_tWidth = _image.Width / COLUMNS;
				_tHeight = _image.Height / ROWS;

				if (_selectable)
				{
					using (Graphics g = Graphics.FromImage(picBox.Image))
					{
						int x = _x * _tWidth;
						int y = _y * _tHeight;
						g.DrawRectangle(_outerPen, x + 2, y + 2, _tWidth - 4, _tHeight - 4);
						g.DrawRectangle(_innerPen, x + 2, y + 2, _tWidth - 4, _tHeight - 4);
					}
				}
			}
			else
				picBox.Visible = false;
		}

		private void picBox_MouseClick(object sender, MouseEventArgs e)
		{
			Point pnt = picBox.PointToClient(MousePosition);
			if (pnt.X < picBox.Image.Width && pnt.Y < picBox.Image.Height)
			{
				int x = pnt.X / _tWidth;
				int y = pnt.Y / _tHeight;
				if (x != _x || y != _y)
				{
					_x = x;
					_y = y;
					RefreshImage();
				}
			}
		}

		#endregion
	}
}
