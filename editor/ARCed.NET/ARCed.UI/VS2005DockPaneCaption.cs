#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

#endregion

namespace ARCed.UI
{
	internal class VS2005DockPaneCaption : DockPaneCaptionBase
	{
        private sealed class InertButton : InertButtonBase
        {
            private readonly Bitmap m_image, m_imageAutoHide;

            public InertButton(VS2005DockPaneCaption dockPaneCaption, Bitmap image, Bitmap imageAutoHide)
            {
                this.m_dockPaneCaption = dockPaneCaption;
                this.m_image = image;
                this.m_imageAutoHide = imageAutoHide;
                RefreshChanges();
            }

            private readonly VS2005DockPaneCaption m_dockPaneCaption;
            private VS2005DockPaneCaption DockPaneCaption
            {
                get { return this.m_dockPaneCaption; }
            }

            public bool IsAutoHide
            {
                get { return this.DockPaneCaption.DockPane.IsAutoHide; }
            }

            public override Bitmap Image
            {
                get { return this.IsAutoHide ? this.m_imageAutoHide : this.m_image; }
            }

            protected override void OnRefreshChanges()
            {
                if (this.DockPaneCaption.DockPane.DockPanel != null)
                {
                    if (this.DockPaneCaption.TextColor != ForeColor)
                    {
                        ForeColor = this.DockPaneCaption.TextColor;
                        Invalidate();
                    }
                }
            }
        }

		#region consts
		private const int _TextGapTop = 2;
		private const int _TextGapBottom = 0;
		private const int _TextGapLeft = 3;
		private const int _TextGapRight = 3;
		private const int _ButtonGapTop = 2;
		private const int _ButtonGapBottom = 1;
		private const int _ButtonGapBetween = 1;
		private const int _ButtonGapLeft = 1;
		private const int _ButtonGapRight = 2;
		#endregion

        private static Bitmap _imageButtonClose;
        private static Bitmap ImageButtonClose
        {
            get
            {
                if (_imageButtonClose == null)
                    _imageButtonClose = Resources.DockPane_Close;
                return _imageButtonClose;
            }
        }

		private InertButton m_buttonClose;
        private InertButton ButtonClose
        {
            get
            {
                if (this.m_buttonClose == null)
                {
                    this.m_buttonClose = new InertButton(this, ImageButtonClose, ImageButtonClose);
                    this.m_toolTip.SetToolTip(this.m_buttonClose, ToolTipClose);
                    this.m_buttonClose.Click += this.Close_Click;
                    Controls.Add(this.m_buttonClose);
                }

                return this.m_buttonClose;
            }
        }

        private static Bitmap _imageButtonAutoHide;
        private static Bitmap ImageButtonAutoHide
        {
            get
            {
                if (_imageButtonAutoHide == null)
                    _imageButtonAutoHide = Resources.DockPane_AutoHide;

                return _imageButtonAutoHide;
            }
        }

        private static Bitmap _imageButtonDock;
        private static Bitmap ImageButtonDock
        {
            get
            {
                if (_imageButtonDock == null)
                    _imageButtonDock = Resources.DockPane_Dock;

                return _imageButtonDock;
            }
        }

        private InertButton m_buttonAutoHide;
        private InertButton ButtonAutoHide
        {
            get
            {
                if (this.m_buttonAutoHide == null)
                {
                    this.m_buttonAutoHide = new InertButton(this, ImageButtonDock, ImageButtonAutoHide);
                    this.m_toolTip.SetToolTip(this.m_buttonAutoHide, ToolTipAutoHide);
                    this.m_buttonAutoHide.Click += this.AutoHide_Click;
                    Controls.Add(this.m_buttonAutoHide);
                }

                return this.m_buttonAutoHide;
            }
        }

        private static Bitmap _imageButtonOptions;
        private static Bitmap ImageButtonOptions
        {
            get
            {
                if (_imageButtonOptions == null)
                    _imageButtonOptions = Resources.DockPane_Option;

                return _imageButtonOptions;
            }
        }

        private InertButton m_buttonOptions;
        private InertButton ButtonOptions
        {
            get
            {
                if (this.m_buttonOptions == null)
                {
                    this.m_buttonOptions = new InertButton(this, ImageButtonOptions, ImageButtonOptions);
                    this.m_toolTip.SetToolTip(this.m_buttonOptions, ToolTipOptions);
                    this.m_buttonOptions.Click += this.Options_Click;
                    Controls.Add(this.m_buttonOptions);
                }
                return this.m_buttonOptions;
            }
        }

        private readonly IContainer m_components;
        private IContainer Components
        {
            get { return this.m_components; }
        }

        private readonly ToolTip m_toolTip;

		public VS2005DockPaneCaption(DockPane pane) : base(pane)
		{
			SuspendLayout();

            this.m_components = new Container();
            this.m_toolTip = new ToolTip(this.Components);

			ResumeLayout();
		}

