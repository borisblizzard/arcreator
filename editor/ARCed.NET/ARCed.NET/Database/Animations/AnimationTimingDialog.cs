using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Dialogs;

namespace ARCed.Database.Animations
{
	/// <summary>
	/// Dialog for creating/editing RPG.Animation.Timing objects.
	/// </summary>
	public partial class AnimationTimingDialog : Form
	{
		#region Public Properties

		/// <summary>
		/// Gets or sets the RPG.Animation.Timing object associated with the dialog.
		/// </summary>
		public RPG.Animation.Timing Timing 
		{
			get { return GetTiming(); }
			set { SetTiming(value); }
		}

		#endregion

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public AnimationTimingDialog()
		{
			InitializeComponent();
			numericUpDownStrength.DataBindings.Add("Value", trackBarStrength, "Value", false,
				DataSourceUpdateMode.OnPropertyChanged | DataSourceUpdateMode.OnValidation);
		}

		#endregion

		#region Private Methods

		private RPG.Animation.Timing GetTiming()
		{
			RPG.Animation.Timing timing = new RPG.Animation.Timing();
			timing.frame = (int)numericUpDownFrame.Value;
			timing.condition = comboBoxCondition.SelectedIndex;
			timing.flash_duration = (int)numericUpDownDuration.Value;
            timing.flash_color = panelColor.BackColor;
			timing.flash_color.alpha = (float)numericUpDownStrength.Value;
			List<RadioButton> btns = new List<RadioButton> { radioNone, radioTarget, radioScreen, radioHide };
			timing.flash_scope = btns.FindIndex(delegate(RadioButton btn) { return btn.Checked; });
			timing.se = textBoxSE.Tag == null ? new RPG.AudioFile() : (RPG.AudioFile)textBoxSE.Tag;
			return timing;
		}

		private void SetTiming(RPG.Animation.Timing timing)
		{
			numericUpDownFrame.Value = timing.frame.Clamp(1, 999);
			numericUpDownDuration.Value = timing.flash_duration;
			trackBarStrength.Value = (int)timing.flash_color.alpha;
			panelColor.BackColor = Color.FromArgb(255, (int)timing.flash_color.red, 
				(int)timing.flash_color.green, (int)timing.flash_color.blue); 
			comboBoxCondition.SelectedIndex = timing.condition;
			textBoxSE.Tag = timing.se;
			textBoxSE.Text = timing.se.ToString();
			switch (timing.flash_scope)
			{
				case 1: radioTarget.Checked = true; break;
				case 2: radioScreen.Checked = true; break;
				case 3: radioHide.Checked = true; break;
				default: radioNone.Checked = true; break;
			}
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}

		private void panelColor_DoubleClick(object sender, EventArgs e)
		{
			using (ColorChooserForm dialog = new ColorChooserForm())
			{
				dialog.AlphaEnabled = false;
				Color c = panelColor.BackColor;
				dialog.Color = Color.FromArgb(255, c.R, c.G, c.B);
				if (dialog.ShowDialog() == DialogResult.OK)
					panelColor.BackColor = dialog.Color;
			}
		}

		#endregion
	}
}
