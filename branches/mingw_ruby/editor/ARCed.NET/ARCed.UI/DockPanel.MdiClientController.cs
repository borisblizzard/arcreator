#region Using Directives

using System;
using System.ComponentModel;
using System.ComponentModel.Design;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Core.Win32;
using ScrollBars = ARCed.Core.Win32.ScrollBars;

#endregion

namespace ARCed.UI
{
    partial class DockPanel
    {
        //  This class comes from Jacob Slusser's MdiClientController class:
        //  http://www.codeproject.com/cs/miscctrl/mdiclientcontroller.asp
        private class MdiClientController : NativeWindow, IComponent, IDisposable
        {
            private bool m_autoScroll = true;
            private BorderStyle m_borderStyle = BorderStyle.Fixed3D;
            private MdiClient m_mdiClient;
            private Form m_parentForm;
            private ISite m_site;

            public void Dispose()
            {
                this.Dispose(true);
                GC.SuppressFinalize(this);
            }

            protected virtual void Dispose(bool disposing)
            {
                if (disposing)
                {
                    lock (this)
                    {
                        if (this.Site != null && this.Site.Container != null)
                            this.Site.Container.Remove(this);

                        if (this.Disposed != null)
                            this.Disposed(this, EventArgs.Empty);
                    }
                }
            }

            public bool AutoScroll
            {
                get { return this.m_autoScroll; }
                set
                {
                    // By default the MdiClient control scrolls. It can appear though that
                    // there are no scrollbars by turning them off when the non-client
                    // area is calculated. I decided to expose this method following
                    // the .NET vernacular of an AutoScroll property.
                    this.m_autoScroll = value;
                    if (this.MdiClient != null)
                        this.UpdateStyles();
                }
            }

            public BorderStyle BorderStyle
            {
                set
                {
                    // Error-check the enum.
                    if (!Enum.IsDefined(typeof(BorderStyle), value))
                        throw new InvalidEnumArgumentException();

                    this.m_borderStyle = value;

                    if (this.MdiClient == null)
                        return;

                    // This property can actually be visible in design-mode,
                    // but to keep it consistent with the others,
                    // prevent this from being show at design-time.
                    if (this.Site != null && this.Site.DesignMode)
                        return;

                    // There is no BorderStyle property exposed by the MdiClient class,
                    // but this can be controlled by Win32 functions. A Win32 ExStyle
                    // of WS_EX_CLIENTEDGE is equivalent to a Fixed3D border and a
                    // Style of WS_BORDER is equivalent to a FixedSingle border.

                    // This code is inspired Jason Dori's article:
                    // "Adding designable borders to user controls".
                    // http://www.codeproject.com/cs/miscctrl/CsAddingBorders.asp

                    // Get styles using Win32 calls
                    int style = NativeMethods.GetWindowLong(this.MdiClient.Handle, (int)GetWindowLongIndex.GWL_STYLE);
                    int exStyle = NativeMethods.GetWindowLong(this.MdiClient.Handle, (int)GetWindowLongIndex.GWL_EXSTYLE);

                    // Add or remove style flags as necessary.
                    switch (this.m_borderStyle)
                    {
                        case BorderStyle.Fixed3D:
                            exStyle |= (int)WindowExStyles.WS_EX_CLIENTEDGE;
                            style &= ~((int)WindowStyles.WS_BORDER);
                            break;

                        case BorderStyle.FixedSingle:
                            exStyle &= ~((int)WindowExStyles.WS_EX_CLIENTEDGE);
                            style |= (int)WindowStyles.WS_BORDER;
                            break;

                        case BorderStyle.None:
                            style &= ~((int)WindowStyles.WS_BORDER);
                            exStyle &= ~((int)WindowExStyles.WS_EX_CLIENTEDGE);
                            break;
                    }

                    // Set the styles using Win32 calls
                    NativeMethods.SetWindowLong(this.MdiClient.Handle, (int)GetWindowLongIndex.GWL_STYLE, style);
                    NativeMethods.SetWindowLong(this.MdiClient.Handle, (int)GetWindowLongIndex.GWL_EXSTYLE, exStyle);

                    // Cause an update of the non-client area.
                    this.UpdateStyles();
                }
            }

            public MdiClient MdiClient
            {
                get { return this.m_mdiClient; }
            }

