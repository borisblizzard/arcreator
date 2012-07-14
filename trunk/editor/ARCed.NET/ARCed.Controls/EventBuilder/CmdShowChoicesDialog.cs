using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ARCed.EventBuilder
{
	/// <summary>
	/// TEMPORARY until dynamic number of choices is implemented
	/// </summary>
	public partial class CmdShowChoicesDialog : Form
	{

		public string[] Choices
		{
			get { return GetChoices(); }
			set { SetChoices(value); }
		}

		public int CancelIndex 
		{
			get { return GetIndex(); }
			set { SetIndex(value); }
		}

		public CmdShowChoicesDialog()
		{
			InitializeComponent();
		}

		private void SetChoices(string[] choices)
		{
			TextBox[] textBoxes = new[] { textBox1, textBox2, textBox3, textBox4 };
			for (int i = 0; i < choices.Length; i++)
				textBoxes[i].Text = choices[i];
		}

		private string[] GetChoices()
		{
			var choices = new List<string>();
			string text;
			foreach (TextBox box in new[] { textBox1, textBox2, textBox3, textBox4 })
			{
				text = box.Text;
				if (text != "")
					choices.Add(box.Text);
			}
			return choices.ToArray();
		}

		private void SetIndex(int index)
		{
			(groupBoxOnCancel.Controls[index] as RadioButton).Checked = true;
		}

		private int GetIndex()
		{
			int index = 0;
			foreach (RadioButton button in groupBoxOnCancel.Controls)
			{
				if (button.Checked)
					return index;
				index++;
			}
			return 0;
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}
	}
}
