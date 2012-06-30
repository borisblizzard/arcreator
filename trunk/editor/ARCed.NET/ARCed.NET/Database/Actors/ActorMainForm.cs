using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using ARCed.UI;

namespace ARCed.Database.Actors
{
	public partial class ActorMainForm : DatabaseWindow
	{
		#region Private Fields

		private ParameterMiniChart[] _paramCharts;
		private EquipSlot[] _equipSlots;
		private RPG.Actor _actor;

		#endregion

		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return dataObjectList; } }

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the data associated with this panel.
		/// </summary>
		public override List<dynamic> Data { get { return Project.Data.Actors; } }

		#endregion

		#region Construction

		public ActorMainForm() : base()
		{
			InitializeComponent();
			InitializeParameters();
			InitializeEquipmentSlots();
			RefreshObjectList();
			RefreshClasses();
			dataObjectList.SelectedIndex = 0;
			RefreshImages();
		}

		#endregion

		#region Control Initialization

		private void InitializeEquipmentSlots()
		{
			panelEquipment.SuspendLayout();
			_equipSlots = new EquipSlot[Project.Settings.EquipmentSettings.Count];
			int width = groupBoxEquipment.Width - 13;
			for (int i = 0; i < Project.Settings.EquipmentSettings.Count; i++)
			{
				EquipSlot slot = new EquipSlot() { Parent = groupBoxEquipment };
				slot.Configuration = Project.Settings.EquipmentSettings[i];
				slot.Location = new Point(7, 19 + (i * 27));
				slot.Size = new Size(width, slot.Size.Height);
				slot.Anchor = AnchorStyles.Left | AnchorStyles.Right | AnchorStyles.Top;
				_equipSlots[i] = slot;
				panelEquipment.Controls.Add(slot);
				slot.OnEquipmentChange += new EquipSlot.EquipmentChangedEventHandler(slot_OnEquipmentChange);
				slot.OnEquipFixChange += new EquipSlot.EquipFixChangedEventHandler(slot_OnEquipFixChange);
			}
			panelEquipment.ResumeLayout();
		}

		/// <summary>
		/// Initializes the tab pages and charts based of defined parameters
		/// </summary>
		private void InitializeParameters()
		{
			// TODO: Implement dynamic number of charts
			List<string> parameterNames = Project.Settings.Parameters;
			int count = parameterNames.Count;
			_paramCharts = new ParameterMiniChart[count];
			for (int i = 0; i < count; i++)
			{
				ParameterMiniChart chart = new ParameterMiniChart();
				chart.Dock = DockStyle.Fill;
				chart.ParameterLabel = parameterNames[i];
				chart.ParameterIndex = i;
				_paramCharts[i] = chart;
				tableLayoutPanel.Controls.Add(chart);
			}
		}

		#endregion

		#region Control Refreshing

		private void RefreshEquipmentSlots()
		{
			RPG.Class klass = Project.Data.Classes[_actor.class_id];
			foreach (EquipSlot slot in _equipSlots)
			{
				if (slot.EquipKind < 0)
					slot.RefreshItems(klass.weapon_set);
				else
					slot.RefreshItems(klass.armor_set);
			}
		}

		private void RefreshClasses()
		{
			comboClass.Items.Clear();
			DatabaseHelper.Populate(comboClass, Project.Data.Classes, false);
			if (_actor != null)
			{
				if (_actor.class_id > Project.Data.Classes.Count)
					_actor.class_id = 1;
				comboClass.SelectedIndex = _actor.class_id - 1;
			}
		}

		private void RefreshChart(int index = -1)
		{
			if (index == -1)
			{
				foreach (ParameterMiniChart chart in _paramCharts)
					chart.RefreshChart();
			}
			else
				_paramCharts[index].RefreshChart();
		}

		private void RefreshImages()
		{
			pictureCharacter.Image =
				Cache.CharacterStance(_actor.character_name, 0, 1, _actor.character_hue);
			pictureBattler.Image = Cache.Battler(_actor.battler_name, _actor.battler_hue);
		}

		private void RefreshGeneral()
		{
			suppressEvents = true;
			textBoxName.Text = _actor.name;
			numericLevelInit.Value = _actor.initial_level;
			numericLevelFinal.Value = _actor.final_level;
			comboClass.SelectedIndex = _actor.class_id - 1;
			textBoxExpCurve.Text = String.Format("Basis: {0}, Inflation: {1}",
				_actor.exp_basis, _actor.exp_inflation);
			suppressEvents = false;
		}

		private void RefreshEquipment()
		{
			// Edit to allow dynamic slots
			suppressEvents = true;
			_equipSlots[0].SetItemId(_actor.weapon_id);
			_equipSlots[1].SetItemId(_actor.armor1_id);
			_equipSlots[2].SetItemId(_actor.armor2_id);
			_equipSlots[3].SetItemId(_actor.armor3_id);
			_equipSlots[4].SetItemId(_actor.armor4_id);
			_equipSlots[0].Fixed = _actor.weapon_fix;
			_equipSlots[1].Fixed = _actor.armor1_fix;
			_equipSlots[2].Fixed = _actor.armor2_fix;
			_equipSlots[3].Fixed = _actor.armor3_fix;
			_equipSlots[4].Fixed = _actor.armor4_fix;
			suppressEvents = false;
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

		public override void RefreshCurrentObject()
		{
			suppressEvents = true;
			RefreshGeneral();
			RefreshEquipmentSlots();
			RefreshEquipment();
			RefreshImages();
			foreach (ParameterMiniChart chart in _paramCharts)
				chart.ChangeActor(_actor);
			suppressEvents = false;
		}

		#region Events

		private void slot_OnEquipFixChange(object sender, EquipFixChangedEventArgs e)
		{
			if (!suppressEvents)
			{
				if (!String.IsNullOrEmpty(e.PropertyName))
					typeof(RPG.Actor).GetProperty(e.PropertyName).SetValue(_actor, e.Fixed, null);
			}
		}

		private void slot_OnEquipmentChange(object sender, EquipmentChangedEventArgs e)
		{
			if (!suppressEvents)
			{
				if (!String.IsNullOrEmpty(e.PropertyName))
					typeof(RPG.Actor).GetProperty(e.PropertyName).SetValue(_actor, e.EquipmentId, null);
			}
		}

		private void listBoxActors_SelectedIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_actor = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void contextImagesSizeMode_Clicked(object sender, EventArgs e)
		{
			int num = Convert.ToInt32((sender as ToolStripMenuItem).Tag);
			PictureBoxSizeMode mode = (PictureBoxSizeMode)num;
			(contextMenuImages.SourceControl as PictureBox).SizeMode = mode;
		}

		private void comboClass_SelectedIndexChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				_actor.class_id = comboClass.SelectedIndex + 1;
				RefreshEquipmentSlots();
				RefreshEquipment();
			}
		}

		private void numericLevelInit_ValueChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_actor.initial_level = (int)numericLevelInit.Value;
		}

		private void numericLevelFinal_ValueChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
				_actor.final_level = (int)numericLevelFinal.Value;
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				_actor.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _actor.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void contextMenuImages_Opening(object sender, CancelEventArgs e)
		{
			PictureBoxSizeMode mode =
				(contextMenuImages.SourceControl as PictureBox).SizeMode;
			contextImageNormal.Checked = mode == PictureBoxSizeMode.Normal;
			contextImageCenter.Checked = mode == PictureBoxSizeMode.CenterImage;
			contextImageStretch.Checked = mode == PictureBoxSizeMode.StretchImage;
			contextImageZoom.Checked = mode == PictureBoxSizeMode.Zoom;
		}

		private void buttonExperience_Click(object sender, EventArgs e)
		{
			ExperienceCurveForm form = new ExperienceCurveForm();
			form.ChangeActor(_actor);
			form.Show(Editor.MainDock);
		}

		private void pictureCharacter_DoubleClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog = 
				new ImageSelectionForm(@"Graphics\Characters", _actor.character_name, _actor.character_hue))
			{
				dialog.TileSelection = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_actor.character_name = dialog.ImageName;
					_actor.character_hue = dialog.ImageHue;
					pictureCharacter.Image =
						Cache.CharacterStance(_actor.character_name, 0, 1, _actor.character_hue);
				}
			}
		}

		private void pictureBattler_DoubleClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog =
				new ImageSelectionForm(@"Graphics\Battlers", _actor.battler_name, _actor.battler_hue))
			{
				dialog.TileSelection = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_actor.battler_name = dialog.ImageName;
					_actor.battler_hue = dialog.ImageHue;
					pictureBattler.Image =
						Cache.Battler(_actor.battler_name, _actor.battler_hue);
				}
			}
		}

		#endregion
	}
}
