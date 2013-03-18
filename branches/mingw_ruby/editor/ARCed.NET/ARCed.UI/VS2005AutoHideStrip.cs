#region Using Directives

using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;

#endregion

namespace ARCed.UI
{
    internal class VS2005AutoHideStrip : AutoHideStripBase
    {
        private class TabVS2005 : Tab
        {
            internal TabVS2005(IDockContent content)
                : base(content)
            {
            }

            private int m_tabX;
            public int TabX
            {
                get { return this.m_tabX; }
                set { this.m_tabX = value; }
            }

            private int m_tabWidth;
            public int TabWidth
            {
                get { return this.m_tabWidth; }
                set { this.m_tabWidth = value; }
            }

        }

        private const int _ImageHeight = 16;
        private const int _ImageWidth = 16;
        private const int _ImageGapTop = 2;
        private const int _ImageGapLeft = 4;
        private const int _ImageGapRight = 2;
        private const int _ImageGapBottom = 2;
        private const int _TextGapLeft = 0;
        private const int _TextGapRight = 0;
        private const int _TabGapTop = 3;
        private const int _TabGapLeft = 4;
        private const int _TabGapBetween = 10;

        #region Customizable Properties
        public Font TextFont
        {
            get { return DockPanel.Skin.AutoHideStripSkin.TextFont; }
        }

        private static StringFormat _stringFormatTabHorizontal;
        private StringFormat StringFormatTabHorizontal
        {
            get
            {
                if (_stringFormatTabHorizontal == null)
                {
                    _stringFormatTabHorizontal = new StringFormat
                    {
                        Alignment = StringAlignment.Near,
                        LineAlignment = StringAlignment.Center,
                        FormatFlags = StringFormatFlags.NoWrap,
                        Trimming = StringTrimming.None
                    };
                }

                if (RightToLeft == RightToLeft.Yes)
                    _stringFormatTabHorizontal.FormatFlags |= StringFormatFlags.DirectionRightToLeft;
                else
                    _stringFormatTabHorizontal.FormatFlags &= ~StringFormatFlags.DirectionRightToLeft;

                return _stringFormatTabHorizontal;
            }
        }

        private static StringFormat _stringFormatTabVertical;
        private StringFormat StringFormatTabVertical
        {
            get
            {
                if (_stringFormatTabVertical == null)
                {
                    _stringFormatTabVertical = new StringFormat
                    {
                        Alignment = StringAlignment.Near,
                        LineAlignment = StringAlignment.Center,
                        FormatFlags = StringFormatFlags.NoWrap | StringFormatFlags.DirectionVertical,
                        Trimming = StringTrimming.None
                    };
                }
                if (RightToLeft == RightToLeft.Yes)
                    _stringFormatTabVertical.FormatFlags |= StringFormatFlags.DirectionRightToLeft;
                else
                    _stringFormatTabVertical.FormatFlags &= ~StringFormatFlags.DirectionRightToLeft;

                return _stringFormatTabVertical;
            }
        }

        private static int ImageHeight
        {
            get { return _ImageHeight; }
        }

        private static int ImageWidth
        {
            get { return _ImageWidth; }
        }

        private static int ImageGapTop
        {
            get { return _ImageGapTop; }
        }

        private static int ImageGapLeft
        {
            get { return _ImageGapLeft; }
        }

        private static int ImageGapRight
        {
            get { return _ImageGapRight; }
        }

        private static int ImageGapBottom
        {
            get { return _ImageGapBottom; }
        }

        private static int TextGapLeft
        {
            get { return _TextGapLeft; }
        }

        private static int TextGapRight
        {
            get { return _TextGapRight; }
        }

        private static int TabGapTop
        {
            get { return _TabGapTop; }
        }

        private static int TabGapLeft
        {
            get { return _TabGapLeft; }
        }

        private static int TabGapBetween
        {
            get { return _TabGapBetween; }
        }

        private static Pen PenTabBorder
        {
            get { return SystemPens.GrayText; }
        }
        #endregion

        private readonly static Matrix _matrixIdentity = new Matrix();
        private static Matrix MatrixIdentity
        {
            get { return _matrixIdentity; }
        }

        private static DockState[] _dockStates;
        private static DockState[] DockStates
        {
            get
            {
                if (_dockStates == null)
                {
                    _dockStates = new DockState[4];
                    _dockStates[0] = DockState.DockLeftAutoHide;
                    _dockStates[1] = DockState.DockRightAutoHide;
                    _dockStates[2] = DockState.DockTopAutoHide;
                    _dockStates[3] = DockState.DockBottomAutoHide;
                }
                return _dockStates;
            }
        }

