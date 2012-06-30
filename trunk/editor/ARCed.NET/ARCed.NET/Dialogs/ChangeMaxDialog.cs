using System;
using System.Windows.Forms;

namespace ARCed.Dialogs
{
	public partial class ChangeMaxDialog : Form
	{
		/// <summary>
		/// Gets the maximum value defined by the user on the form
		/// </summary>
		public int MaxValue { get { return (int)numericMax.Value; } }

		/// <summary>
		/// Default contstructor
		/// </summary>
		/// <param name="current">Current value</param>
		/// <param name="min">Minimum allowed value</param>
		/// <param name="max">Maximim allowed value</param>
		public ChangeMaxDialog(int current, int min, int max)
		{
			InitializeComponent();
			numericMax.Maximum = max;
			numericMax.Minimum = min;
			numericMax.Value = current.Clamp(min, max);
			labelCurrent.Text = String.Format("Current: {0}", current);
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}
	}
}