        protected override void Dispose(bool disposing)
        {
            if (disposing)
                this.Components.Dispose();
            base.Dispose(disposing);
        }

		private static int TextGapTop
		{
			get	{	return _TextGapTop;	}
		}

        public Font TextFont
        {
            get { return DockPane.DockPanel.Skin.DockPaneStripSkin.TextFont; }
        }

		private static int TextGapBottom
		{
			get	{	return _TextGapBottom;	}
		}

		private static int TextGapLeft
		{
			get	{	return _TextGapLeft;	}
		}

		private static int TextGapRight
		{
			get	{	return _TextGapRight;	}
		}

		private static int ButtonGapTop
		{
			get	{	return _ButtonGapTop;	}
		}

		private static int ButtonGapBottom
		{
			get	{	return _ButtonGapBottom;	}
		}

		private static int ButtonGapLeft
		{
			get	{	return _ButtonGapLeft;	}
		}

		private static int ButtonGapRight
		{
			get	{	return _ButtonGapRight;	}
		}

		private static int ButtonGapBetween
		{
			get	{	return _ButtonGapBetween;	}
		}

		private static string _toolTipClose;
		private static string ToolTipClose
		{
			get
			{	
				if (_toolTipClose == null)
					_toolTipClose = Strings.DockPaneCaption_ToolTipClose;
				return _toolTipClose;
			}
		}

        private static string _toolTipOptions;
        private static string ToolTipOptions
        {
            get
            {
                if (_toolTipOptions == null)
                    _toolTipOptions = Strings.DockPaneCaption_ToolTipOptions;

                return _toolTipOptions;
            }
        }

		private static string _toolTipAutoHide;
		private static string ToolTipAutoHide
		{
			get
			{	
				if (_toolTipAutoHide == null)
					_toolTipAutoHide = Strings.DockPaneCaption_ToolTipAutoHide;
				return _toolTipAutoHide;
			}
		}

        private static Blend _activeBackColorGradientBlend;
        private static Blend ActiveBackColorGradientBlend
        {
            get
            {
                if (_activeBackColorGradientBlend == null)
                {
                    var blend = new Blend(2)
                    {
                        Factors = new[]
                        {
                            0.5F, 1.0F
                        },
                        Positions = new[]
                        {
                            0.0F, 1.0F
                        }
                    };

                    _activeBackColorGradientBlend = blend;
                }

                return _activeBackColorGradientBlend;
            }
        }

        private Color TextColor
        {
            get
            {
                if (DockPane.IsActivated)
                    return DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.ActiveCaptionGradient.TextColor;
                else
                    return DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.InactiveCaptionGradient.TextColor;
            }
        }

	    private const TextFormatFlags TEXT_FORMAT = TextFormatFlags.SingleLine | TextFormatFlags.EndEllipsis | TextFormatFlags.VerticalCenter;

	    private TextFormatFlags TextFormat
		{
            get
            {
                if (RightToLeft == RightToLeft.No)
                    return TEXT_FORMAT;
                else
                    return TEXT_FORMAT | TextFormatFlags.RightToLeft | TextFormatFlags.Right;
            }
		}

		protected internal override int MeasureHeight()
		{
			int height = this.TextFont.Height + TextGapTop + TextGapBottom;

			if (height < this.ButtonClose.Image.Height + ButtonGapTop + ButtonGapBottom)
				height = this.ButtonClose.Image.Height + ButtonGapTop + ButtonGapBottom;

			return height;
		}

		protected override void OnPaint(PaintEventArgs e)
		{
			base.OnPaint (e);
			this.DrawCaption(e.Graphics);
		}

		private void DrawCaption(Graphics g)
		{
            if (ClientRectangle.Width == 0 || ClientRectangle.Height == 0)
                return;

            if (DockPane.IsActivated)
            {
                Color startColor = DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.ActiveCaptionGradient.StartColor;
                Color endColor = DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.ActiveCaptionGradient.EndColor;
                LinearGradientMode gradientMode = DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.ActiveCaptionGradient.LinearGradientMode;
                using (var brush = new LinearGradientBrush(ClientRectangle, startColor, endColor, gradientMode))
                {
                    brush.Blend = ActiveBackColorGradientBlend;
                    g.FillRectangle(brush, ClientRectangle);
                }
            }
            else
            {
                Color startColor = DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.InactiveCaptionGradient.StartColor;
                Color endColor = DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.InactiveCaptionGradient.EndColor;
                LinearGradientMode gradientMode = DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.InactiveCaptionGradient.LinearGradientMode;
                using (var brush = new LinearGradientBrush(ClientRectangle, startColor, endColor, gradientMode))
                {
                    g.FillRectangle(brush, ClientRectangle);
                }
            }

			Rectangle rectCaption = ClientRectangle;

			Rectangle rectCaptionText = rectCaption;
            rectCaptionText.X += TextGapLeft;
            rectCaptionText.Width -= TextGapLeft + TextGapRight;
            rectCaptionText.Width -= ButtonGapLeft + this.ButtonClose.Width + ButtonGapRight;
            if (this.ShouldShowAutoHideButton)
                rectCaptionText.Width -= this.ButtonAutoHide.Width + ButtonGapBetween;
            if (HasTabPageContextMenu)
                rectCaptionText.Width -= this.ButtonOptions.Width + ButtonGapBetween;
			rectCaptionText.Y += TextGapTop;
			rectCaptionText.Height -= TextGapTop + TextGapBottom;

            Color colorText;
            if (DockPane.IsActivated)
                colorText = DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.ActiveCaptionGradient.TextColor;
            else
                colorText = DockPane.DockPanel.Skin.DockPaneStripSkin.ToolWindowGradient.InactiveCaptionGradient.TextColor;

            TextRenderer.DrawText(g, DockPane.CaptionText, this.TextFont, DrawHelper.RtlTransform(this, rectCaptionText), colorText, this.TextFormat);
		}