        private static GraphicsPath _graphicsPath;
        internal static GraphicsPath GraphicsPath
        {
            get
            {
                if (_graphicsPath == null)
                    _graphicsPath = new GraphicsPath();

                return _graphicsPath;
            }
        }

        public VS2005AutoHideStrip(DockPanel panel)
            : base(panel)
        {
            SetStyle(ControlStyles.ResizeRedraw |
                ControlStyles.UserPaint |
                ControlStyles.AllPaintingInWmPaint |
                ControlStyles.OptimizedDoubleBuffer, true);
            BackColor = SystemColors.ControlLight;
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;

            Color startColor = DockPanel.Skin.AutoHideStripSkin.DockStripGradient.StartColor;
            Color endColor = DockPanel.Skin.AutoHideStripSkin.DockStripGradient.EndColor;
            LinearGradientMode gradientMode = DockPanel.Skin.AutoHideStripSkin.DockStripGradient.LinearGradientMode;
            using (var brush = new LinearGradientBrush(ClientRectangle, startColor, endColor, gradientMode))
            {
                g.FillRectangle(brush, ClientRectangle);
            }

            this.DrawTabStrip(g);
        }

        protected override void OnLayout(LayoutEventArgs levent)
        {
            this.CalculateTabs();
            base.OnLayout(levent);
        }

        private void DrawTabStrip(Graphics g)
        {
            this.DrawTabStrip(g, DockState.DockTopAutoHide);
            this.DrawTabStrip(g, DockState.DockBottomAutoHide);
            this.DrawTabStrip(g, DockState.DockLeftAutoHide);
            this.DrawTabStrip(g, DockState.DockRightAutoHide);
        }

        private void DrawTabStrip(Graphics g, DockState dockState)
        {
            Rectangle rectTabStrip = this.GetLogicalTabStripRectangle(dockState);

            if (rectTabStrip.IsEmpty)
                return;

            Matrix matrixIdentity = g.Transform;
            if (dockState == DockState.DockLeftAutoHide || dockState == DockState.DockRightAutoHide)
            {
                var matrixRotated = new Matrix();
                matrixRotated.RotateAt(90, new PointF(rectTabStrip.X + (float)rectTabStrip.Height / 2,
                    rectTabStrip.Y + (float)rectTabStrip.Height / 2));
                g.Transform = matrixRotated;
            }

            foreach (Pane pane in GetPanes(dockState))
            {
                foreach (TabVS2005 tab in pane.AutoHideTabs)
                    this.DrawTab(g, tab);
            }
            g.Transform = matrixIdentity;
        }

        private void CalculateTabs()
        {
            this.CalculateTabs(DockState.DockTopAutoHide);
            this.CalculateTabs(DockState.DockBottomAutoHide);
            this.CalculateTabs(DockState.DockLeftAutoHide);
            this.CalculateTabs(DockState.DockRightAutoHide);
        }

        private void CalculateTabs(DockState dockState)
        {
            Rectangle rectTabStrip = this.GetLogicalTabStripRectangle(dockState);

            int imageHeight = rectTabStrip.Height - ImageGapTop - ImageGapBottom;
            int imageWidth = ImageWidth;
            if (imageHeight > ImageHeight)
                imageWidth = ImageWidth * (imageHeight / ImageHeight);

            int x = TabGapLeft + rectTabStrip.X;
            foreach (Pane pane in GetPanes(dockState))
            {
                foreach (TabVS2005 tab in pane.AutoHideTabs)
                {
                    int width = imageWidth + ImageGapLeft + ImageGapRight +
                        TextRenderer.MeasureText(tab.Content.DockHandler.TabText, this.TextFont).Width +
                        TextGapLeft + TextGapRight;
                    tab.TabX = x;
                    tab.TabWidth = width;
                    x += width;
                }

                x += TabGapBetween;
            }
        }

        private Rectangle RtlTransform(Rectangle rect, DockState dockState)
        {
            Rectangle rectTransformed;
            if (dockState == DockState.DockLeftAutoHide || dockState == DockState.DockRightAutoHide)
                rectTransformed = rect;
            else
                rectTransformed = DrawHelper.RtlTransform(this, rect);

            return rectTransformed;
        }

