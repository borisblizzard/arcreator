#region Using Directives

using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Security.Permissions;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed.UI
{
	public abstract class DockPaneStripBase : Control
	{
        [SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]        
        protected internal class Tab : IDisposable
        {
            private readonly IDockContent _mContent;

            public Tab(IDockContent content)
            {
                this._mContent = content;
            }

            ~Tab()
            {
                this.Dispose(false);
            }

            public IDockContent Content
            {
                get { return this._mContent; }
            }

            public Form ContentForm
            {
                get { return this._mContent as Form; }
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
                this._mDockPane = pane;
            }

            private readonly DockPane _mDockPane;
            public DockPane DockPane
            {
                get { return this._mDockPane; }
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
                    return content.DockHandler.GetTab(this.DockPane.TabStripControl);
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

                return this.DockPane.DisplayingContents.IndexOf(tab.Content);
            }

            public int IndexOf(IDockContent content)
            {
                return this.DockPane.DisplayingContents.IndexOf(content);
            }
        }

		protected DockPaneStripBase(DockPane pane)
		{
			this._mDockPane = pane;

			SetStyle(ControlStyles.OptimizedDoubleBuffer, true);
			SetStyle(ControlStyles.Selectable, false);
            AllowDrop = true;
		}

        private readonly DockPane _mDockPane;
		protected DockPane DockPane
		{
			get	{	return this._mDockPane;	}
		}

		protected DockPane.AppearanceStyle Appearance
		{
			get	{	return this.DockPane.Appearance;	}
		}

        private TabCollection m_tabs;
		protected TabCollection Tabs
		{
			get
            {
                if (this.m_tabs == null)
                    this.m_tabs = new TabCollection(this.DockPane);

                return this.m_tabs;
            }
		}

		internal void RefreshChanges()
		{
            if (IsDisposed)
                return;

			this.OnRefreshChanges();
		}

		protected virtual void OnRefreshChanges()
		{
		}

		protected internal abstract int MeasureHeight();

		protected internal abstract void EnsureTabVisible(IDockContent content);

		protected int HitTest()
		{
			return this.HitTest(PointToClient(MousePosition));
		}

		protected internal abstract int HitTest(Point point);

		protected internal abstract GraphicsPath GetOutline(int index);

        protected internal virtual Tab CreateTab(IDockContent content)
        {
            return new Tab(content);
        }

        protected override void OnMouseDown(MouseEventArgs e)
        {
            base.OnMouseDown(e);

            int index = this.HitTest();
            if (index != -1)
            {
                IDockContent content = this.Tabs[index].Content;
                if (this.DockPane.ActiveContent != content)
                    this.DockPane.ActiveContent = content;
            }

            if (e.Button == MouseButtons.Left)
            {
                if (this.DockPane.DockPanel.AllowEndUserDocking && this.DockPane.AllowDockDragAndDrop && this.DockPane.ActiveContent.DockHandler.AllowEndUserDocking)
                    this.DockPane.DockPanel.BeginDrag(this.DockPane.ActiveContent.DockHandler);
            }
        }

        protected bool HasTabPageContextMenu
        {
            get { return this.DockPane.HasTabPageContextMenu; }
        }

        protected void ShowTabPageContextMenu(Point position)
        {
            this.DockPane.ShowTabPageContextMenu(this, position);
        }

        protected override void OnMouseUp(MouseEventArgs e)
        {
            base.OnMouseUp(e);

            if (e.Button == MouseButtons.Right)
                this.ShowTabPageContextMenu(new Point(e.X, e.Y));
            else if ((e.Button == MouseButtons.Middle) && (this.DockPane.Appearance == DockPane.AppearanceStyle.Document))
            {
                // Get the content located under the click (if there is one)
                int index = this.HitTest();
                if (index != -1)
                {
                    // Close the specified content.
                    IDockContent content = this.Tabs[index].Content;
                    this.DockPane.CloseContent(content);
                }
            }
        }

        [SecurityPermission(SecurityAction.LinkDemand, Flags = SecurityPermissionFlag.UnmanagedCode)]
		protected override void WndProc(ref Message m)
		{
			if (m.Msg == (int)Msgs.WM_LBUTTONDBLCLK)
			{
				base.WndProc(ref m);

				int index = this.HitTest();
				if (this.DockPane.DockPanel.AllowEndUserDocking && index != -1)
				{
					IDockContent content = this.Tabs[index].Content;
                    if (content.DockHandler.CheckDockState(!content.DockHandler.IsFloat) != DockState.Unknown)
					    content.DockHandler.IsFloat = !content.DockHandler.IsFloat;	
				}

				return;
			}

			base.WndProc(ref m);
			return;
		}

        protected override void OnDragOver(DragEventArgs drgevent)
        {
            base.OnDragOver(drgevent);

            int index = this.HitTest();
            if (index != -1)
            {
                IDockContent content = this.Tabs[index].Content;
                if (this.DockPane.ActiveContent != content)
                    this.DockPane.ActiveContent = content;
            }
        }
	}
}
