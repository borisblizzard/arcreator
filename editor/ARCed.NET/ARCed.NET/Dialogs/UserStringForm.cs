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
			get { return this.textBoxString.Text; }
			set { this.textBoxString.Text = value; }
		}

		/// <summary>
		/// Gets or sets the label for the <see cref="TextBox"/> control on the form.
		/// </summary>
		public string Label
		{
			get { return this.labelString.Text; }
			set { this.labelString.Text = value; }
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
			this.InitializeComponent();
			this.Text = title;
			this.textBoxString.Text = defaultText;
			this.labelString.Text = label;
			this._validate = validate;
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
			if (this._validate)
				Util.ValidateTextBox(this.textBoxString);
			this.buttonOK.Enabled = this.textBoxString.Text.Trim() != "";
        }

        #endregion
    }
}
