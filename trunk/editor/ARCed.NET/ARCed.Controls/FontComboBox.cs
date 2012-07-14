using System;
using System.Collections;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using ARCed.Helpers;
using System.Windows.Forms;

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
				if (index >= -1)
					return Items[index].ToString();
				return null;
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
			Populate();
		}

		public void Populate()
		{
			BeginUpdate();
			Items.Clear();
			ttimg = Resources.TrueType;
			foreach (FontFamily ff in FontHelper.FontCollection.Families)
			{
				if (ff.IsStyleAvailable(FontStyle.Regular))
					Items.Add(ff.Name);
			}
			memFontCount = Items.Count;
			foreach (FontFamily ff in FontFamily.Families)
			{
				if (ff.IsStyleAvailable(FontStyle.Regular))
					Items.Add(ff.Name);
			}
			if (Items.Count > 0)
				SelectedIndex = 0;
			EndUpdate();
		}

		protected override void OnMeasureItem(System.Windows.Forms.MeasureItemEventArgs e)
		{
			if (e.Index > -1)
			{
				int w = 0;
				string fontstring = Items[e.Index].ToString();
				using (Font tempFont = FontHelper.GetFont(fontstring, 10f, FontStyle.Regular))
				{
					e.ItemHeight = (int)e.Graphics.MeasureString(fontstring, tempFont).Height;
					w = (int)e.Graphics.MeasureString(fontstring, tempFont).Width;
					w += ttimg.Width * 2;
					maxwid = Math.Max(w, maxwid);
					e.ItemHeight = Math.Min(20, e.ItemHeight);
				}
				e.Graphics.Dispose();
			}
		}

		protected override void OnDrawItem(System.Windows.Forms.DrawItemEventArgs e)
		{
			if (e.Index > -1)
			{
				string fontString = Items[e.Index].ToString();
				x = e.Bounds.X + ttimg.Width;
				y = e.Bounds.Y;
				width = e.Bounds.Width;
				height = e.Bounds.Height;
				nfont = FontHelper.GetFont(fontString, 10f, FontStyle.Regular);
				if (!DroppedDown)
				{
					e.Graphics.FillRectangle(SystemBrushes.Window, x, y, width, height);
					e.Graphics.DrawString(fontString, nfont, SystemBrushes.WindowText, x * 2, y);
				}
				else if (!e.State.HasFlag(DrawItemState.Focus))
				{
					if (e.Index < memFontCount)
					{
						e.Graphics.FillRectangle(Brushes.PowderBlue, x, y, width, height);
						e.Graphics.DrawString(fontString, nfont, SystemBrushes.WindowText, x * 2, y);
					}
					else
					{
						e.Graphics.FillRectangle(SystemBrushes.Window, x, y, width, height);
						e.Graphics.DrawString(fontString, nfont, SystemBrushes.WindowText, x * 2, y);
					}
				}
				else
				{
					e.Graphics.FillRectangle(SystemBrushes.Highlight, x, y, width, height);
					e.Graphics.DrawString(fontString, nfont, SystemBrushes.HighlightText, x * 2, y);
				}
				e.Graphics.DrawImage(ttimg, new Point(e.Bounds.X, y));
			}
		}

		int x, y, width, height;
		Font nfont;
		int maxwid = 0;
		int memFontCount;
		Image ttimg;

		protected override void OnDropDown(System.EventArgs e)
		{
			this.DropDownWidth = maxwid + 30;
		}
	}
}
