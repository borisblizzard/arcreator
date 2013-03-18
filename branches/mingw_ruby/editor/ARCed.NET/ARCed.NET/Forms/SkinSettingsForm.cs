#region Using Directives

using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Windows.Forms;
using ARCed.Core;
using ARCed.Dialogs;
using ARCed.Helpers;
using ARCed.UI;

#endregion

namespace ARCed.Forms
{
	public partial class SkinSettingsForm : DockContent
	{
		private static readonly string[] AutoHideGradients = { "Dock Strip", "Tab" };
		private static readonly string[] DockPaneStripGradients = 
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

		private static DockPanelSkin Skin
		{
			get { return Editor.Settings.WindowSkin; }
			set { Editor.Settings.WindowSkin = value; }
		}

		private DockPanelGradient CurrentGradient
		{
			get
			{
				int index = this.listBoxGradients.SelectedIndex;
				if (this.radioDockPanel.Checked)
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

		private SerializableFont CurrentFont
		{
			get
			{
				return this.radioDockPanel.Checked ? Skin.DockPaneStripSkin.TextFont :
					Skin.AutoHideStripSkin.TextFont;
			}
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public SkinSettingsForm()
		{
			this.InitializeComponent();
			this.radioPanel_CheckedChanged(null, null);
			this.listBoxGradients.SelectedIndex = 0;
		}

		private void listBoxGradients_SelectedIndexChanged(object sender, EventArgs e)
		{
			this.RefreshDisplay();
		}

		private void RefreshDisplay()
		{
			DockPanelGradient gradient = this.CurrentGradient;
			bool enable = gradient != null;
			bool docGradient = this.listBoxGradients.SelectedIndex > 3;
			if (enable)
			{
				this.panelStartColor.BackColor = gradient.StartColor;
				this.panelEndColor.BackColor = gradient.EndColor;
				this.comboBoxGradient.SelectedIndex = (int)gradient.LinearGradientMode;
				if (docGradient)
					this.panelTextColor.BackColor = (gradient as TabGradient).TextColor;
			}
			this.panelStartColor.Enabled = enable;
			this.panelEndColor.Enabled = enable;
			this.panelTextColor.Enabled = enable && docGradient;
			this.labelTextColor.ForeColor = enable && docGradient ?
				SystemColors.ControlText : SystemColors.GrayText;
		}

		private void radioPanel_CheckedChanged(object sender, EventArgs e)
		{
			this.labelFont.Text = this.CurrentFont.SerializeFontAttribute;
			this.listBoxGradients.Items.Clear();
			this.listBoxGradients.Items.AddRange(this.radioDockPanel.Checked ?
			DockPaneStripGradients : AutoHideGradients);
			this.listBoxGradients.SelectedIndex = 0;
		}

		private void panelColor_DoubleClick(object sender, EventArgs e)
		{
			string tag = (sender as Control).Tag.ToString();
			Color color;
			switch (tag)
			{
			    case "START":
			        color = this.panelStartColor.BackColor;
			        break;
			    case "END":
			        color = this.panelEndColor.BackColor;
			        break;
			    default:
			        color = this.panelTextColor.BackColor;
			        break;
			}
			using (var dialog = new ColorChooserForm())
			{
				dialog.Color = color;
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					if (tag == "START") this.CurrentGradient.StartColor = dialog.Color;
					else if (tag == "END") this.CurrentGradient.EndColor = dialog.Color;
					this.RefreshDisplay();
				}
			}
		}

		private void comboBoxGradient_SelectedIndexChanged(object sender, EventArgs e)
		{
			this.CurrentGradient.LinearGradientMode = 
				(LinearGradientMode)this.comboBoxGradient.SelectedIndex;
		}

		private void buttonFont_Click(object sender, EventArgs e)
		{
			using (var dialog = new FontSelectionDialog())
			{
				dialog.UserFont = this.CurrentFont;
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					if (this.radioDockPanel.Checked)
						Skin.DockPaneStripSkin.TextFont = dialog.UserFont;
					else
						Skin.AutoHideStripSkin.TextFont = dialog.UserFont;
				}
			}
		}

		private void buttonDefault_Click(object sender, EventArgs e)
		{
			Skin = new DockPanelSkin();
			this.RefreshDisplay();
			Editor.MainDock.Refresh();
		}

		private void buttonApply_Click(object sender, EventArgs e)
		{
			Editor.MainDock.Skin = Util.CloneObject(Editor.Settings.WindowSkin);
		}

		private void groupBoxSkinType_CollapseBoxClickedEvent(object sender)
		{
			int y = this.groupBoxSkinType.FullHeight - this.groupBoxSkinType.CollapsedHeight;
			if (this.groupBoxSkinType.IsCollapsed)
				y *= -1;
			Control[] ctrls = { this.groupBoxFontSettings, this.groupBoxGradientSettings, this.buttonApply, this.buttonDefault };
			foreach (Control ctrl in ctrls)
				ctrl.Location = new Point(ctrl.Location.X, ctrl.Location.Y + y);
		}

		private void groupBoxFontSettings_CollapseBoxClickedEvent(object sender)
		{
			int y = this.groupBoxFontSettings.FullHeight - this.groupBoxFontSettings.CollapsedHeight;
			if (this.groupBoxFontSettings.IsCollapsed)
				y *= -1;
			Control[] ctrls = { this.groupBoxGradientSettings, this.buttonApply, this.buttonDefault };
			foreach (Control ctrl in ctrls)
				ctrl.Location = new Point(ctrl.Location.X, ctrl.Location.Y + y);
		}

		private void groupBoxGradientSettings_CollapseBoxClickedEvent(object sender)
		{
			int y = this.groupBoxGradientSettings.FullHeight - this.groupBoxGradientSettings.CollapsedHeight;
			if (this.groupBoxGradientSettings.IsCollapsed)
				y *= -1;
			Control[] ctrls = { this.buttonApply, this.buttonDefault };
			foreach (Control ctrl in ctrls)
				ctrl.Location = new Point(ctrl.Location.X, ctrl.Location.Y + y);
		}
	}
}
