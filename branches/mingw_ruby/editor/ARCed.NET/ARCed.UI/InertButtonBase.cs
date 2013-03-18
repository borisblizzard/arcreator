#region Using Directives

using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Windows.Forms;

#endregion

namespace ARCed.UI
{
    internal abstract class InertButtonBase : Control
    {
        protected InertButtonBase()
        {
            SetStyle(ControlStyles.SupportsTransparentBackColor, true);
            BackColor = Color.Transparent;
        }

        public abstract Bitmap Image
        {
            get;
        }

        private bool m_isMouseOver;
        protected bool IsMouseOver
        {
            get { return this.m_isMouseOver; }
            private set
            {
                if (this.m_isMouseOver == value)
                    return;

                this.m_isMouseOver = value;
                Invalidate();
            }
        }

        protected override Size DefaultSize
        {
            get { return Resources.DockPane_Close.Size; }
        }

        protected override void OnMouseMove(MouseEventArgs e)
        {
            base.OnMouseMove(e);
            bool over = ClientRectangle.Contains(e.X, e.Y);
            if (this.IsMouseOver != over)
                this.IsMouseOver = over;
        }

        protected override void OnMouseEnter(EventArgs e)
        {
            base.OnMouseEnter(e);
            if (!this.IsMouseOver)
                this.IsMouseOver = true;
        }

        protected override void OnMouseLeave(EventArgs e)
        {
            base.OnMouseLeave(e);
            if (this.IsMouseOver)
                this.IsMouseOver = false;
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            if (this.IsMouseOver && Enabled)
            {
                using (var pen = new Pen(ForeColor))
                {
                    e.Graphics.DrawRectangle(pen, Rectangle.Inflate(ClientRectangle, -1, -1));
                }
            }

            using (var imageAttributes = new ImageAttributes())
            {
                var colorMap = new ColorMap[2];
                colorMap[0] = new ColorMap
                {
                    OldColor = Color.FromArgb(0, 0, 0),
                    NewColor = ForeColor
                };
                colorMap[1] = new ColorMap
                {
                    OldColor = this.Image.GetPixel(0, 0),
                    NewColor = Color.Transparent
                };

                imageAttributes.SetRemapTable(colorMap);

                e.Graphics.DrawImage(
                   this.Image,
                   new Rectangle(0, 0, this.Image.Width, this.Image.Height),
                   0, 0,
                   this.Image.Width,
                   this.Image.Height,
                   GraphicsUnit.Pixel,
                   imageAttributes);
            }

            base.OnPaint(e);
        }

        public void RefreshChanges()
        {
            if (IsDisposed)
                return;

            bool mouseOver = ClientRectangle.Contains(PointToClient(MousePosition));
            if (mouseOver != this.IsMouseOver)
                this.IsMouseOver = mouseOver;

            this.OnRefreshChanges();
        }

        protected virtual void OnRefreshChanges()
        {
        }
    }
}
