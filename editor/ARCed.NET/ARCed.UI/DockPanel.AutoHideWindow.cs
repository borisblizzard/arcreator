#region Using Directives

using System;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.UI
{
    partial class DockPanel
    {
        private class AutoHideWindowControl : Panel, ISplitterDragSource
        {
            private class SplitterControl : SplitterBase
            {
                public SplitterControl(AutoHideWindowControl autoHideWindow)
                {
                    this._mAutoHideWindow = autoHideWindow;
                }

                private readonly AutoHideWindowControl _mAutoHideWindow;
                private AutoHideWindowControl AutoHideWindow
                {
                    get { return this._mAutoHideWindow; }
                }

                protected override int SplitterSize
                {
                    get { return Measures.SplitterSize; }
                }

                protected override void StartDrag()
                {
        			this.AutoHideWindow.DockPanel.BeginDrag(this.AutoHideWindow, this.AutoHideWindow.RectangleToScreen(Bounds));
                }
            }

            #region consts
            private const int ANIMATE_TIME = 100;	// in mini-seconds
            #endregion

            private readonly Timer _mTimerMouseTrack;
            private readonly SplitterControl _mSplitter;

            public AutoHideWindowControl(DockPanel dockPanel)
            {
                this._mDockPanel = dockPanel;

                this._mTimerMouseTrack = new Timer();
                this._mTimerMouseTrack.Tick += this.TimerMouseTrack_Tick;

                Visible = false;
                this._mSplitter = new SplitterControl(this);
                Controls.Add(this._mSplitter);
            }

            protected override void Dispose(bool disposing)
            {
                if (disposing)
                {
                    this._mTimerMouseTrack.Dispose();
                }
                base.Dispose(disposing);
            }

            private readonly DockPanel _mDockPanel;
            public DockPanel DockPanel
            {
                get { return this._mDockPanel; }
            }

            private DockPane m_activePane;
            public DockPane ActivePane
            {
                get { return this.m_activePane; }
            }
            private void SetActivePane()
            {
                DockPane value = (this.ActiveContent == null ? null : this.ActiveContent.DockHandler.Pane);

                if (value == this.m_activePane)
                    return;

                this.m_activePane = value;
            }

            private IDockContent m_activeContent;
            public IDockContent ActiveContent
            {
                get { return this.m_activeContent; }
                set
                {
                    if (value == this.m_activeContent)
                        return;

                    if (value != null)
                    {
                        if (!DockHelper.IsDockStateAutoHide(value.DockHandler.DockState) || value.DockHandler.DockPanel != this.DockPanel)
                            throw (new InvalidOperationException(Strings.DockPanel_ActiveAutoHideContent_InvalidValue));
                    }

                    this.DockPanel.SuspendLayout();

                    if (this.m_activeContent != null)
                    {
                        if (this.m_activeContent.DockHandler.Form.ContainsFocus)
                            this.DockPanel.ContentFocusManager.GiveUpFocus(this.m_activeContent);
                        this.AnimateWindow(false);
                    }

                    this.m_activeContent = value;
                    this.SetActivePane();
                    if (this.ActivePane != null)
                        this.ActivePane.ActiveContent = this.m_activeContent;

                    if (this.m_activeContent != null)
                        this.AnimateWindow(true);

                    this.DockPanel.ResumeLayout();
                    this.DockPanel.RefreshAutoHideStrip();

                    this.SetTimerMouseTrack();
                }
            }

            public DockState DockState
            {
                get { return this.ActiveContent == null ? DockState.Unknown : this.ActiveContent.DockHandler.DockState; }
            }

            private bool m_flagAnimate = true;
            private bool FlagAnimate
            {
                get { return this.m_flagAnimate; }
                set { this.m_flagAnimate = value; }
            }

            private bool m_flagDragging;
            internal bool FlagDragging
            {
                get { return this.m_flagDragging; }
                set
                {
                    if (this.m_flagDragging == value)
                        return;

                    this.m_flagDragging = value;
                    this.SetTimerMouseTrack();
                }
            }

            private void AnimateWindow(bool show)
            {
                if (!this.FlagAnimate && Visible != show)
                {
                    Visible = show;
                    return;
                }

                Parent.SuspendLayout();

                Rectangle rectSource = this.GetRectangle(!show);
                Rectangle rectTarget = this.GetRectangle(show);
                int dxLoc, dyLoc;
                int dWidth, dHeight;
                dxLoc = dyLoc = dWidth = dHeight = 0;
                if (this.DockState == DockState.DockTopAutoHide)
                    dHeight = show ? 1 : -1;
                else if (this.DockState == DockState.DockLeftAutoHide)
                    dWidth = show ? 1 : -1;
                else if (this.DockState == DockState.DockRightAutoHide)
                {
                    dxLoc = show ? -1 : 1;
                    dWidth = show ? 1 : -1;
                }
                else if (this.DockState == DockState.DockBottomAutoHide)
                {
                    dyLoc = (show ? -1 : 1);
                    dHeight = (show ? 1 : -1);
                }

                if (show)
                {
                    Bounds = this.DockPanel.GetAutoHideWindowBounds(new Rectangle(-rectTarget.Width, -rectTarget.Height, rectTarget.Width, rectTarget.Height));
                    if (Visible == false)
                        Visible = true;
                    PerformLayout();
                }

                SuspendLayout();

                this.LayoutAnimateWindow(rectSource);
                if (Visible == false)
                    Visible = true;

                int speedFactor = 1;
                int totalPixels = (rectSource.Width != rectTarget.Width) ?
                    Math.Abs(rectSource.Width - rectTarget.Width) :
                    Math.Abs(rectSource.Height - rectTarget.Height);
                int remainPixels = totalPixels;
                DateTime startingTime = DateTime.Now;
                while (rectSource != rectTarget)
                {
                    DateTime startPerMove = DateTime.Now;

                    rectSource.X += dxLoc * speedFactor;
                    rectSource.Y += dyLoc * speedFactor;
                    rectSource.Width += dWidth * speedFactor;
                    rectSource.Height += dHeight * speedFactor;
                    if (Math.Sign(rectTarget.X - rectSource.X) != Math.Sign(dxLoc))
                        rectSource.X = rectTarget.X;
                    if (Math.Sign(rectTarget.Y - rectSource.Y) != Math.Sign(dyLoc))
                        rectSource.Y = rectTarget.Y;
                    if (Math.Sign(rectTarget.Width - rectSource.Width) != Math.Sign(dWidth))
                        rectSource.Width = rectTarget.Width;
                    if (Math.Sign(rectTarget.Height - rectSource.Height) != Math.Sign(dHeight))
                        rectSource.Height = rectTarget.Height;

                    this.LayoutAnimateWindow(rectSource);
                    if (Parent != null)
                        Parent.Update();

                    remainPixels -= speedFactor;

                    while (true)
                    {
                        var time = new TimeSpan(0, 0, 0, 0, ANIMATE_TIME);
                        TimeSpan elapsedPerMove = DateTime.Now - startPerMove;
                        TimeSpan elapsedTime = DateTime.Now - startingTime;
                        if (((int)((time - elapsedTime).TotalMilliseconds)) <= 0)
                        {
                            speedFactor = remainPixels;
                            break;
                        }
                        else
                            speedFactor = remainPixels * (int)elapsedPerMove.TotalMilliseconds / (int)((time - elapsedTime).TotalMilliseconds);
                        if (speedFactor >= 1)
                            break;
                    }
                }
                ResumeLayout();
                Parent.ResumeLayout();
            }

            private void LayoutAnimateWindow(Rectangle rect)
            {
                Bounds = this.DockPanel.GetAutoHideWindowBounds(rect);

                Rectangle rectClient = ClientRectangle;

                if (this.DockState == DockState.DockLeftAutoHide)
                    this.ActivePane.Location = new Point(rectClient.Right - 2 - Measures.SplitterSize - this.ActivePane.Width, this.ActivePane.Location.Y);
                else if (this.DockState == DockState.DockTopAutoHide)
                    this.ActivePane.Location = new Point(this.ActivePane.Location.X, rectClient.Bottom - 2 - Measures.SplitterSize - this.ActivePane.Height);
            }

            private Rectangle GetRectangle(bool show)
            {
                if (this.DockState == DockState.Unknown)
                    return Rectangle.Empty;

                Rectangle rect = this.DockPanel.AutoHideWindowRectangle;

                if (show)
                    return rect;

                if (this.DockState == DockState.DockLeftAutoHide)
                    rect.Width = 0;
                else if (this.DockState == DockState.DockRightAutoHide)
                {
                    rect.X += rect.Width;
                    rect.Width = 0;
                }
                else if (this.DockState == DockState.DockTopAutoHide)
                    rect.Height = 0;
                else
                {
                    rect.Y += rect.Height;
                    rect.Height = 0;
                }

                return rect;
            }

            private void SetTimerMouseTrack()
            {
                if (this.ActivePane == null || this.ActivePane.IsActivated || this.FlagDragging)
                {
                    this._mTimerMouseTrack.Enabled = false;
                    return;
                }

                // start the timer
                int hovertime = SystemInformation.MouseHoverTime ;

                // assign a default value 400 in case of setting Timer.Interval invalid value exception
                if (hovertime <= 0)
                    hovertime = 400;

                this._mTimerMouseTrack.Interval = 2 * hovertime;
                this._mTimerMouseTrack.Enabled = true;
            }

            protected virtual Rectangle DisplayingRectangle
            {
                get
                {
                    Rectangle rect = ClientRectangle;

                    // exclude the border and the splitter
                    if (this.DockState == DockState.DockBottomAutoHide)
                    {
                        rect.Y += 2 + Measures.SplitterSize;
                        rect.Height -= 2 + Measures.SplitterSize;
                    }
                    else if (this.DockState == DockState.DockRightAutoHide)
                    {
                        rect.X += 2 + Measures.SplitterSize;
                        rect.Width -= 2 + Measures.SplitterSize;
                    }
                    else if (this.DockState == DockState.DockTopAutoHide)
                        rect.Height -= 2 + Measures.SplitterSize;
                    else if (this.DockState == DockState.DockLeftAutoHide)
                        rect.Width -= 2 + Measures.SplitterSize;

                    return rect;
                }
            }

            protected override void OnLayout(LayoutEventArgs levent)
            {
                DockPadding.All = 0;
                if (this.DockState == DockState.DockLeftAutoHide)
                {
                    DockPadding.Right = 2;
                    this._mSplitter.Dock = DockStyle.Right;
                }
                else if (this.DockState == DockState.DockRightAutoHide)
                {
                    DockPadding.Left = 2;
                    this._mSplitter.Dock = DockStyle.Left;
                }
                else if (this.DockState == DockState.DockTopAutoHide)
                {
                    DockPadding.Bottom = 2;
                    this._mSplitter.Dock = DockStyle.Bottom;
                }
                else if (this.DockState == DockState.DockBottomAutoHide)
                {
                    DockPadding.Top = 2;
                    this._mSplitter.Dock = DockStyle.Top;
                }

                Rectangle rectDisplaying = this.DisplayingRectangle;
                var rectHidden = new Rectangle(-rectDisplaying.Width, rectDisplaying.Y, rectDisplaying.Width, rectDisplaying.Height);
                foreach (Control c in Controls)
                {
                    var pane = c as DockPane;
                    if (pane == null)
                        continue;
                    
                    
                    if (pane == this.ActivePane)
                        pane.Bounds = rectDisplaying;
                    else
                        pane.Bounds = rectHidden;
                }

                base.OnLayout(levent);
            }

            protected override void OnPaint(PaintEventArgs e)
            {
                // Draw the border
                Graphics g = e.Graphics;

                if (this.DockState == DockState.DockBottomAutoHide)
                    g.DrawLine(SystemPens.ControlLightLight, 0, 1, ClientRectangle.Right, 1);
                else if (this.DockState == DockState.DockRightAutoHide)
                    g.DrawLine(SystemPens.ControlLightLight, 1, 0, 1, ClientRectangle.Bottom);
                else if (this.DockState == DockState.DockTopAutoHide)
                {
                    g.DrawLine(SystemPens.ControlDark, 0, ClientRectangle.Height - 2, ClientRectangle.Right, ClientRectangle.Height - 2);
                    g.DrawLine(SystemPens.ControlDarkDark, 0, ClientRectangle.Height - 1, ClientRectangle.Right, ClientRectangle.Height - 1);
                }
                else if (this.DockState == DockState.DockLeftAutoHide)
                {
                    g.DrawLine(SystemPens.ControlDark, ClientRectangle.Width - 2, 0, ClientRectangle.Width - 2, ClientRectangle.Bottom);
                    g.DrawLine(SystemPens.ControlDarkDark, ClientRectangle.Width - 1, 0, ClientRectangle.Width - 1, ClientRectangle.Bottom);
                }

                base.OnPaint(e);
            }

            public void RefreshActiveContent()
            {
                if (this.ActiveContent == null)
                    return;

                if (!DockHelper.IsDockStateAutoHide(this.ActiveContent.DockHandler.DockState))
                {
                    this.FlagAnimate = false;
                    this.ActiveContent = null;
                    this.FlagAnimate = true;
                }
            }

            public void RefreshActivePane()
            {
                this.SetTimerMouseTrack();
            }

            private void TimerMouseTrack_Tick(object sender, EventArgs e)
            {
                if (IsDisposed)
                    return;

                if (this.ActivePane == null || this.ActivePane.IsActivated)
                {
                    this._mTimerMouseTrack.Enabled = false;
                    return;
                }

                DockPane pane = this.ActivePane;
                Point ptMouseInAutoHideWindow = PointToClient(MousePosition);
                Point ptMouseInDockPanel = this.DockPanel.PointToClient(MousePosition);

                Rectangle rectTabStrip = this.DockPanel.GetTabStripRectangle(pane.DockState);

                if (!ClientRectangle.Contains(ptMouseInAutoHideWindow) && !rectTabStrip.Contains(ptMouseInDockPanel))
                {
                    this.ActiveContent = null;
                    this._mTimerMouseTrack.Enabled = false;
                }
            }

            #region ISplitterDragSource Members

            void ISplitterDragSource.BeginDrag(Rectangle rectSplitter)
            {
                this.FlagDragging = true;
            }

            void ISplitterDragSource.EndDrag()
            {
                this.FlagDragging = false;
            }

            bool ISplitterDragSource.IsVertical
            {
                get { return (this.DockState == DockState.DockLeftAutoHide || this.DockState == DockState.DockRightAutoHide); }
            }

            Rectangle ISplitterDragSource.DragLimitBounds
            {
                get
                {
                    Rectangle rectLimit = this.DockPanel.DockArea;

                    if ((this as ISplitterDragSource).IsVertical)
                    {
                        rectLimit.X += MeasurePane.MinSize;
                        rectLimit.Width -= 2 * MeasurePane.MinSize;
                    }
                    else
                    {
                        rectLimit.Y += MeasurePane.MinSize;
                        rectLimit.Height -= 2 * MeasurePane.MinSize;
                    }

                    return this.DockPanel.RectangleToScreen(rectLimit);
                }
            }

            void ISplitterDragSource.MoveSplitter(int offset)
            {
                Rectangle rectDockArea = this.DockPanel.DockArea;
                IDockContent content = this.ActiveContent;
                if (this.DockState == DockState.DockLeftAutoHide && rectDockArea.Width > 0)
                {
                    if (content.DockHandler.AutoHidePortion < 1)
                        content.DockHandler.AutoHidePortion += (offset) / (double)rectDockArea.Width;
                    else
                        content.DockHandler.AutoHidePortion = Width + offset;
                }
                else if (this.DockState == DockState.DockRightAutoHide && rectDockArea.Width > 0)
                {
                    if (content.DockHandler.AutoHidePortion < 1)
                        content.DockHandler.AutoHidePortion -= (offset) / (double)rectDockArea.Width;
                    else
                        content.DockHandler.AutoHidePortion = Width - offset;
                }
                else if (this.DockState == DockState.DockBottomAutoHide && rectDockArea.Height > 0)
                {
                    if (content.DockHandler.AutoHidePortion < 1)
                        content.DockHandler.AutoHidePortion -= (offset) / (double)rectDockArea.Height;
                    else
                        content.DockHandler.AutoHidePortion = Height - offset;
                }
                else if (this.DockState == DockState.DockTopAutoHide && rectDockArea.Height > 0)
                {
                    if (content.DockHandler.AutoHidePortion < 1)
                        content.DockHandler.AutoHidePortion += (offset) / (double)rectDockArea.Height;
                    else
                        content.DockHandler.AutoHidePortion = Height + offset;
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

        private AutoHideWindowControl AutoHideWindow
        {
            get { return this._mAutoHideWindow; }
        }

        internal Control AutoHideControl
        {
            get { return this._mAutoHideWindow; }
        }

        internal void RefreshActiveAutoHideContent()
        {
            this.AutoHideWindow.RefreshActiveContent();
        }

        internal Rectangle AutoHideWindowRectangle
        {
            get
            {
                DockState state = this.AutoHideWindow.DockState;
                Rectangle rectDockArea = this.DockArea;
                if (this.ActiveAutoHideContent == null)
                    return Rectangle.Empty;

                if (Parent == null)
                    return Rectangle.Empty;

                Rectangle rect = Rectangle.Empty;
                double autoHideSize = this.ActiveAutoHideContent.DockHandler.AutoHidePortion;
                if (state == DockState.DockLeftAutoHide)
                {
                    if (autoHideSize < 1)
                        autoHideSize = rectDockArea.Width * autoHideSize;
                    if (autoHideSize > rectDockArea.Width - MeasurePane.MinSize)
                        autoHideSize = rectDockArea.Width - MeasurePane.MinSize;
                    rect.X = rectDockArea.X;
                    rect.Y = rectDockArea.Y;
                    rect.Width = (int)autoHideSize;
                    rect.Height = rectDockArea.Height;
                }
                else if (state == DockState.DockRightAutoHide)
                {
                    if (autoHideSize < 1)
                        autoHideSize = rectDockArea.Width * autoHideSize;
                    if (autoHideSize > rectDockArea.Width - MeasurePane.MinSize)
                        autoHideSize = rectDockArea.Width - MeasurePane.MinSize;
                    rect.X = rectDockArea.X + rectDockArea.Width - (int)autoHideSize;
                    rect.Y = rectDockArea.Y;
                    rect.Width = (int)autoHideSize;
                    rect.Height = rectDockArea.Height;
                }
                else if (state == DockState.DockTopAutoHide)
                {
                    if (autoHideSize < 1)
                        autoHideSize = rectDockArea.Height * autoHideSize;
                    if (autoHideSize > rectDockArea.Height - MeasurePane.MinSize)
                        autoHideSize = rectDockArea.Height - MeasurePane.MinSize;
                    rect.X = rectDockArea.X;
                    rect.Y = rectDockArea.Y;
                    rect.Width = rectDockArea.Width;
                    rect.Height = (int)autoHideSize;
                }
                else if (state == DockState.DockBottomAutoHide)
                {
                    if (autoHideSize < 1)
                        autoHideSize = rectDockArea.Height * autoHideSize;
                    if (autoHideSize > rectDockArea.Height - MeasurePane.MinSize)
                        autoHideSize = rectDockArea.Height - MeasurePane.MinSize;
                    rect.X = rectDockArea.X;
                    rect.Y = rectDockArea.Y + rectDockArea.Height - (int)autoHideSize;
                    rect.Width = rectDockArea.Width;
                    rect.Height = (int)autoHideSize;
                }

                return rect;
            }
        }

        internal Rectangle GetAutoHideWindowBounds(Rectangle rectAutoHideWindow)
        {
            if (this.DocumentStyle == DocumentStyle.SystemMdi ||
                this.DocumentStyle == DocumentStyle.DockingMdi)
                return (Parent == null) ? Rectangle.Empty : Parent.RectangleToClient(RectangleToScreen(rectAutoHideWindow));
            else
                return rectAutoHideWindow;
        }

        internal void RefreshAutoHideStrip()
        {
            this.AutoHideStripControl.RefreshChanges();
        }

    }
}
