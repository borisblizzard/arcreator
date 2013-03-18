#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using System.Windows.Forms;
using ARCed.Dialogs;
using ARCed.Helpers;
using ARCed.Properties;
using ARCed.UI;

#endregion

namespace ARCed.Scripting
{
	public partial class ScriptMenuForm : DockContent
	{
		// Get rid of using Binding list
		private BindingList<Script> _scripts;
		private bool _suppressUpdate;
		private string _scriptDirectory;

		/// <summary>
		/// Gets or sets the directory where the project's scripts are found
		/// </summary>
		public string ScriptsDirectory
		{
			get { return this._scriptDirectory; }
			set { this.LoadScripts(value); }
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public ScriptMenuForm() 
		{
			this.InitializeComponent();
			this.LoadScripts(Project.ScriptsDirectory);
			Icon = Icon.FromHandle(Resources.Ruby.GetHicon());
		}

		private void LoadScripts(string directory)
		{
			if (this._scriptDirectory != directory)
			{
				this._scriptDirectory = directory;
				this._scripts = Project.ScriptManager.BindingList;
				this.listBoxScripts.DataSource = this._scripts;
				this.listBoxScripts.DisplayMember = "Title";

				this.fileSystemWatcher.Path = Project.ScriptsDirectory;
			}
		}

		private void RefreshStatus(bool forceRefresh = false)
		{
			if (this.listBoxScripts.SelectedIndex >= 0 && (ContainsFocus || forceRefresh))
			{
				FileInfo fileInfo = (this.listBoxScripts.SelectedItem as Script).FileInfo;
				if (fileInfo != null)
				{
					Editor.StatusBar.Items[0].Text = 
						String.Format("Created On: {0}", fileInfo.CreationTime);
					Editor.StatusBar.Items[1].Text =
						String.Format("Last Saved: {0}", fileInfo.LastWriteTime);
					Editor.StatusBar.Items[2].Text = "";
				}
				else
				{
					Editor.StatusBar.Items[0].Text = "Created On: <Pending>";
					Editor.StatusBar.Items[1].Text = "Last Saved: <Pending>";
					Editor.StatusBar.Items[2].Text = "";
				}
			}
			else
			{
				foreach (ToolStripStatusLabel item in Editor.StatusBar.Items)
					item.Text = "";
			}
		}

		private static void OpenScript(Script script)
		{
			Editor.OpenScript(script, true);
		}

		private void listBoxScripts_SelectedIndexChanged(object sender, EventArgs e)
		{
			var item = this.listBoxScripts.SelectedItem;
			bool enable = item != null;
			this.buttonOpen.Enabled = enable;
			this.buttonMoveUp.Enabled = enable;
			this.buttonMoveDown.Enabled = enable;
			this.buttonDelete.Enabled = enable;
			this.textBoxName.Enabled = enable;
			this._suppressUpdate = true;
			this.textBoxName.Text = enable ? (item as Script).Title : "";
			this._suppressUpdate = false;
			this.RefreshStatus();
		}

		private void buttonImport_Click(object sender, EventArgs e)
		{
			using (var loadDialog = new OpenFileDialog())
			{
				loadDialog.DefaultExt = ".rb";
				loadDialog.Filter = "Ruby File|*.rb";
				loadDialog.InitialDirectory =
					Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
				loadDialog.Title = "Import Script...";
				loadDialog.Multiselect = true;
				if (loadDialog.ShowDialog() == DialogResult.OK)
				{
					foreach (string filename in loadDialog.FileNames)
						this._scripts.Add(new Script(filename));
				}
			}
		}

		private void buttonOpen_Click(object sender, EventArgs e)
		{
			int index = this.listBoxScripts.SelectedIndex;
			if (index >= 0)
				OpenScript(this._scripts[index]);
		}

		private void buttonMoveUp_Click(object sender, EventArgs e)
		{
			int index = this.listBoxScripts.SelectedIndex;
			if (index > 0)
			{
				Script script = Project.ScriptManager.Scripts[index];
				this._scripts.RemoveAt(index);
				this._scripts.Insert(index - 1, script);
				this.listBoxScripts.SelectedIndex = index - 1;
			}
		}

		private void buttonMoveDown_Click(object sender, EventArgs e)
		{
			int index = this.listBoxScripts.SelectedIndex;
			if (index >= 0 && index < this.listBoxScripts.Items.Count - 1)
			{
				Script script = Project.ScriptManager.Scripts[index];
				this._scripts.RemoveAt(index);
				this._scripts.Insert(index + 1, script);
				this.listBoxScripts.SelectedIndex = index + 1;
			}
		}

		private void buttonDelete_Click(object sender, EventArgs e)
		{
			int index = this.listBoxScripts.SelectedIndex;
			if (index >= 0)
			{
				var form = Windows.ScriptEditors.Find(f => f.Script == this._scripts[index]);
				if (form != null)
					form.Close();
				this._scripts.RemoveAt(index);
			}
		}

		private void buttonFind_Click(object sender, EventArgs e)
		{
			if (Editor.MainDock.ActiveDocumentPane != null)
				Windows.ScriptSearchForm.Show(Editor.MainDock.ActiveDocument.DockHandler.DockPanel);
			else
				Editor.Show(Windows.ScriptSearchForm);
		}

		private void buttonAdd_Click(object sender, EventArgs e)
		{
			this.AddScript(-1);
		}

		private void AddScript(int index = -1)
		{
			using (var dialog = new NewScriptForm())
			{
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					if (index != -1)
						this._scripts.Insert(index, dialog.NewScript);
					else
					{
						this._scripts.Add(dialog.NewScript);
						index = this._scripts.Count - 1;
					}
					this.listBoxScripts.SelectedIndex = index;
					OpenScript(this._scripts[index]);
					Project.ScriptManager.RefreshScriptIndices();
				}
			}
		}

