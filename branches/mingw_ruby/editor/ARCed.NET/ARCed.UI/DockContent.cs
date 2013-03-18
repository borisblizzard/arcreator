#region Using Directives

using System;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.UI
{
	public class DockContent : Form, IDockContent
	{
		public DockContent()
		{
			this._mDockHandler = new DockContentHandler(this, this.GetPersistString);
			this._mDockHandler.DockStateChanged += this.DockHandler_DockStateChanged;
			//Suggested as a fix by bensty regarding form resize
            ParentChanged += this.DockContent_ParentChanged;
		}

		//Suggested as a fix by bensty regarding form resize
        private void DockContent_ParentChanged(object Sender, EventArgs e)
        {
            if (Parent != null)
                Font = Parent.Font;
		}

	    private readonly DockContentHandler _mDockHandler;
		[Browsable(false)]
		public DockContentHandler DockHandler
		{
			get	{	return this._mDockHandler;	}
		}

		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockContent_AllowEndUserDocking_Description")]
		[DefaultValue(true)]
		public bool AllowEndUserDocking
		{
			get	{	return this.DockHandler.AllowEndUserDocking;	}
			set	{	this.DockHandler.AllowEndUserDocking = value;	}
		}

		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockContent_DockAreas_Description")]
		[DefaultValue(DockAreas.DockLeft|DockAreas.DockRight|DockAreas.DockTop|DockAreas.DockBottom|DockAreas.Document|DockAreas.Float)]
		public DockAreas DockAreas
		{
			get	{	return this.DockHandler.DockAreas;	}
			set	{	this.DockHandler.DockAreas = value;	}
		}

		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockContent_AutoHidePortion_Description")]
		[DefaultValue(0.25)]
		public double AutoHidePortion
		{
			get	{	return this.DockHandler.AutoHidePortion;	}
			set	{	this.DockHandler.AutoHidePortion = value;	}
		}

		[Localizable(true)]
		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockContent_TabText_Description")]
		[DefaultValue(null)]
        private string m_tabText;
		public string TabText
		{
            get { return this.m_tabText; }
            set { this.DockHandler.TabText = this.m_tabText = value; }
		}
		private bool ShouldSerializeTabText()
		{
			return (this.m_tabText != null);
		}

		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockContent_CloseButton_Description")]
		[DefaultValue(true)]
		public bool CloseButton
		{
			get	{	return this.DockHandler.CloseButton;	}
			set	{	this.DockHandler.CloseButton = value;	}
		}

        [LocalizedCategory("Category_Docking")]
        [LocalizedDescription("DockContent_CloseButtonVisible_Description")]
        [DefaultValue(true)]
        public bool CloseButtonVisible
        {
            get { return this.DockHandler.CloseButtonVisible; }
            set { this.DockHandler.CloseButtonVisible = value; }
        }

		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockContent_DefaultFloatSize_Description")]
		[DefaultValue(null)]
		public Size DefaultFloatSize
		{
			get;
			set;
		}
		
		[Browsable(false)]
		public DockPanel DockPanel
		{
			get {	return this.DockHandler.DockPanel; }
			set	{	this.DockHandler.DockPanel = value;	}
		}

		[Browsable(false)]
		public DockState DockState
		{
			get	{	return this.DockHandler.DockState;	}
			set	{	this.DockHandler.DockState = value;	}
		}

		[Browsable(false)]
		public DockPane Pane
		{
			get {	return this.DockHandler.Pane; }
			set	{	this.DockHandler.Pane = value;		}
		}

		[Browsable(false)]
		public bool IsHidden
		{
			get	{	return this.DockHandler.IsHidden;	}
			set	{	this.DockHandler.IsHidden = value;	}
		}

		[Browsable(false)]
		public DockState VisibleState
		{
			get	{	return this.DockHandler.VisibleState;	}
			set	{	this.DockHandler.VisibleState = value;	}
		}

		[Browsable(false)]
		public bool IsFloat
		{
			get	{	return this.DockHandler.IsFloat;	}
			set	{	this.DockHandler.IsFloat = value;	}
		}

		[Browsable(false)]
		public DockPane PanelPane
		{
			get	{	return this.DockHandler.PanelPane;	}
			set	{	this.DockHandler.PanelPane = value;	}
		}

		[Browsable(false)]
		public DockPane FloatPane
		{
			get	{	return this.DockHandler.FloatPane;	}
			set	{	this.DockHandler.FloatPane = value;	}
		}

        [SuppressMessage("Microsoft.Design", "CA1024:UsePropertiesWhereAppropriate")]
        protected virtual string GetPersistString()
		{
            return GetType().ToString();
		}

		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockContent_HideOnClose_Description")]
		[DefaultValue(false)]
		public bool HideOnClose
		{
			get	{	return this.DockHandler.HideOnClose;	}
			set	{	this.DockHandler.HideOnClose = value;	}
		}

		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockContent_ShowHint_Description")]
		[DefaultValue(DockState.Unknown)]
		public DockState ShowHint
		{
			get	{	return this.DockHandler.ShowHint;	}
			set	{	this.DockHandler.ShowHint = value;	}
		}

		[Browsable(false)]
		public bool IsActivated
		{
			get	{	return this.DockHandler.IsActivated;	}
		}

		public bool IsDockStateValid(DockState dockState)
		{
			return this.DockHandler.IsDockStateValid(dockState);
		}

		[LocalizedCategory("Category_Docking")]
		[LocalizedDescription("DockContent_TabPageContextMenu_Description")]
		[DefaultValue(null)]
		public ContextMenu TabPageContextMenu
		{
			get	{	return this.DockHandler.TabPageContextMenu;	}
			set	{	this.DockHandler.TabPageContextMenu = value;	}
		}

        [LocalizedCategory("Category_Docking")]
        [LocalizedDescription("DockContent_TabPageContextMenuStrip_Description")]
        [DefaultValue(null)]
        public ContextMenuStrip TabPageContextMenuStrip
        {
            get { return this.DockHandler.TabPageContextMenuStrip; }
            set { this.DockHandler.TabPageContextMenuStrip = value; }
        }

		[Localizable(true)]
		[Category("Appearance")]
		[LocalizedDescription("DockContent_ToolTipText_Description")]
		[DefaultValue(null)]
		public string ToolTipText
		{
			get	{	return this.DockHandler.ToolTipText;	}
			set {	this.DockHandler.ToolTipText = value;	}
		}

		public new void Activate()
		{
			this.DockHandler.Activate();
		}

		public new void Hide()
		{
			this.DockHandler.Hide();
		}

		public new void Show()
		{
			this.DockHandler.Show();
		}

		public void Show(DockPanel dockPanel)
		{
			this.DockHandler.Show(dockPanel);
		}

		public void Show(DockPanel dockPanel, DockState dockState)
		{
			this.DockHandler.Show(dockPanel, dockState);
		}

        [SuppressMessage("Microsoft.Naming", "CA1720:AvoidTypeNamesInParameters")]
		public void Show(DockPanel dockPanel, Rectangle floatWindowBounds)
		{
			this.DockHandler.Show(dockPanel, floatWindowBounds);
		}

		public void Show(DockPane pane, IDockContent beforeContent)
		{
			this.DockHandler.Show(pane, beforeContent);
		}

		public void Show(DockPane previousPane, DockAlignment alignment, double proportion)
		{
			this.DockHandler.Show(previousPane, alignment, proportion);
		}

        [SuppressMessage("Microsoft.Naming", "CA1720:AvoidTypeNamesInParameters")]
        public void FloatAt(Rectangle floatWindowBounds)
        {
            this.DockHandler.FloatAt(floatWindowBounds);
        }

        public void DockTo(DockPane paneTo, DockStyle dockStyle, int contentIndex)
        {
            this.DockHandler.DockTo(paneTo, dockStyle, contentIndex);
        }

        public void DockTo(DockPanel panel, DockStyle dockStyle)
        {
            this.DockHandler.DockTo(panel, dockStyle);
        }

		#region IDockContent Members
		void IDockContent.OnActivated(EventArgs e)
		{
			OnActivated(e);
		}

		void IDockContent.OnDeactivate(EventArgs e)
		{
			OnDeactivate(e);
		}
		#endregion

		#region Events
		private void DockHandler_DockStateChanged(object sender, EventArgs e)
		{
			this.OnDockStateChanged(e);
		}

		private static readonly object DockStateChangedEvent = new object();
		[LocalizedCategory("Category_PropertyChanged")]
		[LocalizedDescription("Pane_DockStateChanged_Description")]
		public event EventHandler DockStateChanged
		{
			add	{	Events.AddHandler(DockStateChangedEvent, value);	}
			remove	{	Events.RemoveHandler(DockStateChangedEvent, value);	}
		}
		protected virtual void OnDockStateChanged(EventArgs e)
		{
			var handler = (EventHandler)Events[DockStateChangedEvent];
			if (handler != null)
				handler(this, e);
		}
		#endregion
	}
}
