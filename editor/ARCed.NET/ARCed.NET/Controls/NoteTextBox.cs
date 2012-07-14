using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Dialogs;

namespace ARCed.Controls
{
	/// <summary>
	/// Control used for displaying and editing notes
	/// </summary>
	[Description("Control for providing functionality for editing game object notes.")]
	[ToolboxBitmap(typeof(GroupBox))]
	public partial class NoteTextBox : UserControl
	{
		#region Private Fields

		private bool _busy;

		#endregion

		#region Events

		public delegate void TextChangedEventHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised when the text on the control is changed
		/// </summary>
		[Category("ARCed"), Description("Event raised when the text on the control is changed.")]
		public event TextChangedEventHandler NoteTextChanged;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the note text of the control
		/// </summary>
		[Category("ARCed"), Description("Gets or sets the note text of the control")]
		public string NoteText 
		{ 
			get { return textBoxNotes.Text; } 
			set { textBoxNotes.Text = value; } 
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public NoteTextBox()
		{
			InitializeComponent();
		}

		#endregion

		#region Private Methods

		private void buttonFont_Click(object sender, EventArgs e)
		{
			using (FontSelectionDialog dialog = new FontSelectionDialog())
			{
				dialog.UserFont = textBoxNotes.Font;
				if (dialog.ShowDialog() == DialogResult.OK)
					textBoxNotes.Font = dialog.UserFont;
			}
		}

		private void buttonEditor_Click(object sender, EventArgs e)
		{
			using (NoteForm dialog = new NoteForm())
			{
				dialog.NoteText = textBoxNotes.Text;
				if (dialog.ShowDialog() == DialogResult.OK)
					textBoxNotes.Text = dialog.NoteText;
			}
		}

		private void NoteTextBox_Load(object sender, EventArgs e)
		{
			if (!DesignMode && textBoxNotes.DataBindings.Count == 0)
			{
				textBoxNotes.DataBindings.Add("Font", Editor.Settings, "NoteFont",
					false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
				textBoxNotes.ContextMenuStrip = contextMenuNotes;
			}
		}

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

		private void textBoxNotes_ClientSizeChanged(object sender, EventArgs e)
		{
			if (NoteTextChanged != null)
				NoteTextChanged(this, e);
			if (!_busy)
			{
				_busy = true;
				Size tS = TextRenderer.MeasureText(textBoxNotes.Text, textBoxNotes.Font);
				bool Hsb = textBoxNotes.ClientSize.Height < tS.Height + Convert.ToInt32(textBoxNotes.Font.Size);
				bool Vsb = textBoxNotes.ClientSize.Width < tS.Width;
				if (Hsb && Vsb && textBoxNotes.ScrollBars != ScrollBars.Both)
					textBoxNotes.ScrollBars = ScrollBars.Both;
				else if (!Hsb && !Vsb && textBoxNotes.ScrollBars != ScrollBars.None)
					textBoxNotes.ScrollBars = ScrollBars.None;
				else if (Hsb && !Vsb && textBoxNotes.ScrollBars != ScrollBars.Vertical)
					textBoxNotes.ScrollBars = ScrollBars.Vertical;
				else if (!Hsb && Vsb && textBoxNotes.ScrollBars != ScrollBars.Horizontal)
					textBoxNotes.ScrollBars = ScrollBars.Horizontal;
				_busy = false;
			}
		}

		#endregion
	}
}
