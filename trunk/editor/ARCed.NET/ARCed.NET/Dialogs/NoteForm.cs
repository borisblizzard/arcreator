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
			this.Icon = Icon.FromHandle(Resources.NoteText.GetHicon());
			textBoxNotes.DataBindings.Add("Font", Editor.Settings, "NoteFont",
				false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
		}

		#endregion

		#region Private Methods

		private void buttonCut_Click(object sender, EventArgs e)
		{
			if (textBoxNotes.SelectedText.Length > 0)
			{
				Clipboard.SetText(textBoxNotes.SelectedText);
				textBoxNotes.SelectedText = "";
			}

		}

		private void buttonCopy_Click(object sender, EventArgs e)
		{
			if (textBoxNotes.SelectedText.Length > 0)
				Clipboard.SetText(textBoxNotes.SelectedText);
		}

		private void buttonPaste_Click(object sender, EventArgs e)
		{
			if (Clipboard.ContainsText())
			{
				if (textBoxNotes.SelectedText.Length > 0)
					textBoxNotes.SelectedText = Clipboard.GetText();
				else
					textBoxNotes.AppendText(Clipboard.GetText());
			}
		}

		private void buttonSelectAll_Click(object sender, EventArgs e)
		{
			textBoxNotes.SelectAll();
		}

		private void buttonFont_Click(object sender, EventArgs e)
		{
			using (var dialog = new FontSelectionDialog())
			{
				dialog.UserFont = textBoxNotes.Font;
				if (dialog.ShowDialog() == DialogResult.OK)
					textBoxNotes.Font = dialog.UserFont;
			}
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}

		#endregion
	}
}
