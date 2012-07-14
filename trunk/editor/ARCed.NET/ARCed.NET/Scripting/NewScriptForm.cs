using System;
using System.IO;
using System.Linq;
using System.Windows.Forms;
using ARCed.Helpers;

namespace ARCed.Scripting
{
	public partial class NewScriptForm : Form
	{
		private string[] _templates;

		/// <summary>
		/// Gets a new script object based on the configuration
		/// </summary>
		public Script NewScript
		{
			get
			{
				string text = "";
				if (comboBoxTemplate.SelectedIndex > 0)
				{
					string path = Path.Combine(PathHelper.ScriptTemplateDirectory,
						comboBoxTemplate.Text + ".rb");
					try { text = String.Format(File.ReadAllText(path), textBoxName.Text); }
					catch { }
				}
				Script script = new Script() { Title = textBoxName.Text, Text = text };
				return script;
			}
		}

		public NewScriptForm()
		{
			InitializeComponent();
			RefreshTemplates();
			comboBoxTemplate.SelectedIndex = 0;
		}

		private void RefreshTemplates()
		{
			comboBoxTemplate.Items.Clear();
			comboBoxTemplate.Items.Add("Empty");
			string dir = PathHelper.ScriptTemplateDirectory;
			if (Directory.Exists(dir))
			{
				_templates = Directory.GetFiles(dir, "*.rb");
				foreach (string filename in _templates)
					comboBoxTemplate.Items.Add(Path.GetFileNameWithoutExtension(filename));
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			Util.ValidateTextBox(textBoxName, "");
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}
	}
}