        private GraphicsPath GetTabOutline(TabVS2005 tab, bool transformed, bool rtlTransform)
        {
            DockState dockState = tab.Content.DockHandler.DockState;
            Rectangle rectTab = this.GetTabRectangle(tab, transformed);
            if (rtlTransform)
                rectTab = this.RtlTransform(rectTab, dockState);
            bool upTab = (dockState == DockState.DockLeftAutoHide || dockState == DockState.DockBottomAutoHide);
            DrawHelper.GetRoundedCornerTab(GraphicsPath, rectTab, upTab);

            return GraphicsPath;
        }

        private void DrawTab(Graphics g, TabVS2005 tab)
        {
            Rectangle rectTabOrigin = this.GetTabRectangle(tab);
            if (rectTabOrigin.IsEmpty)
                return;

            DockState dockState = tab.Content.DockHandler.DockState;
            IDockContent content = tab.Content;

            GraphicsPath path = this.GetTabOutline(tab, false, true);

            Color startColor = DockPanel.Skin.AutoHideStripSkin.TabGradient.StartColor;
            Color endColor = DockPanel.Skin.AutoHideStripSkin.TabGradient.EndColor;
            LinearGradientMode gradientMode = DockPanel.Skin.AutoHideStripSkin.TabGradient.LinearGradientMode;
            g.FillPath(new LinearGradientBrush(rectTabOrigin, startColor, endColor, gradientMode), path);
            g.DrawPath(PenTabBorder, path);

            // Set no rotate for drawing icon and text
            Matrix matrixRotate = g.Transform;
            g.Transform = MatrixIdentity;

            // Draw the icon
            Rectangle rectImage = rectTabOrigin;
            rectImage.X += ImageGapLeft;
            rectImage.Y += ImageGapTop;
            int imageHeight = rectTabOrigin.Height - ImageGapTop - ImageGapBottom;
            int imageWidth = ImageWidth;
            if (imageHeight > ImageHeight)
                imageWidth = ImageWidth * (imageHeight / ImageHeight);
            rectImage.Height = imageHeight;
            rectImage.Width = imageWidth;
            rectImage = this.GetTransformedRectangle(dockState, rectImage);

            if (dockState == DockState.DockLeftAutoHide || dockState == DockState.DockRightAutoHide)
            {
                // The DockState is DockLeftAutoHide or DockRightAutoHide, so rotate the _srcTexture 90 degrees to the right. 
                Rectangle rectTransform = this.RtlTransform(rectImage, dockState);
                Point[] rotationPoints =
                { 
                    new Point(rectTransform.X + rectTransform.Width, rectTransform.Y), 
                    new Point(rectTransform.X + rectTransform.Width, rectTransform.Y + rectTransform.Height), 
                    new Point(rectTransform.X, rectTransform.Y)
                };

                using (var rotatedIcon = new Icon(((Form)content).Icon, 16, 16))
                {
                    g.DrawImage(rotatedIcon.ToBitmap(), rotationPoints);
                }
            }
            else
            {
                // Draw the icon normally without any rotation.
                g.DrawIcon(((Form)content).Icon, this.RtlTransform(rectImage, dockState));
            }

            // Draw the text
            Rectangle rectText = rectTabOrigin;
            rectText.X += ImageGapLeft + imageWidth + ImageGapRight + TextGapLeft;
            rectText.Width -= ImageGapLeft + imageWidth + ImageGapRight + TextGapLeft;
            rectText = this.RtlTransform(this.GetTransformedRectangle(dockState, rectText), dockState);

            Color textColor = DockPanel.Skin.AutoHideStripSkin.TabGradient.TextColor;

            if (dockState == DockState.DockLeftAutoHide || dockState == DockState.DockRightAutoHide)
                g.DrawString(content.DockHandler.TabText, this.TextFont, new SolidBrush(textColor), rectText, this.StringFormatTabVertical);
            else
                g.DrawString(content.DockHandler.TabText, this.TextFont, new SolidBrush(textColor), rectText, this.StringFormatTabHorizontal);

            // Set rotate back
            g.Transform = matrixRotate;
        }

        private Rectangle GetLogicalTabStripRectangle(DockState dockState)
        {
            return this.GetLogicalTabStripRectangle(dockState, false);
        }

