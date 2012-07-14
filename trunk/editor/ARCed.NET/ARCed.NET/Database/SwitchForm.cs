using System;
using System.Collections.Generic;
using ARCed.Controls;

namespace ARCed.Database
{
	/// <summary>
	/// Enum for determining data type between switches and variables.
	/// </summary>
	public enum SwitchType
	{
		/// <summary>
		/// Flag representing a game switch.
		/// </summary>
		Switch,
		/// <summary>
		/// Flag representing a game variable.
		/// </summary>
		Variable
	}

	/// <summary>
	/// Form fo displaying and editing in game switches and variables.
	/// </summary>
	public partial class SwitchForm : DatabaseWindow
	{
		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return dataObjectList; } }

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the type of the form when it was initialized 
		/// </summary>
		public SwitchType FormType { get; private set; }
		/// <summary>
		/// Gets or sets the ID of the selected item
		/// </summary>
		public int SelectedId 
		{ 
			get { return dataObjectList.SelectedIndex + 1; }
			set { dataObjectList.SelectedIndex = value - 1; }
		}
		/// <summary>
		/// Gets the selected switch
		/// </summary>
		public RPG.RpgObject SelectedSwitch 
		{ 
			get { return Data[dataObjectList.SelectedIndex + 1]; } 
		}

		private RPG.RpgObject _switch;

		/// <summary>
		/// Gets the data associated with the control
		/// </summary>
		public override List<dynamic> Data
		{
			get { return FormType == SwitchType.Switch ? Project.Switches : Project.Variables; }
		}

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public SwitchForm() : this(SwitchType.Switch) { }

		/// <summary>
		/// Construct the form, specifying the type
		/// </summary>
		/// <param name="switchType">Type of data to edit</param>
		public SwitchForm(SwitchType switchType) : base()
		{
			InitializeComponent();
			FormType = switchType;
			string text;
			if (switchType == SwitchType.Switch)
			{
				text = "Switches";
				this.Icon = System.Drawing.Icon.FromHandle(Properties.Resources.Switch.GetHicon());
			}
			else
			{
				text = "Variables";
				this.Icon = System.Drawing.Icon.FromHandle(Properties.Resources.Variable.GetHicon());
			}
			this.Text = dataObjectList.HeaderText = text;
			dataObjectList.PopulateList(Data);
			dataObjectList.SelectedIndex = 0;
		}

		#endregion

		#region Public Methods

		public override void NotifyRefresh(RefreshType type)
		{

		}

		/// <summary>
		/// Refreshes the current selected object
		/// </summary>
		public override void RefreshCurrentObject()
		{
			suppressEvents = true;
			textBoxName.Text = _switch.name;
			suppressEvents = false;
		}

		#endregion

		#region Private Methods

		private void dataObjectList_OnButtonMaxClick(object sender, EventArgs e)
		{
			for (int i = 1; i < Data.Count; i++)
				Data[i].id = i;
		}

		private void dataObjectList_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_switch = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				int index = dataObjectList.SelectedIndex;
				string text = textBoxName.Text;
				_switch.name = text;
				dataObjectList.Items[index] = _switch.ToString();
				if (FormType == SwitchType.Switch)
				{
					Project.Data.System.switches[index + 1] = text;
					Editor.DatabaseNotify(RefreshType.Switches);
				}
				else
				{
					Project.Data.System.variables[index + 1] = text;
					Editor.DatabaseNotify(RefreshType.Variables);
				}
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		#endregion
	}
}
