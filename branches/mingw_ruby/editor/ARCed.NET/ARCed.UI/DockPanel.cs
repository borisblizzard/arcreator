#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Drawing;
using System.Windows.Forms;
using System.Windows.Forms.Design;

#endregion

// To simplify the process of finding the toolbox image resource:
// #1 Create an internal class called "resfinder" outside of the root namespace.
// #2 Use "resfinder" in the toolbox image attribute instead of the control name.
// #3 use the "<default namespace>.<resourcename>" string to locate the resource.
// See: http://www.bobpowell.net/toolboxbitmap.htm
internal class resfinder
{
}

namespace ARCed.UI
{
    [SuppressMessage("Microsoft.Naming", "CA1720:AvoidTypeNamesInParameters", MessageId = "0#")]
	public delegate IDockContent DeserializeDockContent(string persistString);

    [LocalizedDescription("DockPanel_Description")]
    [Designer(typeof(ControlDesigner))]
    [ToolboxBitmap(typeof(resfinder), "ARCed.UI.DockPanel.bmp")]
    [DefaultProperty("DocumentStyle")]
    [DefaultEvent("ActiveContentChanged")]
	public partial class DockPanel : Panel
	{
        private readonly FocusManagerImpl _mFocusManager;
        private readonly DockPanelExtender _mExtender;
        private readonly DockPaneCollection _mPanes;
        private readonly FloatWindowCollection _mFloatWindows;
        private readonly AutoHideWindowControl _mAutoHideWindow;
        private readonly DockWindowCollection _mDockWindows;
        private readonly DockContent _mDummyContent;
        private readonly Control _mDummyControl;
        
		public DockPanel()
		{
            this._mFocusManager = new FocusManagerImpl(this);
			this._mExtender = new DockPanelExtender(this);
			this._mPanes = new DockPaneCollection();
			this._mFloatWindows = new FloatWindowCollection();

            SuspendLayout();

			this._mAutoHideWindow = new AutoHideWindowControl(this)
			{
			    Visible = false
			};
		    this.SetAutoHideWindowParent();

			this._mDummyControl = new DummyControl
			{
			    Bounds = new Rectangle(0, 0, 1, 1)
			};
		    Controls.Add(this._mDummyControl);

			this._mDockWindows = new DockWindowCollection(this);
			Controls.AddRange(new Control[]	{
				this.DockWindows[DockState.Document],
				this.DockWindows[DockState.DockLeft],
				this.DockWindows[DockState.DockRight],
				this.DockWindows[DockState.DockTop],
				this.DockWindows[DockState.DockBottom]
				});

			this._mDummyContent = new DockContent();
            ResumeLayout();
        }
        
        private Color m_BackColor;
        /// <summary>
        /// Determines the color with which the client rect will be drawn.
        /// If this property is used instead of the BackColor it will not have any influence on the borders to the surrounding controls (DockPane).
        /// The BackColor property changes the borders of surrounding controls (DockPane).
        /// Alternatively both properties may be used (BackColor to draw and define the color of the borders and DockBackColor to define the color of the client rect). 
        /// For Backgroundimages: Set your prefered Image, then set the DockBackColor and the BackColor to the same Color (Control)
        /// </summary>
        [Description("Determines the color with which the client rectangle will be drawn.\r\n" +
            "If this property is used instead of the BackColor it will not have any influence on the borders to the surrounding controls (DockPane).\r\n" +
            "The BackColor property changes the borders of surrounding controls (DockPane).\r\n" +
            "Alternatively both properties may be used (BackColor to draw and define the color of the borders and DockBackColor to define the color of the client rectangle).\r\n" +
            "For Backgroundimages: Set your prefered Image, then set the DockBackColor and the BackColor to the same Color (Control).")]
        public Color DockBackColor
        {
            get
            {
                return !this.m_BackColor.IsEmpty ? this.m_BackColor : base.BackColor;
            }
            set
            {
                if (this.m_BackColor != value)
                {
                    this.m_BackColor = value;
                    Refresh();
                }
            }
        }

