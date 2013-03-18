#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

#endregion

namespace ARCed.Helpers
{
    public static class ControlHelper
    {
        /// <summary>
        /// Clears and fills the control with the given data. 
        /// </summary>
        /// <param name="ctrl">Listbox control to fill</param>
        /// <param name="data">List of data</param>
        /// <param name="none">Flag to fill the first position with "None"</param>
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
        /// <param name="ctrl">Combobox control to fill</param>
        /// <param name="data">List of data</param>
        /// <param name="none">Flag to fill the first position with "None"</param>
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
        /// <param name="picBox"></param>
        /// <param name="text"></param>
        public static void RenderHeaderImage(PictureBox picBox, string text)
        {
            RenderHeaderImage(picBox, text,
                Project.Settings.HeaderImage.Font,
                new SolidBrush(Project.Settings.HeaderImage.TextColor),
                Project.Settings.HeaderImage.GradientLeft,
                Project.Settings.HeaderImage.GradientRight);
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="picBox"></param>
        /// <param name="text"></param>
        /// <param name="font"></param>
        /// <param name="textBrush"></param>
        /// <param name="gradient1"></param>
        /// <param name="gradient2"></param>
        public static void RenderHeaderImage(PictureBox picBox, string text, Font font,
            Brush textBrush, Color gradient1, Color gradient2)
        {
            var rect = new Rectangle(new Point(), picBox.Size);
            var endPoint = new Point(rect.Width, rect.Height);
            if (endPoint.X == 0 || endPoint.Y == 0)
                return;
            Image image = new Bitmap(rect.Width, rect.Height);
            using (var brush =
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
