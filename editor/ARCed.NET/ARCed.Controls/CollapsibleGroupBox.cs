#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using System.Windows.Forms.VisualStyles;

#endregion

namespace ARCed.Controls
{
    /// <summary>
    /// GroupBox control that provides functionality to allow it to be collapsed.
    /// </summary>
	[Description("GroupBox control that provides functionality to allow it to be collapsed.")]
	[ToolboxBitmap(typeof(GroupBox))]
    public partial class CollapsibleGroupBox : GroupBox
    {
        #region Private Fields

        private Rectangle _mToggleRect = new Rectangle(8, 2, 11, 11);
        private Boolean _mCollapsed;
        private Boolean _mBResizingFromCollapse;
        private const int M_COLLAPSED_HEIGHT = 20;
        private Size _mFullSize = Size.Empty;

        #endregion

        #region Events

        public delegate void CollapseBoxClickedEventHandler(object sender);
		/// <summary>
		/// Fired when the Collapse Toggle button is pressed
		/// </summary>
		[Category("ARCed")]
		[Description("Fired when the Collapse Toggle button is pressed")]
        public event CollapseBoxClickedEventHandler CollapseBoxClickedEvent;

        #endregion

        #region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
        public CollapsibleGroupBox()
        {
            InitializeComponent();
        }

        #endregion

        #region Public Properties

		/// <summary>
		/// Gets the height of the groupbox when expanded
		/// </summary>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int FullHeight
        {
            get { return this._mFullSize.Height; }
        }

		/// <summary>
		/// Gets the height of the groupbox when collapsed
		/// </summary>
		[Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
		public int CollapsedHeight
		{
			get { return M_COLLAPSED_HEIGHT; }
		}

		/// <summary>
		/// Gets the collapsed state of the control
		/// </summary>
		[Category("ARCed")]
		[Description("Collapse state of the control")]
        [DefaultValue(false), Browsable(true), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public bool IsCollapsed
        {
            get { return this._mCollapsed; }
            set
            {
                if (value != this._mCollapsed)
                {
                    this._mCollapsed = value;

                    if (!value)
                        // Expand
                        this.Size = this._mFullSize;
                    else
                    {
                        // Collapse
                        this._mBResizingFromCollapse = true;
                        this.Height = M_COLLAPSED_HEIGHT;
                        this._mBResizingFromCollapse = false;
                    }

                    foreach (Control c in Controls)
                        c.Visible = !value;

                    Invalidate();
                }
            }
        }

        #endregion

		#region Public Methods

		/// <summary>
		/// Toggles the collapsed state of the groupbox
		/// </summary>
		public void ToggleCollapsed()
		{
			IsCollapsed = !IsCollapsed;
			if (CollapseBoxClickedEvent != null)
				CollapseBoxClickedEvent(this);
		}

		#endregion

		#region Overrides

		protected override void OnMouseUp(MouseEventArgs e)
        {
            if (this._mToggleRect.Contains(e.Location))
                ToggleCollapsed();
            else
                base.OnMouseUp(e);
        }

        protected override void OnPaint(PaintEventArgs e)
        {
            HandleResize();
            DrawGroupBox(e.Graphics);
            DrawToggleButton(e.Graphics);
        }

        #endregion

        #region Private Methods

        private void DrawGroupBox(Graphics g)
        {
            // Get windows to draw the GroupBox
            var bounds = new Rectangle(ClientRectangle.X, ClientRectangle.Y + 6, ClientRectangle.Width, ClientRectangle.Height - 6);
            GroupBoxRenderer.DrawGroupBox(g, bounds, Enabled ? GroupBoxState.Normal : GroupBoxState.Disabled);

            // Text Formating positioning & Size
            var sf = new StringFormat();
            int i_textPos = (bounds.X + 8) + this._mToggleRect.Width + 2;
            var i_textSize = (int)g.MeasureString(Text, this.Font).Width;
            i_textSize = i_textSize < 1 ? 1 : i_textSize;
            int i_endPos = i_textPos + i_textSize + 1;

            // Draw a line to cover the GroupBox border where the text will sit
            g.DrawLine(SystemPens.Control, i_textPos, bounds.Y, i_endPos, bounds.Y);

            // Draw the GroupBox text
            using (var drawBrush = new SolidBrush(Color.FromArgb(0, 70, 213)))
                g.DrawString(Text, this.Font, drawBrush, i_textPos, 0);
        }

        private void DrawToggleButton(Graphics g)
        {
            if(IsCollapsed)
                g.DrawImage(Resources.FoldExpand, this._mToggleRect);
            else
                g.DrawImage(Resources.FoldCollapse, this._mToggleRect);
        }

        private void HandleResize()
        {
            if (!this._mBResizingFromCollapse && !this._mCollapsed)
                this._mFullSize = this.Size;
        }

        #endregion
    }
}