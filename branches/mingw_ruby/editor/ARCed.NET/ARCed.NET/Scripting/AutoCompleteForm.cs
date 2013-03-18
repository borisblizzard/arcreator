#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Helpers;
using ARCed.Properties;
using ARCed.UI;

#endregion

namespace ARCed.Scripting
{
	public partial class AutoCompleteForm : DockContent
	{
		private readonly BindingList<string> _wordList;

		/// <summary>
		/// Default constructor
		/// </summary>
		public AutoCompleteForm()
		{
			this.InitializeComponent();
			this._wordList = new BindingList<string>(Editor.Settings.Scripting.AutoCompleteWords);
			Icon = Icon.FromHandle(Resources.AutoComplete.GetHicon());
			this.textBoxFillUp.Text = Editor.Settings.Scripting.FillUpCharacters;
			this.textBoxFillUp.Font = FontHelper.MonoFont;
			this.numericAutoLength.Value = Editor.Settings.Scripting.AutoCompleteLength;
			this.listBoxWords.DataSource = this._wordList; 
		}

		public void AddToAutocomplete(string text)
		{
			string[] words = text.Split(' ', '\n', '\t', '.', '@', '$');
			this.listBoxWords.BeginUpdate();
			string currentWord;
			foreach (string word in words)
			{
				currentWord = word.Trim();
				if (currentWord == "" || currentWord.Length < 2) continue;
				if (!this._wordList.Contains(currentWord))
					this._wordList.Add(currentWord);
			}
			this.listBoxWords.EndUpdate();
		}

		private void buttonAdd_Click(object sender, EventArgs e)
		{
			this.AddToAutocomplete(this.textBoxWords.Text);
			this.textBoxWords.Clear();
		}

		private void buttonClear_Click(object sender, EventArgs e)
		{
			this.textBoxWords.Clear();
		}

		private void numericAutoLength_ValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Scripting.AutoCompleteLength = (int)this.numericAutoLength.Value;
		}

		private void removeSelectedToolStripMenuItem_Click(object sender, EventArgs e)
		{
			this.listBoxWords.BeginUpdate();
			var words = new string[this.listBoxWords.SelectedItems.Count];
			for (int i = 0; i < this.listBoxWords.SelectedItems.Count; i++)
				words[i] = this.listBoxWords.SelectedItems[i].ToString();
			foreach (string word in words)
				this._wordList.Remove(word);
			this.listBoxWords.EndUpdate();
		}

		private void listBoxWords_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.KeyData == Keys.Delete)
				this.removeSelectedToolStripMenuItem_Click(null, null);
		}

		private void textBoxFillUp_TextChanged(object sender, EventArgs e)
		{
			Editor.Settings.Scripting.FillUpCharacters = this.textBoxFillUp.Text;
			foreach (ScriptEditorForm form in Windows.ScriptEditors)
				form.ScintillaControl.AutoComplete.FillUpCharacters = this.textBoxFillUp.Text;
		}

		private void buttonPaste_Click(object sender, EventArgs e)
		{
			if (Clipboard.ContainsText())
				this.textBoxWords.Text = Clipboard.GetText();
		}
	}
}
