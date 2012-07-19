#region Using Directives

using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.UI
{
    partial class DockPane
    {
        private class SplitterControl : Control, ISplitterDragSource
        {
            private readonly DockPane _mPane;

            public SplitterControl(DockPane pane)
            {
                SetStyle(ControlStyles.Selectable, false);
                this._mPane = pane;
            }

            public DockPane DockPane
            {
                get { return this._mPane; }
            }

            private DockAlignment m_alignment;
            public DockAlignment Alignment
            {
                get { return this.m_alignment; }
                set
                {
                    this.m_alignment = value;
                    if (this.m_alignment == DockAlignment.Left || this.m_alignment == DockAlignment.Right)
                        Cursor = Cursors.VSplit;
                    else if (this.m_alignment == DockAlignment.Top || this.m_alignment == DockAlignment.Bottom)
                        Cursor = Cursors.HSplit;
                    else
                        Cursor = Cursors.Default;

                    if (this.DockPane.DockState == DockState.Document)
                        Invalidate();
                }
            }

            protected override void OnPaint(PaintEventArgs e)
            {
                base.OnPaint(e);

                if (this.DockPane.DockState != DockState.Document)
                    return;

                Graphics g = e.Graphics;
                Rectangle rect = ClientRectangle;
                if (this.Alignment == DockAlignment.Top || this.Alignment == DockAlignment.Bottom)
                    g.DrawLine(SystemPens.ControlDark, rect.Left, rect.Bottom - 1, rect.Right, rect.Bottom - 1);
                else if (this.Alignment == DockAlignment.Left || this.Alignment == DockAlignment.Right)
                    g.DrawLine(SystemPens.ControlDarkDark, rect.Right - 1, rect.Top, rect.Right - 1, rect.Bottom);
            }

            protected override void OnMouseDown(MouseEventArgs e)
            {
                base.OnMouseDown(e);

                if (e.Button != MouseButtons.Left)
                    return;

                this.DockPane.DockPanel.BeginDrag(this, Parent.RectangleToScreen(Bounds));
            }

            #region ISplitterDragSource Members

            void ISplitterDragSource.BeginDrag(Rectangle rectSplitter)
            {
            }

            void ISplitterDragSource.EndDrag()
            {
            }

            bool ISplitterDragSource.IsVertical
            {
                get
                {
                    NestedDockingStatus status = this.DockPane.NestedDockingStatus;
                    return (status.DisplayingAlignment == DockAlignment.Left ||
                        status.DisplayingAlignment == DockAlignment.Right);
                }
            }

            Rectangle ISplitterDragSource.DragLimitBounds
            {
                get
                {
                    NestedDockingStatus status = this.DockPane.NestedDockingStatus;
                    Rectangle rectLimit = Parent.RectangleToScreen(status.LogicalBounds);
                    if (((ISplitterDragSource)this).IsVertical)
                    {
                        rectLimit.X += MeasurePane.MinSize;
                        rectLimit.Width -= 2 * MeasurePane.MinSize;
                    }
                    else
                    {
                        rectLimit.Y += MeasurePane.MinSize;
                        rectLimit.Height -= 2 * MeasurePane.MinSize;
                    }

                    return rectLimit;
                }
            }

            void ISplitterDragSource.MoveSplitter(int offset)
            {
                NestedDockingStatus status = this.DockPane.NestedDockingStatus;
                double proportion = status.Proportion;
                if (status.LogicalBounds.Width <= 0 || status.LogicalBounds.Height <= 0)
                    return;
                else if (status.DisplayingAlignment == DockAlignment.Left)
                    proportion += (offset) / (double)status.LogicalBounds.Width;
                else if (status.DisplayingAlignment == DockAlignment.Right)
                    proportion -= (offset) / (double)status.LogicalBounds.Width;
                else if (status.DisplayingAlignment == DockAlignment.Top)
                    proportion += (offset) / (double)status.LogicalBounds.Height;
                else
                    proportion -= (offset) / (double)status.LogicalBounds.Height;

                this.DockPane.SetNestedDockingProportion(proportion);
            }

            #region IDragSource Members

            Control IDragSource.DragControl
            {
                get { return this; }
            }

            #endregion

            #endregion
        }

        private SplitterControl m_splitter;
        private SplitterControl Splitter
        {
            get { return this.m_splitter; }
        }

        internal Rectangle SplitterBounds
        {
            set { this.Splitter.Bounds = value; }
        }

        internal DockAlignment SplitterAlignment
        {
            set { this.Splitter.Alignment = value; }
        }
    }
}