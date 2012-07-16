#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Control used for displaying and modifying a efficiency value
	/// </summary>
	[Description("Control used for displaying and modifying a efficiency value.")]
	[ToolboxBitmap(typeof(NumericUpDown))]
	public partial class EfficiencySlot : UserControl
	{
		#region Public Properties

		/// <summary>
		/// Gets or sets the colors used for drawing the corresponding values.
		/// </summary>
		[Category("ARCed"), Description("Define the colors used for drawing the corresponding values.")]
		public Color[] TextColors { get; set; }

		/// <summary>
		/// Gets or sets the items that can be selected in the control.
		/// </summary>
		[Category("ARCed"), Description("Define the items that can be selected in the control.")]
		public string[] Items { get; set; }

		/// <summary>
		/// Gets or sets the selected index of the spin control.
		/// </summary>
		[Browsable(false)]
		public int SelectedIndex
		{
			get { return domainUpDown.SelectedIndex; }
			set { domainUpDown.SelectedIndex = value; }
		}

		#endregion

		#region Events

		public delegate void ItemChangedEventHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised whenever a value of an efficiency slot is changed.
		/// </summary>
		[Category("ARCed")]
		[Description("Event raised whenever a value of an efficiency slot is changed")]
		public event ItemChangedEventHandler OnItemChange;

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor.
		/// </summary>
		/// <param name="label">Label applied to the slot</param>
		/// <param name="items">Values that can be selected</param>
		/// <param name="colors">Text colors used for corresponding values</param>
		public EfficiencySlot(string label, IEnumerable<string> items, Color[] colors)
		{
			InitializeComponent();
			labelValue.Text = label;
			foreach (string item in items)
				domainUpDown.Items.Add(item);
			TextColors = colors;
			domainUpDown.SelectedItemChanged += this.domainUpDown_SelectedItemChanged;
		}

		#endregion

		#region Private Methods

		private void RefreshItems()
		{
			domainUpDown.Items.Clear();
			foreach (string item in Items)
				domainUpDown.Items.Add(item);
		}

		private void domainUpDown_SelectedItemChanged(object sender, EventArgs e)
		{
			domainUpDown.ForeColor = TextColors[domainUpDown.SelectedIndex];
			if (OnItemChange != null)
				OnItemChange(this, e);
		}

		#endregion
	}
}
