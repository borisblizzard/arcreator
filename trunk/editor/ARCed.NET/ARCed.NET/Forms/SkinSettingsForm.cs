using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;
using ARCed.UI;
using ARCed.Helpers;
using ARCed.Dialogs;

namespace ARCed.Forms
{
	public partial class SkinSettingsForm : DockContent
	{
		private static string[] AutoHideGradients = { "Dock Strip", "Tab" };
		private static string[] DockPaneStripGradients = 
		{
			"Document Dock Strip",
			"Document Active Tab",
			"Document Inactive Tab",
			"Tool Window Dock Strip",
			"Tool Window Active Tab",
			"Tool Window Inactive Tab",
			"Tool Window Active Caption",
			"Tool Window Inactive Caption"
		};

		private DockPanelSkin Skin
		{
			get { return Editor.Settings.WindowSkin; }
			set { Editor.Settings.WindowSkin = value; }
		}

		private DockPanelGradient CurrentGradient
		{
			get
			{
				int index = listBoxGradients.SelectedIndex;
				if (radioDockPanel.Checked)
				{
					switch (index)
					{
						case 0: return Skin.DockPaneStripSkin.DocumentGradient.DockStripGradient; 
						case 1: return Skin.DockPaneStripSkin.DocumentGradient.ActiveTabGradient; 
						case 2: return Skin.DockPaneStripSkin.DocumentGradient.InactiveTabGradient; 
						case 3: return Skin.DockPaneStripSkin.ToolWindowGradient.DockStripGradient;
						case 4: return Skin.DockPaneStripSkin.ToolWindowGradient.ActiveTabGradient;
						case 5: return Skin.DockPaneStripSkin.ToolWindowGradient.InactiveTabGradient;
						case 6: return Skin.DockPaneStripSkin.ToolWindowGradient.ActiveCaptionGradient; 
						case 7: return Skin.DockPaneStripSkin.ToolWindowGradient.InactiveCaptionGradient; 
					}
				}
				else
				{
					return index == 0 ? Skin.AutoHideStripSkin.DockStripGradient :
						Skin.AutoHideStripSkin.TabGradient;
				}
				return null;
			}
		}

		private ARCed.Data.SerializableFont CurrentFont
		{
			get
			{
				return radioDockPanel.Checked ? Skin.DockPaneStripSkin.TextFont :
					Skin.AutoHideStripSkin.TextFont;
			}
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public SkinSettingsForm()
		{
			InitializeComponent();
			radioPanel_CheckedChanged(null, null);
			listBoxGradients.SelectedIndex = 0;
		}

		private void listBoxGradients_SelectedIndexChanged(object sender, EventArgs e)
		{
			RefreshDisplay();
		}

		private void RefreshDisplay()
		{
			DockPanelGradient gradient = CurrentGradient;
			bool enable = gradient != null;
			bool docGradient = listBoxGradients.SelectedIndex > 3;
			if (enable)
			{
				panelStartColor.BackColor = gradient.StartColor;
				panelEndColor.BackColor = gradient.EndColor;
				comboBoxGradient.SelectedIndex = (int)gradient.LinearGradientMode;
				if (docGradient)
					panelTextColor.BackColor = (gradient as TabGradient).TextColor;
			}
			panelStartColor.Enabled = enable;
			panelEndColor.Enabled = enable;
			panelTextColor.Enabled = enable && docGradient;
			labelTextColor.ForeColor = enable && docGradient ?
				SystemColors.ControlText : SystemColors.GrayText;
		}

		private void radioPanel_CheckedChanged(object sender, EventArgs e)
		{
			labelFont.Text = CurrentFont.SerializeFontAttribute;
			listBoxGradients.Items.Clear();
			listBoxGradients.Items.AddRange(radioDockPanel.Checked ?
			DockPaneStripGradients : AutoHideGradients);
			listBoxGradients.SelectedIndex = 0;
		}

		private void panelColor_DoubleClick(object sender, EventArgs e)
		{
			string tag = (sender as Control).Tag.ToString();
			Color color;
			if (tag == "START") color = panelStartColor.BackColor;
			else if (tag == "END") color = panelEndColor.BackColor;
			else color = panelTextColor.BackColor;
			using (ColorChooserForm dialog = new ColorChooserForm())
			{
				dialog.Color = color;
				if (dialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
				{
					if (tag == "START") CurrentGradient.StartColor = dialog.Color;
					else if (tag == "END") CurrentGradient.EndColor = dialog.Color;
					else color = (CurrentGradient as TabGradient).TextColor = dialog.Color;
					RefreshDisplay();
				}
			}
		}

		private void comboBoxGradient_SelectedIndexChanged(object sender, EventArgs e)
		{
			CurrentGradient.LinearGradientMode = 
				(LinearGradientMode)comboBoxGradient.SelectedIndex;
		}

		private void buttonFont_Click(object sender, EventArgs e)
		{
			using (FontSelectionDialog dialog = new FontSelectionDialog())
			{
				dialog.UserFont = CurrentFont;
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					if (radioDockPanel.Checked)
						Skin.DockPaneStripSkin.TextFont = dialog.UserFont;
					else
						Skin.AutoHideStripSkin.TextFont = dialog.UserFont;
				}
			}
		}

		private void buttonDefault_Click(object sender, EventArgs e)
		{
			Skin = new DockPanelSkin();
			RefreshDisplay();
			Editor.MainDock.Refresh();
		}

		private void buttonApply_Click(object sender, EventArgs e)
		{
			Editor.MainDock.Skin = Util.CloneObject<DockPanelSkin>(Editor.Settings.WindowSkin);
		}

		private void groupBoxSkinType_CollapseBoxClickedEvent(object sender)
		{
			int y = groupBoxSkinType.FullHeight - groupBoxSkinType.CollapsedHeight;
			if (groupBoxSkinType.IsCollapsed)
				y *= -1;
			Control[] ctrls = { groupBoxFontSettings, groupBoxGradientSettings, buttonApply, buttonDefault };
			foreach (Control ctrl in ctrls)
				ctrl.Location = new Point(ctrl.Location.X, ctrl.Location.Y + y);
		}

		private void groupBoxFontSettings_CollapseBoxClickedEvent(object sender)
		{
			int y = groupBoxFontSettings.FullHeight - groupBoxFontSettings.CollapsedHeight;
			if (groupBoxFontSettings.IsCollapsed)
				y *= -1;
			Control[] ctrls = { groupBoxGradientSettings, buttonApply, buttonDefault };
			foreach (Control ctrl in ctrls)
				ctrl.Location = new Point(ctrl.Location.X, ctrl.Location.Y + y);
		}

		private void groupBoxGradientSettings_CollapseBoxClickedEvent(object sender)
		{
			int y = groupBoxGradientSettings.FullHeight - groupBoxGradientSettings.CollapsedHeight;
			if (groupBoxGradientSettings.IsCollapsed)
				y *= -1;
			Control[] ctrls = { buttonApply, buttonDefault };
			foreach (Control ctrl in ctrls)
				ctrl.Location = new Point(ctrl.Location.X, ctrl.Location.Y + y);
		}
	}
}
