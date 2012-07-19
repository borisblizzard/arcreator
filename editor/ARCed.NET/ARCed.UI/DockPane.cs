#region Using Directives

using System;
using System.ComponentModel;
using System.Diagnostics;
using System.Diagnostics.CodeAnalysis;
using System.Drawing;
using System.Security.Permissions;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed.UI
{
    [ToolboxItem(false)]
    public partial class DockPane : UserControl, IDockDragSource
    {
        public enum AppearanceStyle
        {
            ToolWindow,
            Document
        }

        private enum HitTestArea
        {
            Caption,
            TabStrip,
            Content,
            None
        }

        private struct HitTestResult
        {
            public readonly HitTestArea HitArea;
            public readonly int Index;

            public HitTestResult(HitTestArea hitTestArea, int index)
            {
                this.HitArea = hitTestArea;
                this.Index = index;
            }
        }

        private DockPaneCaptionBase m_captionControl;
        private DockPaneCaptionBase CaptionControl
        {
            get { return this.m_captionControl; }
        }

        private DockPaneStripBase m_tabStripControl;
        internal DockPaneStripBase TabStripControl
        {
            get { return this.m_tabStripControl; }
        }

		public Size DefaultFloatSize { get; set; }

        internal protected DockPane(IDockContent content, DockState visibleState, bool show)
        {
            this.InternalConstruct(content, visibleState, false, Rectangle.Empty, null, DockAlignment.Right, 0.5, show);
        }

        [SuppressMessage("Microsoft.Naming", "CA1720:AvoidTypeNamesInParameters", MessageId = "1#")]
        internal protected DockPane(IDockContent content, FloatWindow floatWindow, bool show)
        {
            if (floatWindow == null)
                throw new ArgumentNullException("floatWindow");
            this.InternalConstruct(content, DockState.Float, false, Rectangle.Empty, floatWindow.NestedPanes.GetDefaultPreviousPane(this), DockAlignment.Right, 0.5, show);
        }

        internal protected DockPane(IDockContent content, DockPane previousPane, DockAlignment alignment, double proportion, bool show)
        {
            if (previousPane == null)
                throw (new ArgumentNullException("previousPane"));
            this.InternalConstruct(content, previousPane.DockState, false, Rectangle.Empty, previousPane, alignment, proportion, show);
        }

        [SuppressMessage("Microsoft.Naming", "CA1720:AvoidTypeNamesInParameters", MessageId = "1#")]
        internal protected DockPane(IDockContent content, Rectangle floatWindowBounds, bool show)
        {
            this.InternalConstruct(content, DockState.Float, true, floatWindowBounds, null, DockAlignment.Right, 0.5, show);
        }

        private void InternalConstruct(IDockContent content, DockState dockState, bool flagBounds, Rectangle floatWindowBounds, DockPane prevPane, DockAlignment alignment, double proportion, bool show)
        {
            if (dockState == DockState.Hidden || dockState == DockState.Unknown)
                throw new ArgumentException(Strings.DockPane_SetDockState_InvalidState);

            if (content == null)
                throw new ArgumentNullException(Strings.DockPane_Constructor_NullContent);

            if (content.DockHandler.DockPanel == null)
                throw new ArgumentException(Strings.DockPane_Constructor_NullDockPanel);

            SuspendLayout();
            SetStyle(ControlStyles.Selectable, false);

            this.m_isFloat = (dockState == DockState.Float);

            this.m_contents = new DockContentCollection();
            this.m_displayingContents = new DockContentCollection(this);
            this.m_dockPanel = content.DockHandler.DockPanel;
            this.m_dockPanel.AddPane(this);

            this.m_splitter = new SplitterControl(this);

            this.m_nestedDockingStatus = new NestedDockingStatus(this);

            this.m_captionControl = this.DockPanel.DockPaneCaptionFactory.CreateDockPaneCaption(this);
            this.m_tabStripControl = this.DockPanel.DockPaneStripFactory.CreateDockPaneStrip(this);
            Controls.AddRange(new Control[] { this.m_captionControl, this.m_tabStripControl });

            this.DockPanel.SuspendLayout(true);
            if (flagBounds)
                this.FloatWindow = this.DockPanel.FloatWindowFactory.CreateFloatWindow(this.DockPanel, this, floatWindowBounds);
            else if (prevPane != null)
                this.DockTo(prevPane.NestedPanesContainer, prevPane, alignment, proportion);

            this.SetDockState(dockState);
			if (show)
			{
				content.DockHandler.Pane = this;
				if (this.IsFloat)
				{
					Size size = (content as DockContent).DefaultFloatSize;
					int x = (Screen.PrimaryScreen.Bounds.Width - size.Width) / 2;
					int y = (Screen.PrimaryScreen.Bounds.Height - size.Height) / 2;
					this.FloatWindow.Bounds = new Rectangle(new Point(x, y), size);
				}
			}
			else if (this.IsFloat)
				content.DockHandler.FloatPane = this;
			else
				content.DockHandler.PanelPane = this;

			

			

            ResumeLayout();
            this.DockPanel.ResumeLayout(true, true);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                this.m_dockState = DockState.Unknown;

                if (this.NestedPanesContainer != null)
                    this.NestedPanesContainer.NestedPanes.Remove(this);

                if (this.DockPanel != null)
                {
                    this.DockPanel.RemovePane(this);
                    this.m_dockPanel = null;
                }

                this.Splitter.Dispose();
                if (this.m_autoHidePane != null)
                    this.m_autoHidePane.Dispose();
            }
            base.Dispose(disposing);
        }

        private IDockContent m_activeContent;
        public virtual IDockContent ActiveContent
        {
            get { return this.m_activeContent; }
            set
            {
                if (this.ActiveContent == value)
                    return;

                if (value != null)
                {
                    if (!this.DisplayingContents.Contains(value))
                        throw (new InvalidOperationException(Strings.DockPane_ActiveContent_InvalidValue));
                }
                else
                {
                    if (this.DisplayingContents.Count != 0)
                        throw (new InvalidOperationException(Strings.DockPane_ActiveContent_InvalidValue));
                }

                IDockContent oldValue = this.m_activeContent;

                if (this.DockPanel.ActiveAutoHideContent == oldValue)
                    this.DockPanel.ActiveAutoHideContent = null;

                this.m_activeContent = value;

                if (this.DockPanel.DocumentStyle == DocumentStyle.DockingMdi && this.DockState == DockState.Document)
                {
                    if (this.m_activeContent != null)
                        this.m_activeContent.DockHandler.Form.BringToFront();
                }
                else
                {
                    if (this.m_activeContent != null)
                        this.m_activeContent.DockHandler.SetVisible();
                    if (oldValue != null && this.DisplayingContents.Contains(oldValue))
                        oldValue.DockHandler.SetVisible();
                    if (this.IsActivated && this.m_activeContent != null)
                        this.m_activeContent.DockHandler.Activate();
                }

                if (this.FloatWindow != null)
                    this.FloatWindow.SetText();

                if (this.DockPanel.DocumentStyle == DocumentStyle.DockingMdi &&
                    this.DockState == DockState.Document)
                    this.RefreshChanges(false);  // delayed layout to reduce screen flicker
                else
                    this.RefreshChanges();

                if (this.m_activeContent != null)
                    this.TabStripControl.EnsureTabVisible(this.m_activeContent);
            }
        }

        private bool m_allowDockDragAndDrop = true;
        public virtual bool AllowDockDragAndDrop
        {
            get { return this.m_allowDockDragAndDrop; }
            set { this.m_allowDockDragAndDrop = value; }
        }

        private IDisposable m_autoHidePane;
        internal IDisposable AutoHidePane
        {
            get { return this.m_autoHidePane; }
            set { this.m_autoHidePane = value; }
        }

        private object m_autoHideTabs;
        internal object AutoHideTabs
        {
            get { return this.m_autoHideTabs; }
            set { this.m_autoHideTabs = value; }
        }

        private object TabPageContextMenu
        {
            get
            {
                IDockContent content = this.ActiveContent;

                if (content == null)
                    return null;

                if (content.DockHandler.TabPageContextMenuStrip != null)
                    return content.DockHandler.TabPageContextMenuStrip;
                else if (content.DockHandler.TabPageContextMenu != null)
                    return content.DockHandler.TabPageContextMenu;
                else
                    return null;
            }
        }

        internal bool HasTabPageContextMenu
        {
            get { return this.TabPageContextMenu != null; }
        }

        internal void ShowTabPageContextMenu(Control control, Point position)
        {
            object menu = this.TabPageContextMenu;

            if (menu == null)
                return;

            var contextMenuStrip = menu as ContextMenuStrip;
            if (contextMenuStrip != null)
            {
                contextMenuStrip.Show(control, position);
                return;
            }

            var contextMenu = menu as ContextMenu;
            if (contextMenu != null)
                contextMenu.Show(this, position);
        }

        private Rectangle CaptionRectangle
        {
            get
            {
                if (!this.HasCaption)
                    return Rectangle.Empty;

                Rectangle rectWindow = this.DisplayingRectangle;
                int x, y, width;
                x = rectWindow.X;
                y = rectWindow.Y;
                width = rectWindow.Width;
                int height = this.CaptionControl.MeasureHeight();

                return new Rectangle(x, y, width, height);
            }
        }

        internal Rectangle ContentRectangle
        {
            get
            {
                Rectangle rectWindow = this.DisplayingRectangle;
                Rectangle rectCaption = this.CaptionRectangle;
                Rectangle rectTabStrip = this.TabStripRectangle;

                int x = rectWindow.X;

                int y = rectWindow.Y + (rectCaption.IsEmpty ? 0 : rectCaption.Height);
                if (this.DockState == DockState.Document && this.DockPanel.DocumentTabStripLocation == DocumentTabStripLocation.Top)
                    y += rectTabStrip.Height;

                int width = rectWindow.Width;
                int height = rectWindow.Height - rectCaption.Height - rectTabStrip.Height;

                return new Rectangle(x, y, width, height);
            }
        }

        internal Rectangle TabStripRectangle
        {
            get
            {
                if (this.Appearance == AppearanceStyle.ToolWindow)
                    return this.TabStripRectangle_ToolWindow;
                else
                    return this.TabStripRectangle_Document;
            }
        }

        private Rectangle TabStripRectangle_ToolWindow
        {
            get
            {
                if (this.DisplayingContents.Count <= 1 || this.IsAutoHide)
                    return Rectangle.Empty;

                Rectangle rectWindow = this.DisplayingRectangle;

                int width = rectWindow.Width;
                int height = this.TabStripControl.MeasureHeight();
                int x = rectWindow.X;
                int y = rectWindow.Bottom - height;
                Rectangle rectCaption = this.CaptionRectangle;
                if (rectCaption.Contains(x, y))
                    y = rectCaption.Y + rectCaption.Height;

                return new Rectangle(x, y, width, height);
            }
        }

        private Rectangle TabStripRectangle_Document
        {
            get
            {
                if (this.DisplayingContents.Count == 0)
                    return Rectangle.Empty;

                if (this.DisplayingContents.Count == 1 && this.DockPanel.DocumentStyle == DocumentStyle.DockingSdi)
                    return Rectangle.Empty;

                Rectangle rectWindow = this.DisplayingRectangle;
                int x = rectWindow.X;
                int width = rectWindow.Width;
                int height = this.TabStripControl.MeasureHeight();

                int y = 0;
                if (this.DockPanel.DocumentTabStripLocation == DocumentTabStripLocation.Bottom)
                    y = rectWindow.Height - height;
                else
                    y = rectWindow.Y;

                return new Rectangle(x, y, width, height);
            }
        }

        public virtual string CaptionText
        {
            get { return this.ActiveContent == null ? string.Empty : this.ActiveContent.DockHandler.TabText; }
        }

        private DockContentCollection m_contents;
        public DockContentCollection Contents
        {
            get { return this.m_contents; }
        }

        private DockContentCollection m_displayingContents;
        public DockContentCollection DisplayingContents
        {
            get { return this.m_displayingContents; }
        }

        private DockPanel m_dockPanel;
        public DockPanel DockPanel
        {
            get { return this.m_dockPanel; }
        }

        private bool HasCaption
        {
            get
            {
                if (this.DockState == DockState.Document ||
                    this.DockState == DockState.Hidden ||
                    this.DockState == DockState.Unknown ||
                    (this.DockState == DockState.Float && this.FloatWindow.VisibleNestedPanes.Count <= 1))
                    return false;
                else
                    return true;
            }
        }

        private bool m_isActivated;
        public bool IsActivated
        {
            get { return this.m_isActivated; }
        }
        internal void SetIsActivated(bool value)
        {
            if (this.m_isActivated == value)
                return;

            this.m_isActivated = value;
            if (this.DockState != DockState.Document)
                this.RefreshChanges(false);
            this.OnIsActivatedChanged(EventArgs.Empty);
        }

        private bool m_isActiveDocumentPane;
        public bool IsActiveDocumentPane
        {
            get { return this.m_isActiveDocumentPane; }
        }
        internal void SetIsActiveDocumentPane(bool value)
        {
            if (this.m_isActiveDocumentPane == value)
                return;

            this.m_isActiveDocumentPane = value;
            if (this.DockState == DockState.Document)
                this.RefreshChanges();
            this.OnIsActiveDocumentPaneChanged(EventArgs.Empty);
        }

        public bool IsDockStateValid(DockState dockState)
        {
            foreach (IDockContent content in this.Contents)
                if (!content.DockHandler.IsDockStateValid(dockState))
                    return false;

            return true;
        }

        public bool IsAutoHide
        {
            get { return DockHelper.IsDockStateAutoHide(this.DockState); }
        }

        public AppearanceStyle Appearance
        {
            get { return (this.DockState == DockState.Document) ? AppearanceStyle.Document : AppearanceStyle.ToolWindow; }
        }

        internal Rectangle DisplayingRectangle
        {
            get { return ClientRectangle; }
        }

        public void Activate()
        {
            if (DockHelper.IsDockStateAutoHide(this.DockState) && this.DockPanel.ActiveAutoHideContent != this.ActiveContent)
                this.DockPanel.ActiveAutoHideContent = this.ActiveContent;
            else if (!this.IsActivated && this.ActiveContent != null)
                this.ActiveContent.DockHandler.Activate();
        }

        internal void AddContent(IDockContent content)
        {
            if (this.Contents.Contains(content))
                return;

            this.Contents.Add(content);
        }

        internal void Close()
        {
            Dispose();
        }

        public void CloseActiveContent()
        {
            this.CloseContent(this.ActiveContent);
        }

        internal void CloseContent(IDockContent content)
        {
            DockPanel dockPanel = this.DockPanel;

            if (content == null)
                return;

            if (!content.DockHandler.CloseButton)
                return;

            dockPanel.SuspendLayout(true);

            try
            {
                if (content.DockHandler.HideOnClose)
                {
                    content.DockHandler.Hide();
                    this.NestedDockingStatus.NestedPanes.SwitchPaneWithFirstChild(this);
                }
                else
                    content.DockHandler.Close();
            }
            finally
            {
                dockPanel.ResumeLayout(true, true);
            }
        }

        private HitTestResult GetHitTest(Point ptMouse)
        {
            Point ptMouseClient = PointToClient(ptMouse);

            Rectangle rectCaption = this.CaptionRectangle;
            if (rectCaption.Contains(ptMouseClient))
                return new HitTestResult(HitTestArea.Caption, -1);

            Rectangle rectContent = this.ContentRectangle;
            if (rectContent.Contains(ptMouseClient))
                return new HitTestResult(HitTestArea.Content, -1);

            Rectangle rectTabStrip = this.TabStripRectangle;
            if (rectTabStrip.Contains(ptMouseClient))
                return new HitTestResult(HitTestArea.TabStrip, this.TabStripControl.HitTest(this.TabStripControl.PointToClient(ptMouse)));

            return new HitTestResult(HitTestArea.None, -1);
        }

        private bool m_isHidden = true;
        public bool IsHidden
        {
            get { return this.m_isHidden; }
        }
        private void SetIsHidden(bool value)
        {
            if (this.m_isHidden == value)
                return;

            this.m_isHidden = value;
            if (DockHelper.IsDockStateAutoHide(this.DockState))
            {
                this.DockPanel.RefreshAutoHideStrip();
                this.DockPanel.PerformLayout();
            }
            else if (this.NestedPanesContainer != null)
                ((Control)this.NestedPanesContainer).PerformLayout();
        }

        protected override void OnLayout(LayoutEventArgs levent)
        {
            this.SetIsHidden(this.DisplayingContents.Count == 0);
            if (!this.IsHidden)
            {
                this.CaptionControl.Bounds = this.CaptionRectangle;
                this.TabStripControl.Bounds = this.TabStripRectangle;

                this.SetContentBounds();

                foreach (IDockContent content in this.Contents)
                {
                    if (this.DisplayingContents.Contains(content))
                        if (content.DockHandler.FlagClipWindow && content.DockHandler.Form.Visible)
                            content.DockHandler.FlagClipWindow = false;
                }
            }

            base.OnLayout(levent);
        }

        internal void SetContentBounds()
        {
            Rectangle rectContent = this.ContentRectangle;
            if (this.DockState == DockState.Document && this.DockPanel.DocumentStyle == DocumentStyle.DockingMdi)
                rectContent = this.DockPanel.RectangleToMdiClient(RectangleToScreen(rectContent));

            var rectInactive = new Rectangle(-rectContent.Width, rectContent.Y, rectContent.Width, rectContent.Height);
            foreach (IDockContent content in this.Contents)
                if (content.DockHandler.Pane == this)
                {
                    if (content == this.ActiveContent)
                        content.DockHandler.Form.Bounds = rectContent;
                    else
                        content.DockHandler.Form.Bounds = rectInactive;
                }
        }

        internal void RefreshChanges()
        {
            this.RefreshChanges(true);
        }

        private void RefreshChanges(bool performLayout)
        {
            if (IsDisposed)
                return;

            this.CaptionControl.RefreshChanges();
            this.TabStripControl.RefreshChanges();
            if (this.DockState == DockState.Float && this.FloatWindow != null)
                this.FloatWindow.RefreshChanges();
            if (DockHelper.IsDockStateAutoHide(this.DockState) && this.DockPanel != null)
            {
                this.DockPanel.RefreshAutoHideStrip();
                this.DockPanel.PerformLayout();
            }

            if (performLayout)
                PerformLayout();
        }

        internal void RemoveContent(IDockContent content)
        {
            if (!this.Contents.Contains(content))
                return;

            this.Contents.Remove(content);
        }

        public void SetContentIndex(IDockContent content, int index)
        {
            int oldIndex = this.Contents.IndexOf(content);
            if (oldIndex == -1)
                throw (new ArgumentException(Strings.DockPane_SetContentIndex_InvalidContent));

            if (index < 0 || index > this.Contents.Count - 1)
                if (index != -1)
                    throw (new ArgumentOutOfRangeException(Strings.DockPane_SetContentIndex_InvalidIndex));

            if (oldIndex == index)
                return;
            if (oldIndex == this.Contents.Count - 1 && index == -1)
                return;

            this.Contents.Remove(content);
            if (index == -1)
                this.Contents.Add(content);
            else if (oldIndex < index)
                this.Contents.AddAt(content, index - 1);
            else
                this.Contents.AddAt(content, index);

            this.RefreshChanges();
        }

        private void SetParent()
        {
            if (this.DockState == DockState.Unknown || this.DockState == DockState.Hidden)
            {
                this.SetParent(null);
                this.Splitter.Parent = null;
            }
            else if (this.DockState == DockState.Float)
            {
                this.SetParent(this.FloatWindow);
                this.Splitter.Parent = this.FloatWindow;
            }
            else if (DockHelper.IsDockStateAutoHide(this.DockState))
            {
                this.SetParent(this.DockPanel.AutoHideControl);
                this.Splitter.Parent = null;
            }
            else
            {
                this.SetParent(this.DockPanel.DockWindows[this.DockState]);
                this.Splitter.Parent = Parent;
            }
        }

        private void SetParent(Control value)
        {
            if (Parent == value)
                return;

            //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            // Workaround of .Net Framework bug:
            // Change the parent of a control with focus may result in the first
            // MDI child form get activated. 
            //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            IDockContent contentFocused = this.GetFocusedContent();
            if (contentFocused != null)
                this.DockPanel.SaveFocus();

            //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            Parent = value;

            //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            // Workaround of .Net Framework bug:
            // Change the parent of a control with focus may result in the first
            // MDI child form get activated. 
            //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if (contentFocused != null)
                contentFocused.DockHandler.Activate();
            //!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        }

        public new void Show()
        {
            this.Activate();
        }

        internal void TestDrop(IDockDragSource dragSource, DockOutlineBase dockOutline)
        {
            if (!dragSource.CanDockTo(this))
                return;

            Point ptMouse = MousePosition;

            HitTestResult hitTestResult = this.GetHitTest(ptMouse);
            if (hitTestResult.HitArea == HitTestArea.Caption)
                dockOutline.Show(this, -1);
            else if (hitTestResult.HitArea == HitTestArea.TabStrip && hitTestResult.Index != -1)
                dockOutline.Show(this, hitTestResult.Index);
        }

        internal void ValidateActiveContent()
        {
            if (this.ActiveContent == null)
            {
                if (this.DisplayingContents.Count != 0)
                    this.ActiveContent = this.DisplayingContents[0];
                return;
            }

            if (this.DisplayingContents.IndexOf(this.ActiveContent) >= 0)
                return;

            IDockContent prevVisible = null;
            for (int i = this.Contents.IndexOf(this.ActiveContent) - 1; i >= 0; i--)
                if (this.Contents[i].DockHandler.DockState == this.DockState)
                {
                    prevVisible = this.Contents[i];
                    break;
                }

            IDockContent nextVisible = null;
            for (int i = this.Contents.IndexOf(this.ActiveContent) + 1; i < this.Contents.Count; i++)
                if (this.Contents[i].DockHandler.DockState == this.DockState)
                {
                    nextVisible = this.Contents[i];
                    break;
                }

            if (prevVisible != null)
                this.ActiveContent = prevVisible;
            else if (nextVisible != null)
                this.ActiveContent = nextVisible;
            else
                this.ActiveContent = null;
        }

        private static readonly object DockStateChangedEvent = new object();
        public event EventHandler DockStateChanged
        {
            add { Events.AddHandler(DockStateChangedEvent, value); }
            remove { Events.RemoveHandler(DockStateChangedEvent, value); }
        }
        protected virtual void OnDockStateChanged(EventArgs e)
        {
            var handler = (EventHandler)Events[DockStateChangedEvent];
            if (handler != null)
                handler(this, e);
        }

        private static readonly object IsActivatedChangedEvent = new object();
        public event EventHandler IsActivatedChanged
        {
            add { Events.AddHandler(IsActivatedChangedEvent, value); }
            remove { Events.RemoveHandler(IsActivatedChangedEvent, value); }
        }
        protected virtual void OnIsActivatedChanged(EventArgs e)
        {
            var handler = (EventHandler)Events[IsActivatedChangedEvent];
            if (handler != null)
                handler(this, e);
        }

        private static readonly object IsActiveDocumentPaneChangedEvent = new object();
        public event EventHandler IsActiveDocumentPaneChanged
        {
            add { Events.AddHandler(IsActiveDocumentPaneChangedEvent, value); }
            remove { Events.RemoveHandler(IsActiveDocumentPaneChangedEvent, value); }
        }
        protected virtual void OnIsActiveDocumentPaneChanged(EventArgs e)
        {
            var handler = (EventHandler)Events[IsActiveDocumentPaneChangedEvent];
            if (handler != null)
                handler(this, e);
        }

        public DockWindow DockWindow
        {
            get { return (this.m_nestedDockingStatus.NestedPanes == null) ? null : this.m_nestedDockingStatus.NestedPanes.Container as DockWindow; }
            set
            {
                DockWindow oldValue = this.DockWindow;
                if (oldValue == value)
                    return;

                this.DockTo(value);
            }
        }

        public FloatWindow FloatWindow
        {
            get { return (this.m_nestedDockingStatus.NestedPanes == null) ? null : this.m_nestedDockingStatus.NestedPanes.Container as FloatWindow; }
            set
            {
                FloatWindow oldValue = this.FloatWindow;
                if (oldValue == value)
                    return;

                this.DockTo(value);
            }
        }

        private NestedDockingStatus m_nestedDockingStatus;
        public NestedDockingStatus NestedDockingStatus
        {
            get { return this.m_nestedDockingStatus; }
        }

        private bool m_isFloat;
        public bool IsFloat
        {
            get { return this.m_isFloat; }
        }

        public INestedPanesContainer NestedPanesContainer
        {
            get
            {
                if (this.NestedDockingStatus.NestedPanes == null)
                    return null;
                else
                    return this.NestedDockingStatus.NestedPanes.Container;
            }
        }

        private DockState m_dockState = DockState.Unknown;
        public DockState DockState
        {
            get { return this.m_dockState; }
            set
            {
                this.SetDockState(value);
            }
        }

        public DockPane SetDockState(DockState value)
        {
            if (value == DockState.Unknown || value == DockState.Hidden)
                throw new InvalidOperationException(Strings.DockPane_SetDockState_InvalidState);

            if ((value == DockState.Float) == this.IsFloat)
            {
                this.InternalSetDockState(value);
                return this;
            }

            if (this.DisplayingContents.Count == 0)
                return null;

            IDockContent firstContent = null;
            for (int i = 0; i < this.DisplayingContents.Count; i++)
            {
                IDockContent content = this.DisplayingContents[i];
                if (content.DockHandler.IsDockStateValid(value))
                {
                    firstContent = content;
                    break;
                }
            }
            if (firstContent == null)
                return null;

            firstContent.DockHandler.DockState = value;
            DockPane pane = firstContent.DockHandler.Pane;
            this.DockPanel.SuspendLayout(true);
            for (int i = 0; i < this.DisplayingContents.Count; i++)
            {
                IDockContent content = this.DisplayingContents[i];
                if (content.DockHandler.IsDockStateValid(value))
                    content.DockHandler.Pane = pane;
            }
            this.DockPanel.ResumeLayout(true, true);
            return pane;
        }

        private void InternalSetDockState(DockState value)
        {
            if (this.m_dockState == value)
                return;

            DockState oldDockState = this.m_dockState;
            INestedPanesContainer oldContainer = this.NestedPanesContainer;

            this.m_dockState = value;

            this.SuspendRefreshStateChange();

            IDockContent contentFocused = this.GetFocusedContent();
            if (contentFocused != null)
                this.DockPanel.SaveFocus();

            if (!this.IsFloat)
                this.DockWindow = this.DockPanel.DockWindows[this.DockState];
			else if (this.FloatWindow == null)
			{
				// ****************************
					this.FloatWindow = this.DockPanel.FloatWindowFactory.CreateFloatWindow(this.DockPanel, this);
					
			}

            if (contentFocused != null)
                this.DockPanel.ContentFocusManager.Activate(contentFocused);

            this.ResumeRefreshStateChange(oldContainer, oldDockState);
        }

        private int m_countRefreshStateChange;
        private void SuspendRefreshStateChange()
        {
            this.m_countRefreshStateChange++;
            this.DockPanel.SuspendLayout(true);
        }

        private void ResumeRefreshStateChange()
        {
            this.m_countRefreshStateChange--;
            Debug.Assert(this.m_countRefreshStateChange >= 0);
            this.DockPanel.ResumeLayout(true, true);
        }

        private bool IsRefreshStateChangeSuspended
        {
            get { return this.m_countRefreshStateChange != 0; }
        }

        private void ResumeRefreshStateChange(INestedPanesContainer oldContainer, DockState oldDockState)
        {
            this.ResumeRefreshStateChange();
            this.RefreshStateChange(oldContainer, oldDockState);
        }

        private void RefreshStateChange(INestedPanesContainer oldContainer, DockState oldDockState)
        {
            lock (this)
            {
                if (this.IsRefreshStateChangeSuspended)
                    return;

                this.SuspendRefreshStateChange();
            }

            this.DockPanel.SuspendLayout(true);

            IDockContent contentFocused = this.GetFocusedContent();
            if (contentFocused != null)
                this.DockPanel.SaveFocus();
            this.SetParent();

            if (this.ActiveContent != null)
                this.ActiveContent.DockHandler.SetDockState(this.ActiveContent.DockHandler.IsHidden, this.DockState, this.ActiveContent.DockHandler.Pane);
            foreach (IDockContent content in this.Contents)
            {
                if (content.DockHandler.Pane == this)
                    content.DockHandler.SetDockState(content.DockHandler.IsHidden, this.DockState, content.DockHandler.Pane);
            }

            if (oldContainer != null)
            {
                var oldContainerControl = (Control)oldContainer;
                if (oldContainer.DockState == oldDockState && !oldContainerControl.IsDisposed)
                    oldContainerControl.PerformLayout();
            }
            if (DockHelper.IsDockStateAutoHide(oldDockState))
                this.DockPanel.RefreshActiveAutoHideContent();

            if (this.NestedPanesContainer.DockState == this.DockState)
                ((Control)this.NestedPanesContainer).PerformLayout();
            if (DockHelper.IsDockStateAutoHide(this.DockState))
                this.DockPanel.RefreshActiveAutoHideContent();

            if (DockHelper.IsDockStateAutoHide(oldDockState) ||
                DockHelper.IsDockStateAutoHide(this.DockState))
            {
                this.DockPanel.RefreshAutoHideStrip();
                this.DockPanel.PerformLayout();
            }

            this.ResumeRefreshStateChange();

            if (contentFocused != null)
                contentFocused.DockHandler.Activate();

            this.DockPanel.ResumeLayout(true, true);

            if (oldDockState != this.DockState)
                this.OnDockStateChanged(EventArgs.Empty);
        }

        private IDockContent GetFocusedContent()
        {
            IDockContent contentFocused = null;
            foreach (IDockContent content in this.Contents)
            {
                if (content.DockHandler.Form.ContainsFocus)
                {
                    contentFocused = content;
                    break;
                }
            }

            return contentFocused;
        }

        public DockPane DockTo(INestedPanesContainer container)
        {
            if (container == null)
                throw new InvalidOperationException(Strings.DockPane_DockTo_NullContainer);

            DockAlignment alignment;
            if (container.DockState == DockState.DockLeft || container.DockState == DockState.DockRight)
                alignment = DockAlignment.Bottom;
            else
                alignment = DockAlignment.Right;

            return this.DockTo(container, container.NestedPanes.GetDefaultPreviousPane(this), alignment, 0.5);
        }

        public DockPane DockTo(INestedPanesContainer container, DockPane previousPane, DockAlignment alignment, double proportion)
        {
            if (container == null)
                throw new InvalidOperationException(Strings.DockPane_DockTo_NullContainer);

            if (container.IsFloat == this.IsFloat)
            {
                this.InternalAddToDockList(container, previousPane, alignment, proportion);
                return this;
            }

            IDockContent firstContent = this.GetFirstContent(container.DockState);
            if (firstContent == null)
                return null;

            DockPane pane;
            this.DockPanel.DummyContent.DockPanel = this.DockPanel;
            if (container.IsFloat)
                pane = this.DockPanel.DockPaneFactory.CreateDockPane(this.DockPanel.DummyContent, (FloatWindow)container, true);
            else
                pane = this.DockPanel.DockPaneFactory.CreateDockPane(this.DockPanel.DummyContent, container.DockState, true);

            pane.DockTo(container, previousPane, alignment, proportion);
            this.SetVisibleContentsToPane(pane);
            this.DockPanel.DummyContent.DockPanel = null;

            return pane;
        }

        private void SetVisibleContentsToPane(DockPane pane)
        {
            this.SetVisibleContentsToPane(pane, this.ActiveContent);
        }

        private void SetVisibleContentsToPane(DockPane pane, IDockContent activeContent)
        {
            for (int i = 0; i < this.DisplayingContents.Count; i++)
            {
                IDockContent content = this.DisplayingContents[i];
                if (content.DockHandler.IsDockStateValid(pane.DockState))
                {
                    content.DockHandler.Pane = pane;
                    i--;
                }
            }

            if (activeContent.DockHandler.Pane == pane)
                pane.ActiveContent = activeContent;
        }

        private void InternalAddToDockList(INestedPanesContainer container, DockPane prevPane, DockAlignment alignment, double proportion)
        {
            if ((container.DockState == DockState.Float) != this.IsFloat)
                throw new InvalidOperationException(Strings.DockPane_DockTo_InvalidContainer);

            int count = container.NestedPanes.Count;
            if (container.NestedPanes.Contains(this))
                count--;
            if (prevPane == null && count > 0)
                throw new InvalidOperationException(Strings.DockPane_DockTo_NullPrevPane);

            if (prevPane != null && !container.NestedPanes.Contains(prevPane))
                throw new InvalidOperationException(Strings.DockPane_DockTo_NoPrevPane);

            if (prevPane == this)
                throw new InvalidOperationException(Strings.DockPane_DockTo_SelfPrevPane);

            INestedPanesContainer oldContainer = this.NestedPanesContainer;
            DockState oldDockState = this.DockState;
            container.NestedPanes.Add(this);
            this.NestedDockingStatus.SetStatus(container.NestedPanes, prevPane, alignment, proportion);

            if (DockHelper.IsDockWindowState(this.DockState))
                this.m_dockState = container.DockState;

            this.RefreshStateChange(oldContainer, oldDockState);
        }

        public void SetNestedDockingProportion(double proportion)
        {
            this.NestedDockingStatus.SetStatus(this.NestedDockingStatus.NestedPanes, this.NestedDockingStatus.PreviousPane, this.NestedDockingStatus.Alignment, proportion);
            if (this.NestedPanesContainer != null)
                ((Control)this.NestedPanesContainer).PerformLayout();
        }

        public DockPane Float()
        {
            this.DockPanel.SuspendLayout(true);

            IDockContent activeContent = this.ActiveContent;

            DockPane floatPane = this.GetFloatPaneFromContents();
            if (floatPane == null)
            {
                IDockContent firstContent = this.GetFirstContent(DockState.Float);
                if (firstContent == null)
                {
                    this.DockPanel.ResumeLayout(true, true);
                    return null;
                }
                floatPane = this.DockPanel.DockPaneFactory.CreateDockPane(firstContent, DockState.Float, true);
            }
            this.SetVisibleContentsToPane(floatPane, activeContent);

            this.DockPanel.ResumeLayout(true, true);
            return floatPane;
        }

        private DockPane GetFloatPaneFromContents()
        {
            DockPane floatPane = null;
            for (int i = 0; i < this.DisplayingContents.Count; i++)
            {
                IDockContent content = this.DisplayingContents[i];
                if (!content.DockHandler.IsDockStateValid(DockState.Float))
                    continue;

                if (floatPane != null && content.DockHandler.FloatPane != floatPane)
                    return null;
                else
                    floatPane = content.DockHandler.FloatPane;
            }

            return floatPane;
        }

        private IDockContent GetFirstContent(DockState dockState)
        {
            for (int i = 0; i < this.DisplayingContents.Count; i++)
            {
                IDockContent content = this.DisplayingContents[i];
                if (content.DockHandler.IsDockStateValid(dockState))
                    return content;
            }
            return null;
        }

        public void RestoreToPanel()
        {
            this.DockPanel.SuspendLayout(true);

            IDockContent activeContent = this.DockPanel.ActiveContent;

            for (int i = this.DisplayingContents.Count - 1; i >= 0; i--)
            {
                IDockContent content = this.DisplayingContents[i];
                if (content.DockHandler.CheckDockState(false) != DockState.Unknown)
                    content.DockHandler.IsFloat = false;
            }

            this.DockPanel.ResumeLayout(true, true);
        }

        [SecurityPermission(SecurityAction.LinkDemand, Flags = SecurityPermissionFlag.UnmanagedCode)]
        protected override void WndProc(ref Message m)
        {
            if (m.Msg == (int)Msgs.WM_MOUSEACTIVATE)
                this.Activate();

            base.WndProc(ref m);
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

            if (pane == this)
                return false;

            return true;
        }

        Rectangle IDockDragSource.BeginDrag(Point ptMouse)
        {
            Point location = PointToScreen(new Point(0, 0));
            Size size;

            DockPane floatPane = this.ActiveContent.DockHandler.FloatPane;
            if (this.DockState == DockState.Float || floatPane == null || floatPane.FloatWindow.NestedPanes.Count != 1)
                size = this.DockPanel.DefaultFloatWindowSize;
            else
                size = floatPane.FloatWindow.Size;

            if (ptMouse.X > location.X + size.Width)
                location.X += ptMouse.X - (location.X + size.Width) + Measures.SplitterSize;

            return new Rectangle(location, size);
        }

        public void FloatAt(Rectangle floatWindowBounds)
        {
			if (this.FloatWindow == null || this.FloatWindow.NestedPanes.Count != 1)
			{

				var p = new Point(floatWindowBounds.Left, floatWindowBounds.Top);
				floatWindowBounds = new Rectangle(p, (this.Contents[0] as DockContent).DefaultFloatSize);


				this.FloatWindow = this.DockPanel.FloatWindowFactory.CreateFloatWindow(this.DockPanel, this, floatWindowBounds);
			}
			else
				this.FloatWindow.Bounds = floatWindowBounds;

            this.DockState = DockState.Float;

            this.NestedDockingStatus.NestedPanes.Remove(this);
        }

        public void DockTo(DockPane pane, DockStyle dockStyle, int contentIndex)
        {
            if (dockStyle == DockStyle.Fill)
            {
                IDockContent activeContent = this.ActiveContent;
                for (int i = this.Contents.Count - 1; i >= 0; i--)
                {
                    IDockContent c = this.Contents[i];
                    if (c.DockHandler.DockState == this.DockState)
                    {
                        c.DockHandler.Pane = pane;
                        if (contentIndex != -1)
                            pane.SetContentIndex(c, contentIndex);
                    }
                }
                pane.ActiveContent = activeContent;
            }
            else
            {
                if (dockStyle == DockStyle.Left)
                    this.DockTo(pane.NestedPanesContainer, pane, DockAlignment.Left, 0.5);
                else if (dockStyle == DockStyle.Right)
                    this.DockTo(pane.NestedPanesContainer, pane, DockAlignment.Right, 0.5);
                else if (dockStyle == DockStyle.Top)
                    this.DockTo(pane.NestedPanesContainer, pane, DockAlignment.Top, 0.5);
                else if (dockStyle == DockStyle.Bottom)
                    this.DockTo(pane.NestedPanesContainer, pane, DockAlignment.Bottom, 0.5);

                this.DockState = pane.DockState;
            }
        }

        public void DockTo(DockPanel panel, DockStyle dockStyle)
        {
            if (panel != this.DockPanel)
                throw new ArgumentException(Strings.IDockDragSource_DockTo_InvalidPanel, "panel");

            if (dockStyle == DockStyle.Top)
                this.DockState = DockState.DockTop;
            else if (dockStyle == DockStyle.Bottom)
                this.DockState = DockState.DockBottom;
            else if (dockStyle == DockStyle.Left)
                this.DockState = DockState.DockLeft;
            else if (dockStyle == DockStyle.Right)
                this.DockState = DockState.DockRight;
            else if (dockStyle == DockStyle.Fill)
                this.DockState = DockState.Document;
        }

        #endregion
    }
}
