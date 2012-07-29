using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ARCed.Helpers;

namespace ARCed.Controls
{
	public sealed partial class MapSourceSelectorPanel : PictureBox
	{
		#region Private Fields

		private RPG.Tileset _tileset;
		private Point _originPoint, _endPoint;
		private Rectangle _selectRect;
		private Image _srcImage;
		private bool _mouseDown, _selectionActive;

		private static Pen _innerPen = new Pen(Color.White, 2);
		private static Pen _outterPen = new Pen(Color.Black, 4);

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the <see cref="Rectangle"/> of the selector.
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
		/// Gets or sets the current <see cref="RPG.Tileset"/> displayed in the control.
		/// </summary>
		[Browsable(false)]
		public RPG.Tileset Tileset
		{
			get { return _tileset; }
			set { SetTileset(value); }
		}

		#endregion

		/// <summary>
		/// Creates and returns a new instance of a <see cref="MapSourceSelectorPanel"/> object.
		/// </summary>
		public MapSourceSelectorPanel()
		{
			InitializeComponent();
			ResetPoints();
		}

		#region Private Methods

		private void ResetPoints()
		{
			_originPoint = _endPoint = new Point(-1, -1);
		}

		private void RefreshSelection() 
		{ 
			Rectangle rect = SelectionRectangle;
			if (_selectRect != rect)
			{
				_selectRect = rect;
				using (Graphics g = Graphics.FromImage(Image))
				{
					g.Clear(Color.White);
					g.DrawImageUnscaled(_srcImage, 0, 0);
					g.DrawRectangle(_outterPen, rect);
					g.DrawRectangle(_innerPen, rect);
				}
				Invalidate();
			}
		}

		private void SetTileset(RPG.Tileset tileset)
		{
			_tileset = tileset;
			if (_tileset == null)
			{
				Image = null;
				return;
			}
			_srcImage = Cache.Tileset(_tileset.tileset_name);
			Image = new Bitmap(_srcImage);
			Size = Image.Size;
		}

		private void PictureBoxTilesetMouseDown(object sender, MouseEventArgs e)
		{
			_mouseDown = true;
			ResetPoints();
			if (_originPoint.X < 0 && _originPoint.Y < 0)
			{
				_originPoint.X = _endPoint.X = e.X;
				_originPoint.Y = _endPoint.Y = e.Y;
				_selectionActive = true;
				RefreshSelection();
			}
		}

		private void PictureBoxTilesetMouseUp(object sender, MouseEventArgs e)
		{
			_mouseDown = false;
			_selectionActive = false;
		}

		private void PictureBoxTilesetMouseMove(object sender, MouseEventArgs e)
		{
			if (Image != null)
			{
				int x = e.X.Clamp(0, Image.Width);
				int y = e.Y.Clamp(0, Image.Height);
				if (_mouseDown && _selectionActive)
				{
					_endPoint.X = x;
					_endPoint.Y = y;
				}
				this.RefreshSelection();
			}
		}

		#endregion
	}
}
