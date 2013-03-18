#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

namespace ARCed.Controls
{
	public class FontComboBox : ComboBox
	{
		/// <summary>
		/// Gets the name of the selected font family
		/// </summary>
		[Browsable(false)]
		public string SelectedFontFamily
		{
			get
			{
				int index = SelectedIndex;
				return index >= -1 ? Items[index].ToString() : null;
			}
			set { SelectedIndex = Math.Max(FindStringExact(value), 0); }
		}

		public FontComboBox()
		{
			MaxDropDownItems = 20;
			IntegralHeight = false;
			Sorted = false;
			DropDownStyle = ComboBoxStyle.DropDownList;
			DrawMode = DrawMode.OwnerDrawVariable;
			this.Populate();
		}

		public void Populate()
		{
			BeginUpdate();
			Items.Clear();
			this._ttimg = Resources.TrueType;
			foreach (FontFamily ff in FontHelper.FontCollection.Families)
			{
				if (ff.IsStyleAvailable(FontStyle.Regular))
					Items.Add(ff.Name);
			}
			this._memFontCount = Items.Count;
			foreach (FontFamily ff in FontFamily.Families)
			{
				if (ff.IsStyleAvailable(FontStyle.Regular))
					Items.Add(ff.Name);
			}
			if (Items.Count > 0)
				SelectedIndex = 0;
			EndUpdate();
		}

		protected override void OnMeasureItem(MeasureItemEventArgs e)
		{
			if (e.Index > -1)
			{
				int w = 0;
				string fontstring = Items[e.Index].ToString();
				using (Font tempFont = FontHelper.GetFont(fontstring, 10f, FontStyle.Regular))
				{
					e.ItemHeight = (int)e.Graphics.MeasureString(fontstring, tempFont).Height;
					w = (int)e.Graphics.MeasureString(fontstring, tempFont).Width;
					w += this._ttimg.Width * 2;
					this._maxwid = Math.Max(w, this._maxwid);
					e.ItemHeight = Math.Min(20, e.ItemHeight);
				}
				e.Graphics.Dispose();
			}
		}

		protected override void OnDrawItem(DrawItemEventArgs e)
		{
			if (e.Index > -1)
			{
				string fontString = Items[e.Index].ToString();
				this._x = e.Bounds.X + this._ttimg.Width;
				this._y = e.Bounds.Y;
				this._width = e.Bounds.Width;
				this._height = e.Bounds.Height;
				this._nfont = FontHelper.GetFont(fontString, 10f, FontStyle.Regular);
				if (!DroppedDown)
				{
					e.Graphics.FillRectangle(SystemBrushes.Window, this._x, this._y, this._width, this._height);
					e.Graphics.DrawString(fontString, this._nfont, SystemBrushes.WindowText, this._x * 2, this._y);
				}
				else if (!e.State.HasFlag(DrawItemState.Focus))
				{
					if (e.Index < this._memFontCount)
					{
						e.Graphics.FillRectangle(Brushes.PowderBlue, this._x, this._y, this._width, this._height);
						e.Graphics.DrawString(fontString, this._nfont, SystemBrushes.WindowText, this._x * 2, this._y);
					}
					else
					{
						e.Graphics.FillRectangle(SystemBrushes.Window, this._x, this._y, this._width, this._height);
						e.Graphics.DrawString(fontString, this._nfont, SystemBrushes.WindowText, this._x * 2, this._y);
					}
				}
				else
				{
					e.Graphics.FillRectangle(SystemBrushes.Highlight, this._x, this._y, this._width, this._height);
					e.Graphics.DrawString(fontString, this._nfont, SystemBrushes.HighlightText, this._x * 2, this._y);
				}
				e.Graphics.DrawImage(this._ttimg, new Point(e.Bounds.X, this._y));
			}
		}

        private int _x, _y, _width, _height;
        private Font _nfont;
	    private int _maxwid;
		int _memFontCount;
        private Image _ttimg;

		protected override void OnDropDown(EventArgs e)
		{
			DropDownWidth = this._maxwid + 30;
		}
	}
}
