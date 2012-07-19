#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// CheckedListBox control that allows multiple states and markers.
	/// </summary>
	[ToolboxBitmap(typeof(GroupBox))]
	[Description("CheckedListBox control that allows multiple states and markers.")]
	public partial class MultiStateCheckedListBox : GroupBox
	{
		#region Private Fields

		private bool _suppressEvents;
		private static readonly Padding _padding = new Padding(3, 0, 3, 0);

		#endregion

		#region Events

		/// <summary>
		/// Handler for events raised when an item is changed on the control
		/// </summary>
		/// <param name="sender">Invoker of the event</param>
		/// <param name="e">Event arguments</param>
		public delegate void ItemValueChangedEventHandler(object sender, MultiStateCheckEventArgs e);

		/// <summary>
		/// Event raised when an item is changed on the control
		/// </summary>
		[Category("ARCed")]
		[Description("Event raised when an item is changed on the control")]
		public event ItemValueChangedEventHandler OnItemChanged;

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public MultiStateCheckedListBox()
		{
			this.InitializeComponent();
			this.flowPanel.Padding = new Padding(0);
		}

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the string values that can be selected
		/// </summary>
		[Category("ARCed")]
		[Description("Define the selectable values in the slots")]
		public string[] Items { get; set; }

		/// <summary>
		/// Gets or sets the colors used for the text for different items
		/// </summary>
		[Category("ARCed")]
		[Description("Define the text colors used for the corresponding items")]
		public Color[] Colors { get; set; }

		#endregion

		#region Public Methods

		/// <summary>
		/// Clears the controls of the container
		/// </summary>
		public void ClearItems()
		{
			this.flowPanel.Controls.Clear();
		}

		/// <summary>
		/// Adds a new slot to the container
		/// </summary>
		/// <param name="label">Label to apply to the slot</param>
		public void AddItem(string label)
		{
			this.AddItem(label, -1);
		}

		/// <summary>
		/// Adds a new slot to the container
		/// </summary>
		/// <param name="label">Label to apply to the slot</param>
		/// <param name="valueIndex">Index of the slot's value</param>
		public void AddItem(string label, int valueIndex)
		{
			var checkBox = new MultiStateCheckbox
			{
			    Margin = _padding,
			    Characters = this.Items,
			    CharColors = this.Colors,
			    Height = 16,
			    Text = label
			};
		    if (valueIndex >= 0)
				checkBox.SelectedState = valueIndex;
			checkBox.MouseDown += this.slot_OnTextChange;
			this.flowPanel.Controls.Add(checkBox);
		}

		/// <summary>
		/// Sets the value index of the MultiStateCheckBox at the given index
		/// </summary>
		/// <param name="itemIndex">Index of the control in the parent container</param>
		/// <param name="valueIndex">Index of the slot's value</param>
		public void SetItemIndex(int itemIndex, int valueIndex)
		{
			this._suppressEvents = true;
			if (itemIndex.IsBetween(0, this.flowPanel.Controls.Count - 1))
			{
				(this.flowPanel.Controls[itemIndex] as MultiStateCheckbox).SelectedState =
					valueIndex.Clamp(0, this.Items.Length - 1);
			}
			this._suppressEvents = false;
		}

		/// <summary>
		/// Sets all checkbox controls to the given state
		/// </summary>
		/// <param name="index">State to set the checkboxes</param>
		/// <remarks>This methods does not raise events</remarks>
		public void SetAll(int index)
		{
			this._suppressEvents = true;
			foreach (MultiStateCheckbox cBox in this.flowPanel.Controls)
				cBox.SelectedState = index;
			this._suppressEvents = false;
		}

		#endregion

		#region Private Methods

		private void slot_OnTextChange(object sender, EventArgs e)
		{
			if (this.OnItemChanged != null && !this._suppressEvents)
			{
				var checkBox = sender as MultiStateCheckbox;
				int vIndex = checkBox.SelectedState;
				int index = this.flowPanel.Controls.IndexOf(checkBox);
				this.OnItemChanged(sender, new MultiStateCheckEventArgs(index, vIndex));
			}
		}

		#endregion
	}

	/// <summary>
	/// Arguments for EfficiencySlot events
	/// </summary>
	public class MultiStateCheckEventArgs : EventArgs 
	{
		/// <summary>
		/// Index of the control in the parent container
		/// </summary>
		public int Index { get; private set; }
		/// <summary>
		/// Index of the slot's value
		/// </summary>
		public int ValueIndex { get; private set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		/// <param name="index">Index of the control in the parent container</param>
		/// <param name="valueIndex">Index of the slot's value</param>
		public MultiStateCheckEventArgs(int index, int valueIndex)
		{
			this.Index = index;
			this.ValueIndex = valueIndex;
		}
	}
}
