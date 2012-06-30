using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Helpers;
using ARCed.Dialogs;

namespace ARCed.Controls
{
	/// <summary>
	/// Control that handles selecting and changing quantity of a collection of game objects.
	/// </summary>
	[Description("Control that handles selecting and changing quantity of a collection of game objects.")]
	[ToolboxBitmap(typeof(GroupBox))]
	public partial class DatabaseObjectListBox : GroupBox
	{

		#region Events

		public delegate void ButtonMaxClickEventHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised when "Change Maximum" button is clicked
		/// </summary>
		[Category("ARCed")]
		[Description("Event raised when \"Change Maximum\" button is clicked")]
		public event ButtonMaxClickEventHandler OnButtonMaxClick;

		public delegate void ObjectListIndexChangedEventHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised when the index of the control's listbox is changed
		/// </summary>
		[Category("ARCed")]
		[Description("Event raised when the index of the control's listbox is changed")]
		public event ObjectListIndexChangedEventHandler OnListBoxIndexChanged; 

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the text drawn in the header
		/// </summary>
		[Category("ARCed")]
		[Description("Defines the text drawn in the header")]
		[DefaultValue("")]
		public string HeaderText { get; set; }

		/// <summary>
		/// Gets or sets the selected index of the listbox on the control
		/// </summary>
		[Browsable(false)]
		public int SelectedIndex 
		{
			get { return listBoxObjects.SelectedIndex; }
			set { listBoxObjects.SelectedIndex = value; }
		}

		/// <summary>
		/// Gets the "Change Max" button on the control
		/// </summary>
		[Browsable(false)]
		[DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
		public Button ButtonMaximum { get { return buttonMaximum; } }

		/// <summary>
		/// Gets the listbox on the control
		/// </summary>
		[Browsable(false)]
		[DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
		public ListBox ListBox { get { return listBoxObjects; } }

		/// <summary>
		/// Gets the picture box on the control
		/// </summary>
		[Browsable(false)]
		[DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
		public PictureBox PictureBox { get { return pictureBoxHeader; } }

		/// <summary>
		/// Gets the items in the listbox on the control
		/// </summary>
		[Browsable(false)]
		[DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
		public ListBox.ObjectCollection Items { get { return listBoxObjects.Items; } }

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public DatabaseObjectListBox()
		{
			InitializeComponent();
			toolStripMenuItemEdit.Click += new EventHandler(pictureBoxHeader_DoubleClick);
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Returns the bounding rectangle for an item in the control's listbox
		/// </summary>
		/// <param name="index">Index of the item in the listbox to get the rectangle for</param>
		/// <returns>Rectangle of the item</returns>
		public System.Drawing.Rectangle GetItemRectangle(int index)
		{
			return listBoxObjects.GetItemRectangle(index);
		}

		/// <summary>
		/// Clears and populates the listbox on the control with the given collection of objects
		/// </summary>
		/// <typeparam name="T">Object type that interfaces RPG.IRpgObject</typeparam>
		/// <param name="objectList">Collection of items</param>
		public void PopulateList(List<dynamic> objectList)
		{
			DatabaseHelper.Populate(listBoxObjects, objectList, false);
		}

		/// <summary>
		/// Maintains performance while items are added to the control's 
		/// listbox one at a time by preventing painting until EndUpdate() is called.
		/// </summary>
		public void BeginUpdate()
		{
			listBoxObjects.BeginUpdate();
		}

		/// <summary>
		/// Resumes painting of the control's listbox after painting 
		/// is suspended from calling BeginUpdate().
		/// </summary>
		public void EndUpdate()
		{
			listBoxObjects.EndUpdate();
		}

		/// <summary>
		/// Forces a repainting of the header. Called after settings have changed.
		/// </summary>
		public void RefreshHeader()
		{
			DatabaseHelper.RenderHeaderImage(pictureBoxHeader, HeaderText);
		}

		#endregion

		#region Private Methods

		private void pictureBoxHeader_DoubleClick(object sender, EventArgs e)
		{
			using (HeaderSettingsDialog dialog = new HeaderSettingsDialog())
				dialog.ShowDialog();
		}

		private void listBoxObjects_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (OnListBoxIndexChanged != null)
				OnListBoxIndexChanged(sender, e);
		}

		private void pictureBoxHeader_Resize(object sender, EventArgs e)
		{
			if (!DesignMode)
				DatabaseHelper.RenderHeaderImage(pictureBoxHeader, HeaderText);
		}

		private void buttonMaximum_Click(object sender, EventArgs e)
		{
			if (OnButtonMaxClick != null)
				OnButtonMaxClick(sender, e);
		}

		#endregion
	}
}
