using System;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using System.Windows.Forms;
using ARCed.UI;
using ARCed.Dialogs;
using ARCed.Helpers;

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
			get { return _scriptDirectory; }
			set { LoadScripts(value); }
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public ScriptMenuForm() 
		{
			InitializeComponent();
			LoadScripts(Project.ScriptsDirectory);
			this.Icon = Icon.FromHandle(Properties.Resources.Ruby.GetHicon());
		}

		private void LoadScripts(string directory)
		{
			if (_scriptDirectory != directory)
			{
				_scriptDirectory = directory;
				_scripts = Project.ScriptManager.BindingList;
				listBoxScripts.DataSource = _scripts;
				listBoxScripts.DisplayMember = "Title";

				fileSystemWatcher.Path = Project.ScriptsDirectory;
			}
		}

		private void RefreshStatus(bool forceRefresh = false)
		{
			if (listBoxScripts.SelectedIndex >= 0 && (this.ContainsFocus || forceRefresh))
			{
				FileInfo fileInfo = (listBoxScripts.SelectedItem as Script).FileInfo;
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

		private void OpenScript(Script script)
		{
			Editor.OpenScript(script, true);
		}

		private void listBoxScripts_SelectedIndexChanged(object sender, EventArgs e)
		{
			var item = listBoxScripts.SelectedItem;
			bool enable = item != null;
			buttonOpen.Enabled = enable;
			buttonMoveUp.Enabled = enable;
			buttonMoveDown.Enabled = enable;
			buttonDelete.Enabled = enable;
			textBoxName.Enabled = enable;
			_suppressUpdate = true;
			textBoxName.Text = enable ? (item as Script).Title : "";
			_suppressUpdate = false;
			RefreshStatus();
		}

		private void buttonImport_Click(object sender, EventArgs e)
		{
			using (OpenFileDialog loadDialog = new OpenFileDialog())
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
						_scripts.Add(new Script(filename));
				}
			}
		}

		private void buttonOpen_Click(object sender, EventArgs e)
		{
			int index = listBoxScripts.SelectedIndex;
			if (index >= 0)
				OpenScript(_scripts[index]);
		}

		private void buttonMoveUp_Click(object sender, EventArgs e)
		{
			int index = listBoxScripts.SelectedIndex;
			if (index > 0)
			{
				Script script = Project.ScriptManager.Scripts[index];
				_scripts.RemoveAt(index);
				_scripts.Insert(index - 1, script);
				listBoxScripts.SelectedIndex = index - 1;
			}
		}

		private void buttonMoveDown_Click(object sender, EventArgs e)
		{
			int index = listBoxScripts.SelectedIndex;
			if (index >= 0 && index < listBoxScripts.Items.Count - 1)
			{
				Script script = Project.ScriptManager.Scripts[index];
				_scripts.RemoveAt(index);
				_scripts.Insert(index + 1, script);
				listBoxScripts.SelectedIndex = index + 1;
			}
		}

		private void buttonDelete_Click(object sender, EventArgs e)
		{
			int index = listBoxScripts.SelectedIndex;
			if (index >= 0)
			{
				ScriptEditorForm form = Windows.ScriptEditors.Find(
					delegate(ScriptEditorForm f) { return f.Script == _scripts[index]; });
				if (form != null)
					form.Close();
				_scripts.RemoveAt(index);
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
			AddScript(-1);
		}

		private void AddScript(int index = -1)
		{
			using (NewScriptForm dialog = new NewScriptForm())
			{
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					if (index != -1)
						_scripts.Insert(index, dialog.NewScript);
					else
					{
						_scripts.Add(dialog.NewScript);
						index = _scripts.Count - 1;
					}
					listBoxScripts.SelectedIndex = index;
					OpenScript(_scripts[index]);
					Project.ScriptManager.RefreshScriptIndices();
				}
			}
		}

		private void buttonInsert_Click(object sender, EventArgs e)
		{
			int index = listBoxScripts.SelectedIndex;
			if (index < 0)
				index = Project.ScriptManager.Scripts.Count;
			Script script = new Script();
			_scripts.Insert(index, script);
			listBoxScripts.SelectedIndex = index;
			buttonOpen_Click(null, null);
			Project.ScriptManager.RefreshScriptIndices();
		}

		private void buttonSaveAll_Click(object sender, EventArgs e)
		{
			Project.ScriptManager.SaveAll();
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			// TODO: Improve this ugly mess...
			if (!_suppressUpdate)
			{
				int index = listBoxScripts.SelectedIndex;
				if (index >= 0)
				{
					Util.ValidateTextBox(textBoxName, "");
					Project.ScriptManager.Scripts[index].Title = textBoxName.Text;
					_scripts.Add(Script.DummyScript);
					_scripts.Remove(Script.DummyScript);
				}
			}
		}

		private void listBoxScripts_MouseDown(object sender, MouseEventArgs e)
		{
			if (e.Button == System.Windows.Forms.MouseButtons.Right)
			{
				int index = listBoxScripts.IndexFromPoint(e.X, e.Y);
				if (index >= 0)
					listBoxScripts.SelectedIndex = index;
			}
		}

		private void buttonTemplate_Click(object sender, EventArgs e)
		{
			
			int index = listBoxScripts.SelectedIndex;
			if (index >= 0)
			{
				string t = (listBoxScripts.SelectedItem as Script).Title;
				using (var dialog =
					new ARCed.Dialogs.UserStringForm("Save as Template", t, "Template Name:", true))
				{
					dialog.Location = listBoxScripts.PointToClient(MousePosition);
					if (dialog.ShowDialog(this) == DialogResult.OK)
					{
						string text = _scripts[index].Text;
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
					_scripts.Remove(script);
			}
			else if (e.ChangeType.HasFlag(WatcherChangeTypes.Created))
			{
				Script script = Project.ScriptManager.WithPath(e.FullPath);
				if (script == null)
					_scripts.Add(new Script(e.FullPath));
			}
		}

		private void pictureHeader_SizeChanged(object sender, EventArgs e)
		{
			RefreshHeader();
		}

		private void pictureHeader_DoubleClick(object sender, EventArgs e)
		{
			using (HeaderSettingsDialog dialog = new HeaderSettingsDialog())
				dialog.ShowDialog();
		}

		public void RefreshHeader()
		{
			DatabaseHelper.RenderHeaderImage(pictureHeader, "Scripts");
		}
	}
}
