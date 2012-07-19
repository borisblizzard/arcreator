#region Using Directives

using System.Drawing;

#endregion

namespace ARCed.UI
{
    partial class DockPanel
    {
        private sealed class SplitterDragHandler : DragHandler
        {
            private class SplitterOutline
            {
                public SplitterOutline()
                {
                    this._mDragForm = new DragForm();
                    this.SetDragForm(Rectangle.Empty);
                    this.DragForm.BackColor = Color.Black;
                    this.DragForm.Opacity = 0.7;
                    this.DragForm.Show(false);
                }

                readonly DragForm _mDragForm;
                private DragForm DragForm
                {
                    get { return this._mDragForm; }
                }

                public void Show(Rectangle rect)
                {
                    this.SetDragForm(rect);
                }

                public void Close()
                {
                    this.DragForm.Close();
                }

                private void SetDragForm(Rectangle rect)
                {
                    this.DragForm.Bounds = rect;
                    if (rect == Rectangle.Empty)
                        this.DragForm.Region = new Region(Rectangle.Empty);
                    else if (this.DragForm.Region != null)
                        this.DragForm.Region = null;
                }
            }

            public SplitterDragHandler(DockPanel dockPanel)
                : base(dockPanel)
            {
            }

            public new ISplitterDragSource DragSource
            {
                get { return base.DragSource as ISplitterDragSource; }
                private set { base.DragSource = value; }
            }

            private SplitterOutline m_outline;
            private SplitterOutline Outline
            {
                get { return this.m_outline; }
                set { this.m_outline = value; }
            }

            private Rectangle m_rectSplitter;
            private Rectangle RectSplitter
            {
                get { return this.m_rectSplitter; }
                set { this.m_rectSplitter = value; }
            }

            public void BeginDrag(ISplitterDragSource dragSource, Rectangle rectSplitter)
            {
                this.DragSource = dragSource;
                this.RectSplitter = rectSplitter;

                if (!BeginDrag())
                {
                    this.DragSource = null;
                    return;
                }

                this.Outline = new SplitterOutline();
                this.Outline.Show(rectSplitter);
                this.DragSource.BeginDrag(rectSplitter);
            }

            protected override void OnDragging()
            {
                this.Outline.Show(this.GetSplitterOutlineBounds(MousePosition));
            }

            protected override void OnEndDrag(bool abort)
            {
                DockPanel.SuspendLayout(true);

                this.Outline.Close();

                if (!abort)
                    this.DragSource.MoveSplitter(this.GetMovingOffset(MousePosition));

                this.DragSource.EndDrag();
                DockPanel.ResumeLayout(true, true);
            }

            private int GetMovingOffset(Point ptMouse)
            {
                Rectangle rect = this.GetSplitterOutlineBounds(ptMouse);
                if (this.DragSource.IsVertical)
                    return rect.X - this.RectSplitter.X;
                else
                    return rect.Y - this.RectSplitter.Y;
            }

            private Rectangle GetSplitterOutlineBounds(Point ptMouse)
            {
                Rectangle rectLimit = this.DragSource.DragLimitBounds;

                Rectangle rect = this.RectSplitter;
                if (rectLimit.Width <= 0 || rectLimit.Height <= 0)
                    return rect;

                if (this.DragSource.IsVertical)
                {
                    rect.X += ptMouse.X - StartMousePosition.X;
                    rect.Height = rectLimit.Height;
                }
                else
                {
                    rect.Y += ptMouse.Y - StartMousePosition.Y;
                    rect.Width = rectLimit.Width;
                }

                if (rect.Left < rectLimit.Left)
                    rect.X = rectLimit.X;
                if (rect.Top < rectLimit.Top)
                    rect.Y = rectLimit.Y;
                if (rect.Right > rectLimit.Right)
                    rect.X -= rect.Right - rectLimit.Right;
                if (rect.Bottom > rectLimit.Bottom)
                    rect.Y -= rect.Bottom - rectLimit.Bottom;

                return rect;
            }
        }

        private SplitterDragHandler m_splitterDragHandler;
        private SplitterDragHandler GetSplitterDragHandler()
        {
            if (this.m_splitterDragHandler == null)
                this.m_splitterDragHandler = new SplitterDragHandler(this);
            return this.m_splitterDragHandler;
        }

        internal void BeginDrag(ISplitterDragSource dragSource, Rectangle rectSplitter)
        {
            this.GetSplitterDragHandler().BeginDrag(dragSource, rectSplitter);
        }
    }
}
