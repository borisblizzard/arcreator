#region Using Directives

using System;
using System.Collections.Generic;
using System.Windows.Forms;
using ARCed.Dialogs;
using RPG;
using Color = System.Drawing.Color;

#endregion

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
		public Animation.Timing Timing 
		{
			get { return this.GetTiming(); }
			set { this.SetTiming(value); }
		}

		#endregion

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public AnimationTimingDialog()
		{
			this.InitializeComponent();
			this.numericUpDownStrength.DataBindings.Add("Value", this.trackBarStrength, "Value", false,
				DataSourceUpdateMode.OnPropertyChanged);
		}

		#endregion

		#region Private Methods

		private Animation.Timing GetTiming()
		{
			var timing = new Animation.Timing
			{
			    frame = (int)this.numericUpDownFrame.Value,
			    condition = this.comboBoxCondition.SelectedIndex,
			    flash_duration = (int)this.numericUpDownDuration.Value,
			    flash_color = this.panelColor.BackColor
			};
		    timing.flash_color.alpha = (float)this.numericUpDownStrength.Value;
			var btns = new List<RadioButton> { this.radioNone, this.radioTarget, this.radioScreen, this.radioHide };
			timing.flash_scope = btns.FindIndex(btn => btn.Checked);
			timing.se = this.textBoxSE.Tag == null ? new AudioFile() : (AudioFile)this.textBoxSE.Tag;
			return timing;
		}

		private void SetTiming(Animation.Timing timing)
		{
			this.numericUpDownFrame.Value = timing.frame.Clamp(1, 999);
			this.numericUpDownDuration.Value = timing.flash_duration;
			this.trackBarStrength.Value = (int)timing.flash_color.alpha;
			this.panelColor.BackColor = Color.FromArgb(255, (int)timing.flash_color.red, 
				(int)timing.flash_color.green, (int)timing.flash_color.blue); 
			this.comboBoxCondition.SelectedIndex = timing.condition;
			this.textBoxSE.Tag = timing.se;
			this.textBoxSE.Text = timing.se.ToString();
			switch (timing.flash_scope)
			{
				case 1: this.radioTarget.Checked = true; break;
				case 2: this.radioScreen.Checked = true; break;
				case 3: this.radioHide.Checked = true; break;
				default: this.radioNone.Checked = true; break;
			}
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}

		private void panelColor_DoubleClick(object sender, EventArgs e)
		{
			using (var dialog = new ColorChooserForm())
			{
				dialog.AlphaEnabled = false;
				Color c = this.panelColor.BackColor;
				dialog.Color = Color.FromArgb(255, c.R, c.G, c.B);
				if (dialog.ShowDialog() == DialogResult.OK)
					this.panelColor.BackColor = dialog.Color;
			}
		}

		#endregion
	}
}