            [Browsable(false)]
            public Form ParentForm
            {
                get { return this.m_parentForm; }
                set
                {
                    // If the ParentForm has previously been set,
                    // unwire events connected to the old parent.
                    if (this.m_parentForm != null)
                    {
                        this.m_parentForm.HandleCreated -= this.ParentFormHandleCreated;
                        this.m_parentForm.MdiChildActivate -= this.ParentFormMdiChildActivate;
                    }

                    this.m_parentForm = value;

                    if (this.m_parentForm == null)
                        return;

                    // If the parent form has not been created yet,
                    // wait to initialize the MDI client until it is.
                    if (this.m_parentForm.IsHandleCreated)
                    {
                        this.InitializeMdiClient();
                        this.RefreshProperties();
                    }
                    else
                        this.m_parentForm.HandleCreated += this.ParentFormHandleCreated;

                    this.m_parentForm.MdiChildActivate += this.ParentFormMdiChildActivate;
                }
            }

            public ISite Site
            {
                get { return this.m_site; }
                set
                {
                    this.m_site = value;

                    if (this.m_site == null)
                        return;

                    // If the component is dropped onto a form during design-time,
                    // set the ParentForm property.
                    var host = (value.GetService(typeof(IDesignerHost)) as IDesignerHost);
                    if (host != null)
                    {
                        var parent = host.RootComponent as Form;
                        if (parent != null)
                            this.ParentForm = parent;
                    }
                }
            }

            public void RenewMdiClient()
            {
                // Reinitialize the MdiClient and its properties.
                this.InitializeMdiClient();
                this.RefreshProperties();
            }

            public event EventHandler Disposed;

            public event EventHandler HandleAssigned;

            public event EventHandler MdiChildActivate;

            public event LayoutEventHandler Layout;

            protected virtual void OnHandleAssigned(EventArgs e)
            {
                // Raise the HandleAssigned event.
                if (this.HandleAssigned != null)
                    this.HandleAssigned(this, e);
            }

            protected virtual void OnMdiChildActivate(EventArgs e)
            {
                // Raise the MdiChildActivate event
                if (this.MdiChildActivate != null)
                    this.MdiChildActivate(this, e);
            }

            protected virtual void OnLayout(LayoutEventArgs e)
            {
                // Raise the Layout event
                if (this.Layout != null)
                    this.Layout(this, e);
            }

            public event PaintEventHandler Paint;

            protected virtual void OnPaint(PaintEventArgs e)
            {
                // Raise the Paint event.
                if (this.Paint != null)
                    this.Paint(this, e);
            }

            protected override void WndProc(ref Message m)
            {
                switch (m.Msg)
                {
                    case (int)Msgs.WM_NCCALCSIZE:
                        // If AutoScroll is set to false, hide the scrollbars when the control
                        // calculates its non-client area.
                        if (!this.AutoScroll)
                            NativeMethods.ShowScrollBar(m.HWnd, (int)ScrollBars.SB_BOTH, 0 /*false*/);
                        break;
                }

                base.WndProc(ref m);
            }

            private void ParentFormHandleCreated(object sender, EventArgs e)
            {
                // The form has been created, unwire the event, and initialize the MdiClient.
                this.m_parentForm.HandleCreated -= this.ParentFormHandleCreated;
                this.InitializeMdiClient();
                this.RefreshProperties();
            }

            private void ParentFormMdiChildActivate(object sender, EventArgs e)
            {
                this.OnMdiChildActivate(e);
            }

            private void MdiClientLayout(object sender, LayoutEventArgs e)
            {
                this.OnLayout(e);
            }

            private void MdiClientHandleDestroyed(object sender, EventArgs e)
            {
                // If the MdiClient handle has been released, drop the reference and
                // release the handle.
                if (this.m_mdiClient != null)
                {
                    this.m_mdiClient.HandleDestroyed -= this.MdiClientHandleDestroyed;
                    this.m_mdiClient = null;
                }

                ReleaseHandle();
            }

            private void InitializeMdiClient()
            {
                // If the mdiClient has previously been set, unwire events connected
                // to the old MDI.
                if (this.MdiClient != null)
                {
                    this.MdiClient.HandleDestroyed -= this.MdiClientHandleDestroyed;
                    this.MdiClient.Layout -= this.MdiClientLayout;
                }

                if (this.ParentForm == null)
                    return;

                // Get the MdiClient from the parent form.
                foreach (Control control in this.ParentForm.Controls)
                {
                    // If the form is an MDI container, it will contain an MdiClient control
                    // just as it would any other control.

                    this.m_mdiClient = control as MdiClient;
                    if (this.m_mdiClient == null)
                        continue;

                    // Assign the MdiClient Handle to the NativeWindow.
                    ReleaseHandle();
                    AssignHandle(this.MdiClient.Handle);

                    // Raise the HandleAssigned event.
                    this.OnHandleAssigned(EventArgs.Empty);

                    // Monitor the MdiClient for when its handle is destroyed.
                    this.MdiClient.HandleDestroyed += this.MdiClientHandleDestroyed;
                    this.MdiClient.Layout += this.MdiClientLayout;

                    break;
                }
            }

