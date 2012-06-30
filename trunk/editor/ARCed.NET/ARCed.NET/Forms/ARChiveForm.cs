using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Windows.Forms;
using ARCed.UI;
using System.Diagnostics;
using ARCed.Settings;
using System.Threading;
using ARCed.Helpers;
using SevenZip;

namespace ARCed.Forms
{
	public partial class ARChiveForm : DockContent
	{
		private string[] _archives;
		private string _archiveName;
		private SevenZipCompressor compressor;

		public ARChiveForm()
		{
			InitializeComponent();
			this.Icon = System.Drawing.Icon.FromHandle(Properties.Resources.SevenZip.GetHicon());
			numericMaxBackups.DataBindings.Add("Value", Project.ARChiveSettings, 
				"MaxBackups", false, DataSourceUpdateMode.OnPropertyChanged);
			numericInterval.DataBindings.Add("Value", Project.ARChiveSettings,
				"Interval", false, DataSourceUpdateMode.OnPropertyChanged);
			checkBoxThreaded.DataBindings.Add("Checked", Project.ARChiveSettings,
				"Threaded", false, DataSourceUpdateMode.OnPropertyChanged);
			RefreshSettings();
		}

		public void RefreshSettings()
		{
			checkBoxTypeAllData.Checked = Project.ARChiveSettings.Type.HasFlag(BackupType.AllData);
			checkBoxTypeMaps.Checked = Project.ARChiveSettings.Type.HasFlag(BackupType.Maps);
			checkBoxTypeScripts.Checked = Project.ARChiveSettings.Type.HasFlag(BackupType.Scripts);
			switch (Project.ARChiveSettings.Frequency)
			{
				case BackupFrequency.Run: radioButtonRun.Checked = true; break;
				case BackupFrequency.Debug: radioButtonDebug.Checked = true; break;
				case BackupFrequency.Save: radioButtonSave.Checked = true; break;
				case BackupFrequency.Timed: radioButtonInterval.Checked = true; break;
				default: radioButtonNone.Checked = true; break;
			}
			numericInterval.Enabled = radioButtonInterval.Checked;
			SetDirectory();
		}


		private void SetDirectory()
		{
			fileSystemWatcher.Path = Project.BackupDirectory;
			RefreshARChiveList();
		}

		private void RefreshARChiveList()
		{
			listViewARChives.Items.Clear();
			_archives = Directory.GetFiles(Project.BackupDirectory, "*.7z");
			listViewARChives.BeginUpdate();
			foreach (string filename in _archives)
			{
				FileInfo info = new FileInfo(filename);
				string[] columns = 
				{ 
					info.CreationTime.ToString(),
					(info.Length / 1000).ToString(),
					Path.GetFileNameWithoutExtension(filename)
				};
				listViewARChives.Items.Add(new ListViewItem(columns) { ImageIndex = 0, Tag = filename });
			}
			listViewARChives.EndUpdate();
		}

		private void listViewARChives_SelectedIndexChanged(object sender, EventArgs e)
		{
			bool enable = listViewARChives.SelectedItems.Count > 0;
			buttonRemove.Enabled = enable;
			buttonRestore.Enabled = enable;
		}

		private void fileSystemWatcher_AnyChange(object sender, FileSystemEventArgs e)
		{
			RefreshARChiveList();
		}

		#region ARChive Buttons

