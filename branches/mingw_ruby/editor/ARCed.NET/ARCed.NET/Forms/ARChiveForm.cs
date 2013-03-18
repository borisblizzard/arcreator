#region Using Directives

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Threading;
using System.Windows.Forms;
using ARCed.Helpers;
using ARCed.Properties;
using ARCed.Settings;
using ARCed.UI;
using SevenZip;

#endregion

namespace ARCed.Forms
{
	public partial class ARChiveForm : DockContent
	{
		private string[] _archives;
		private string _archiveName;
		private SevenZipCompressor compressor;

		public ARChiveForm()
		{
			this.InitializeComponent();
			Icon = Icon.FromHandle(Resources.SevenZip.GetHicon());
			this.numericMaxBackups.DataBindings.Add("Value", Project.ARChiveSettings, 
				"MaxBackups", false, DataSourceUpdateMode.OnPropertyChanged);
			this.numericInterval.DataBindings.Add("Value", Project.ARChiveSettings,
				"Interval", false, DataSourceUpdateMode.OnPropertyChanged);
			this.checkBoxThreaded.DataBindings.Add("Checked", Project.ARChiveSettings,
				"Threaded", false, DataSourceUpdateMode.OnPropertyChanged);
			this.RefreshSettings();
		}

		public void RefreshSettings()
		{
			this.checkBoxTypeAllData.Checked = Project.ARChiveSettings.Type.HasFlag(BackupType.AllData);
			this.checkBoxTypeMaps.Checked = Project.ARChiveSettings.Type.HasFlag(BackupType.Maps);
			this.checkBoxTypeScripts.Checked = Project.ARChiveSettings.Type.HasFlag(BackupType.Scripts);
			switch (Project.ARChiveSettings.Frequency)
			{
				case BackupFrequency.Run: this.radioButtonRun.Checked = true; break;
				case BackupFrequency.Debug: this.radioButtonDebug.Checked = true; break;
				case BackupFrequency.Save: this.radioButtonSave.Checked = true; break;
				case BackupFrequency.Timed: this.radioButtonInterval.Checked = true; break;
				default: this.radioButtonNone.Checked = true; break;
			}
			this.numericInterval.Enabled = this.radioButtonInterval.Checked;
			this.SetDirectory();
		}


		private void SetDirectory()
		{
			this.fileSystemWatcher.Path = Project.BackupDirectory;
			this.RefreshARChiveList();
		}

		private void RefreshARChiveList()
		{
			this.listViewARChives.Items.Clear();
			this._archives = Directory.GetFiles(Project.BackupDirectory, "*.7z");
			this.listViewARChives.BeginUpdate();
			foreach (string filename in this._archives)
			{
				var info = new FileInfo(filename);
				string[] columns = 
				{ 
					info.CreationTime.ToString(),
					(info.Length / 1000).ToString(),
					Path.GetFileNameWithoutExtension(filename)
				};
				this.listViewARChives.Items.Add(new ListViewItem(columns) { ImageIndex = 0, Tag = filename });
			}
			this.listViewARChives.EndUpdate();
		}

		private void listViewARChives_SelectedIndexChanged(object sender, EventArgs e)
		{
			bool enable = this.listViewARChives.SelectedItems.Count > 0;
			this.buttonRemove.Enabled = enable;
			this.buttonRestore.Enabled = enable;
		}

		private void fileSystemWatcher_AnyChange(object sender, FileSystemEventArgs e)
		{
			this.RefreshARChiveList();
		}

		#region ARChive Buttons

