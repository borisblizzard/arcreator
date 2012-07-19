#region Using Directives

using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

#endregion

namespace ARCed.UI
{
	public abstract class AutoHideStripBase : Control
	{
        [SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]
        protected class Tab : IDisposable
        {
            private readonly IDockContent m_content;

            protected internal Tab(IDockContent content)
            {
                this.m_content = content;
            }

            ~Tab()
            {
                this.Dispose(false);
            }

            public IDockContent Content
            {
                get { return this.m_content; }
            }

            public void Dispose()
            {
                this.Dispose(true);
                GC.SuppressFinalize(this);
            }

            protected virtual void Dispose(bool disposing)
            {
            }
        }

        [SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]
        protected sealed class TabCollection : IEnumerable<Tab>
        {
            #region IEnumerable Members
            IEnumerator<Tab> IEnumerable<Tab>.GetEnumerator()
            {
                for (int i = 0; i < this.Count; i++)
                    yield return this[i];
            }

            IEnumerator IEnumerable.GetEnumerator()
            {
                for (int i = 0; i < this.Count; i++)
                    yield return this[i];
            }
            #endregion

            internal TabCollection(DockPane pane)
            {
                this.m_dockPane = pane;
            }

            private readonly DockPane m_dockPane;
            public DockPane DockPane
            {
                get { return this.m_dockPane; }
            }

            public DockPanel DockPanel
            {
                get { return this.DockPane.DockPanel; }
            }

            public int Count
            {
                get { return this.DockPane.DisplayingContents.Count; }
            }

            public Tab this[int index]
            {
                get
                {
                    IDockContent content = this.DockPane.DisplayingContents[index];
                    if (content == null)
                        throw (new ArgumentOutOfRangeException("index"));
                    if (content.DockHandler.AutoHideTab == null)
                        content.DockHandler.AutoHideTab = (this.DockPanel.AutoHideStripControl.CreateTab(content));
                    return content.DockHandler.AutoHideTab as Tab;
                }
            }

            public bool Contains(Tab tab)
            {
                return (IndexOf(tab) != -1);
            }

            public bool Contains(IDockContent content)
            {
                return (IndexOf(content) != -1);
            }

            public int IndexOf(Tab tab)
            {
                if (tab == null)
                    return -1;

                return IndexOf(tab.Content);
            }

            public int IndexOf(IDockContent content)
            {
                return this.DockPane.DisplayingContents.IndexOf(content);
            }
        }

        [SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]
        protected class Pane : IDisposable
        {
            private readonly DockPane m_dockPane;

            protected internal Pane(DockPane dockPane)
            {
                this.m_dockPane = dockPane;
            }

            ~Pane()
            {
                this.Dispose(false);
            }

            public DockPane DockPane
            {
                get { return this.m_dockPane; }
            }

            public TabCollection AutoHideTabs
            {
                get
                {
                    if (this.DockPane.AutoHideTabs == null)
                        this.DockPane.AutoHideTabs = new TabCollection(this.DockPane);
                    return this.DockPane.AutoHideTabs as TabCollection;
                }
            }

            public void Dispose()
            {
                this.Dispose(true);
                GC.SuppressFinalize(this);
            }

            protected virtual void Dispose(bool disposing)
            {
            }
        }

        [SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]
        protected sealed class PaneCollection : IEnumerable<Pane>
        {
            private class AutoHideState
            {
                private readonly DockState _mDockState;
                private bool _mSelected;

                public AutoHideState(DockState dockState)
                {
                    this._mDockState = dockState;
                }

                public DockState DockState
                {
                    get { return this._mDockState; }
                }

                public bool Selected
                {
                    get { return this._mSelected; }
                    set { this._mSelected = value; }
                }
            }

            private class AutoHideStateCollection
            {
                private readonly AutoHideState[] _mStates;

                public AutoHideStateCollection()
                {
                    this._mStates = new[]	{	
												new AutoHideState(DockState.DockTopAutoHide),
												new AutoHideState(DockState.DockBottomAutoHide),
												new AutoHideState(DockState.DockLeftAutoHide),
												new AutoHideState(DockState.DockRightAutoHide)
											};
                }

                public AutoHideState this[DockState dockState]
                {
                    get
                    {
                        for (int i = 0; i < this._mStates.Length; i++)
                        {
                            if (this._mStates[i].DockState == dockState)
                                return this._mStates[i];
                        }
                        throw new ArgumentOutOfRangeException("dockState");
                    }
                }

                public bool ContainsPane(DockPane pane)
                {
                    if (pane.IsHidden)
                        return false;

                    for (int i = 0; i < this._mStates.Length; i++)
                    {
                        if (this._mStates[i].DockState == pane.DockState && this._mStates[i].Selected)
                            return true;
                    }
                    return false;
                }
            }