		private void buttonRemove_Click(object sender, EventArgs e)
		{
			var indices = listViewARChives.SelectedIndices;
			if (indices.Count > 0)
			{
				string file = listViewARChives.SelectedItems[0].Tag.ToString();
				listViewARChives.SelectedItems[0].Selected = false;
				try { File.Delete(file); }
				catch (IOException)
				{
					MessageBox.Show("Failed to delete ARChive.\nFile is locked by another process.",
						"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
				}
			}
			buttonRemove.Enabled = listViewARChives.SelectedItems.Count > 0;
		}

		private void buttonCreateNew_Click(object sender, EventArgs e)
		{
			if (Project.NeedSaved)
			{
				var result = MessageBox.Show("The project contains unsaved changes.\nSave before archiving?", 
					"Confirm", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Question);
				if (result == DialogResult.OK)
					Project.Save();
				else if (result == DialogResult.Cancel)
					return;
			}
			buttonCreateNew.Enabled = false;
			CreateARChive(GetBackupType());
		}

		private void buttonRestore_Click(object sender, EventArgs e)
		{
			string file = listViewARChives.SelectedItems[0].Tag.ToString();
			using (FolderBrowserDialog dialog = new FolderBrowserDialog())
			{
				dialog.Description = "Select folder for ARChive extraction.";
				dialog.ShowNewFolderButton = true;
				dialog.SelectedPath = Project.ProjectFolder;
				if (dialog.ShowDialog() == DialogResult.OK)
					Compressor.ExtractArchive(file, dialog.SelectedPath);
			}
		}

		#endregion

		#region Setting Controls

		private void checkBoxTypeAll_CheckedChanged(object sender, EventArgs e)
		{
			if (checkBoxTypeAllData.Checked)
			{
				checkBoxTypeMaps.Checked = true;
				checkBoxTypeScripts.Checked = true;
			}
		}

		private void checkBoxType_CheckChanged(object sender, EventArgs e)
		{
			bool enable = (sender as CheckBox).Checked;
			if (!enable)
				checkBoxTypeAllData.Checked = false;
			Project.ARChiveSettings.Type = GetBackupType();
		}

		private BackupType GetBackupType()
		{
			BackupType type = BackupType.None;
			if (checkBoxTypeAllData.Checked) type |= BackupType.AllData;
			else
			{
				if (checkBoxTypeMaps.Checked) type |= BackupType.Maps;
				if (checkBoxTypeScripts.Checked) type |= BackupType.Scripts;
			}
			return type;
		}

		private void groupBoxSettings_CollapseBoxClickedEvent(object sender)
		{
			int y = groupBoxSettings.FullHeight - groupBoxSettings.CollapsedHeight;
			if (groupBoxSettings.IsCollapsed)
				y *= -1;
			splitContainer2.Location = new Point(splitContainer2.Location.X, splitContainer2.Location.Y + y);
			splitContainer2.Size = new Size(splitContainer2.Size.Width, splitContainer2.Size.Height - y);
		}

		#endregion

		private void CreateARChive(BackupType type)
		{
			if (compressor == null)
			{
				SevenZipBase.SetLibraryPath(PathHelper.SevenZip_Library);
				compressor = new SevenZipCompressor(Path.GetTempPath());
				compressor.ArchiveFormat = OutArchiveFormat.SevenZip;
				compressor.CompressionLevel = CompressionLevel.Ultra;
				compressor.CompressionMethod = CompressionMethod.Lzma2;
				compressor.CompressionMode = CompressionMode.Create;
				compressor.EventSynchronization = EventSynchronizationStrategy.AlwaysAsynchronous;
				compressor.Compressing += new EventHandler<ProgressEventArgs>(compressor_Compressing);
				compressor.CompressionFinished += new EventHandler<EventArgs>(compressor_CompressionFinished);
			}
			List<string> paths = new List<string>();
			_archiveName = Path.Combine(Project.BackupDirectory, String.Format("{0}.7z", Guid.NewGuid()));
			if (type.HasFlag(BackupType.AllData))
				paths.Add(Path.Combine(Project.ProjectFolder, Project.DataDirectory));
			else
			{
				if (type.HasFlag(BackupType.Scripts))
					paths.Add(Path.Combine(Project.ProjectFolder, Project.ScriptsDirectory));
				if (type.HasFlag(BackupType.Maps))
				{
					DirectoryInfo info = new DirectoryInfo(Project.DataDirectory);
					foreach (FileInfo file in info.GetFiles("*Map*.arc"))
						paths.Add(Path.Combine(Project.ProjectFolder, file.FullName));
				}	
			}
			if (paths.Count == 0)
				compressor_CompressionFinished(null, null);
			else
				AddToArchive(_archiveName, paths);
			Console.WriteLine(String.Join(",\n", paths));
		}

		private void AddToArchive(string archiveName, IEnumerable<string> paths)
		{
			Editor.ProgressBar.Value = 0;
			Editor.ProgressBar.Maximum = 100;
			Editor.ProgressBar.Visible = true;
			foreach (string path in paths)
			{
				compressor.CompressionMode = File.Exists(archiveName) ?
					CompressionMode.Append : CompressionMode.Create;
				if (Project.ARChiveSettings.Threaded)
				{
					if (Directory.Exists(path))
						new Thread(lamda => compressor.CompressDirectory(path, _archiveName)).Start();
					else if (File.Exists(path))
						new Thread(lamda => compressor.CompressFiles(_archiveName, path)).Start();
				}
				else
				{
					if (Directory.Exists(path))
						compressor.CompressDirectory(path, _archiveName);
					else if (File.Exists(path))
						compressor.CompressFiles(_archiveName, path);
				}
			}
		}

		private void EnableCreateButton(bool enable) { buttonCreateNew.Enabled = enable; }

		private void ShowProgressBar(bool hide) { Editor.ProgressBar.Visible = hide; }

		private void UpdateProgress(int percent) { Editor.ProgressBar.Value = percent; }

		void compressor_CompressionFinished(object sender, EventArgs e)
		{
			if (this.InvokeRequired)
			{
				this.Invoke(new MethodInvoker(delegate() { EnableCreateButton(true); }));
				this.Invoke(new MethodInvoker(delegate() { ShowProgressBar(false); }));
			}
			else
			{
				buttonCreateNew.Enabled = true;
				Editor.ProgressBar.Visible = false;
			}
			Project.ARChiveSettings.TrimExcess();
		}

		private void compressor_Compressing(object sender, ProgressEventArgs e)
		{
			if (this.InvokeRequired)
			{
				this.Invoke(new MethodInvoker(delegate() { EnableCreateButton(false); }));
				this.Invoke(new MethodInvoker(delegate() { UpdateProgress(e.PercentDone); }));
			}
			else
			{
				buttonCreateNew.Enabled = false;
				Editor.ProgressBar.Value = e.PercentDone;
			}
		}

		private void listViewARChives_MouseDown(object sender, MouseEventArgs e)
		{
			if (e.Button == System.Windows.Forms.MouseButtons.Right)
			{
				var item = listViewARChives.GetItemAt(e.X, e.Y);
				if (item != null)
					item.Selected = true;
			}
		}

		private void openFileLocationToolStripMenuItem_Click(object sender, EventArgs e)
		{
			Process.Start(Project.BackupDirectory);
		}

		private void shellOpenToolStripMenuItem_Click(object sender, EventArgs e)
		{
			string filename = listViewARChives.SelectedItems[0].Tag.ToString();
			if (File.Exists(filename))
				Process.Start(filename);
		}

		private void contextMenuStrip_Opened(object sender, EventArgs e)
		{
			contextMenuStrip.Enabled = listViewARChives.SelectedItems.Count > 0;
		}

		private void listViewARChives_DoubleClick(object sender, EventArgs e)
		{
			if (listViewARChives.SelectedItems.Count > 0)
				buttonRestore_Click(null, null);
		}

		private void radioButtonFrequency_Click(object sender, EventArgs e)
		{
			numericInterval.Enabled = radioButtonInterval.Checked;
			bool enable = !radioButtonNone.Checked;
			groupBoxType.Enabled = enable;
			numericMaxBackups.Enabled = enable;
			checkBoxThreaded.Enabled = enable;
			BackupFrequency frequency;
			if (radioButtonRun.Checked) frequency = BackupFrequency.Run;
			else if (radioButtonDebug.Checked) frequency = BackupFrequency.Debug;
			else if (radioButtonSave.Checked) frequency = BackupFrequency.Save;
			else if (radioButtonInterval.Checked) frequency = BackupFrequency.Timed;
			else frequency = BackupFrequency.None;
			Project.ARChiveSettings.Frequency = frequency;
		}
	}
}
