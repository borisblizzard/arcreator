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
		public string NoteText { get { return textBoxNotes.Text; } set { textBoxNotes.Text = value; } }

		#endregion

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public NoteForm()
		{
			InitializeComponent();
			Icon = Icon.FromHandle(Resources.NoteText.GetHicon());
			textBoxNotes.DataBindings.Add("Font", Editor.Settings, "NoteFont",
				false, DataSourceUpdateMode.OnPropertyChanged);
		}

		#endregion

		#region Private Methods

		private void ButtonCutClick(object sender, EventArgs e)
		{
			if (textBoxNotes.SelectedText.Length > 0)
			{
				Clipboard.SetText(textBoxNotes.SelectedText);
				textBoxNotes.SelectedText = "";
			}

		}

		private void ButtonCopyClick(object sender, EventArgs e)
		{
			if (textBoxNotes.SelectedText.Length > 0)
				Clipboard.SetText(textBoxNotes.SelectedText);
		}

		private void ButtonPasteClick(object sender, EventArgs e)
		{
			if (Clipboard.ContainsText())
			{
				if (textBoxNotes.SelectedText.Length > 0)
					textBoxNotes.SelectedText = Clipboard.GetText();
				else
					textBoxNotes.AppendText(Clipboard.GetText());
			}
		}

		private void ButtonSelectAllClick(object sender, EventArgs e)
		{
			textBoxNotes.SelectAll();
		}

		private void ButtonFontClick(object sender, EventArgs e)
		{
			using (var dialog = new FontSelectionDialog())
			{
				dialog.UserFont = textBoxNotes.Font;
				if (dialog.ShowDialog() == DialogResult.OK)
					textBoxNotes.Font = dialog.UserFont;
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
