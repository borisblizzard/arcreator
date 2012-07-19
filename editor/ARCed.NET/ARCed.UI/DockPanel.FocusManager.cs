#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Runtime.InteropServices;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed.UI
{
    internal interface IContentFocusManager
    {
        void Activate(IDockContent content);
        void GiveUpFocus(IDockContent content);
        void AddToList(IDockContent content);
        void RemoveFromList(IDockContent content);
    }

    partial class DockPanel
    {
        private interface IFocusManager
        {
            void SuspendFocusTracking();
            void ResumeFocusTracking();
            bool IsFocusTrackingSuspended { get; }
            IDockContent ActiveContent { get; }
            DockPane ActivePane { get; }
            IDockContent ActiveDocument { get; }
            DockPane ActiveDocumentPane { get; }
        }

        private class FocusManagerImpl : Component, IContentFocusManager, IFocusManager
        {
            private class HookEventArgs : EventArgs
            {
                [SuppressMessage("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
                public int HookCode;
                [SuppressMessage("Microsoft.Performance", "CA1823:AvoidUnusedPrivateFields")]
                public IntPtr wParam;
                public IntPtr lParam;
            }

            private class LocalWindowsHook : IDisposable
            {
                // Internal properties
                private IntPtr _mHHook = IntPtr.Zero;
                private readonly NativeMethods.HookProc _mFilterFunc;
                private readonly HookType _mHookType;

                // Event delegate
                public delegate void HookEventHandler(object sender, HookEventArgs e);

                // Event: HookInvoked 
                public event HookEventHandler HookInvoked;
                protected void OnHookInvoked(HookEventArgs e)
                {
                    if (this.HookInvoked != null)
                        this.HookInvoked(this, e);
                }

                public LocalWindowsHook(HookType hook)
                {
                    this._mHookType = hook;
                    this._mFilterFunc = this.CoreHookProc;
                }

                // Default filter function
                public IntPtr CoreHookProc(int code, IntPtr wParam, IntPtr lParam)
                {
                    if (code < 0)
                        return NativeMethods.CallNextHookEx(this._mHHook, code, wParam, lParam);

                    // Let clients determine what to do
                    var e = new HookEventArgs
                    {
                        HookCode = code,
                        wParam = wParam,
                        lParam = lParam
                    };
                    this.OnHookInvoked(e);

                    // Yield to the next hook in the chain
                    return NativeMethods.CallNextHookEx(this._mHHook, code, wParam, lParam);
                }

                // Install the hook
                public void Install()
                {
                    if (this._mHHook != IntPtr.Zero)
                        this.Uninstall();

                    int threadId = NativeMethods.GetCurrentThreadId();
                    this._mHHook = NativeMethods.SetWindowsHookEx(this._mHookType, this._mFilterFunc, IntPtr.Zero, threadId);
                }

                // Uninstall the hook
                public void Uninstall()
                {
                    if (this._mHHook != IntPtr.Zero)
                    {
                        NativeMethods.UnhookWindowsHookEx(this._mHHook);
                        this._mHHook = IntPtr.Zero;
                    }
                }

                ~LocalWindowsHook()
                {
                    this.Dispose(false);
                }

                public void Dispose()
                {
                    this.Dispose(true);
                    GC.SuppressFinalize(this);
                }

                protected virtual void Dispose(bool disposing)
                {
                    this.Uninstall();
                }
            }

            private readonly LocalWindowsHook _mLocalWindowsHook;
            private readonly LocalWindowsHook.HookEventHandler _mHookEventHandler;

            public FocusManagerImpl(DockPanel dockPanel)
            {
                this._mDockPanel = dockPanel;
                this._mLocalWindowsHook = new LocalWindowsHook(HookType.WH_CALLWNDPROCRET);
                this._mHookEventHandler = this.HookEventHandler;
                this._mLocalWindowsHook.HookInvoked += this._mHookEventHandler;
                this._mLocalWindowsHook.Install();
            }

            private readonly DockPanel _mDockPanel;
            public DockPanel DockPanel
            {
                get { return this._mDockPanel; }
            }

            private bool m_disposed;
            protected override void Dispose(bool disposing)
            {
                lock (this)
                {
                    if (!this.m_disposed && disposing)
                    {
                        this._mLocalWindowsHook.Dispose();
                        this.m_disposed = true;
                    }

                    base.Dispose(disposing);
                }
            }

            private IDockContent m_contentActivating;
            private IDockContent ContentActivating
            {
                get { return this.m_contentActivating; }
                set { this.m_contentActivating = value; }
            }

            public void Activate(IDockContent content)
            {
                if (this.IsFocusTrackingSuspended)
                {
                    this.ContentActivating = content;
                    return;
                }

                if (content == null)
                    return;
                DockContentHandler handler = content.DockHandler;
                if (handler.Form.IsDisposed)
                    return; // Should not reach here, but better than throwing an exception
                if (ContentContains(content, handler.ActiveWindowHandle))
                    NativeMethods.SetFocus(handler.ActiveWindowHandle);
                if (!handler.Form.ContainsFocus)
                {
                    if (!handler.Form.SelectNextControl(handler.Form.ActiveControl, true, true, true, true))
                        // Since DockContent Form is not selectalbe, use Win32 SetFocus instead
                        NativeMethods.SetFocus(handler.Form.Handle);
                }
            }

            private readonly List<IDockContent> _mListContent = new List<IDockContent>();
            private List<IDockContent> ListContent
            {
                get { return this._mListContent; }
            }
            public void AddToList(IDockContent content)
            {
                if (this.ListContent.Contains(content) || this.IsInActiveList(content))
                    return;

                this.ListContent.Add(content);
            }

            public void RemoveFromList(IDockContent content)
            {
                if (this.IsInActiveList(content))
                    this.RemoveFromActiveList(content);
                if (this.ListContent.Contains(content))
                    this.ListContent.Remove(content);
            }

            private IDockContent m_lastActiveContent;
            private IDockContent LastActiveContent
            {
                get { return this.m_lastActiveContent; }
                set { this.m_lastActiveContent = value; }
            }

            private bool IsInActiveList(IDockContent content)
            {
                return !(content.DockHandler.NextActive == null && this.LastActiveContent != content);
            }

            private void AddLastToActiveList(IDockContent content)
            {
                IDockContent last = this.LastActiveContent;
                if (last == content)
                    return;

                DockContentHandler handler = content.DockHandler;

                if (this.IsInActiveList(content))
                    this.RemoveFromActiveList(content);

                handler.PreviousActive = last;
                handler.NextActive = null;
                this.LastActiveContent = content;
                if (last != null)
                    last.DockHandler.NextActive = this.LastActiveContent;
            }

            private void RemoveFromActiveList(IDockContent content)
            {
                if (this.LastActiveContent == content)
                    this.LastActiveContent = content.DockHandler.PreviousActive;

                IDockContent prev = content.DockHandler.PreviousActive;
                IDockContent next = content.DockHandler.NextActive;
                if (prev != null)
                    prev.DockHandler.NextActive = next;
                if (next != null)
                    next.DockHandler.PreviousActive = prev;

                content.DockHandler.PreviousActive = null;
                content.DockHandler.NextActive = null;
            }

            public void GiveUpFocus(IDockContent content)
            {
                DockContentHandler handler = content.DockHandler;
                if (!handler.Form.ContainsFocus)
                    return;

                if (this.IsFocusTrackingSuspended)
                    this.DockPanel.DummyControl.Focus();

                if (this.LastActiveContent == content)
                {
                    IDockContent prev = handler.PreviousActive;
                    if (prev != null)
                        this.Activate(prev);
                    else if (this.ListContent.Count > 0)
                        this.Activate(this.ListContent[this.ListContent.Count - 1]);
                }
                else if (this.LastActiveContent != null)
                    this.Activate(this.LastActiveContent);
                else if (this.ListContent.Count > 0)
                    this.Activate(this.ListContent[this.ListContent.Count - 1]);
            }

            private static bool ContentContains(IDockContent content, IntPtr hWnd)
            {
                Control control = FromChildHandle(hWnd);
                for (Control parent = control; parent != null; parent = parent.Parent)
                    if (parent == content.DockHandler.Form)
                        return true;

                return false;
            }

            private int m_countSuspendFocusTracking;
            public void SuspendFocusTracking()
            {
                this.m_countSuspendFocusTracking++;
                this._mLocalWindowsHook.HookInvoked -= this._mHookEventHandler;
            }

            public void ResumeFocusTracking()
            {
                if (this.m_countSuspendFocusTracking > 0)
                    this.m_countSuspendFocusTracking--;

                if (this.m_countSuspendFocusTracking == 0)
                {
                    if (this.ContentActivating != null)
                    {
                        this.Activate(this.ContentActivating);
                        this.ContentActivating = null;
                    }
                    this._mLocalWindowsHook.HookInvoked += this._mHookEventHandler;
                    if (!this.InRefreshActiveWindow)
                        this.RefreshActiveWindow();
                }
            }

            public bool IsFocusTrackingSuspended
            {
                get { return this.m_countSuspendFocusTracking != 0; }
            }

            // Windows hook event handler
            private void HookEventHandler(object sender, HookEventArgs e)
            {
                var msg = (Msgs)Marshal.ReadInt32(e.lParam, IntPtr.Size * 3);

                if (msg == Msgs.WM_KILLFOCUS)
                {
                    IntPtr wParam = Marshal.ReadIntPtr(e.lParam, IntPtr.Size * 2);
                    DockPane pane = this.GetPaneFromHandle(wParam);
                    if (pane == null)
                        this.RefreshActiveWindow();
                }
                else if (msg == Msgs.WM_SETFOCUS)
                    this.RefreshActiveWindow();
            }

            private DockPane GetPaneFromHandle(IntPtr hWnd)
            {
                Control control = FromChildHandle(hWnd);

                IDockContent content = null;
                DockPane pane = null;
                for (; control != null; control = control.Parent)
                {
                    content = control as IDockContent;
                    if (content != null)
                        content.DockHandler.ActiveWindowHandle = hWnd;

                    if (content != null && content.DockHandler.DockPanel == this.DockPanel)
                        return content.DockHandler.Pane;

                    pane = control as DockPane;
                    if (pane != null && pane.DockPanel == this.DockPanel)
                        break;
                }

                return pane;
            }

            private bool m_inRefreshActiveWindow;
            private bool InRefreshActiveWindow
            {
                get { return this.m_inRefreshActiveWindow; }
            }

            private void RefreshActiveWindow()
            {
                this.SuspendFocusTracking();
                this.m_inRefreshActiveWindow = true;

                DockPane oldActivePane = this.ActivePane;
                IDockContent oldActiveContent = this.ActiveContent;
                IDockContent oldActiveDocument = this.ActiveDocument;

                this.SetActivePane();
                this.SetActiveContent();
                this.SetActiveDocumentPane();
                this.SetActiveDocument();
                this.DockPanel.AutoHideWindow.RefreshActivePane();

                this.ResumeFocusTracking();
                this.m_inRefreshActiveWindow = false;

                if (oldActiveContent != this.ActiveContent)
                    this.DockPanel.OnActiveContentChanged(EventArgs.Empty);
                if (oldActiveDocument != this.ActiveDocument)
                    this.DockPanel.OnActiveDocumentChanged(EventArgs.Empty);
                if (oldActivePane != this.ActivePane)
                    this.DockPanel.OnActivePaneChanged(EventArgs.Empty);
            }

            private DockPane m_activePane;
            public DockPane ActivePane
            {
                get { return this.m_activePane; }
            }

            private void SetActivePane()
            {
                DockPane value = this.GetPaneFromHandle(NativeMethods.GetFocus());
                if (this.m_activePane == value)
                    return;

                if (this.m_activePane != null)
                    this.m_activePane.SetIsActivated(false);

                this.m_activePane = value;

                if (this.m_activePane != null)
                    this.m_activePane.SetIsActivated(true);
            }

            private IDockContent m_activeContent;
            public IDockContent ActiveContent
            {
                get { return this.m_activeContent; }
            }

            internal void SetActiveContent()
            {
                IDockContent value = this.ActivePane == null ? null : this.ActivePane.ActiveContent;

                if (this.m_activeContent == value)
                    return;

                if (this.m_activeContent != null)
                    this.m_activeContent.DockHandler.IsActivated = false;

                this.m_activeContent = value;

                if (this.m_activeContent != null)
                {
                    this.m_activeContent.DockHandler.IsActivated = true;
                    if (!DockHelper.IsDockStateAutoHide((this.m_activeContent.DockHandler.DockState)))
                        this.AddLastToActiveList(this.m_activeContent);
                }
            }

            private DockPane m_activeDocumentPane;
            public DockPane ActiveDocumentPane
            {
                get { return this.m_activeDocumentPane; }
            }

            private void SetActiveDocumentPane()
            {
                DockPane value = null;

                if (this.ActivePane != null && this.ActivePane.DockState == DockState.Document)
                    value = this.ActivePane;

                if (value == null && this.DockPanel.DockWindows != null)
                {
                    if (this.ActiveDocumentPane == null)
                        value = this.DockPanel.DockWindows[DockState.Document].DefaultPane;
                    else if (this.ActiveDocumentPane.DockPanel != this.DockPanel || this.ActiveDocumentPane.DockState != DockState.Document)
                        value = this.DockPanel.DockWindows[DockState.Document].DefaultPane;
                    else
                        value = this.ActiveDocumentPane;
                }

                if (this.m_activeDocumentPane == value)
                    return;

                if (this.m_activeDocumentPane != null)
                    this.m_activeDocumentPane.SetIsActiveDocumentPane(false);

                this.m_activeDocumentPane = value;

                if (this.m_activeDocumentPane != null)
                    this.m_activeDocumentPane.SetIsActiveDocumentPane(true);
            }

            private IDockContent m_activeDocument;
            public IDockContent ActiveDocument
            {
                get { return this.m_activeDocument; }
            }

            private void SetActiveDocument()
            {
                IDockContent value = this.ActiveDocumentPane == null ? null : this.ActiveDocumentPane.ActiveContent;

                if (this.m_activeDocument == value)
                    return;

                this.m_activeDocument = value;
            }
        }

        private IFocusManager FocusManager
        {
            get { return this._mFocusManager; }
        }

        internal IContentFocusManager ContentFocusManager
        {
            get { return this._mFocusManager; }
        }

        internal void SaveFocus()
        {
            this.DummyControl.Focus();
        }

        [Browsable(false)]
        public IDockContent ActiveContent
        {
            get { return this.FocusManager.ActiveContent; }
        }

        [Browsable(false)]
        public DockPane ActivePane
        {
            get { return this.FocusManager.ActivePane; }
        }

        [Browsable(false)]
        public IDockContent ActiveDocument
        {
            get { return this.FocusManager.ActiveDocument; }
        }

        [Browsable(false)]
        public DockPane ActiveDocumentPane
        {
            get { return this.FocusManager.ActiveDocumentPane; }
        }

        private static readonly object ActiveDocumentChangedEvent = new object();
        [LocalizedCategory("Category_PropertyChanged")]
        [LocalizedDescription("DockPanel_ActiveDocumentChanged_Description")]
        public event EventHandler ActiveDocumentChanged
        {
            add { Events.AddHandler(ActiveDocumentChangedEvent, value); }
            remove { Events.RemoveHandler(ActiveDocumentChangedEvent, value); }
        }
        protected virtual void OnActiveDocumentChanged(EventArgs e)
        {
            var handler = (EventHandler)Events[ActiveDocumentChangedEvent];
            if (handler != null)
                handler(this, e);
        }

        private static readonly object ActiveContentChangedEvent = new object();
        [LocalizedCategory("Category_PropertyChanged")]
        [LocalizedDescription("DockPanel_ActiveContentChanged_Description")]
        public event EventHandler ActiveContentChanged
        {
            add { Events.AddHandler(ActiveContentChangedEvent, value); }
            remove { Events.RemoveHandler(ActiveContentChangedEvent, value); }
        }
        protected void OnActiveContentChanged(EventArgs e)
        {
            var handler = (EventHandler)Events[ActiveContentChangedEvent];
            if (handler != null)
                handler(this, e);
        }

        private static readonly object ActivePaneChangedEvent = new object();
        [LocalizedCategory("Category_PropertyChanged")]
        [LocalizedDescription("DockPanel_ActivePaneChanged_Description")]
        public event EventHandler ActivePaneChanged
        {
            add { Events.AddHandler(ActivePaneChangedEvent, value); }
            remove { Events.RemoveHandler(ActivePaneChangedEvent, value); }
        }
        protected virtual void OnActivePaneChanged(EventArgs e)
        {
            var handler = (EventHandler)Events[ActivePaneChangedEvent];
            if (handler != null)
                handler(this, e);
        }
    }
}