            private void RefreshProperties()
            {
                // Refresh all the properties
                this.BorderStyle = this.m_borderStyle;
                this.AutoScroll = this.m_autoScroll;
            }

            private void UpdateStyles()
            {
                // To show style changes, the non-client area must be repainted. Using the
                // control's Invalidate method does not affect the non-client area.
                // Instead use a Win32 call to signal the style has changed.
                NativeMethods.SetWindowPos(this.MdiClient.Handle, IntPtr.Zero, 0, 0, 0, 0,
                    FlagsSetWindowPos.SWP_NOACTIVATE |
                    FlagsSetWindowPos.SWP_NOMOVE |
                    FlagsSetWindowPos.SWP_NOSIZE |
                    FlagsSetWindowPos.SWP_NOZORDER |
                    FlagsSetWindowPos.SWP_NOOWNERZORDER |
                    FlagsSetWindowPos.SWP_FRAMECHANGED);
            }
        }

        private MdiClientController m_mdiClientController;
        private MdiClientController GetMdiClientController()
        {
            if (this.m_mdiClientController == null)
            {
                this.m_mdiClientController = new MdiClientController();
                this.m_mdiClientController.HandleAssigned += this.MdiClientHandleAssigned;
                this.m_mdiClientController.MdiChildActivate += this.ParentFormMdiChildActivate;
                this.m_mdiClientController.Layout += this.MdiClient_Layout;
            }

            return this.m_mdiClientController;
        }

        private void ParentFormMdiChildActivate(object sender, EventArgs e)
        {
            if (this.GetMdiClientController().ParentForm == null)
                return;

            var content = this.GetMdiClientController().ParentForm.ActiveMdiChild as IDockContent;
            if (content == null)
                return;

            if (content.DockHandler.DockPanel == this && content.DockHandler.Pane != null)
                content.DockHandler.Pane.ActiveContent = content;
        }

        private bool MdiClientExists
        {
            get { return this.GetMdiClientController().MdiClient != null; }
        }

        private void SetMdiClientBounds(Rectangle bounds)
        {
            this.GetMdiClientController().MdiClient.Bounds = bounds;
        }

        private void SuspendMdiClientLayout()
        {
            if (this.GetMdiClientController().MdiClient != null)
                this.GetMdiClientController().MdiClient.SuspendLayout();
        }

        private void ResumeMdiClientLayout(bool perform)
        {
            if (this.GetMdiClientController().MdiClient != null)
                this.GetMdiClientController().MdiClient.ResumeLayout(perform);
        }

        private void PerformMdiClientLayout()
        {
            if (this.GetMdiClientController().MdiClient != null)
                this.GetMdiClientController().MdiClient.PerformLayout();
        }

        // Called when:
        // 1. DockPanel.DocumentStyle changed
        // 2. DockPanel.Visible changed
        // 3. MdiClientController.Handle assigned
        private void SetMdiClient()
        {
            MdiClientController controller = this.GetMdiClientController();

            if (this.DocumentStyle == DocumentStyle.DockingMdi)
            {
                controller.AutoScroll = false;
                controller.BorderStyle = BorderStyle.None;
                if (this.MdiClientExists)
                    controller.MdiClient.Dock = DockStyle.Fill;
            }
            else if (this.DocumentStyle == DocumentStyle.DockingSdi || this.DocumentStyle == DocumentStyle.DockingWindow)
            {
                controller.AutoScroll = true;
                controller.BorderStyle = BorderStyle.Fixed3D;
                if (this.MdiClientExists)
                    controller.MdiClient.Dock = DockStyle.Fill;
            }
            else if (this.DocumentStyle == DocumentStyle.SystemMdi)
            {
                controller.AutoScroll = true;
                controller.BorderStyle = BorderStyle.Fixed3D;
                if (controller.MdiClient != null)
                {
                    controller.MdiClient.Dock = DockStyle.None;
                    controller.MdiClient.Bounds = this.SystemMdiClientBounds;
                }
            }
        }

        internal Rectangle RectangleToMdiClient(Rectangle rect)
        {
            if (this.MdiClientExists)
                return this.GetMdiClientController().MdiClient.RectangleToClient(rect);
            else
                return Rectangle.Empty;
        }
    }
}
