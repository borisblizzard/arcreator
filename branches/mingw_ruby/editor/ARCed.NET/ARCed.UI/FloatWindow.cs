#region Using Directives

using System;
using System.Diagnostics.CodeAnalysis;
using System.Drawing;
using System.Security.Permissions;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed.UI
{
	public class FloatWindow : Form, INestedPanesContainer, IDockDragSource
	{
		private NestedPaneCollection m_nestedPanes;
		internal const int WM_CHECKDISPOSE = (int)(Msgs.WM_USER + 1);

		internal protected FloatWindow(DockPanel dockPanel, DockPane pane)
		{
			this.InternalConstruct(dockPanel, pane, false, Rectangle.Empty);
		}

		internal protected FloatWindow(DockPanel dockPanel, DockPane pane, Rectangle bounds)
		{
			this.InternalConstruct(dockPanel, pane, true, bounds);
		}

		private void InternalConstruct(DockPanel dockPanel, DockPane pane, bool boundsSpecified, Rectangle bounds)
		{

			if (dockPanel == null)
				throw(new ArgumentNullException(Strings.FloatWindow_Constructor_NullDockPanel));

			this.m_nestedPanes = new NestedPaneCollection(this);

			FormBorderStyle = FormBorderStyle.SizableToolWindow;
			ShowInTaskbar = false;
            if (dockPanel.RightToLeft != RightToLeft)
                RightToLeft = dockPanel.RightToLeft;
            if (RightToLeftLayout != dockPanel.RightToLeftLayout)
                RightToLeftLayout = dockPanel.RightToLeftLayout;
			
			SuspendLayout();

            if (!boundsSpecified)
            {
                Bounds = bounds;
                StartPosition = FormStartPosition.Manual;
            }
            else
            {
                StartPosition = FormStartPosition.WindowsDefaultLocation;
            }

			if (pane != null)
				pane.FloatWindow = this;

			this.m_dockPanel = dockPanel;
			Owner = this.DockPanel.FindForm();

			Size = bounds.Size;
			// Suspend child controls from resizing every pixel
			ResizeBegin += (s, e) => SuspendLayout();
			ResizeEnd += (s, e) => ResumeLayout(true);

			this.DockPanel.AddFloatWindow(this);

			ResumeLayout();
		}

		protected override void Dispose(bool disposing)
		{
			if (disposing)
			{
				if (this.DockPanel != null)
					this.DockPanel.RemoveFloatWindow(this);
				this.m_dockPanel = null;
			}
			base.Dispose(disposing);
		}

		private bool m_allowEndUserDocking = true;
		public bool AllowEndUserDocking
		{
			get	{	return this.m_allowEndUserDocking;	}
			set	{	this.m_allowEndUserDocking = value;	}
		}

		public NestedPaneCollection NestedPanes
		{
			get	{	return this.m_nestedPanes;	}
		}

		public VisibleNestedPaneCollection VisibleNestedPanes
		{
			get	{	return this.NestedPanes.VisibleNestedPanes;	}
		}

		private DockPanel m_dockPanel;
		public DockPanel DockPanel
		{
			get	{	return this.m_dockPanel;	}
		}

		public DockState DockState
		{
			get	{	return DockState.Float;	}
		}
	
		public bool IsFloat
		{
			get	{	return this.DockState == DockState.Float;	}
		}

		internal bool IsDockStateValid(DockState dockState)
		{
			foreach (DockPane pane in this.NestedPanes)
				foreach (IDockContent content in pane.Contents)
					if (!DockHelper.IsDockStateValid(dockState, content.DockHandler.DockAreas))
						return false;

			return true;
		}

		protected override void OnActivated(EventArgs e)
		{
			this.DockPanel.FloatWindows.BringWindowToFront(this);
			base.OnActivated (e);
			// Propagate the Activated event to the visible panes content objects
			foreach (DockPane pane in this.VisibleNestedPanes)
				foreach (IDockContent content in pane.Contents)
					content.OnActivated(e);
		}

		protected override void OnDeactivate(EventArgs e)
		{
			base.OnDeactivate(e);
			// Propagate the Deactivate event to the visible panes content objects
			foreach (DockPane pane in this.VisibleNestedPanes)
				foreach (IDockContent content in pane.Contents)
					content.OnDeactivate(e);
		}

		protected override void OnLayout(LayoutEventArgs levent)
		{
			this.VisibleNestedPanes.Refresh();
			this.RefreshChanges();
            Visible = (this.VisibleNestedPanes.Count > 0);
            this.SetText();

			base.OnLayout(levent);
		}


        [SuppressMessage("Microsoft.Globalization", "CA1303:DoNotPassLiteralsAsLocalizedParameters", MessageId = "System.Windows.Forms.Control.set_Text(System.String)")]
        internal void SetText()
		{
			DockPane theOnlyPane = (this.VisibleNestedPanes.Count == 1) ? this.VisibleNestedPanes[0] : null;

			if (theOnlyPane == null)
				Text = " ";	// use " " instead of string.Empty because the whole title bar will disappear when ControlBox is set to false.
			else if (theOnlyPane.ActiveContent == null)
				Text = " ";
			else
				Text = theOnlyPane.ActiveContent.DockHandler.TabText;
		}

		protected override void SetBoundsCore(int x, int y, int width, int height, BoundsSpecified specified)
		{
			Rectangle rectWorkArea = SystemInformation.VirtualScreen;

			if (y + height > rectWorkArea.Bottom)
				y -= (y + height) - rectWorkArea.Bottom;

			if (y < rectWorkArea.Top)
				y += rectWorkArea.Top - y;

			base.SetBoundsCore (x, y, width, height, specified);
		}

        [SecurityPermission(SecurityAction.LinkDemand, Flags = SecurityPermissionFlag.UnmanagedCode)]
		protected override void WndProc(ref Message m)
		{
			if (m.Msg == (int)Msgs.WM_NCLBUTTONDOWN)
			{
				if (IsDisposed)
					return;

				uint result = NativeMethods.SendMessage(Handle, (int)Msgs.WM_NCHITTEST, 0, (uint)m.LParam);
				if (result == 2 && this.DockPanel.AllowEndUserDocking && this.AllowEndUserDocking)	// HITTEST_CAPTION
				{
					Activate();
					this.m_dockPanel.BeginDrag(this);
				}
				else
					base.WndProc(ref m);

				return;
			}
            else if (m.Msg == (int)Msgs.WM_NCRBUTTONDOWN)
            {
                uint result = NativeMethods.SendMessage(Handle, (int)Msgs.WM_NCHITTEST, 0, (uint)m.LParam);
                if (result == 2)	// HITTEST_CAPTION
                {
                    DockPane theOnlyPane = (this.VisibleNestedPanes.Count == 1) ? this.VisibleNestedPanes[0] : null;
                    if (theOnlyPane != null && theOnlyPane.ActiveContent != null)
                    {
                        theOnlyPane.ShowTabPageContextMenu(this, PointToClient(MousePosition));
                        return;
                    }
                }

                base.WndProc(ref m);
                return;
            }
            else if (m.Msg == (int)Msgs.WM_CLOSE)
            {
                if (this.NestedPanes.Count == 0)
                {
                    base.WndProc(ref m);
                    return;
                }

                for (int i = this.NestedPanes.Count - 1; i >= 0; i--)
                {
                    DockContentCollection contents = this.NestedPanes[i].Contents;
                    for (int j = contents.Count - 1; j >= 0; j--)
                    {
                        IDockContent content = contents[j];
                        if (content.DockHandler.DockState != DockState.Float)
                            continue;

                        if (!content.DockHandler.CloseButton)
                            continue;

                        if (content.DockHandler.HideOnClose)
                            content.DockHandler.Hide();
                        else
                            content.DockHandler.Close();
                    }
                }

                return;
            }
            else if (m.Msg == (int)Msgs.WM_NCLBUTTONDBLCLK)
            {
                uint result = NativeMethods.SendMessage(Handle, (int)Msgs.WM_NCHITTEST, 0, (uint)m.LParam);
                if (result != 2)	// HITTEST_CAPTION
                {
                    base.WndProc(ref m);
                    return;
                }

                this.DockPanel.SuspendLayout(true);

                // Restore to panel
                foreach (DockPane pane in this.NestedPanes)
                {
                    if (pane.DockState != DockState.Float)
                        continue;
                    pane.RestoreToPanel();
                }


                this.DockPanel.ResumeLayout(true, true);
                return;
            }
            else if (m.Msg == WM_CHECKDISPOSE)
            {
                if (this.NestedPanes.Count == 0)
                    Dispose();

                return;
            }

			base.WndProc(ref m);
		}

		internal void RefreshChanges()
		{
            if (IsDisposed)
                return;

			if (this.VisibleNestedPanes.Count == 0)
			{
				ControlBox = true;
				return;
			}

			for (int i=this.VisibleNestedPanes.Count - 1; i>=0; i--)
			{
				DockContentCollection contents = this.VisibleNestedPanes[i].Contents;
				for (int j=contents.Count - 1; j>=0; j--)
				{
					IDockContent content = contents[j];
					if (content.DockHandler.DockState != DockState.Float)
						continue;

					if (content.DockHandler.CloseButton && content.DockHandler.CloseButtonVisible)
					{
						ControlBox = true;
						return;
					}
				}
			}
			//Only if there is a ControlBox do we turn it off
			//old code caused a flash of the window.
            if (ControlBox)
				ControlBox = false;
		}

		public virtual Rectangle DisplayingRectangle
		{
			get	{	return ClientRectangle;	}
		}

		internal void TestDrop(IDockDragSource dragSource, DockOutlineBase dockOutline)
		{
            if (this.VisibleNestedPanes.Count == 1)
            {
                DockPane pane = this.VisibleNestedPanes[0];
                if (!dragSource.CanDockTo(pane))
                    return;

                Point ptMouse = MousePosition;
                uint lParam = Win32Helper.MakeLong(ptMouse.X, ptMouse.Y);
                if (NativeMethods.SendMessage(Handle, (int)Msgs.WM_NCHITTEST, 0, lParam) == (uint)HitTest.HTCAPTION)
                    dockOutline.Show(this.VisibleNestedPanes[0], -1);
            }
		}

        #region IDockDragSource Members

        #region IDragSource Members

        Control IDragSource.DragControl
        {
            get { return this; }
        }

        #endregion

        bool IDockDragSource.IsDockStateValid(DockState dockState)
        {
            return this.IsDockStateValid(dockState);
        }

        bool IDockDragSource.CanDockTo(DockPane pane)
        {
            if (!this.IsDockStateValid(pane.DockState))
                return false;

            if (pane.FloatWindow == this)
                return false;

            return true;
        }

        Rectangle IDockDragSource.BeginDrag(Point ptMouse)
        {
            return Bounds;
        }

        public  void FloatAt(Rectangle floatWindowBounds)
        {
            Bounds = floatWindowBounds;
        }

        public void DockTo(DockPane pane, DockStyle dockStyle, int contentIndex)
        {
            if (dockStyle == DockStyle.Fill)
            {
                for (int i = this.NestedPanes.Count - 1; i >= 0; i--)
                {
                    DockPane paneFrom = this.NestedPanes[i];
                    for (int j = paneFrom.Contents.Count - 1; j >= 0; j--)
                    {
                        IDockContent c = paneFrom.Contents[j];
                        c.DockHandler.Pane = pane;
                        if (contentIndex != -1)
                            pane.SetContentIndex(c, contentIndex);
                        c.DockHandler.Activate();
                    }
                }
            }
            else
            {
                var alignment = DockAlignment.Left;
                if (dockStyle == DockStyle.Left)
                    alignment = DockAlignment.Left;
                else if (dockStyle == DockStyle.Right)
                    alignment = DockAlignment.Right;
                else if (dockStyle == DockStyle.Top)
                    alignment = DockAlignment.Top;
                else if (dockStyle == DockStyle.Bottom)
                    alignment = DockAlignment.Bottom;

                MergeNestedPanes(this.VisibleNestedPanes, pane.NestedPanesContainer.NestedPanes, pane, alignment, 0.5);
            }
        }

        public void DockTo(DockPanel panel, DockStyle dockStyle)
        {
            if (panel != this.DockPanel)
                throw new ArgumentException(Strings.IDockDragSource_DockTo_InvalidPanel, "panel");

            NestedPaneCollection nestedPanesTo = null;

            if (dockStyle == DockStyle.Top)
                nestedPanesTo = this.DockPanel.DockWindows[DockState.DockTop].NestedPanes;
            else if (dockStyle == DockStyle.Bottom)
                nestedPanesTo = this.DockPanel.DockWindows[DockState.DockBottom].NestedPanes;
            else if (dockStyle == DockStyle.Left)
                nestedPanesTo = this.DockPanel.DockWindows[DockState.DockLeft].NestedPanes;
            else if (dockStyle == DockStyle.Right)
                nestedPanesTo = this.DockPanel.DockWindows[DockState.DockRight].NestedPanes;
            else if (dockStyle == DockStyle.Fill)
                nestedPanesTo = this.DockPanel.DockWindows[DockState.Document].NestedPanes;

            DockPane prevPane = null;
            for (int i = nestedPanesTo.Count - 1; i >= 0; i--)
                if (nestedPanesTo[i] != this.VisibleNestedPanes[0])
                    prevPane = nestedPanesTo[i];
            MergeNestedPanes(this.VisibleNestedPanes, nestedPanesTo, prevPane, DockAlignment.Left, 0.5);
        }

        private static void MergeNestedPanes(VisibleNestedPaneCollection nestedPanesFrom, NestedPaneCollection nestedPanesTo, DockPane prevPane, DockAlignment alignment, double proportion)
        {
            if (nestedPanesFrom.Count == 0)
                return;

            int count = nestedPanesFrom.Count;
            var panes = new DockPane[count];
            var prevPanes = new DockPane[count];
            var alignments = new DockAlignment[count];
            var proportions = new double[count];

            for (int i = 0; i < count; i++)
            {
                panes[i] = nestedPanesFrom[i];
                prevPanes[i] = nestedPanesFrom[i].NestedDockingStatus.PreviousPane;
                alignments[i] = nestedPanesFrom[i].NestedDockingStatus.Alignment;
                proportions[i] = nestedPanesFrom[i].NestedDockingStatus.Proportion;
            }

            DockPane pane = panes[0].DockTo(nestedPanesTo.Container, prevPane, alignment, proportion);
            panes[0].DockState = nestedPanesTo.DockState;

            for (int i = 1; i < count; i++)
            {
                for (int j = i; j < count; j++)
                {
                    if (prevPanes[j] == panes[i - 1])
                        prevPanes[j] = pane;
                }
                pane = panes[i].DockTo(nestedPanesTo.Container, prevPanes[i], alignments[i], proportions[i]);
                panes[i].DockState = nestedPanesTo.DockState;
            }
        }

        #endregion
    }
}
