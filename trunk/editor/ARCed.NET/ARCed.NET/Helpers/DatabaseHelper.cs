using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;
using ARCed.Database;
using ARCed.Dialogs;

namespace ARCed.Helpers
{
	public static class DatabaseHelper
	{
		/// <summary>
		/// Clears and fills the control with the given data. 
		/// </summary>
		/// <param _frames="ctrl">Listbox control to fill</param>
		/// <param _frames="data">List of data</param>
		/// <param _frames="none">Flag to fill the first position with "None"</param>
		/// <remarks>Painting is suspended until after items have been added</remarks>
		public static void Populate(ListBox ctrl, IList<dynamic> data, bool none) 
		{
			ctrl.BeginUpdate();
			ctrl.Items.Clear();
			if (none)
				ctrl.Items.Add("<None>");
			for (int i = 1; i < data.Count; i++)
				ctrl.Items.Add(data[i].ToString());
			ctrl.EndUpdate();
		}

		/// <summary>
		/// Clears and fills the control with the given data. 
		/// </summary>
		/// <param _frames="ctrl">Combobox control to fill</param>
		/// <param _frames="data">List of data</param>
		/// <param _frames="none">Flag to fill the first position with "None"</param>
		/// <remarks>Painting is suspended until after items have been added</remarks>
		public static void Populate(ComboBox ctrl, IList<dynamic> data, bool none) 
		{
			ctrl.BeginUpdate();
			ctrl.Items.Clear();
			if (none)
				ctrl.Items.Add("<None>");
			for (int i = 1; i < data.Count; i++)
				ctrl.Items.Add(data[i].ToString()); 
			ctrl.EndUpdate();
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param _frames="picBox"></param>
		/// <param _frames="text"></param>
		public static void RenderHeaderImage(PictureBox picBox, string text)
		{
			RenderHeaderImage(picBox, text,
				Editor.Settings.HeaderImage.Font,
				new SolidBrush(Editor.Settings.HeaderImage.TextColor),
				Editor.Settings.HeaderImage.GradientLeft,
				Editor.Settings.HeaderImage.GradientRight);
		}

		/// <summary>
		/// 
		/// </summary>
		/// <param _frames="picBox"></param>
		/// <param _frames="text"></param>
		/// <param _frames="font"></param>
		/// <param _frames="textBrush"></param>
		/// <param _frames="gradient1"></param>
		/// <param _frames="gradient2"></param>
		public static void RenderHeaderImage(PictureBox picBox, string text, Font font,
			Brush textBrush, Color gradient1, Color gradient2)
		{
			Rectangle rect = new Rectangle(new Point(), picBox.Size);
			Point endPoint = new Point(rect.Width, rect.Height);
			if (endPoint.X == 0 || endPoint.Y == 0)
				return;
			Image image = new Bitmap(rect.Width, rect.Height);
			using (LinearGradientBrush brush =
				new LinearGradientBrush(rect.Location, endPoint, gradient1, gradient2))
			{
				using (Graphics g = Graphics.FromImage(image))
				{
					g.Clear(Color.Black);
					g.FillRectangle(brush, rect);
					SizeF size = g.MeasureString(text, font);
					float x = (rect.Width - size.Width) / 2;
					float y = (rect.Height - size.Height) / 2;
					g.DrawString(text, font, textBrush, x, y);
				}
			}
			if (picBox.Image != null)
			{
				picBox.Image.Dispose();
				picBox.Image = null;
			}
			picBox.Image = image;
		}


		public static string GetMapLabel(int id)
		{
			return String.Format("{0:d4}: {1}", id, Project.Data.MapInfos[id].name);
		}
	}
}
