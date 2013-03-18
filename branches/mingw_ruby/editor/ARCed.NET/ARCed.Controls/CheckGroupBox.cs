#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Groupbox control that contains a CheckedListBox with buttons for selecting/deseleting all items
	/// </summary>
	[Description("GroupBox control that contains a CheckedListBox with buttons for selecting/deseleting all items.")]
	[ToolboxBitmap(typeof(GroupBox))]
	public partial class CheckGroupBox : GroupBox
	{
		#region Public Properties

		/// <summary>
		/// Gets the items of the control's CheckedListBox
		/// </summary>
		[Category("ARCed")]
		[Description("Edit the items contained in the control")]
		public CheckedListBox.ObjectCollection Items
		{
			get { return this.checkedList.Items; }
		}

		/// <summary>
		/// Gets the instance of the control's CheckedListBox
		/// </summary>
		[Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
		public CheckedListBox CheckListBox
		{
			get { return this.checkedList; }
		}

		/// <summary>
		/// Gets the selected index of the control's CheckedListBox
		/// </summary>
		[Browsable(false)]
		public int SelectedIndex
		{
			get { return this.checkedList.SelectedIndex; }
			set { this.checkedList.SelectedIndex = value; }
		}

		#endregion

		#region Events

		public delegate void CheckChangeEventHandler(object sender, ItemCheckEventArgs e);
		/// <summary>
		/// Event raised when a checkbox state is changed in the list control
		/// </summary>
		[Category("ARCed")]
		[Description("Event raised when a checkbox state is changed in the list control")]
		public event CheckChangeEventHandler OnCheckChange;

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public CheckGroupBox()
		{
			this.InitializeComponent();
		}

		/// <summary>
		/// Constructor with arguments
		/// </summary>
		/// <param name="container">Container for components</param>
		public CheckGroupBox(IContainer container)
		{
			this.InitializeComponent();
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Maintains performance while items are added to the control's 
		/// CheckedListBox one at a time by preventing painting until EndUpdate() is called.
		/// </summary>
		public void BeginUpdate()
		{
			this.checkedList.BeginUpdate();
		}

		/// <summary>
		/// Resumes painting of the control's CheckedListBox after painting 
		/// is suspended from calling BeginUpdate().
		/// </summary>
		public void EndUpdate()
		{
			this.checkedList.EndUpdate();
		}

		/// <summary>
		/// Sets all checkboxes to the given state
		/// </summary>
		/// <param name="checkState">State to set the checkboxes</param>
		public void CheckAll(bool checkState)
		{
			for (int i = 0; i < this.checkedList.Items.Count; i++)
				this.checkedList.SetItemChecked(i, checkState);
		}

		/// <summary>
		/// Sets a checkbox to the given state
		/// </summary>
		/// <param name="index">Index of the checkbox</param>
		/// <param name="checkState">State to set checkbox</param>
		public void SetItemChecked(int index, bool checkState)
		{
			this.checkedList.SetItemChecked(index, checkState);
		}

		/// <summary>
		/// Gets the state of a checkbox
		/// </summary>
		/// <param name="index">Index of the checkbox</param>
		/// <returns>State of the checkbox</returns>
		public bool GetItemChecked(int index)
		{
			return this.checkedList.GetItemChecked(index);
		}

		#endregion

		#region Private Methods

		private void buttonNone_Click(object sender, EventArgs e)
		{
			this.CheckAll(false);
		}

		private void buttonAll_Click(object sender, EventArgs e)
		{
			this.CheckAll(true);
		}

		private void checkedList_ItemCheck(object sender, ItemCheckEventArgs e)
		{
			if (this.OnCheckChange != null)
				this.OnCheckChange(this, e);
		}

		#endregion
	}
}
