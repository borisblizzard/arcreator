#region Using Directives

using System;
using System.Windows.Forms;

#endregion

namespace ARCed.Dialogs
{
    /// <summary>
    /// Dialog for getting a new maximum capacity for data.
    /// </summary>
	public partial class ChangeMaxDialog : Form
    {
        #region Public Properties

        /// <summary>
		/// Gets the maximum value defined by the user on the form
		/// </summary>
		public int MaxValue { get { return (int)numericMax.Value; } }

        #endregion

        #region Constructor

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

        #endregion

        #region Private Methods

        private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
        }

        #endregion
    }
}
