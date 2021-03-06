﻿#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using ARCed.Controls;
using ARCed.Properties;
using RPG;

#endregion

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
	public sealed partial class SwitchForm : DatabaseWindow
	{
		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

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
			get { return this.dataObjectList.SelectedIndex + 1; }
			set { this.dataObjectList.SelectedIndex = value - 1; }
		}
		/// <summary>
		/// Gets the selected switch
		/// </summary>
		public RpgObject SelectedSwitch
		{
			get { return this.Data[this.dataObjectList.SelectedIndex + 1]; }
		}

		private RpgObject _switch;

		/// <summary>
		/// Gets the data associated with the control
		/// </summary>
		public override List<dynamic> Data
		{
			get { return this.FormType == SwitchType.Switch ? Project.Switches : Project.Variables; }
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
		public SwitchForm(SwitchType switchType)
		{
			this.InitializeComponent();
			this.FormType = switchType;
			string text;
			if (switchType == SwitchType.Switch)
			{
				text = "Switches";
				Icon = Icon.FromHandle(Resources.Switch.GetHicon());
			}
			else
			{
				text = "Variables";
				Icon = Icon.FromHandle(Resources.Variable.GetHicon());
			}
			Text = this.dataObjectList.HeaderText = text;
			this.dataObjectList.PopulateList(this.Data);
			this.dataObjectList.SelectedIndex = 0;
		}

		#endregion

		#region Public Methods

		public override void NotifyRefresh(RefreshType type)
		{

		}

		/// <summary>
		/// Refreshes the form to display data for the currently selected <see cref="RPG.RpgObject"/>.
		/// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			this.textBoxName.Text = this._switch.name;
			SuppressEvents = false;
		}

		#endregion

		#region Private Methods

		private void dataObjectList_OnButtonMaxClick(object sender, EventArgs e)
		{
			for (int i = 1; i < this.Data.Count; i++)
				this.Data[i].id = i;
		}

		private void dataObjectList_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = this.dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				this._switch = this.Data[index + 1];
				this.RefreshCurrentObject();
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				int index = this.dataObjectList.SelectedIndex;
				string text = this.textBoxName.Text;
				this._switch.name = text;
				this.dataObjectList.Items[index] = this._switch.ToString();
				if (this.FormType == SwitchType.Switch)
				{
					Project.Data.System.switches[index + 1] = text;
					Editor.DatabaseNotify(RefreshType.Switches);
				}
				else
				{
					Project.Data.System.variables[index + 1] = text;
					Editor.DatabaseNotify(RefreshType.Variables);
				}
				this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
			}
		}

		#endregion
	}
}
