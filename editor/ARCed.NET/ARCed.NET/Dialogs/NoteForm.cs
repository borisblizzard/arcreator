#region Using Directives

using System;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Properties;

#endregion

namespace ARCed.Dialogs
{
	/// <summary>
	/// Basic form to display a full editor for database notes.
	/// </summary>
	public partial class NoteForm : Form
	{
		#region Public Properties

		/// <summary>
		/// Gets or sets the text of the textbox control on the form
		/// </summary>
		public string NoteText { get { return this.textBoxNotes.Text; } set { this.textBoxNotes.Text = value; } }

		#endregion

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public NoteForm()
		{
			this.InitializeComponent();
			Icon = Icon.FromHandle(Resources.NoteText.GetHicon());
			this.textBoxNotes.DataBindings.Add("Font", Editor.Settings, "NoteFont",
				false, DataSourceUpdateMode.OnPropertyChanged);
		}

		#endregion

		#region Private Methods

		private void ButtonCutClick(object sender, EventArgs e)
		{
			if (this.textBoxNotes.SelectedText.Length > 0)
			{
				Clipboard.SetText(this.textBoxNotes.SelectedText);
				this.textBoxNotes.SelectedText = "";
			}

		}

		private void ButtonCopyClick(object sender, EventArgs e)
		{
			if (this.textBoxNotes.SelectedText.Length > 0)
				Clipboard.SetText(this.textBoxNotes.SelectedText);
		}

		private void ButtonPasteClick(object sender, EventArgs e)
		{
			if (Clipboard.ContainsText())
			{
				if (this.textBoxNotes.SelectedText.Length > 0)
					this.textBoxNotes.SelectedText = Clipboard.GetText();
				else
					this.textBoxNotes.AppendText(Clipboard.GetText());
			}
		}

		private void ButtonSelectAllClick(object sender, EventArgs e)
		{
			this.textBoxNotes.SelectAll();
		}

		private void ButtonFontClick(object sender, EventArgs e)
		{
			using (var dialog = new FontSelectionDialog())
			{
				dialog.UserFont = this.textBoxNotes.Font;
				if (dialog.ShowDialog() == DialogResult.OK)
					this.textBoxNotes.Font = dialog.UserFont;
			}
		}

		private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}

		#endregion
	}
}
