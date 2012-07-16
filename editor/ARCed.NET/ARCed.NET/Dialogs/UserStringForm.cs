#region Using Directives

using System;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

namespace ARCed.Dialogs
{
    /// <summary>
    /// Dialog for getting a user-defined <see langword="string"/>.
    /// </summary>
	public partial class UserStringForm : Form
    {
        #region Private Fields

        private readonly bool _validate;

        #endregion

        #region Public Properties

        /// <summary>
        /// Gets or sets the text in the <see cref="TextBox"/> field.
		/// </summary>
		public string UserString
		{
			get { return textBoxString.Text; }
			set { textBoxString.Text = value; }
		}

		/// <summary>
		/// Gets or sets the label for the <see cref="TextBox"/> control on the form.
		/// </summary>
		public string Label
		{
			get { return labelString.Text; }
			set { labelString.Text = value; }
		}

        /// <summary>
        /// Gets or sets the text of the control.
        /// </summary>
        public override sealed string Text
        {
            get { return base.Text; }
            set { base.Text = value; }
        }

        #endregion

        #region Constructor

        /// <summary>
		/// Creates a new instance of the form
		/// </summary>
		/// <param name="title">The title of the form in the header</param>
        /// <param name="defaultText">Default text for the <see cref="TextBox"/> field</param>
        /// <param name="label">The text for the <see cref="TextBox"/> label</param>
		/// <param name="validate">Flag to validate text for filenames</param>
		public UserStringForm(string title, string defaultText, string label, bool validate = false)
		{
			InitializeComponent();
			Text = title;
			textBoxString.Text = defaultText;
			labelString.Text = label;
			_validate = validate;
		}

        #endregion

        #region Private Fields

        private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}

		private void TextBoxStringTextChanged(object sender, EventArgs e)
		{
			if (_validate)
				Util.ValidateTextBox(textBoxString);
			buttonOK.Enabled = textBoxString.Text.Trim() != "";
        }

        #endregion
    }
}
