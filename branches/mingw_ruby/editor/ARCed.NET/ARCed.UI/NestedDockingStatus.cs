#region Using Directives

using System.Drawing;

#endregion

namespace ARCed.UI
{
	public sealed class NestedDockingStatus
	{
		internal NestedDockingStatus(DockPane pane)
		{
			this._mDockPane = pane;
		}

	    private readonly DockPane _mDockPane;
		public DockPane DockPane
		{
			get	{	return this._mDockPane;	}
		}

	    private NestedPaneCollection m_nestedPanes;
		public NestedPaneCollection NestedPanes
		{
			get	{	return this.m_nestedPanes;	}
		}
		
		private DockPane m_previousPane;
		public DockPane PreviousPane
		{
			get	{	return this.m_previousPane;	}
		}

		private DockAlignment m_alignment = DockAlignment.Left;
		public DockAlignment Alignment
		{
			get	{	return this.m_alignment;	}
		}

		private double m_proportion = 0.5;
		public double Proportion
		{
			get	{	return this.m_proportion;	}
		}

		private bool m_isDisplaying;
		public bool IsDisplaying
		{
			get	{	return this.m_isDisplaying;	}
		}

		private DockPane m_displayingPreviousPane;
		public DockPane DisplayingPreviousPane
		{
			get	{	return this.m_displayingPreviousPane;	}
		}

		private DockAlignment m_displayingAlignment = DockAlignment.Left;
		public DockAlignment DisplayingAlignment
		{
			get	{	return this.m_displayingAlignment;	}
		}

		private double m_displayingProportion = 0.5;
		public double DisplayingProportion
		{
			get	{	return this.m_displayingProportion;	}
		}

		private Rectangle m_logicalBounds = Rectangle.Empty; 
		public Rectangle LogicalBounds
		{
			get	{	return this.m_logicalBounds;	}
		}

		private Rectangle m_paneBounds = Rectangle.Empty;
		public Rectangle PaneBounds
		{
			get	{	return this.m_paneBounds;	}
		}

		private Rectangle m_splitterBounds = Rectangle.Empty;
		public Rectangle SplitterBounds
		{
			get	{	return this.m_splitterBounds;	}
		}

		internal void SetStatus(NestedPaneCollection nestedPanes, DockPane previousPane, DockAlignment alignment, double proportion)
		{
			this.m_nestedPanes = nestedPanes;
			this.m_previousPane = previousPane;
			this.m_alignment = alignment;
			this.m_proportion = proportion;
		}

		internal void SetDisplayingStatus(bool isDisplaying, DockPane displayingPreviousPane, DockAlignment displayingAlignment, double displayingProportion)
		{
			this.m_isDisplaying = isDisplaying;
			this.m_displayingPreviousPane = displayingPreviousPane;
			this.m_displayingAlignment = displayingAlignment;
			this.m_displayingProportion = displayingProportion;
		}

		internal void SetDisplayingBounds(Rectangle logicalBounds, Rectangle paneBounds, Rectangle splitterBounds)
		{
			this.m_logicalBounds = logicalBounds;
			this.m_paneBounds = paneBounds;
			this.m_splitterBounds = splitterBounds;
		}
	}
}
