using System;
using System.Drawing;
using System.Windows.Forms;

namespace ARCed.Dialogs
{
	/// <summary>
	/// Simple dialog for choosing a font resource
	/// </summary>
	public partial class FontSelectionDialog : Form
	{

		#region Public Properties

		/// <summary>
		/// Gets or sets the user-defined font of the control
		/// </summary>
		public Font UserFont 
		{ 
			get { return fontSelector.UserFont; }
			set { fontSelector.UserFont = value; }
		}

		#endregion

		#region Construct/Dispose

		/// <summary>
		/// Default constructor
		/// </summary>
		public FontSelectionDialog()
		{
			InitializeComponent();
		}

		#endregion

		#region Private Methods

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}

		#endregion
	}
}