		private void buttonInsert_Click(object sender, EventArgs e)
		{
			int index = this.listBoxScripts.SelectedIndex;
			if (index < 0)
				index = Project.ScriptManager.Scripts.Count;
			var script = new Script();
			this._scripts.Insert(index, script);
			this.listBoxScripts.SelectedIndex = index;
			this.buttonOpen_Click(null, null);
			Project.ScriptManager.RefreshScriptIndices();
		}

		private void buttonSaveAll_Click(object sender, EventArgs e)
		{
			Project.ScriptManager.SaveAll();
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			// TODO: Improve this ugly mess...
			if (!this._suppressUpdate)
			{
				int index = this.listBoxScripts.SelectedIndex;
				if (index >= 0)
				{
					Util.ValidateTextBox(this.textBoxName, "");
					Project.ScriptManager.Scripts[index].Title = this.textBoxName.Text;
					this._scripts.Add(Script.DummyScript);
					this._scripts.Remove(Script.DummyScript);
				}
			}
		}

		private void listBoxScripts_MouseDown(object sender, MouseEventArgs e)
		{
			if (e.Button == MouseButtons.Right)
			{
				int index = this.listBoxScripts.IndexFromPoint(e.X, e.Y);
				if (index >= 0)
					this.listBoxScripts.SelectedIndex = index;
			}
		}

		private void buttonTemplate_Click(object sender, EventArgs e)
		{
			
			int index = this.listBoxScripts.SelectedIndex;
			if (index >= 0)
			{
				string t = (this.listBoxScripts.SelectedItem as Script).Title;
				using (var dialog =
					new UserStringForm("Save as Template", t, "Template Name:", true))
				{
					dialog.Location = this.listBoxScripts.PointToClient(MousePosition);
					if (dialog.ShowDialog(this) == DialogResult.OK)
					{
						string text = this._scripts[index].Text;
						string filename = Path.Combine(PathHelper.ScriptTemplateDirectory,
							String.Format("{0}.rb", dialog.UserString));
						if (File.Exists(filename) && 
							MessageBox.Show("Template already exists.\n\nOverwrite?",
							"Confirm", MessageBoxButtons.OKCancel, MessageBoxIcon.Exclamation) != DialogResult.OK)
						{
							return;
						}
						try { File.WriteAllText(filename, text); }
						catch
						{
							MessageBox.Show("Failed to save template.",
								"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
						}
					}
				}
			}
		}

		private void fileSystemWatcher_CreatedorDeleted(object sender, FileSystemEventArgs e)
		{
			
			if (e.ChangeType.HasFlag(WatcherChangeTypes.Deleted))
			{
				Script script = Project.ScriptManager.WithPath(e.FullPath);
				if (script != null)
					this._scripts.Remove(script);
			}
			else if (e.ChangeType.HasFlag(WatcherChangeTypes.Created))
			{
				Script script = Project.ScriptManager.WithPath(e.FullPath);
				if (script == null)
					this._scripts.Add(new Script(e.FullPath));
			}
		}

		private void pictureHeader_SizeChanged(object sender, EventArgs e)
		{
			this.RefreshHeader();
		}

		private void pictureHeader_DoubleClick(object sender, EventArgs e)
		{
			using (var dialog = new HeaderSettingsDialog())
				dialog.ShowDialog();
		}

		public void RefreshHeader()
		{
			ControlHelper.RenderHeaderImage(this.pictureHeader, "Scripts");
		}
	}
}
