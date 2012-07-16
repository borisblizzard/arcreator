#region Using Directives

using System;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.Dialogs
{
	/// <summary>
	/// Simple dialog for getting a user-defined <see cref="Font"/>.
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

		private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}

		#endregion
	}
}
