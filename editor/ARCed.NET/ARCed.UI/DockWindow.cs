#region Using Directives

using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.UI
{
	[ToolboxItem(false)]
	public partial class DockWindow : Panel, INestedPanesContainer, ISplitterDragSource
	{
        private readonly DockPanel _mDockPanel;
        private readonly DockState _mDockState;
        private readonly SplitterControl _mSplitter;
        private readonly NestedPaneCollection _mNestedPanes;

		internal DockWindow(DockPanel dockPanel, DockState dockState)
		{
			this._mNestedPanes = new NestedPaneCollection(this);
			this._mDockPanel = dockPanel;
			this._mDockState = dockState;
			Visible = false;

			SuspendLayout();

			if (this.DockState == DockState.DockLeft || this.DockState == DockState.DockRight ||
				this.DockState == DockState.DockTop || this.DockState == DockState.DockBottom)
			{
				this._mSplitter = new SplitterControl();
				Controls.Add(this._mSplitter);
			}

			if (this.DockState == DockState.DockLeft)
			{
				Dock = DockStyle.Left;
				this._mSplitter.Dock = DockStyle.Right;
			}
			else if (this.DockState == DockState.DockRight)
			{
				Dock = DockStyle.Right;
				this._mSplitter.Dock = DockStyle.Left;
			}
			else if (this.DockState == DockState.DockTop)
			{
				Dock = DockStyle.Top;
				this._mSplitter.Dock = DockStyle.Bottom;
			}
			else if (this.DockState == DockState.DockBottom)
			{
				Dock = DockStyle.Bottom;
				this._mSplitter.Dock = DockStyle.Top;
			}
			else if (this.DockState == DockState.Document)
			{
				Dock = DockStyle.Fill;
			}

			ResumeLayout();
		}

		public VisibleNestedPaneCollection VisibleNestedPanes
		{
			get	{	return this.NestedPanes.VisibleNestedPanes;	}
		}

		public NestedPaneCollection NestedPanes
		{
			get	{	return this._mNestedPanes;	}
		}

		public DockPanel DockPanel
		{
			get	{	return this._mDockPanel;	}
		}

		public DockState DockState
		{
			get	{	return this._mDockState;	}
		}

		public bool IsFloat
		{
			get	{	return this.DockState == DockState.Float;	}
		}

		internal DockPane DefaultPane
		{
			get	{	return this.VisibleNestedPanes.Count == 0 ? null : this.VisibleNestedPanes[0];	}
		}

		public virtual Rectangle DisplayingRectangle
		{
			get
			{
				Rectangle rect = ClientRectangle;
				// if DockWindow is document, exclude the border
				if (this.DockState == DockState.Document)
				{
					rect.X += 1;
					rect.Y += 1;
					rect.Width -= 2;
					rect.Height -= 2;
				}
				// exclude the splitter
				else if (this.DockState == DockState.DockLeft)
					rect.Width -= Measures.SplitterSize;
				else if (this.DockState == DockState.DockRight)
				{
					rect.X += Measures.SplitterSize;
					rect.Width -= Measures.SplitterSize;
				}
				else if (this.DockState == DockState.DockTop)
					rect.Height -= Measures.SplitterSize;
				else if (this.DockState == DockState.DockBottom)
				{
					rect.Y += Measures.SplitterSize;
					rect.Height -= Measures.SplitterSize;
				}

				return rect;
			}
		}

		protected override void OnPaint(PaintEventArgs e)
		{
			// if DockWindow is document, draw the border
            if (this.DockState == DockState.Document)
                e.Graphics.DrawRectangle(SystemPens.ControlDark, ClientRectangle.X, ClientRectangle.Y, ClientRectangle.Width - 1, ClientRectangle.Height - 1);

			base.OnPaint(e);
		}

		protected override void OnLayout(LayoutEventArgs levent)
		{
			this.VisibleNestedPanes.Refresh();
			if (this.VisibleNestedPanes.Count == 0)
			{
                if (Visible)
                    Visible = false;
			}
			else if (!Visible)
			{
				Visible = true;
				this.VisibleNestedPanes.Refresh();
			}

			base.OnLayout (levent);
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
            get { return (this.DockState == DockState.DockLeft || this.DockState == DockState.DockRight); }
        }

        Rectangle ISplitterDragSource.DragLimitBounds
        {
            get
            {
                Rectangle rectLimit = this.DockPanel.DockArea;
                Point location;
                if ((ModifierKeys & Keys.Shift) == 0)
                    location = Location;
                else
                    location = this.DockPanel.DockArea.Location;

                if (((ISplitterDragSource)this).IsVertical)
                {
                    rectLimit.X += MeasurePane.MinSize;
                    rectLimit.Width -= 2 * MeasurePane.MinSize;
                    rectLimit.Y = location.Y;
                    if ((ModifierKeys & Keys.Shift) == 0)
                        rectLimit.Height = Height;
                }
                else
                {
                    rectLimit.Y += MeasurePane.MinSize;
                    rectLimit.Height -= 2 * MeasurePane.MinSize;
                    rectLimit.X = location.X;
                    if ((ModifierKeys & Keys.Shift) == 0)
                        rectLimit.Width = Width;
                }

                return this.DockPanel.RectangleToScreen(rectLimit);
            }
        }

        void ISplitterDragSource.MoveSplitter(int offset)
        {
            if ((ModifierKeys & Keys.Shift) != 0)
                SendToBack();

            Rectangle rectDockArea = this.DockPanel.DockArea;
            if (this.DockState == DockState.DockLeft && rectDockArea.Width > 0)
            {
                if (this.DockPanel.DockLeftPortion > 1)
                    this.DockPanel.DockLeftPortion = Width + offset;
                else
                    this.DockPanel.DockLeftPortion += (offset) / (double)rectDockArea.Width;
            }
            else if (this.DockState == DockState.DockRight && rectDockArea.Width > 0)
            {
                if (this.DockPanel.DockRightPortion > 1)
                    this.DockPanel.DockRightPortion = Width - offset;
                else
                    this.DockPanel.DockRightPortion -= (offset) / (double)rectDockArea.Width;
            }
            else if (this.DockState == DockState.DockBottom && rectDockArea.Height > 0)
            {
                if (this.DockPanel.DockBottomPortion > 1)
                    this.DockPanel.DockBottomPortion = Height - offset;
                else
                    this.DockPanel.DockBottomPortion -= (offset) / (double)rectDockArea.Height;
            }
            else if (this.DockState == DockState.DockTop && rectDockArea.Height > 0)
            {
                if (this.DockPanel.DockTopPortion > 1)
                    this.DockPanel.DockTopPortion = Height + offset;
                else
                    this.DockPanel.DockTopPortion += (offset) / (double)rectDockArea.Height;
            }
        }

        #region IDragSource Members

        Control IDragSource.DragControl
        {
            get { return this; }
        }

        #endregion
        #endregion
    }
}
