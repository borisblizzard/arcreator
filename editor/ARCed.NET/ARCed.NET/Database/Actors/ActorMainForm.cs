#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using RPG;

#endregion

namespace ARCed.Database.Actors
{
	public sealed partial class ActorMainForm : DatabaseWindow
	{
		#region Private Fields

		private ParameterMiniChart[] _paramCharts;
		private EquipSlot[] _equipSlots;
		private Actor _actor;

		#endregion

		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the data associated with this panel.
		/// </summary>
		public override List<dynamic> Data { get { return Project.Data.Actors; } }

		#endregion

		#region Construction

		public ActorMainForm()
		{
			this.InitializeComponent();
			this.InitializeParameters();
			this.InitializeEquipmentSlots();
			RefreshObjectList();
			this.RefreshClasses();
			this.dataObjectList.SelectedIndex = 0;
			this.RefreshImages();
		}

		#endregion

		#region Control Initialization

		private void InitializeEquipmentSlots()
		{
			this.panelEquipment.SuspendLayout();
			this._equipSlots = new EquipSlot[Project.Settings.EquipmentSettings.Count];
			int width = this.groupBoxEquipment.Width - 13;
			for (int i = 0; i < Project.Settings.EquipmentSettings.Count; i++)
			{
				var slot = new EquipSlot
				{
				    Parent = this.groupBoxEquipment,
				    Configuration = Project.Settings.EquipmentSettings[i],
				    Location = new Point(7, 19 + (i * 27))
				};
			    slot.Size = new Size(width, slot.Size.Height);
				slot.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Top;
				this._equipSlots[i] = slot;
				this.panelEquipment.Controls.Add(slot);
				slot.OnEquipmentChange += this.slot_OnEquipmentChange;
				slot.OnEquipFixChange += this.slot_OnEquipFixChange;
			}
			this.panelEquipment.ResumeLayout();
		}

		/// <summary>
		/// Initializes the tab pages and charts based of defined parameters
		/// </summary>
		private void InitializeParameters()
		{
			// TODO: Implement dynamic number of charts
			var parameterNames = Project.Settings.Parameters;
			var count = parameterNames.Count;
			this._paramCharts = new ParameterMiniChart[count];
			for (var i = 0; i < count; i++)
			{
				var chart = new ParameterMiniChart
				{
				    Dock = DockStyle.Fill,
				    ParameterLabel = parameterNames[i],
				    ParameterIndex = i
				};
			    this._paramCharts[i] = chart;
				this.tableLayoutPanel.Controls.Add(chart);
			}
		}

		#endregion

		#region Control Refreshing

		private void RefreshEquipmentSlots()
		{
			Class klass = Project.Data.Classes[this._actor.class_id];
			foreach (EquipSlot slot in this._equipSlots)
			{
			    slot.RefreshItems(slot.EquipKind < 0 ? klass.weapon_set : klass.armor_set);
			}
		}

		private void RefreshClasses()
		{
			this.comboClass.Items.Clear();
			ControlHelper.Populate(this.comboClass, Project.Data.Classes, false);
			if (this._actor != null)
			{
				if (this._actor.class_id > Project.Data.Classes.Count)
					this._actor.class_id = 1;
				this.comboClass.SelectedIndex = this._actor.class_id - 1;
			}
		}

		private void RefreshImages()
		{
			this.pictureCharacter.Image =
				Cache.CharacterStance(this._actor.character_name, 0, 1, this._actor.character_hue);
			this.pictureBattler.Image = Cache.Battler(this._actor.battler_name, this._actor.battler_hue);
		}

		private void RefreshGeneral()
		{
			SuppressEvents = true;
			this.textBoxName.Text = this._actor.name;
			this.numericLevelInit.Value = this._actor.initial_level;
			this.numericLevelFinal.Value = this._actor.final_level;
			this.comboClass.SelectedIndex = this._actor.class_id - 1;
			this.textBoxExpCurve.Text = String.Format("Basis: {0}, Inflation: {1}",
				this._actor.exp_basis, this._actor.exp_inflation);
			SuppressEvents = false;
		}

		private void RefreshEquipment()
		{
			// Edit to allow dynamic slots
			SuppressEvents = true;
			this._equipSlots[0].SetItemId(this._actor.weapon_id);
			this._equipSlots[1].SetItemId(this._actor.armor1_id);
			this._equipSlots[2].SetItemId(this._actor.armor2_id);
			this._equipSlots[3].SetItemId(this._actor.armor3_id);
			this._equipSlots[4].SetItemId(this._actor.armor4_id);
			this._equipSlots[0].Fixed = this._actor.weapon_fix;
			this._equipSlots[1].Fixed = this._actor.armor1_fix;
			this._equipSlots[2].Fixed = this._actor.armor2_fix;
			this._equipSlots[3].Fixed = this._actor.armor3_fix;
			this._equipSlots[4].Fixed = this._actor.armor4_fix;
			SuppressEvents = false;
		}

