#region Using Directives

using System.Drawing;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed.UI
{
    partial class DockPanel
    {
        /// <summary>
        /// DragHandlerBase is the base class for drag handlers. The derived class should:
        ///   1. Define its public method BeginDrag. From within this public BeginDrag method,
        ///      DragHandlerBase.BeginDrag should be called to initialize the mouse capture
        ///      and message filtering.
        ///   2. Override the OnDragging and OnEndDrag methods.
        /// </summary>
        private abstract class DragHandlerBase : NativeWindow, IMessageFilter
        {
            protected abstract Control DragControl
            {
                get;
            }

            private Point m_startMousePosition = Point.Empty;
            protected Point StartMousePosition
            {
                get { return this.m_startMousePosition; }
                private set { this.m_startMousePosition = value; }
            }

            protected bool BeginDrag()
            {
                // Avoid re-entrance;
                lock (this)
                {
                    if (this.DragControl == null)
                        return false;

                    this.StartMousePosition = MousePosition;

                    if (!NativeMethods.DragDetect(this.DragControl.Handle, this.StartMousePosition))
                        return false;

                    this.DragControl.FindForm().Capture = true;
                    AssignHandle(this.DragControl.FindForm().Handle);
                    Application.AddMessageFilter(this);
                    return true;
                }
            }

            protected abstract void OnDragging();

            protected abstract void OnEndDrag(bool abort);

            private void EndDrag(bool abort)
            {
                ReleaseHandle();
                Application.RemoveMessageFilter(this);
                this.DragControl.FindForm().Capture = false;

                this.OnEndDrag(abort);
            }

            bool IMessageFilter.PreFilterMessage(ref Message m)
            {
                if (m.Msg == (int)Msgs.WM_MOUSEMOVE)
                    this.OnDragging();
                else if (m.Msg == (int)Msgs.WM_LBUTTONUP)
                    this.EndDrag(false);
                else if (m.Msg == (int)Msgs.WM_CAPTURECHANGED)
                    this.EndDrag(true);
                else if (m.Msg == (int)Msgs.WM_KEYDOWN && (int)m.WParam == (int)Keys.Escape)
                    this.EndDrag(true);

                return this.OnPreFilterMessage(ref m);
            }

            protected virtual bool OnPreFilterMessage(ref Message m)
            {
                return false;
            }

            protected sealed override void WndProc(ref Message m)
            {
                if (m.Msg == (int)Msgs.WM_CANCELMODE || m.Msg == (int)Msgs.WM_CAPTURECHANGED)
                    this.EndDrag(true);

                base.WndProc(ref m);
            }
        }

        private abstract class DragHandler : DragHandlerBase
        {
            private readonly DockPanel _mDockPanel;

            protected DragHandler(DockPanel dockPanel)
            {
                this._mDockPanel = dockPanel;
            }

            public DockPanel DockPanel
            {
                get { return this._mDockPanel; }
            }

            private IDragSource m_dragSource;
            protected IDragSource DragSource
            {
                get { return this.m_dragSource; }
                set { this.m_dragSource = value; }
            }

            protected sealed override Control DragControl
            {
                get { return this.DragSource == null ? null : this.DragSource.DragControl; }
            }

            protected sealed override bool OnPreFilterMessage(ref Message m)
            {
                if ((m.Msg == (int)Msgs.WM_KEYDOWN || m.Msg == (int)Msgs.WM_KEYUP) &&
                    ((int)m.WParam == (int)Keys.ControlKey || (int)m.WParam == (int)Keys.ShiftKey))
                    OnDragging();

                return base.OnPreFilterMessage(ref m);
            }
        }
    }
}
