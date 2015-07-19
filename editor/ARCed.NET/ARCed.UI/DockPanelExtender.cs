#region Using Directives

using System;
using System.Diagnostics.CodeAnalysis;
using System.Drawing;

#endregion

namespace ARCed.UI
{
	public sealed class DockPanelExtender
	{
		[SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]
		public interface IDockPaneFactory
		{
			DockPane CreateDockPane(IDockContent content, DockState visibleState, bool show);
			[SuppressMessage("Microsoft.Naming", "CA1720:AvoidTypeNamesInParameters", MessageId = "1#")]
			DockPane CreateDockPane(IDockContent content, FloatWindow floatWindow, bool show);
			DockPane CreateDockPane(IDockContent content, DockPane previousPane, DockAlignment alignment, double proportion, bool show);
			[SuppressMessage("Microsoft.Naming", "CA1720:AvoidTypeNamesInParameters", MessageId = "1#")]
			DockPane CreateDockPane(IDockContent content, Rectangle floatWindowBounds, bool show);
		}

		[SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]
		public interface IFloatWindowFactory
		{
			FloatWindow CreateFloatWindow(DockPanel dockPanel, DockPane pane);
			FloatWindow CreateFloatWindow(DockPanel dockPanel, DockPane pane, Rectangle bounds);
		}

		[SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]
		public interface IDockPaneCaptionFactory
		{
			DockPaneCaptionBase CreateDockPaneCaption(DockPane pane);
		}

		[SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]
		public interface IDockPaneStripFactory
		{
			DockPaneStripBase CreateDockPaneStrip(DockPane pane);
		}

		[SuppressMessage("Microsoft.Design", "CA1034:NestedTypesShouldNotBeVisible")]
		public interface IAutoHideStripFactory
		{
			AutoHideStripBase CreateAutoHideStrip(DockPanel panel);
		}

		#region DefaultDockPaneFactory
		private class DefaultDockPaneFactory : IDockPaneFactory
		{
			public DockPane CreateDockPane(IDockContent content, DockState visibleState, bool show)
			{
				return new DockPane(content, visibleState, show);
			}

			public DockPane CreateDockPane(IDockContent content, FloatWindow floatWindow, bool show)
			{
				return new DockPane(content, floatWindow, show);
			}

			public DockPane CreateDockPane(IDockContent content, DockPane prevPane, DockAlignment alignment, double proportion, bool show)
			{
				return new DockPane(content, prevPane, alignment, proportion, show);
			}

			public DockPane CreateDockPane(IDockContent content, Rectangle floatWindowBounds, bool show)
			{
				return new DockPane(content, floatWindowBounds, show);
			}
		}
		#endregion

		#region DefaultFloatWindowFactory
		private class DefaultFloatWindowFactory : IFloatWindowFactory
		{
			public FloatWindow CreateFloatWindow(DockPanel dockPanel, DockPane pane)
			{
				return new FloatWindow(dockPanel, pane);
			}

			public FloatWindow CreateFloatWindow(DockPanel dockPanel, DockPane pane, Rectangle bounds)
			{
				return new FloatWindow(dockPanel, pane, bounds);
			}
		}
		#endregion

		#region DefaultDockPaneCaptionFactory
		private class DefaultDockPaneCaptionFactory : IDockPaneCaptionFactory
		{
			public DockPaneCaptionBase CreateDockPaneCaption(DockPane pane)
			{
				return new VS2005DockPaneCaption(pane);
			}
		}
		#endregion

		#region DefaultDockPaneTabStripFactory
		private class DefaultDockPaneStripFactory : IDockPaneStripFactory
		{
			public DockPaneStripBase CreateDockPaneStrip(DockPane pane)
			{
				return new VS2005DockPaneStrip(pane);
			}
		}
		#endregion

		#region DefaultAutoHideStripFactory
		private class DefaultAutoHideStripFactory : IAutoHideStripFactory
		{
			public AutoHideStripBase CreateAutoHideStrip(DockPanel panel)
			{
				return new VS2005AutoHideStrip(panel);
			}
		}
		#endregion

		internal DockPanelExtender(DockPanel dockPanel)
		{
			this._mDockPanel = dockPanel;
		}

		private readonly DockPanel _mDockPanel;
		private DockPanel DockPanel
		{
			get { return this._mDockPanel; }
		}

		private IDockPaneFactory m_dockPaneFactory;
		public IDockPaneFactory DockPaneFactory
		{
			get
			{
				if (this.m_dockPaneFactory == null)
					this.m_dockPaneFactory = new DefaultDockPaneFactory();

				return this.m_dockPaneFactory;
			}
			set
			{
				if (this.DockPanel.Panes.Count > 0)
					throw new InvalidOperationException();

				this.m_dockPaneFactory = value;
			}
		}

		private IFloatWindowFactory m_floatWindowFactory;
		public IFloatWindowFactory FloatWindowFactory
		{
			get
			{
				if (this.m_floatWindowFactory == null)
					this.m_floatWindowFactory = new DefaultFloatWindowFactory();

				return this.m_floatWindowFactory;
			}
			set
			{
				if (this.DockPanel.FloatWindows.Count > 0)
					throw new InvalidOperationException();

				this.m_floatWindowFactory = value;
			}
		}

		private IDockPaneCaptionFactory m_dockPaneCaptionFactory;
		public IDockPaneCaptionFactory DockPaneCaptionFactory
		{
			get
			{
				if (this.m_dockPaneCaptionFactory == null)
					this.m_dockPaneCaptionFactory = new DefaultDockPaneCaptionFactory();

				return this.m_dockPaneCaptionFactory;
			}
			set
			{
				if (this.DockPanel.Panes.Count > 0)
					throw new InvalidOperationException();

				this.m_dockPaneCaptionFactory = value;
			}
		}

		private IDockPaneStripFactory m_dockPaneStripFactory;
		public IDockPaneStripFactory DockPaneStripFactory
		{
			get
			{
				if (this.m_dockPaneStripFactory == null)
					this.m_dockPaneStripFactory = new DefaultDockPaneStripFactory();

				return this.m_dockPaneStripFactory;
			}
			set
			{
				if (this.DockPanel.Contents.Count > 0)
					throw new InvalidOperationException();

				this.m_dockPaneStripFactory = value;
			}
		}

		private IAutoHideStripFactory m_autoHideStripFactory;
		public IAutoHideStripFactory AutoHideStripFactory
		{
			get
			{
				if (this.m_autoHideStripFactory == null)
					this.m_autoHideStripFactory = new DefaultAutoHideStripFactory();

				return this.m_autoHideStripFactory;
			}
			set
			{
				if (this.DockPanel.Contents.Count > 0)
					throw new InvalidOperationException();

				if (this.m_autoHideStripFactory == value)
					return;

				this.m_autoHideStripFactory = value;
				this.DockPanel.ResetAutoHideStripControl();
			}
		}
	}
}
