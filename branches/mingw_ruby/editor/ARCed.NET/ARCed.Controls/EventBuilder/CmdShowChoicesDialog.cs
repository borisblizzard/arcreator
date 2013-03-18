#region Using Directives

using System;
using System.Collections.Generic;
using System.Windows.Forms;

#endregion

namespace ARCed.EventBuilder
{
	/// <summary>
	/// TEMPORARY until dynamic number of choices is implemented
	/// </summary>
	public partial class CmdShowChoicesDialog : Form
	{

		public string[] Choices
		{
			get { return this.GetChoices(); }
			set { this.SetChoices(value); }
		}

		public int CancelIndex 
		{
			get { return this.GetIndex(); }
			set { this.SetIndex(value); }
		}

		public CmdShowChoicesDialog()
		{
			this.InitializeComponent();
		}

		private void SetChoices(IList<string> choices)
		{
			var textBoxes = new[] { this.textBox1, this.textBox2, this.textBox3, this.textBox4 };
			for (int i = 0; i < choices.Count; i++)
				textBoxes[i].Text = choices[i];
		}

		private string[] GetChoices()
		{
			var choices = new List<string>();
			string text;
			foreach (TextBox box in new[] { this.textBox1, this.textBox2, this.textBox3, this.textBox4 })
			{
				text = box.Text;
				if (text != "")
					choices.Add(box.Text);
			}
			return choices.ToArray();
		}

		private void SetIndex(int index)
		{
			(this.groupBoxOnCancel.Controls[index] as RadioButton).Checked = true;
		}

		private int GetIndex()
		{
			int index = 0;
			foreach (RadioButton button in this.groupBoxOnCancel.Controls)
			{
				if (button.Checked)
					return index;
				index++;
			}
			return 0;
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}
	}
}
