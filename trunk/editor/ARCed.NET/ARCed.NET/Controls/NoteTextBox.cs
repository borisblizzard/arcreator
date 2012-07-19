#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Dialogs;

#endregion

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
			get { return this.textBoxNotes.Text; } 
			set { this.textBoxNotes.Text = value; } 
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public NoteTextBox()
		{
			this.InitializeComponent();
		}

		#endregion

		#region Private Methods

		private void buttonFont_Click(object sender, EventArgs e)
		{
			using (var dialog = new FontSelectionDialog())
			{
				dialog.UserFont = this.textBoxNotes.Font;
				if (dialog.ShowDialog() == DialogResult.OK)
					this.textBoxNotes.Font = dialog.UserFont;
			}
		}

		private void buttonEditor_Click(object sender, EventArgs e)
		{
			using (var dialog = new NoteForm())
			{
				dialog.NoteText = this.textBoxNotes.Text;
				if (dialog.ShowDialog() == DialogResult.OK)
					this.textBoxNotes.Text = dialog.NoteText;
			}
		}

		private void NoteTextBox_Load(object sender, EventArgs e)
		{
			if (!DesignMode && this.textBoxNotes.DataBindings.Count == 0)
			{
				this.textBoxNotes.DataBindings.Add("Font", Editor.Settings, "NoteFont",
					false, DataSourceUpdateMode.OnPropertyChanged);
				this.textBoxNotes.ContextMenuStrip = this.contextMenuNotes;
			}
		}

		private void buttonCut_Click(object sender, EventArgs e)
		{
			if (this.textBoxNotes.SelectedText.Length > 0)
			{
				Clipboard.SetText(this.textBoxNotes.SelectedText);
				this.textBoxNotes.SelectedText = "";
			}
		}

		private void buttonCopy_Click(object sender, EventArgs e)
		{
			if (this.textBoxNotes.SelectedText.Length > 0)
				Clipboard.SetText(this.textBoxNotes.SelectedText);
		}

		private void buttonPaste_Click(object sender, EventArgs e)
		{
			if (Clipboard.ContainsText())
			{
				if (this.textBoxNotes.SelectedText.Length > 0)
					this.textBoxNotes.SelectedText = Clipboard.GetText();
				else
					this.textBoxNotes.AppendText(Clipboard.GetText());
			}
		}

		private void buttonSelectAll_Click(object sender, EventArgs e)
		{
			this.textBoxNotes.SelectAll();
		}

		private void textBoxNotes_ClientSizeChanged(object sender, EventArgs e)
		{
			if (this.NoteTextChanged != null)
				this.NoteTextChanged(this, e);
			if (!this._busy)
			{
				this._busy = true;
				Size tS = TextRenderer.MeasureText(this.textBoxNotes.Text, this.textBoxNotes.Font);
				bool Hsb = this.textBoxNotes.ClientSize.Height < tS.Height + Convert.ToInt32(this.textBoxNotes.Font.Size);
				bool Vsb = this.textBoxNotes.ClientSize.Width < tS.Width;
				if (Hsb && Vsb && this.textBoxNotes.ScrollBars != ScrollBars.Both)
					this.textBoxNotes.ScrollBars = ScrollBars.Both;
				else if (!Hsb && !Vsb && this.textBoxNotes.ScrollBars != ScrollBars.None)
					this.textBoxNotes.ScrollBars = ScrollBars.None;
				else if (Hsb && !Vsb && this.textBoxNotes.ScrollBars != ScrollBars.Vertical)
					this.textBoxNotes.ScrollBars = ScrollBars.Vertical;
				else if (!Hsb && Vsb && this.textBoxNotes.ScrollBars != ScrollBars.Horizontal)
					this.textBoxNotes.ScrollBars = ScrollBars.Horizontal;
				this._busy = false;
			}
		}

		#endregion
	}
}