        private Rectangle GetLogicalTabStripRectangle(DockState dockState, bool transformed)
        {
            if (!DockHelper.IsDockStateAutoHide(dockState))
                return Rectangle.Empty;

            int leftPanes = GetPanes(DockState.DockLeftAutoHide).Count;
            int rightPanes = GetPanes(DockState.DockRightAutoHide).Count;
            int topPanes = GetPanes(DockState.DockTopAutoHide).Count;
            int bottomPanes = GetPanes(DockState.DockBottomAutoHide).Count;

            int x, y, width, height;

            height = this.MeasureHeight();
            if (dockState == DockState.DockLeftAutoHide && leftPanes > 0)
            {
                x = 0;
                y = (topPanes == 0) ? 0 : height;
                width = Height - (topPanes == 0 ? 0 : height) - (bottomPanes == 0 ? 0 : height);
            }
            else if (dockState == DockState.DockRightAutoHide && rightPanes > 0)
            {
                x = Width - height;
                if (leftPanes != 0 && x < height)
                    x = height;
                y = (topPanes == 0) ? 0 : height;
                width = Height - (topPanes == 0 ? 0 : height) - (bottomPanes == 0 ? 0 : height);
            }
            else if (dockState == DockState.DockTopAutoHide && topPanes > 0)
            {
                x = leftPanes == 0 ? 0 : height;
                y = 0;
                width = Width - (leftPanes == 0 ? 0 : height) - (rightPanes == 0 ? 0 : height);
            }
            else if (dockState == DockState.DockBottomAutoHide && bottomPanes > 0)
            {
                x = leftPanes == 0 ? 0 : height;
                y = Height - height;
                if (topPanes != 0 && y < height)
                    y = height;
                width = Width - (leftPanes == 0 ? 0 : height) - (rightPanes == 0 ? 0 : height);
            }
            else
                return Rectangle.Empty;

            if (!transformed)
                return new Rectangle(x, y, width, height);
            else
                return this.GetTransformedRectangle(dockState, new Rectangle(x, y, width, height));
        }

        private Rectangle GetTabRectangle(TabVS2005 tab)
        {
            return this.GetTabRectangle(tab, false);
        }

        private Rectangle GetTabRectangle(TabVS2005 tab, bool transformed)
        {
            DockState dockState = tab.Content.DockHandler.DockState;
            Rectangle rectTabStrip = this.GetLogicalTabStripRectangle(dockState);

            if (rectTabStrip.IsEmpty)
                return Rectangle.Empty;

            int x = tab.TabX;
            int y = rectTabStrip.Y +
                (dockState == DockState.DockTopAutoHide || dockState == DockState.DockRightAutoHide ?
                0 : TabGapTop);
            int width = tab.TabWidth;
            int height = rectTabStrip.Height - TabGapTop;

            if (!transformed)
                return new Rectangle(x, y, width, height);
            else
                return this.GetTransformedRectangle(dockState, new Rectangle(x, y, width, height));
        }

        private Rectangle GetTransformedRectangle(DockState dockState, Rectangle rect)
        {
            if (dockState != DockState.DockLeftAutoHide && dockState != DockState.DockRightAutoHide)
                return rect;

            var pts = new PointF[1];
            // the center of the rect
            pts[0].X = rect.X + (float)rect.Width / 2;
            pts[0].Y = rect.Y + (float)rect.Height / 2;
            Rectangle rectTabStrip = this.GetLogicalTabStripRectangle(dockState);
            var matrix = new Matrix();
            matrix.RotateAt(90, new PointF(rectTabStrip.X + (float)rectTabStrip.Height / 2,
                rectTabStrip.Y + (float)rectTabStrip.Height / 2));
            matrix.TransformPoints(pts);

            return new Rectangle((int)(pts[0].X - (float)rect.Height / 2 + .5F),
                (int)(pts[0].Y - (float)rect.Width / 2 + .5F),
                rect.Height, rect.Width);
        }

        protected override IDockContent HitTest(Point ptMouse)
        {
            foreach (DockState state in DockStates)
            {
                Rectangle rectTabStrip = this.GetLogicalTabStripRectangle(state, true);
                if (!rectTabStrip.Contains(ptMouse))
                    continue;

                foreach (Pane pane in GetPanes(state))
                {
                    foreach (TabVS2005 tab in pane.AutoHideTabs)
                    {
                        GraphicsPath path = this.GetTabOutline(tab, true, true);
                        if (path.IsVisible(ptMouse))
                            return tab.Content;
                    }
                }
            }

            return null;
        }

        protected internal override int MeasureHeight()
        {
            return Math.Max(ImageGapBottom +
                ImageGapTop + ImageHeight,
                this.TextFont.Height) + TabGapTop;
        }

        protected override void OnRefreshChanges()
        {
            this.CalculateTabs();
            Invalidate();
        }

        protected override Tab CreateTab(IDockContent content)
        {
            return new TabVS2005(content);
        }
    }
}
