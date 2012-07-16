#region Using Directives

using System;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

namespace ARCed.Dialogs
{
	public partial class UserStringForm : Form
	{
		/// <summary>
		/// Gets or sets the text in the textbox field
		/// </summary>
		public string UserString
		{
			get { return textBoxString.Text; }
			set { textBoxString.Text = value; }
		}

		/// <summary>
		/// Gets or sets the label for the textbox
		/// </summary>
		public string Label
		{
			get { return labelString.Text; }
			set { labelString.Text = value; }
		}

		private readonly bool _validate;

		/// <summary>
		/// Creates a new instance of the form
		/// </summary>
		/// <param name="title">The title of the form in the header</param>
		/// <param name="defaultText">Default text for the textbox field</param>
		/// <param name="label">The text for the textbox label</param>
		/// <param name="validate">Flag to validate text for filenames</param>
		public UserStringForm(string title, string defaultText, string label, bool validate = false)
		{
			InitializeComponent();
			this.Text = title;
			textBoxString.Text = defaultText;
			labelString.Text = label;
			_validate = validate;
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}

		private void textBoxString_TextChanged(object sender, EventArgs e)
		{
			if (_validate)
				Util.ValidateTextBox(textBoxString);
			buttonOK.Enabled = textBoxString.Text.Trim() != "";
		}
	}
}