		#endregion

		/// <summary>
		/// Refreshes objects by type flag
		/// </summary>
		/// <param name="type">Flag for type of object to refresh</param>
		public override void NotifyRefresh(RefreshType type)
		{
			if (type.HasFlag(RefreshType.Classes))
			{

			}
			if (type.HasFlag(RefreshType.Parameters))
			{

			}
		}

        /// <summary>
        /// Refreshes the form to display data for the currently selected <see cref="RPG.Skill"/>.
        /// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			this.RefreshGeneral();
			this.RefreshEquipmentSlots();
			this.RefreshEquipment();
			this.RefreshImages();
			foreach (ParameterMiniChart chart in this._paramCharts)
				chart.ChangeActor(this._actor);
			SuppressEvents = false;
		}

		#region Events

		private void slot_OnEquipFixChange(object sender, EquipFixChangedEventArgs e)
		{
			if (!SuppressEvents)
			{
				if (!String.IsNullOrEmpty(e.PropertyName))
					typeof(Actor).GetProperty(e.PropertyName).SetValue(this._actor, e.Fixed, null);
			}
		}

		private void slot_OnEquipmentChange(object sender, EquipmentChangedEventArgs e)
		{
			if (!SuppressEvents)
			{
				if (!String.IsNullOrEmpty(e.PropertyName))
					typeof(Actor).GetProperty(e.PropertyName).SetValue(this._actor, e.EquipmentId, null);
			}
		}

		private void ListBoxActorsSelectedIndexChanged(object sender, EventArgs e)
		{
			int index = this.dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				this._actor = this.Data[index + 1];
				this.RefreshCurrentObject();
			}
		}

		private void ContextImagesSizeModeClicked(object sender, EventArgs e)
		{
		    var toolStripMenuItem = sender as ToolStripMenuItem;
		    if (toolStripMenuItem == null) return;
		    var num = Convert.ToInt32(toolStripMenuItem.Tag);
		    var mode = (PictureBoxSizeMode)num;
		    var pictureBox = this.contextMenuImages.SourceControl as PictureBox;
		    if (pictureBox != null)
		        pictureBox.SizeMode = mode;
		}

	    private void ComboClassSelectedIndexChanged(object sender, EventArgs e)
		{
	        if (SuppressEvents) return;
	        this._actor.class_id = this.comboClass.SelectedIndex + 1;
	        this.RefreshEquipmentSlots();
	        this.RefreshEquipment();
		}

		private void NumericLevelInitValueChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._actor.initial_level = (int)this.numericLevelInit.Value;
		}

		private void NumericLevelFinalValueChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
				this._actor.final_level = (int)this.numericLevelFinal.Value;
		}

		private void TextBoxNameTextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				this._actor.name = this.textBoxName.Text;
				int index = this.dataObjectList.SelectedIndex;
				this.dataObjectList.Items[index] = this._actor.ToString();
				this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
			}
		}

		private void ContextMenuImagesOpening(object sender, CancelEventArgs e)
		{
		    var pictureBox = this.contextMenuImages.SourceControl as PictureBox;
		    if (pictureBox == null) return;
		    PictureBoxSizeMode mode = pictureBox.SizeMode;
		    this.contextImageNormal.Checked = mode == PictureBoxSizeMode.Normal;
		    this.contextImageCenter.Checked = mode == PictureBoxSizeMode.CenterImage;
		    this.contextImageStretch.Checked = mode == PictureBoxSizeMode.StretchImage;
		    this.contextImageZoom.Checked = mode == PictureBoxSizeMode.Zoom;
		}

	    private void ButtonExperienceClick(object sender, EventArgs e)
		{
			var form = new ExperienceCurveForm();
			form.ChangeActor(this._actor);
			form.Show(Editor.MainDock);
		}

		private void PictureCharacterDoubleClick(object sender, EventArgs e)
		{
			using (var dialog = new ImageSelectionForm(@"Characters", this._actor.character_name))
			{
				dialog.Hue = this._actor.character_hue;
				dialog.OptionsEnabled = false;
			    if (dialog.ShowDialog(this) != DialogResult.OK) return;
			    this._actor.character_name = dialog.ImageName;
			    this._actor.character_hue = dialog.Hue;
			    this.pictureCharacter.Image =
			        Cache.CharacterStance(this._actor.character_name, 0, 1, this._actor.character_hue);
			}
		}

		private void PictureBattlerDoubleClick(object sender, EventArgs e)
		{
			using (var dialog =
				new ImageSelectionForm(@"Battlers", this._actor.battler_name))
			{
				dialog.Hue = this._actor.battler_hue;
				dialog.OptionsEnabled = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					this._actor.battler_name = dialog.ImageName;
					this._actor.battler_hue = dialog.Hue;
					this.pictureBattler.Image =
						Cache.Battler(this._actor.battler_name, this._actor.battler_hue);
				}
			}
		}

		#endregion
	}
}