            internal PaneCollection(DockPanel panel, DockState dockState)
            {
                this._mDockPanel = panel;
                this._mStates = new AutoHideStateCollection();
                this.States[DockState.DockTopAutoHide].Selected = (dockState == DockState.DockTopAutoHide);
                this.States[DockState.DockBottomAutoHide].Selected = (dockState == DockState.DockBottomAutoHide);
                this.States[DockState.DockLeftAutoHide].Selected = (dockState == DockState.DockLeftAutoHide);
                this.States[DockState.DockRightAutoHide].Selected = (dockState == DockState.DockRightAutoHide);
            }

            private readonly DockPanel _mDockPanel;
            public DockPanel DockPanel
            {
                get { return this._mDockPanel; }
            }

            private readonly AutoHideStateCollection _mStates;
            private AutoHideStateCollection States
            {
                get { return this._mStates; }
            }

            public int Count
            {
                get
                {
                    int count = 0;
                    foreach (DockPane pane in this.DockPanel.Panes)
                    {
                        if (this.States.ContainsPane(pane))
                            count++;
                    }

                    return count;
                }
            }

            public Pane this[int index]
            {
                get
                {
                    int count = 0;
                    foreach (DockPane pane in this.DockPanel.Panes)
                    {
                        if (!this.States.ContainsPane(pane))
                            continue;

                        if (count == index)
                        {
                            if (pane.AutoHidePane == null)
                                pane.AutoHidePane = this.DockPanel.AutoHideStripControl.CreatePane(pane);
                            return pane.AutoHidePane as Pane;
                        }

                        count++;
                    }
                    throw new ArgumentOutOfRangeException("index");
                }
            }

            public bool Contains(Pane pane)
            {
                return (this.IndexOf(pane) != -1);
            }

            public int IndexOf(Pane pane)
            {
                if (pane == null)
                    return -1;

                int index = 0;
                foreach (DockPane dockPane in this.DockPanel.Panes)
                {
                    if (!this.States.ContainsPane(pane.DockPane))
                        continue;

                    if (pane == dockPane.AutoHidePane)
                        return index;

                    index++;
                }
                return -1;
            }

            #region IEnumerable Members

            IEnumerator<Pane> IEnumerable<Pane>.GetEnumerator()
            {
                for (int i = 0; i < this.Count; i++)
                    yield return this[i];
            }

            IEnumerator IEnumerable.GetEnumerator()
            {
                for (int i = 0; i < this.Count; i++)
                    yield return this[i];
            }

            #endregion
        }

		protected AutoHideStripBase(DockPanel panel)
		{
			this._mDockPanel = panel;
			this._mPanesTop = new PaneCollection(panel, DockState.DockTopAutoHide);
			this._mPanesBottom = new PaneCollection(panel, DockState.DockBottomAutoHide);
			this._mPanesLeft = new PaneCollection(panel, DockState.DockLeftAutoHide);
			this._mPanesRight = new PaneCollection(panel, DockState.DockRightAutoHide);

			SetStyle(ControlStyles.OptimizedDoubleBuffer, true);
			SetStyle(ControlStyles.Selectable, false);
		}

        private readonly DockPanel _mDockPanel;
		protected DockPanel DockPanel
		{
			get	{	return this._mDockPanel;	}
		}

        private readonly PaneCollection _mPanesTop;
		protected PaneCollection PanesTop
		{
			get	{	return this._mPanesTop;	}
		}

        private readonly PaneCollection _mPanesBottom;
		protected PaneCollection PanesBottom
		{
			get	{	return this._mPanesBottom;	}
		}

        private readonly PaneCollection _mPanesLeft;
		protected PaneCollection PanesLeft
		{
			get	{	return this._mPanesLeft;	}
		}

        private readonly PaneCollection _mPanesRight;
		protected PaneCollection PanesRight
		{
			get	{	return this._mPanesRight;	}
		}

		protected PaneCollection GetPanes(DockState dockState)
		{
			if (dockState == DockState.DockTopAutoHide)
				return this.PanesTop;
			else if (dockState == DockState.DockBottomAutoHide)
				return this.PanesBottom;
			else if (dockState == DockState.DockLeftAutoHide)
				return this.PanesLeft;
			else if (dockState == DockState.DockRightAutoHide)
				return this.PanesRight;
			else
				throw new ArgumentOutOfRangeException("dockState");
		}

        internal int GetNumberOfPanes(DockState dockState)
        {
            return this.GetPanes(dockState).Count;
        }

		protected Rectangle RectangleTopLeft
		{
			get
			{	
				int height = this.MeasureHeight();
				return this.PanesTop.Count > 0 && this.PanesLeft.Count > 0 ? new Rectangle(0, 0, height, height) : Rectangle.Empty;
			}
		}