		private void buttonRemove_Click(object sender, EventArgs e)
		{
			var indices = this.listViewARChives.SelectedIndices;
			if (indices.Count > 0)
			{
				string file = this.listViewARChives.SelectedItems[0].Tag.ToString();
				this.listViewARChives.SelectedItems[0].Selected = false;
				try { File.Delete(file); }
				catch (IOException)
				{
					MessageBox.Show("Failed to delete ARChive.\nFile is locked by another process.",
						"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
				}
			}
			this.buttonRemove.Enabled = this.listViewARChives.SelectedItems.Count > 0;
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
			this.buttonCreateNew.Enabled = false;
			this.CreateARChive(this.GetBackupType());
		}

		private void buttonRestore_Click(object sender, EventArgs e)
		{
			string file = this.listViewARChives.SelectedItems[0].Tag.ToString();
			using (var dialog = new FolderBrowserDialog())
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
			if (this.checkBoxTypeAllData.Checked)
			{
				this.checkBoxTypeMaps.Checked = true;
				this.checkBoxTypeScripts.Checked = true;
			}
		}

		private void checkBoxType_CheckChanged(object sender, EventArgs e)
		{
			bool enable = (sender as CheckBox).Checked;
			if (!enable)
				this.checkBoxTypeAllData.Checked = false;
			Project.ARChiveSettings.Type = this.GetBackupType();
		}

		private BackupType GetBackupType()
		{
			var type = BackupType.None;
			if (this.checkBoxTypeAllData.Checked) type |= BackupType.AllData;
			else
			{
				if (this.checkBoxTypeMaps.Checked) type |= BackupType.Maps;
				if (this.checkBoxTypeScripts.Checked) type |= BackupType.Scripts;
			}
			return type;
		}

		private void groupBoxSettings_CollapseBoxClickedEvent(object sender)
		{
			int y = this.groupBoxSettings.FullHeight - this.groupBoxSettings.CollapsedHeight;
			if (this.groupBoxSettings.IsCollapsed)
				y *= -1;
			this.splitContainer2.Location = new Point(this.splitContainer2.Location.X, this.splitContainer2.Location.Y + y);
			this.splitContainer2.Size = new Size(this.splitContainer2.Size.Width, this.splitContainer2.Size.Height - y);
		}

		#endregion

		private void CreateARChive(BackupType type)
		{
			if (this.compressor == null)
			{
				SevenZipBase.SetLibraryPath(PathHelper.SevenZipLibrary);
				this.compressor = new SevenZipCompressor(Path.GetTempPath())
				{
				    ArchiveFormat = OutArchiveFormat.SevenZip,
				    CompressionLevel = CompressionLevel.Ultra,
				    CompressionMethod = CompressionMethod.Lzma2,
				    CompressionMode = CompressionMode.Create,
				    EventSynchronization = EventSynchronizationStrategy.AlwaysAsynchronous
				};
			    this.compressor.Compressing += this.compressor_Compressing;
				this.compressor.CompressionFinished += this.compressor_CompressionFinished;
			}
			var paths = new List<string>();
			this._archiveName = Path.Combine(Project.BackupDirectory, String.Format("{0}.7z", Guid.NewGuid()));
			if (type.HasFlag(BackupType.AllData))
				paths.Add(Path.Combine(Project.ProjectFolder, Project.DataDirectory));
			else
			{
				if (type.HasFlag(BackupType.Scripts))
					paths.Add(Path.Combine(Project.ProjectFolder, Project.ScriptsDirectory));
				if (type.HasFlag(BackupType.Maps))
				{
				    var info = new DirectoryInfo(Project.DataDirectory);
				    paths.AddRange(info.GetFiles("*Map*.arc").Select(file => 
                        Path.Combine(Project.ProjectFolder, file.FullName)));
				}
			}
			if (paths.Count == 0)
				this.compressor_CompressionFinished(null, null);
			else
				this.AddToArchive(this._archiveName, paths);
			Console.WriteLine(String.Join(",\n", paths));
		}

		private void AddToArchive(string archiveName, IEnumerable<string> paths)
		{
			foreach (string path in paths)
			{
				this.compressor.CompressionMode = File.Exists(archiveName) ?
					CompressionMode.Append : CompressionMode.Create;
				if (Project.ARChiveSettings.Threaded)
				{
					if (Directory.Exists(path))
						new Thread(lamda => this.compressor.CompressDirectory(path, this._archiveName)).Start();
					else if (File.Exists(path))
						new Thread(lamda => this.compressor.CompressFiles(this._archiveName, path)).Start();
				}
				else
				{
					if (Directory.Exists(path))
						this.compressor.CompressDirectory(path, this._archiveName);
					else if (File.Exists(path))
						this.compressor.CompressFiles(this._archiveName, path);
				}
			}
		}

		private void EnableCreateButton(bool enable) { this.buttonCreateNew.Enabled = enable; }

		void compressor_CompressionFinished(object sender, EventArgs e)
		{
			if (InvokeRequired)
			{
				Invoke(new MethodInvoker(() => this.EnableCreateButton(true)));
			}
			else
			{
				this.buttonCreateNew.Enabled = true;
			}
            Project.CleanARChives();
		}

		private void compressor_Compressing(object sender, ProgressEventArgs e)
		{
			if (InvokeRequired)
			{
				Invoke(new MethodInvoker(() => this.EnableCreateButton(false)));
			}
			else
			{
				this.buttonCreateNew.Enabled = false;
			}
		}

		private void listViewARChives_MouseDown(object sender, MouseEventArgs e)
		{
			if (e.Button == MouseButtons.Right)
			{
				var item = this.listViewARChives.GetItemAt(e.X, e.Y);
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
			string filename = this.listViewARChives.SelectedItems[0].Tag.ToString();
			if (File.Exists(filename))
				Process.Start(filename);
		}

		private void contextMenuStrip_Opened(object sender, EventArgs e)
		{
			this.contextMenuStrip.Enabled = this.listViewARChives.SelectedItems.Count > 0;
		}

		private void listViewARChives_DoubleClick(object sender, EventArgs e)
		{
			if (this.listViewARChives.SelectedItems.Count > 0)
				this.buttonRestore_Click(null, null);
		}

		private void radioButtonFrequency_Click(object sender, EventArgs e)
		{
			this.numericInterval.Enabled = this.radioButtonInterval.Checked;
			bool enable = !this.radioButtonNone.Checked;
			this.groupBoxType.Enabled = enable;
			this.numericMaxBackups.Enabled = enable;
			this.checkBoxThreaded.Enabled = enable;
			BackupFrequency frequency;
			if (this.radioButtonRun.Checked) frequency = BackupFrequency.Run;
			else if (this.radioButtonDebug.Checked) frequency = BackupFrequency.Debug;
			else if (this.radioButtonSave.Checked) frequency = BackupFrequency.Save;
			else if (this.radioButtonInterval.Checked) frequency = BackupFrequency.Timed;
			else frequency = BackupFrequency.None;
			Project.ARChiveSettings.Frequency = frequency;
		}
	}
}
