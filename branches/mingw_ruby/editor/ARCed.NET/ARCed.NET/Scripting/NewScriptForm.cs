#region Using Directives

using System;
using System.IO;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

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
				if (this.comboBoxTemplate.SelectedIndex > 0)
				{
					string path = Path.Combine(PathHelper.ScriptTemplateDirectory,
						this.comboBoxTemplate.Text + ".rb");
					try { text = String.Format(File.ReadAllText(path), this.textBoxName.Text); }
					catch { }
				}
				var script = new Script
				{ Title = this.textBoxName.Text, Text = text };
				return script;
			}
		}

		public NewScriptForm()
		{
			this.InitializeComponent();
			this.RefreshTemplates();
			this.comboBoxTemplate.SelectedIndex = 0;
		}

		private void RefreshTemplates()
		{
			this.comboBoxTemplate.Items.Clear();
			this.comboBoxTemplate.Items.Add("Empty");
			string dir = PathHelper.ScriptTemplateDirectory;
			if (Directory.Exists(dir))
			{
				this._templates = Directory.GetFiles(dir, "*.rb");
				foreach (string filename in this._templates)
					this.comboBoxTemplate.Items.Add(Path.GetFileNameWithoutExtension(filename));
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			Util.ValidateTextBox(this.textBoxName, "");
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}
	}
}