		protected override void OnLayout(LayoutEventArgs levent)
		{
			this.SetButtonsPosition();
			base.OnLayout (levent);
		}

		protected override void OnRefreshChanges()
		{
			this.SetButtons();
			Invalidate();
		}

		private bool CloseButtonEnabled
		{
			get	{	return (DockPane.ActiveContent != null)? DockPane.ActiveContent.DockHandler.CloseButton : false;	}
		}

        /// <summary>
        /// Determines whether the close button is visible on the content
        /// </summary>
        private bool CloseButtonVisible
        {
            get { return (DockPane.ActiveContent != null) ? DockPane.ActiveContent.DockHandler.CloseButtonVisible : false; }
        }

		private bool ShouldShowAutoHideButton
		{
			get	{	return !DockPane.IsFloat;	}
		}

		private void SetButtons()
		{
			this.ButtonClose.Enabled = this.CloseButtonEnabled;
            this.ButtonClose.Visible = this.CloseButtonVisible;
			this.ButtonAutoHide.Visible = this.ShouldShowAutoHideButton;
            this.ButtonOptions.Visible = HasTabPageContextMenu;
            this.ButtonClose.RefreshChanges();
            this.ButtonAutoHide.RefreshChanges();
            this.ButtonOptions.RefreshChanges();
			
			this.SetButtonsPosition();
		}

		private void SetButtonsPosition()
		{
			// set the size and location for close and auto-hide buttons
			Rectangle rectCaption = ClientRectangle;
			int buttonWidth = this.ButtonClose.Image.Width;
			int buttonHeight = this.ButtonClose.Image.Height;
			int height = rectCaption.Height - ButtonGapTop - ButtonGapBottom;
			if (buttonHeight < height)
			{
				buttonWidth = buttonWidth * (height / buttonHeight);
				buttonHeight = height;
			}
			var buttonSize = new Size(buttonWidth, buttonHeight);
			int x = rectCaption.X + rectCaption.Width - 1 - ButtonGapRight - this.m_buttonClose.Width;
			int y = rectCaption.Y + ButtonGapTop;
			var point = new Point(x, y);
            this.ButtonClose.Bounds = DrawHelper.RtlTransform(this, new Rectangle(point, buttonSize));

            // If the close button is not visible draw the auto hide button overtop.
            // Otherwise it is drawn to the left of the close button.
            if (this.CloseButtonVisible)
			    point.Offset(-(buttonWidth + ButtonGapBetween), 0);
            
            this.ButtonAutoHide.Bounds = DrawHelper.RtlTransform(this, new Rectangle(point, buttonSize));
            if (this.ShouldShowAutoHideButton)
                point.Offset(-(buttonWidth + ButtonGapBetween), 0);
            this.ButtonOptions.Bounds = DrawHelper.RtlTransform(this, new Rectangle(point, buttonSize));
		}

		private void Close_Click(object sender, EventArgs e)
		{
			DockPane.CloseActiveContent();
		}

		private void AutoHide_Click(object sender, EventArgs e)
		{
			DockPane.DockState = DockHelper.ToggleAutoHideState(DockPane.DockState);
            if (DockHelper.IsDockStateAutoHide(DockPane.DockState))
            {
                DockPane.DockPanel.ActiveAutoHideContent = null;
                DockPane.NestedDockingStatus.NestedPanes.SwitchPaneWithFirstChild(DockPane);
            }
		}

        private void Options_Click(object sender, EventArgs e)
        {
            ShowTabPageContextMenu(PointToClient(MousePosition));
        }

        protected override void OnRightToLeftChanged(EventArgs e)
        {
            base.OnRightToLeftChanged(e);
            PerformLayout();
        }
	}
}