		protected Rectangle RectangleTopRight
		{
			get
			{
				int height = this.MeasureHeight();
				return this.PanesTop.Count > 0 && this.PanesRight.Count > 0 ? new Rectangle(Width - height, 0, height, height) : Rectangle.Empty;
			}
		}

		protected Rectangle RectangleBottomLeft
		{
			get
			{
				int height = this.MeasureHeight();
				return this.PanesBottom.Count > 0 && this.PanesLeft.Count > 0 ? new Rectangle(0, Height - height, height, height) : Rectangle.Empty;
			}
		}

		protected Rectangle RectangleBottomRight
		{
			get
			{
				int height = this.MeasureHeight();
				return this.PanesBottom.Count > 0 && this.PanesRight.Count > 0 ? new Rectangle(Width - height, Height - height, height, height) : Rectangle.Empty;
			}
		}

		protected internal Rectangle GetTabStripRectangle(DockState dockState)
		{
			int height = this.MeasureHeight();
			if (dockState == DockState.DockTopAutoHide && this.PanesTop.Count > 0)
				return new Rectangle(this.RectangleTopLeft.Width, 0, Width - this.RectangleTopLeft.Width - this.RectangleTopRight.Width, height);
			else if (dockState == DockState.DockBottomAutoHide && this.PanesBottom.Count > 0)
				return new Rectangle(this.RectangleBottomLeft.Width, Height - height, Width - this.RectangleBottomLeft.Width - this.RectangleBottomRight.Width, height);
			else if (dockState == DockState.DockLeftAutoHide && this.PanesLeft.Count > 0)
				return new Rectangle(0, this.RectangleTopLeft.Width, height, Height - this.RectangleTopLeft.Height - this.RectangleBottomLeft.Height);
			else if (dockState == DockState.DockRightAutoHide && this.PanesRight.Count > 0)
				return new Rectangle(Width - height, this.RectangleTopRight.Width, height, Height - this.RectangleTopRight.Height - this.RectangleBottomRight.Height);
			else
				return Rectangle.Empty;
		}

		private GraphicsPath m_displayingArea;
		private GraphicsPath DisplayingArea
		{
			get
			{
				if (this.m_displayingArea == null)
					this.m_displayingArea = new GraphicsPath();

				return this.m_displayingArea;
			}
		}

		private void SetRegion()
		{
			this.DisplayingArea.Reset();
			this.DisplayingArea.AddRectangle(this.RectangleTopLeft);
			this.DisplayingArea.AddRectangle(this.RectangleTopRight);
			this.DisplayingArea.AddRectangle(this.RectangleBottomLeft);
			this.DisplayingArea.AddRectangle(this.RectangleBottomRight);
			this.DisplayingArea.AddRectangle(this.GetTabStripRectangle(DockState.DockTopAutoHide));
			this.DisplayingArea.AddRectangle(this.GetTabStripRectangle(DockState.DockBottomAutoHide));
			this.DisplayingArea.AddRectangle(this.GetTabStripRectangle(DockState.DockLeftAutoHide));
			this.DisplayingArea.AddRectangle(this.GetTabStripRectangle(DockState.DockRightAutoHide));
			Region = new Region(this.DisplayingArea);
		}

		protected override void OnMouseDown(MouseEventArgs e)
		{
			base.OnMouseDown(e);

			if (e.Button != MouseButtons.Left)
				return;

			IDockContent content = this.HitTest();
			if (content == null)
				return;

			content.DockHandler.Activate();
		}

		protected override void OnMouseHover(EventArgs e)
		{
			base.OnMouseHover(e);

			IDockContent content = this.HitTest();
			if (content != null && this.DockPanel.ActiveAutoHideContent != content)
				this.DockPanel.ActiveAutoHideContent = content;

			// requires further tracking of mouse hover behavior,
            ResetMouseEventArgs();
		}

		protected override void OnLayout(LayoutEventArgs levent)
		{
			this.RefreshChanges();
			base.OnLayout (levent);
		}

		internal void RefreshChanges()
		{
            if (IsDisposed)
                return;

			this.SetRegion();
			this.OnRefreshChanges();
		}

		protected virtual void OnRefreshChanges()
		{
		}

		protected internal abstract int MeasureHeight();

		private IDockContent HitTest()
		{
			Point ptMouse = PointToClient(MousePosition);
			return this.HitTest(ptMouse);
		}

        protected virtual Tab CreateTab(IDockContent content)
        {
            return new Tab(content);
        }

        protected virtual Pane CreatePane(DockPane dockPane)
        {
            return new Pane(dockPane);
        }

		protected abstract IDockContent HitTest(Point point);
	}
}