		private AutoHideStripBase m_autoHideStripControl;
		internal AutoHideStripBase AutoHideStripControl
		{
			get
			{	
				if (this.m_autoHideStripControl == null)
				{
					this.m_autoHideStripControl = this.AutoHideStripFactory.CreateAutoHideStrip(this);
					Controls.Add(this.m_autoHideStripControl);
				}
				return this.m_autoHideStripControl;
			}
		}
        internal void ResetAutoHideStripControl()
        {
            if (this.m_autoHideStripControl != null)
                this.m_autoHideStripControl.Dispose();

            this.m_autoHideStripControl = null;
        }

		private void MdiClientHandleAssigned(object sender, EventArgs e)
		{
			this.SetMdiClient();
			PerformLayout();
		}

		private void MdiClient_Layout(object sender, LayoutEventArgs e)
		{
			if (this.DocumentStyle != DocumentStyle.DockingMdi)
				return;

			foreach (DockPane pane in this.Panes)
				if (pane.DockState == DockState.Document)
					pane.SetContentBounds();

			this.InvalidateWindowRegion();
		}

		private bool m_disposed;
		protected override void Dispose(bool disposing)
		{
			lock (this)
			{
				if (!this.m_disposed && disposing)
				{
                    this._mFocusManager.Dispose();
					if (this.m_mdiClientController != null)
					{
						this.m_mdiClientController.HandleAssigned -= this.MdiClientHandleAssigned;
						this.m_mdiClientController.MdiChildActivate -= this.ParentFormMdiChildActivate;
						this.m_mdiClientController.Layout -= this.MdiClient_Layout;
						this.m_mdiClientController.Dispose();
					}
					this.FloatWindows.Dispose();
					this.Panes.Dispose();
					this.DummyContent.Dispose();

					this.m_disposed = true;
				}
				
				base.Dispose(disposing);
			}
		}

		[Browsable(false)]
		public IDockContent ActiveAutoHideContent
		{
			get	{	return this.AutoHideWindow.ActiveContent;	}
			set	{	this.AutoHideWindow.ActiveContent = value;	}
		}

        private bool m_allowEndUserDocking = true;
		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockPanel_AllowEndUserDocking_Description")]
		[DefaultValue(true)]
		public bool AllowEndUserDocking
		{
			get	{	return this.m_allowEndUserDocking;	}
			set	{	this.m_allowEndUserDocking = value;	}
		}

        private bool m_allowEndUserNestedDocking = true;
        [LocalizedCategory("Category_Docking")]
        [LocalizedDescription("DockPanel_AllowEndUserNestedDocking_Description")]
        [DefaultValue(true)]
        public bool AllowEndUserNestedDocking
        {
            get { return this.m_allowEndUserNestedDocking; }
            set { this.m_allowEndUserNestedDocking = value; }
        }

        private readonly DockContentCollection _mContents = new DockContentCollection();
		[Browsable(false)]
		public DockContentCollection Contents
		{
			get	{	return this._mContents;	}
		}

		internal DockContent DummyContent
		{
			get	{	return this._mDummyContent;	}
		}

        private bool m_rightToLeftLayout;
        [DefaultValue(false)]
        [LocalizedCategory("Appearance")]
        [LocalizedDescription("DockPanel_RightToLeftLayout_Description")]
        public bool RightToLeftLayout
        {
            get { return this.m_rightToLeftLayout; }
            set
            {
                if (this.m_rightToLeftLayout == value)
                    return;

                this.m_rightToLeftLayout = value;
                foreach (FloatWindow floatWindow in this.FloatWindows)
                    floatWindow.RightToLeftLayout = value;
            }
        }

        protected override void OnRightToLeftChanged(EventArgs e)
        {
            base.OnRightToLeftChanged(e);
            foreach (FloatWindow floatWindow in this.FloatWindows)
            {
                if (floatWindow.RightToLeft != RightToLeft)
                    floatWindow.RightToLeft = RightToLeft;
            }
        }

		private bool m_showDocumentIcon;
		[DefaultValue(false)]
		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockPanel_ShowDocumentIcon_Description")]
		public bool ShowDocumentIcon
		{
			get	{	return this.m_showDocumentIcon;	}
			set
			{
				if (this.m_showDocumentIcon == value)
					return;

				this.m_showDocumentIcon = value;
				Refresh();
			}
		}

