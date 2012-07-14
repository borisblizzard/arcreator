using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using ARCed.UI;
using System.Windows.Forms;

namespace ARCed.Scripting
{
	public partial class AutoCompleteForm : DockContent
	{
		private BindingList<string> _wordList;

		/// <summary>
		/// Default constructor
		/// </summary>
		public AutoCompleteForm()
		{
			InitializeComponent();
			_wordList = new BindingList<string>(Editor.Settings.Scripting.AutoCompleteWords);
			this.Icon = System.Drawing.Icon.FromHandle(Properties.Resources.AutoComplete.GetHicon());
			textBoxFillUp.Text = Editor.Settings.Scripting.FillUpCharacters;
			textBoxFillUp.Font = Helpers.FontHelper.MonoFont;
			numericAutoLength.Value = Editor.Settings.Scripting.AutoCompleteLength;
			listBoxWords.DataSource = _wordList; 
		}

		public void AddToAutocomplete(string text)
		{
			string[] words = text.Split(' ', '\n', '\t', '.', '@', '$');
			listBoxWords.BeginUpdate();
			string currentWord;
			foreach (string word in words)
			{
				currentWord = word.Trim();
				if (currentWord == "" || currentWord.Length < 2) continue;
				if (!_wordList.Contains(currentWord))
					_wordList.Add(currentWord);
			}
			listBoxWords.EndUpdate();
		}

		private void buttonAdd_Click(object sender, EventArgs e)
		{
			AddToAutocomplete(textBoxWords.Text);
			textBoxWords.Clear();
		}

		private void buttonClear_Click(object sender, EventArgs e)
		{
			textBoxWords.Clear();
		}

		private void numericAutoLength_ValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Scripting.AutoCompleteLength = (int)numericAutoLength.Value;
		}

		private void removeSelectedToolStripMenuItem_Click(object sender, EventArgs e)
		{
			listBoxWords.BeginUpdate();
			string[] words = new string[listBoxWords.SelectedItems.Count];
			for (int i = 0; i < listBoxWords.SelectedItems.Count; i++)
				words[i] = listBoxWords.SelectedItems[i].ToString();
			foreach (string word in words)
				_wordList.Remove(word);
			listBoxWords.EndUpdate();
		}

		private void listBoxWords_KeyDown(object sender, KeyEventArgs e)
		{
			if (e.KeyData == Keys.Delete)
				removeSelectedToolStripMenuItem_Click(null, null);
		}

		private void textBoxFillUp_TextChanged(object sender, EventArgs e)
		{
			Editor.Settings.Scripting.FillUpCharacters = textBoxFillUp.Text;
			foreach (ScriptEditorForm form in Windows.ScriptEditors)
				form.ScintillaControl.AutoComplete.FillUpCharacters = textBoxFillUp.Text;
		}

		private void buttonPaste_Click(object sender, EventArgs e)
		{
			if (Clipboard.ContainsText())
				textBoxWords.Text = Clipboard.GetText();
		}
	}
}