        private DockPanelSkin m_dockPanelSkin = new DockPanelSkin();
        [LocalizedCategory("Category_Docking")]
        [LocalizedDescription("DockPanel_DockPanelSkin")]
		[DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public DockPanelSkin Skin
        {
            get { return this.m_dockPanelSkin; }
            set { this.m_dockPanelSkin = value; }
        }

        private DocumentTabStripLocation m_documentTabStripLocation = DocumentTabStripLocation.Top;
        [DefaultValue(DocumentTabStripLocation.Top)]
        [LocalizedCategory("Category_Docking")]
        [LocalizedDescription("DockPanel_DocumentTabStripLocation")]
        public DocumentTabStripLocation DocumentTabStripLocation
        {
            get { return this.m_documentTabStripLocation; }
            set { this.m_documentTabStripLocation = value; }
        }

		[Browsable(false)]
		public DockPanelExtender Extender
		{
			get	{	return this._mExtender;	}
		}

        [Browsable(false)]
		public DockPanelExtender.IDockPaneFactory DockPaneFactory
		{
			get	{	return this.Extender.DockPaneFactory;	}
		}

        [Browsable(false)]
		public DockPanelExtender.IFloatWindowFactory FloatWindowFactory
		{
			get	{	return this.Extender.FloatWindowFactory;	}
		}

		internal DockPanelExtender.IDockPaneCaptionFactory DockPaneCaptionFactory
		{
			get	{	return this.Extender.DockPaneCaptionFactory;	}
		}

		internal DockPanelExtender.IDockPaneStripFactory DockPaneStripFactory
		{
			get	{	return this.Extender.DockPaneStripFactory;	}
		}

		internal DockPanelExtender.IAutoHideStripFactory AutoHideStripFactory
		{
			get	{	return this.Extender.AutoHideStripFactory;	}
		}

		[Browsable(false)]
		public DockPaneCollection Panes
		{
			get	{	return this._mPanes;	}
		}

		internal Rectangle DockArea
		{
			get
			{
				return new Rectangle(DockPadding.Left, DockPadding.Top,
					ClientRectangle.Width - DockPadding.Left - DockPadding.Right,
					ClientRectangle.Height - DockPadding.Top - DockPadding.Bottom);
			}
		}

		private double m_dockBottomPortion = 0.25;
		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockPanel_DockBottomPortion_Description")]
		[DefaultValue(0.25)]
		public double DockBottomPortion
		{
			get	{	return this.m_dockBottomPortion;	}
			set
			{
				if (value <= 0)
					throw new ArgumentOutOfRangeException("value");

				if (value == this.m_dockBottomPortion)
					return;

				this.m_dockBottomPortion = value;

                if (this.m_dockBottomPortion < 1 && this.m_dockTopPortion < 1)
                {
                    if (this.m_dockTopPortion + this.m_dockBottomPortion > 1)
                        this.m_dockTopPortion = 1 - this.m_dockBottomPortion;
                }

				PerformLayout();
			}
		}

		private double m_dockLeftPortion = 0.25;
		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockPanel_DockLeftPortion_Description")]
		[DefaultValue(0.25)]
		public double DockLeftPortion
		{
			get	{	return this.m_dockLeftPortion;	}
			set
			{
				if (value <= 0)
					throw new ArgumentOutOfRangeException("value");

				if (value == this.m_dockLeftPortion)
					return;

				this.m_dockLeftPortion = value;

                if (this.m_dockLeftPortion < 1 && this.m_dockRightPortion < 1)
                {
                    if (this.m_dockLeftPortion + this.m_dockRightPortion > 1)
                        this.m_dockRightPortion = 1 - this.m_dockLeftPortion;
                }
				PerformLayout();
			}
		}

		private double m_dockRightPortion = 0.25;
		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockPanel_DockRightPortion_Description")]
		[DefaultValue(0.25)]
		public double DockRightPortion
		{
			get	{	return this.m_dockRightPortion;	}
			set
			{
				if (value <= 0)
					throw new ArgumentOutOfRangeException("value");

				if (value == this.m_dockRightPortion)
					return;

				this.m_dockRightPortion = value;

                if (this.m_dockLeftPortion < 1 && this.m_dockRightPortion < 1)
                {
                    if (this.m_dockLeftPortion + this.m_dockRightPortion > 1)
                        this.m_dockLeftPortion = 1 - this.m_dockRightPortion;
                }
				PerformLayout();
			}
		}

		private double m_dockTopPortion = 0.25;
		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockPanel_DockTopPortion_Description")]
		[DefaultValue(0.25)]
		public double DockTopPortion
		{
			get	{	return this.m_dockTopPortion;	}
			set
			{
				if (value <= 0)
					throw new ArgumentOutOfRangeException("value");

				if (value == this.m_dockTopPortion)
					return;

				this.m_dockTopPortion = value;

                if (this.m_dockTopPortion < 1 && this.m_dockBottomPortion < 1)
                {
                    if (this.m_dockTopPortion + this.m_dockBottomPortion > 1)
                        this.m_dockBottomPortion = 1 - this.m_dockTopPortion;
                }
				PerformLayout();
			}
		}

		[Browsable(false)]
		public DockWindowCollection DockWindows
		{
			get	{	return this._mDockWindows;	}
		}

        public void UpdateDockWindowZOrder(DockStyle dockStyle, bool fullPanelEdge)
        {
            if (dockStyle == DockStyle.Left)
            {
                if (fullPanelEdge)
                    this.DockWindows[DockState.DockLeft].SendToBack();
                else
                    this.DockWindows[DockState.DockLeft].BringToFront();
            }
            else if (dockStyle == DockStyle.Right)
            {
                if (fullPanelEdge)
                    this.DockWindows[DockState.DockRight].SendToBack();
                else
                    this.DockWindows[DockState.DockRight].BringToFront();
            }
            else if (dockStyle == DockStyle.Top)
            {
                if (fullPanelEdge)
                    this.DockWindows[DockState.DockTop].SendToBack();
                else
                    this.DockWindows[DockState.DockTop].BringToFront();
            }
            else if (dockStyle == DockStyle.Bottom)
            {
                if (fullPanelEdge)
                    this.DockWindows[DockState.DockBottom].SendToBack();
                else
                    this.DockWindows[DockState.DockBottom].BringToFront();
            }
        }

        [Browsable(false)]
        public int DocumentsCount
        {
            get
            {
                int count = 0;
                foreach (IDockContent content in this.Documents)
                    count++;

                return count;
            }
        }

        public IDockContent[] DocumentsToArray()
        {
            int count = this.DocumentsCount;
            var documents = new IDockContent[count];
            int i = 0;
            foreach (IDockContent content in this.Documents)
            {
                documents[i] = content;
                i++;
            }

            return documents;
        }

        [Browsable(false)]
		public IEnumerable<IDockContent> Documents
		{
            get
            {
                foreach (IDockContent content in this.Contents)
                {
                    if (content.DockHandler.DockState == DockState.Document)
                        yield return content;
                }
            }
		}

		private Rectangle DocumentRectangle
		{
			get
			{
				Rectangle rect = this.DockArea;
				if (this.DockWindows[DockState.DockLeft].VisibleNestedPanes.Count != 0)
				{
					rect.X += (int)(this.DockArea.Width * this.DockLeftPortion);
					rect.Width -= (int)(this.DockArea.Width * this.DockLeftPortion);
				}
				if (this.DockWindows[DockState.DockRight].VisibleNestedPanes.Count != 0)
					rect.Width -= (int)(this.DockArea.Width * this.DockRightPortion);
				if (this.DockWindows[DockState.DockTop].VisibleNestedPanes.Count != 0)
				{
					rect.Y += (int)(this.DockArea.Height * this.DockTopPortion);
					rect.Height -= (int)(this.DockArea.Height * this.DockTopPortion);
				}
				if (this.DockWindows[DockState.DockBottom].VisibleNestedPanes.Count != 0)
					rect.Height -= (int)(this.DockArea.Height * this.DockBottomPortion);

				return rect;
			}
		}

		private Control DummyControl
		{
			get	{	return this._mDummyControl;	}
		}

		[Browsable(false)]
		public FloatWindowCollection FloatWindows
		{
			get	{	return this._mFloatWindows;	}
		}

        private Size m_defaultFloatWindowSize = new Size(300, 300);
        [Category("Layout")]
        [LocalizedDescription("DockPanel_DefaultFloatWindowSize_Description")]
        public Size DefaultFloatWindowSize
        {
            get { return this.m_defaultFloatWindowSize; }
            set { this.m_defaultFloatWindowSize = value; }
        }
        private bool ShouldSerializeDefaultFloatWindowSize()
        {
            return this.DefaultFloatWindowSize != new Size(300, 300);
        }

		private DocumentStyle m_documentStyle = DocumentStyle.DockingMdi;
		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockPanel_DocumentStyle_Description")]
		[DefaultValue(DocumentStyle.DockingMdi)]
		public DocumentStyle DocumentStyle
		{
			get	{	return this.m_documentStyle;	}
			set
			{
				if (value == this.m_documentStyle)
					return;

				if (!Enum.IsDefined(typeof(DocumentStyle), value))
					throw new InvalidEnumArgumentException();

				if (value == DocumentStyle.SystemMdi && this.DockWindows[DockState.Document].VisibleNestedPanes.Count > 0)
					throw new InvalidEnumArgumentException();

				this.m_documentStyle = value;

				this.SuspendLayout(true);

                this.SetAutoHideWindowParent();
				this.SetMdiClient();
				this.InvalidateWindowRegion();

				foreach (IDockContent content in this.Contents)
				{
					if (content.DockHandler.DockState == DockState.Document)
						content.DockHandler.SetPaneAndVisible(content.DockHandler.Pane);
				}

                this.PerformMdiClientLayout();

				this.ResumeLayout(true, true);
			}
		}

        private int GetDockWindowSize(DockState dockState)
        {
            if (dockState == DockState.DockLeft || dockState == DockState.DockRight)
            {
                int width = ClientRectangle.Width - DockPadding.Left - DockPadding.Right;
                int dockLeftSize = this.m_dockLeftPortion >= 1 ? (int)this.m_dockLeftPortion : (int)(width * this.m_dockLeftPortion);
                int dockRightSize = this.m_dockRightPortion >= 1 ? (int)this.m_dockRightPortion : (int)(width * this.m_dockRightPortion);

                if (dockLeftSize < MeasurePane.MinSize)
                    dockLeftSize = MeasurePane.MinSize;
                if (dockRightSize < MeasurePane.MinSize)
                    dockRightSize = MeasurePane.MinSize;

                if (dockLeftSize + dockRightSize > width - MeasurePane.MinSize)
                {
                    int adjust = (dockLeftSize + dockRightSize) - (width - MeasurePane.MinSize);
                    dockLeftSize -= adjust / 2;
                    dockRightSize -= adjust / 2;
                }

                return dockState == DockState.DockLeft ? dockLeftSize : dockRightSize;
            }
            else if (dockState == DockState.DockTop || dockState == DockState.DockBottom)
            {
                int height = ClientRectangle.Height - DockPadding.Top - DockPadding.Bottom;
                int dockTopSize = this.m_dockTopPortion >= 1 ? (int)this.m_dockTopPortion : (int)(height * this.m_dockTopPortion);
                int dockBottomSize = this.m_dockBottomPortion >= 1 ? (int)this.m_dockBottomPortion : (int)(height * this.m_dockBottomPortion);

                if (dockTopSize < MeasurePane.MinSize)
                    dockTopSize = MeasurePane.MinSize;
                if (dockBottomSize < MeasurePane.MinSize)
                    dockBottomSize = MeasurePane.MinSize;

                if (dockTopSize + dockBottomSize > height - MeasurePane.MinSize)
                {
                    int adjust = (dockTopSize + dockBottomSize) - (height - MeasurePane.MinSize);
                    dockTopSize -= adjust / 2;
                    dockBottomSize -= adjust / 2;
                }

                return dockState == DockState.DockTop ? dockTopSize : dockBottomSize;
            }
            else
                return 0;
        }

        protected override void OnLayout(LayoutEventArgs levent)
		{
			this.SuspendLayout(true);

			this.AutoHideStripControl.Bounds = ClientRectangle;

			this.CalculateDockPadding();

            this.DockWindows[DockState.DockLeft].Width = this.GetDockWindowSize(DockState.DockLeft);
			this.DockWindows[DockState.DockRight].Width = this.GetDockWindowSize(DockState.DockRight);
			this.DockWindows[DockState.DockTop].Height = this.GetDockWindowSize(DockState.DockTop);
			this.DockWindows[DockState.DockBottom].Height = this.GetDockWindowSize(DockState.DockBottom);

			this.AutoHideWindow.Bounds = this.GetAutoHideWindowBounds(this.AutoHideWindowRectangle);

			this.DockWindows[DockState.Document].BringToFront();
			this.AutoHideWindow.BringToFront();

			base.OnLayout(levent);

            if (this.DocumentStyle == DocumentStyle.SystemMdi && this.MdiClientExists)
            {
                this.SetMdiClientBounds(this.SystemMdiClientBounds);
                this.InvalidateWindowRegion();
            }
            else if (this.DocumentStyle == DocumentStyle.DockingMdi)
                this.InvalidateWindowRegion();

			this.ResumeLayout(true, true);
		}

		internal Rectangle GetTabStripRectangle(DockState dockState)
		{
			return this.AutoHideStripControl.GetTabStripRectangle(dockState);
		}

		protected override void OnPaint(PaintEventArgs e)
		{
			base.OnPaint(e);

		    if (this.DockBackColor == BackColor) return;

		    Graphics g = e.Graphics;
		    var bgBrush = new SolidBrush(this.DockBackColor);
		    g.FillRectangle(bgBrush, ClientRectangle);
		}

		internal void AddContent(IDockContent content)
		{
			if (content == null)
				throw(new ArgumentNullException());

			if (!this.Contents.Contains(content))
			{
				this.Contents.Add(content);
				this.OnContentAdded(new DockContentEventArgs(content));
			}
		}

		internal void AddPane(DockPane pane)
		{
			if (this.Panes.Contains(pane))
				return;

			this.Panes.Add(pane);
		}

		internal void AddFloatWindow(FloatWindow floatWindow)
		{
			if (this.FloatWindows.Contains(floatWindow))
				return;
			this.FloatWindows.Add(floatWindow);
		}

		private void CalculateDockPadding()
		{
			DockPadding.All = 0;

			int height = this.AutoHideStripControl.MeasureHeight();

			if (this.AutoHideStripControl.GetNumberOfPanes(DockState.DockLeftAutoHide) > 0)
				DockPadding.Left = height;
			if (this.AutoHideStripControl.GetNumberOfPanes(DockState.DockRightAutoHide) > 0)
				DockPadding.Right = height;
			if (this.AutoHideStripControl.GetNumberOfPanes(DockState.DockTopAutoHide) > 0)
				DockPadding.Top = height;
			if (this.AutoHideStripControl.GetNumberOfPanes(DockState.DockBottomAutoHide) > 0)
				DockPadding.Bottom = height;
		}

		public void RemoveContent(IDockContent content)
		{
			if (content == null)
				throw(new ArgumentNullException());
			
			if (this.Contents.Contains(content))
			{
				this.Contents.Remove(content);
				this.OnContentRemoved(new DockContentEventArgs(content));
			}
		}

		internal void RemovePane(DockPane pane)
		{
			if (!this.Panes.Contains(pane))
				return;

			this.Panes.Remove(pane);
		}

		internal void RemoveFloatWindow(FloatWindow floatWindow)
		{
			if (!this.FloatWindows.Contains(floatWindow))
				return;

			this.FloatWindows.Remove(floatWindow);
		}

		public void SetPaneIndex(DockPane pane, int index)
		{
			int oldIndex = this.Panes.IndexOf(pane);
			if (oldIndex == -1)
				throw(new ArgumentException(Strings.DockPanel_SetPaneIndex_InvalidPane));

			if (index < 0 || index > this.Panes.Count - 1)
				if (index != -1)
					throw(new ArgumentOutOfRangeException(Strings.DockPanel_SetPaneIndex_InvalidIndex));
				
			if (oldIndex == index)
				return;
			if (oldIndex == this.Panes.Count - 1 && index == -1)
				return;

			this.Panes.Remove(pane);
			if (index == -1)
				this.Panes.Add(pane);
			else if (oldIndex < index)
				this.Panes.AddAt(pane, index - 1);
			else
				this.Panes.AddAt(pane, index);
		}

		public void SuspendLayout(bool allWindows)
		{
            this.FocusManager.SuspendFocusTracking();
			SuspendLayout();
			if (allWindows)
				this.SuspendMdiClientLayout();
		}

		public void ResumeLayout(bool performLayout, bool allWindows)
		{
            this.FocusManager.ResumeFocusTracking();
            ResumeLayout(performLayout);
            if (allWindows)
                this.ResumeMdiClientLayout(performLayout);
		}

	    internal Form ParentForm
		{
			get
			{	
				if (!this.IsParentFormValid())
					throw new InvalidOperationException(Strings.DockPanel_ParentForm_Invalid);

				return this.GetMdiClientController().ParentForm;
			}
		}

		private bool IsParentFormValid()
		{
			if (this.DocumentStyle == DocumentStyle.DockingSdi || this.DocumentStyle == DocumentStyle.DockingWindow)
				return true;

            if (!this.MdiClientExists)
                this.GetMdiClientController().RenewMdiClient();

            return (this.MdiClientExists);
		}

		protected override void OnParentChanged(EventArgs e)
		{
            this.SetAutoHideWindowParent();
            this.GetMdiClientController().ParentForm = (Parent as Form);
			base.OnParentChanged (e);
		}

        private void SetAutoHideWindowParent()
        {
            Control parent;
            if (this.DocumentStyle == DocumentStyle.DockingMdi ||
                this.DocumentStyle == DocumentStyle.SystemMdi)
                parent = Parent;
            else
                parent = this;
            if (this.AutoHideWindow.Parent != parent)
            {
                this.AutoHideWindow.Parent = parent;
                this.AutoHideWindow.BringToFront();
            }
        }

		protected override void OnVisibleChanged(EventArgs e)
		{
			base.OnVisibleChanged (e);

			if (Visible)
				this.SetMdiClient();
		}

		private Rectangle SystemMdiClientBounds
		{
			get
			{
				if (!this.IsParentFormValid() || !Visible)
					return Rectangle.Empty;

				Rectangle rect = this.ParentForm.RectangleToClient(RectangleToScreen(this.DocumentWindowBounds));
				return rect;
			}
		}

		internal Rectangle DocumentWindowBounds
		{
			get
			{
				Rectangle rectDocumentBounds = DisplayRectangle;
				if (this.DockWindows[DockState.DockLeft].Visible)
				{
					rectDocumentBounds.X += this.DockWindows[DockState.DockLeft].Width;
					rectDocumentBounds.Width -= this.DockWindows[DockState.DockLeft].Width;
				}
				if (this.DockWindows[DockState.DockRight].Visible)
					rectDocumentBounds.Width -= this.DockWindows[DockState.DockRight].Width;
				if (this.DockWindows[DockState.DockTop].Visible)
				{
					rectDocumentBounds.Y += this.DockWindows[DockState.DockTop].Height;
					rectDocumentBounds.Height -= this.DockWindows[DockState.DockTop].Height;
				}
				if (this.DockWindows[DockState.DockBottom].Visible)
					rectDocumentBounds.Height -= this.DockWindows[DockState.DockBottom].Height;

				return rectDocumentBounds;

			}
		}

        private PaintEventHandler m_dummyControlPaintEventHandler;
        private void InvalidateWindowRegion()
        {
            if (DesignMode)
                return;

            if (this.m_dummyControlPaintEventHandler == null)
                this.m_dummyControlPaintEventHandler = this.DummyControl_Paint;

            this.DummyControl.Paint += this.m_dummyControlPaintEventHandler;
            this.DummyControl.Invalidate();
        }

        void DummyControl_Paint(object sender, PaintEventArgs e)
        {
            this.DummyControl.Paint -= this.m_dummyControlPaintEventHandler;
            this.UpdateWindowRegion();
        }

		private void UpdateWindowRegion()
		{
			if (this.DocumentStyle == DocumentStyle.DockingMdi)
				this.UpdateWindowRegion_ClipContent();
			else if (this.DocumentStyle == DocumentStyle.DockingSdi ||
				this.DocumentStyle == DocumentStyle.DockingWindow)
				this.UpdateWindowRegion_FullDocumentArea();
			else if (this.DocumentStyle == DocumentStyle.SystemMdi)
				this.UpdateWindowRegion_EmptyDocumentArea();
		}

		private void UpdateWindowRegion_FullDocumentArea()
		{
			this.SetRegion(null);
		}

		private void UpdateWindowRegion_EmptyDocumentArea()
		{
			Rectangle rect = this.DocumentWindowBounds;
			this.SetRegion(new[] { rect });
		}

		private void UpdateWindowRegion_ClipContent()
		{
			int count = 0;
			foreach (DockPane pane in this.Panes)
			{
				if (!pane.Visible || pane.DockState != DockState.Document)
					continue;

				count ++;
			}

            if (count == 0)
            {
                this.SetRegion(null);
                return;
            }

			var rects = new Rectangle[count];
			int i = 0;
			foreach (DockPane pane in this.Panes)
			{
				if (!pane.Visible || pane.DockState != DockState.Document)
					continue;

                rects[i] = RectangleToClient(pane.RectangleToScreen(pane.ContentRectangle));
				i++;
			}

			this.SetRegion(rects);
		}

		private Rectangle[] m_clipRects;
		private void SetRegion(Rectangle[] clipRects)
		{
			if (!this.IsClipRectsChanged(clipRects))
				return;

			this.m_clipRects = clipRects;

			if (this.m_clipRects == null || this.m_clipRects.GetLength(0) == 0)
				Region = null;
			else
			{
				var region = new Region(new Rectangle(0, 0, Width, Height));
				foreach (Rectangle rect in this.m_clipRects)
					region.Exclude(rect);
				Region = region;
			}
		}

		private bool IsClipRectsChanged(Rectangle[] clipRects)
		{
			if (clipRects == null && this.m_clipRects == null)
				return false;
			else if ((clipRects == null) != (this.m_clipRects == null))
				return true;

			foreach (Rectangle rect in clipRects)
			{
				bool matched = false;
				foreach (Rectangle rect2 in this.m_clipRects)
				{
					if (rect == rect2)
					{
						matched = true;
						break;
					}
				}
				if (!matched)
					return true;
			}

			foreach (Rectangle rect2 in this.m_clipRects)
			{
				bool matched = false;
				foreach (Rectangle rect in clipRects)
				{
					if (rect == rect2)
					{
						matched = true;
						break;
					}
				}
				if (!matched)
					return true;
			}
			return false;
		}

		private static readonly object ContentAddedEvent = new object();
		[LocalizedCategory("Category_DockingNotification")]
		[LocalizedDescription("DockPanel_ContentAdded_Description")]
		public event EventHandler<DockContentEventArgs> ContentAdded
		{
			add	{	Events.AddHandler(ContentAddedEvent, value);	}
			remove	{	Events.RemoveHandler(ContentAddedEvent, value);	}
		}
		protected virtual void OnContentAdded(DockContentEventArgs e)
		{
			var handler = (EventHandler<DockContentEventArgs>)Events[ContentAddedEvent];
			if (handler != null)
				handler(this, e);
		}

		private static readonly object ContentRemovedEvent = new object();
		[LocalizedCategory("Category_DockingNotification")]
		[LocalizedDescription("DockPanel_ContentRemoved_Description")]
		public event EventHandler<DockContentEventArgs> ContentRemoved
		{
			add	{	Events.AddHandler(ContentRemovedEvent, value);	}
			remove	{	Events.RemoveHandler(ContentRemovedEvent, value);	}
		}
		protected virtual void OnContentRemoved(DockContentEventArgs e)
		{
			var handler = (EventHandler<DockContentEventArgs>)Events[ContentRemovedEvent];
			if (handler != null)
				handler(this, e);
		}
    }
}