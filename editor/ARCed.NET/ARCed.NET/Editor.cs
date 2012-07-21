#region Using Directives

using System;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Core.Win32;
using ARCed.Database;
using ARCed.Database.Actors;
using ARCed.Database.Animations;
using ARCed.Database.Armors;
using ARCed.Database.Classes;
using ARCed.Database.CommonEvents;
using ARCed.Database.Enemies;
using ARCed.Database.Items;
using ARCed.Database.Skills;
using ARCed.Database.States;
using ARCed.Database.Sys;
using ARCed.Database.Tilesets;
using ARCed.Database.Troops;
using ARCed.Database.Weapons;
using ARCed.Dialogs;
using ARCed.Forms;
using ARCed.Forms.Splash;
using ARCed.Helpers;
using ARCed.Plugins;
using ARCed.Scintilla;
using ARCed.Scripting;
using ARCed.Settings;
using ARCed.UI;

#endregion

namespace ARCed
{
	public partial class Editor : Form, IPluginHost
	{
		/// <summary>
		/// Possible editor modes
		/// </summary>
		[Flags]
		public enum EditorMode
		{
			/// <summary>
			/// Normal mode without debugging or logging
			/// </summary>
			Normal,
			/// <summary>
			/// Debug mode with output console attached
			/// </summary>
			Debug,
			/// <summary>
			/// Generates log file of various events and errors
			/// </summary>
			Logging
		}

		#region Private Fields

		private readonly DeserializeDockContent _deserializeDockContent;

		#endregion

		#region Properties

		public DockPanel DockPanel { get { return this.dockMain; } }

		#endregion

		#region Constructor

		/// <summary>
		/// Constructs a new Editor, automatically opening a a project if filename is given
		/// </summary>
		/// <param name="filename"></param>
		public Editor(string filename = null)
        {
            //******************************************************************************
            #if DEBUG
                // This will automatically remove editor settings on startup, since during development
                // they have been changing and can be corrupted, preventing a proper run. Final version
                // will remove old settings and create new in event of corrupted data due to user edit.
                string editorSetting = PathHelper.EditorSettings;
                if (File.Exists(editorSetting))
                    File.Delete(editorSetting);
            #endif
            //*******************************************************************************
            ResourceHelper.Initialize();
            FontHelper.LoadUserFonts();
            LoadSettings();
            //Log.AppendFormat("ARCed Log File: {0}\n\n", DateTime.Now);
            // Create editor form and set the icon to match the executable
            this.InitializeComponent();
            MainInstance = this;
            Registry.Host = this;
            ///////////////////////////////
            MainDock = this.dockMain;
            TilesetXnaPanel.Settings = Settings.ImageColorSettings;
            //////////////////////////////
            FindReplace.ParentDock = this.dockMain;
            StatusBar = this.statusStripMain;
            Windows.ScriptTabContextMenu = this.contextMenuScriptTab;
            this.dockMain.Skin = Settings.WindowSkin;

            Icon = Icon.ExtractAssociatedIcon(PathHelper.EditorPath);
            if (Mode.HasFlag(EditorMode.Debug))
                new Thread(lamda => NativeMethods.SetConsoleIcon(Icon.Handle)).Start();

            // Show the splash screen
            if (Settings.ShowSplash)
            {
                Hide();
                var splashthread = new Thread(SplashScreen.ShowSplashScreen)
                {
                    IsBackground = true
                };
                splashthread.Start();
                this.StartSplash(filename);
            }
            else
            {
                this.RestoreWindowLocation();
                if (File.Exists(filename) && Path.GetExtension(filename) == ".arcproj")
                    this.LoadProject(filename);
            }
            Registry.LoadAll();
            // Set deserializer for restoring window layout.
            this._deserializeDockContent = GetContentFromPersistString;

            Project.Settings = new ProjectSettings();

            // TEST /////////////////////////////////////////////////////////////////////////////////////

            string testPath = Path.Combine(PathHelper.EditorDirectory,
                @"Chronicles of Sir Lag-A-Lot\Chronicles of Sir Lag-A-Lot.arcproj");
            if (File.Exists(testPath))
                this.LoadProject(testPath);

            Console.WriteLine(File.Exists(testPath));
			new StateMainForm().Show(MainDock);
            new AnimationMainForm().Show(MainDock);
            new TilesetsMainForm().Show(MainDock);
            //new Database.Troops.TroopMainForm().Show(Editor.MainDock);

            // TEST /////////////////////////////////////////////////////////////////////////////////////

            // Suspend child controls from resizing every pixel
            ResizeBegin += (s, e) => SuspendLayout();
            ResizeEnd += (s, e) => ResumeLayout(true);

        }

		/// <summary>
		/// Restores the window size, state, and location it was in from the last save
		/// </summary>
		private void RestoreWindowLocation()
		{
			if (Settings.WindowState.HasFlag(FormWindowState.Maximized))
				WindowState = FormWindowState.Maximized;
			else
			{
				Size = Settings.Size;
				Location = Settings.Location;
			}
		}

		/// <summary>
		/// Creates a window from a string representation of the original and returns it
		/// </summary>
		/// <param name="persistString">The string representation of the window</param>
		/// <returns>The created window</returns>
		/// <remarks>It is important that any plug-in have a parameterless constructor, else
		/// it will fail to load from a saved layout.</remarks>
		private static IDockContent GetContentFromPersistString(string persistString)
		{
			if (persistString == typeof(ScriptEditorForm).ToString())
			{
				if (Project.Settings.OpenScripts.Count > 0)
				{
					string file = Project.Settings.OpenScripts[0];
					Project.Settings.OpenScripts.RemoveAt(0);
					return OpenScript(file);
				}
				return null;
			}
			if (persistString == typeof(FindReplaceDialog).ToString())
				return Windows.ScintillaFindReplace;
			if (persistString == typeof(ScriptStyleForm).ToString())
				return Windows.ScriptStyleMenu;
			if (persistString == typeof(ScriptMenuForm).ToString())
				return Windows.ScriptMenu;
			if (persistString == typeof(ARChiveForm).ToString())
				return Windows.ARChiveForm;
			if (persistString == typeof(EditorOptionsForm).ToString())
				return Windows.EditorOptionsMenu;
			if (persistString == typeof(SkinSettingsForm).ToString())
				return Windows.SkinSettingForm;
			if (persistString == typeof(AutoCompleteForm).ToString())
				return Windows.AutoCompleteWindow;

			// Attempt to create windows not defined, searching plug-in assemblies
			try
			{
				Type type = null;
				foreach (var assembly in ARCedAssemblies)
				{
					type = assembly.GetType(persistString);
					if (type != null)
						break;
				}
				return (IDockContent)Activator.CreateInstance(type);
			}
			catch { return null; }
		}

		#endregion

		#region Forms Screen

		private void StartSplash(string filename)
		{
			Project.NeedSaved = false;
			if (Settings.ShowSplash)
			{
				SplashScreen.UdpateStatusText("Initializing Ruby engine...");
				Thread.Sleep(500);
				this.RestoreWindowLocation();
				if (File.Exists(filename) && Path.GetExtension(filename) == ".arcproj")
				{
					this.LoadProject(filename);
					SplashScreen.UdpateStatusText("Opening project...");
					Thread.Sleep(500);
				}
				SplashScreen.UdpateStatusText("Restoring layout...");
				Thread.Sleep(500);
				Show();
				SplashScreen.CloseSplashScreen();
				Activate();
			}
		}

		#endregion

		/// <summary>
		/// Loads the settings of the editor or initializes new ones if not found.
		/// </summary>
		private static void LoadSettings()
		{
			Settings = EditorSettings.Load();
		}
	
		/// <summary>
		/// Loads the project file at the given path.
		/// </summary>
		/// <param name="path">Full path to the project file</param>
		private void LoadProject(string path)
		{
            Console.WriteLine(path);
			if (Project.IsLoaded)
				Project.Close();
			Project.NeedSaved = false;
            Cursor = Cursors.WaitCursor;
			Project.Load(path);
            Cursor = Cursors.Default;
			//try
			//{
				
				if (File.Exists(Project.LayoutSettings))
					this.dockMain.LoadFromXml(Project.LayoutSettings, this._deserializeDockContent);
				Windows.ScriptMenu.ScriptsDirectory = Project.ScriptsDirectory;
				Windows.ARChiveForm.RefreshSettings();
				Text = Project.Title;
				Settings.AddToRecent(path);
			//}
			//catch
			//{
				//CloseProject();
				//MessageBox.Show("Error loading project.", 
					//"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
			//}
		}

		/// <summary>
		/// Closes the project and resets the Editor back to default
		/// </summary>
		private void CloseProject()
		{
			var contents = this.dockMain.Contents;
			for (int i = 0; i < contents.Count; i++)
				this.dockMain.RemoveContent(contents[i]);
			Project.Close();
			Text = @"ARCed.NET";
			Windows.DisposeAll();
		}

		private void SaveProject()
		{
			try
			{
				Project.Save();
				Project.ScriptManager.SaveAll();
				this.dockMain.SaveAsXml(Project.LayoutSettings, Encoding.UTF8);
				Project.NeedSaved = false;
			}
			catch
			{

			}
		}
		
		/// <summary>
		/// Asks confirmation before continuing if there are unsaved changes to the project.
		/// </summary>
		/// <returns>Flag if it is OK to continue</returns>
		private bool ConfirmProjectClose()
		{
			if (!Project.NeedSaved)
				return true;
			DialogResult result = MessageBox.Show(String.Format("Save changes to {0}?", Project.Title), 
				@"Advanced RPG Creator", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Exclamation);
			switch (result)
			{
			    case DialogResult.Yes:
			        this.SaveProject();
			        return true;
			    case DialogResult.No:
			        return true;
			    default:
			        return false;
			}
		}

		private void EditorFormClosing(object sender, FormClosingEventArgs e)
		{
			Settings.Location = Location;
			Settings.Size = Size;
			Settings.WindowState = WindowState;
			Settings.Save();
			Properties.Settings.Default.Save();
		}

		private void ButtonOpenGameDirectoryClick(object sender, EventArgs e)
		{
			var toolStripMenuItem = sender as ToolStripMenuItem;
			if (toolStripMenuItem == null) return;
			var tag = toolStripMenuItem.Tag.ToString();
			string dir;
			switch (tag)
			{
				case "Game": dir = Project.ProjectFolder; break;
				case "Graphics": dir = Project.GraphicsDirectory; break;
				case "Audio": dir = Project.AudioDirectory; break;
				case "Data": dir = Project.DataDirectory; break;
				case "Scripts": dir = Project.ScriptsDirectory; break;
				case "Templates": dir = PathHelper.TemplateDirectory; break;
				case "TemplatesProjects": dir = PathHelper.ProjectTemplateDirectory; break;
				case "TemplatesScripts": dir = PathHelper.ScriptTemplateDirectory; break;
				case "Plugins": dir = PathHelper.PluginDirectory; break;
				case "Settings": dir = PathHelper.SettingsDirectory; break;
				default: dir = PathHelper.EditorDirectory; break;
			}
			Process.Start(dir + @"\");
		}

		private void StyleManagerToolStripMenuItemClick(object sender, EventArgs e)
		{
			if (Windows.ScriptStyleMenu.IsHidden)
				Windows.ScriptStyleMenu.Show(this.dockMain);
			Windows.ScriptStyleMenu.Show();
		}

		private void BackupUtilityToolStripMenuItemClick(object sender, EventArgs e)
		{
			Windows.ARChiveForm.RefreshSettings();
			Show(Windows.ARChiveForm);
		}

		private void ToolMenuScriptManagerClick(object sender, EventArgs e)
		{
			Show(Windows.ScriptMenu);
		}

		private void ToolMenuEditorOptionsClick(object sender, EventArgs e)
		{
			Show(Windows.EditorOptionsMenu);
		}

		#region Menu Strip: File

		/// <summary>
		/// Invoked when "File" drop-down is opening on menu strip, 
		/// enabling/disabling specific options as needed.
		/// </summary>
		private void MenuItemFileDropDownOpening(object sender, EventArgs e)
		{
			bool enable = Project.IsLoaded;
			this.fileMenuSaveProject.Enabled = enable;
			this.fileMenuSaveTemplate.Enabled = enable;
			this.fileMenuCloseProject.Enabled = enable;
			this.fileMenuOpenRecent.DropDownItems.Clear();
			foreach (string filename in Settings.RecentlyOpened)
			{
				// TODO: Implement custom game icon to tool item?
				var item = new ToolStripMenuItem(Path.GetFileNameWithoutExtension(filename));
				item.Click += this.OpenRecentFileClick;
				item.ToolTipText = filename;
				this.fileMenuOpenRecent.DropDownItems.Add(item);
			}
			//
		}

		private void OpenRecentFileClick(object sender, EventArgs e)
		{
			var toolStripMenuItem = sender as ToolStripMenuItem;
			if (toolStripMenuItem == null) return;
			var filename = toolStripMenuItem.ToolTipText;
			if (File.Exists(filename))
				this.LoadProject(filename);
			else
			{
				MessageBox.Show("Project cannot be found.", 
				                "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
				Settings.RecentlyOpened.Remove(filename);
			}
		}

		/// <summary>
		/// Menu: File -> New Project...
		/// </summary>
		private void FileMenuNewProjectClicked(object sender, EventArgs e)
		{
			if (this.ConfirmProjectClose())
			{
				using (var dialog = new NewProjectForm())
				{
					if (dialog.ShowDialog() == DialogResult.OK)
					{
						string template;
						string dir = dialog.ProjectDirectory;
						if (dialog.ProjectTemplate == "Default")
						{
							template = Path.GetTempFileName();
							Util.ExtractResource("ARCed.Files.Default.7z", template);
						}
						else
							template = Path.Combine(PathHelper.ProjectTemplateDirectory,
								String.Format("{0}.7z", dialog.ProjectTemplate));
                        string lib = Is64bit ?
                            Path.Combine(PathHelper.EditorDirectory, @"x64\7z64.dll") :
                            Path.Combine(PathHelper.EditorDirectory, @"x86\7z.dll");
						string proj = Project.CreateProject(lib, dir, dialog.ProjectTitle, template);
						this.LoadProject(proj);
					}
				}
			}
		}

		/// <summary>
		/// Menu: File -> Open Project...
		/// </summary>
		private void FileMenuOpenProjectClick(object sender, EventArgs e)
		{
			if (this.ConfirmProjectClose())
			{
				using (var loadDialog = new OpenFileDialog())
				{
					loadDialog.DefaultExt = "";
					loadDialog.Filter = @"ARC Project File|*.arcproj|All Documents|*.*";
					loadDialog.InitialDirectory = PathHelper.DefaultSaveDirectory;
					loadDialog.Title = "Open ARC Project...";
					if (loadDialog.ShowDialog() == DialogResult.OK)
					{
						if (Project.IsLoaded && !this.ConfirmProjectClose())
							return;
						this.CloseProject();
						this.LoadProject(loadDialog.FileName);
					}
				}
			}
		}

		/// <summary>
		/// Menu: File -> Close Project
		/// </summary>
		private void FileMenuCloseProjectClick(object sender, EventArgs e)
		{
			if (this.ConfirmProjectClose())
				this.CloseProject();
		}

		/// <summary>
		/// Menu: File -> Save Project
		/// </summary>
		private void FileMenuSaveProjectClick(object sender, EventArgs e)
		{
			this.SaveProject();
		}

		/// <summary>
		/// Menu: File -> Save As Template...
		/// </summary>
		private void FileMenuSaveTemplateClick(object sender, EventArgs e)
		{
			const string title = "Save Project Template";
			const string label = "Template Name:";
			string text = Project.Title;
			using (var dialog = new UserStringForm(title, text, label, true))
			{
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					string path = Path.Combine(PathHelper.ProjectTemplateDirectory,
						String.Format("{0}.7z", dialog.UserString));
					if (File.Exists(path))
					{
						string msg = String.Format("\"{0}\" already exists.\nOverwrite?", dialog.UserString);
						var result = MessageBox.Show(msg, 
							"Confirm Overwrite", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);
						if (result != DialogResult.Yes)
							return;
					}
					new Thread(lamda =>
						Compressor.CompressDirectory(Project.ProjectFolder, path, true)).Start();
				}
			}
		}

		/// <summary>
		/// Menu: File -> Exit
		/// </summary>
		private void FileMenuExitClick(object sender, EventArgs e)
		{
			if (this.ConfirmProjectClose())
				Close();
		}

		#endregion

		#region Menu Strip: Edit

		/// <summary>
		/// Invoked when the "Tools" drop-down is opening on menu strip, 
		/// enabling/disabling specific options as needed.
		/// </summary>
		private void MenuStripEditDropDownOpening(object sender, EventArgs e)
		{
			bool enable = Project.IsLoaded;
			// TODO: Enable/disable items as needed.
		}

		#endregion

		#region Menu Strip: Tools

		private void MenuStripToolsDropDownOpening(object sender, EventArgs e)
		{
			bool enable = Project.IsLoaded;
			this.toolMenuARChiveUtility.Enabled = enable;
			this.toolMenuDatabaseManager.Enabled = enable;
			this.toolMenuPlugins.Enabled = enable;
			this.toolMenuScriptManager.Enabled = enable;
			this.toolMenuSkinManager.Enabled = enable;

			// Add plugins to dropdown
			this.toolMenuPlugins.DropDownItems.Clear();
			foreach (RegistryEntry entry in Registry.Entries)
			{
				var extractAssociatedIcon = Icon.ExtractAssociatedIcon(entry.Plugin.Filename);
				if (extractAssociatedIcon == null) continue;
				var item = new ToolStripMenuItem(entry.Name)
				{
					Image = extractAssociatedIcon.ToBitmap(),
					ToolTipText = entry.Description,
					Tag = entry
				};
				item.Click += MenuStripPluginsClicked;
				this.toolMenuPlugins.DropDownItems.Add(item);
			}
		}

		private static void MenuStripPluginsClicked(object sender, EventArgs e)
		{
			var toolStripMenuItem = sender as ToolStripMenuItem;
			if (toolStripMenuItem != null)
			{
				var registryEntry = toolStripMenuItem.Tag as RegistryEntry;
				if (registryEntry != null) registryEntry.Show();
			}
		}

		#endregion

		#region Script Context Menu

		private void SaveToolStripMenuItemClick(object sender, EventArgs e)
		{
			var scriptEditorForm = MainDock.ActivePane.ActiveContent as ScriptEditorForm;
			if (scriptEditorForm != null)
				scriptEditorForm.Script.Save();
		}

		private void CloseToolStripMenuItemClick(object sender, EventArgs e)
		{
			MainDock.ActivePane.CloseActiveContent();
		}

		private void CloseAllButThisToolStripMenuItemClick(object sender, EventArgs e)
		{
			var keepForm = this.dockMain.ActiveDocumentPane.ActiveContent;
			if (this.dockMain.DocumentStyle == DocumentStyle.SystemMdi)
			{
				foreach (Form form in MdiChildren)
					if (form != keepForm)
						form.Close();
			}
			else
			{
                IDockContent[] documents = this.dockMain.DocumentsToArray();
				foreach (IDockContent content in documents)
					if (content != keepForm)
						content.DockHandler.Close();
			}
		}

		private void FloatToolStripMenuItemClick(object sender, EventArgs e)
		{
			var size = new Size(720, 512);
			Rectangle screenRect = Screen.FromControl(this).Bounds;
			var point = new Point((screenRect.Width - 720) / 2, (screenRect.Height - 512) / 2);
			MainDock.ActivePane.ActiveContent.DockHandler.FloatAt(new Rectangle(point, size));
		}

		#endregion

		private void ToolMenuSkinManagerClick(object sender, EventArgs e)
		{
			Show(Windows.SkinSettingForm);
		}

		private void ToolScriptMenuAutoCompleteClick(object sender, EventArgs e)
		{
			Show(Windows.AutoCompleteWindow);
		}

		private void HelpMenuAboutClick(object sender, EventArgs e)
		{
			using (var aboutDialog = new AboutBox())
				aboutDialog.ShowDialog(this);
		}

		/// <summary>
		/// TEST PURPOSES ONLY
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void ToolComboDatabaseItemClick(object sender, EventArgs e)
		{
			var toolStripMenuItem = sender as ToolStripMenuItem;
			if (toolStripMenuItem == null) return;
			var index = Convert.ToInt32(toolStripMenuItem.Tag);
			DatabaseWindow window = null;
			switch (index)
			{
				case 0: window = Windows.DatabaseForm<ActorMainForm>(); break;
				case 1: window = Windows.DatabaseForm<ClassMainForm>(); break;
				case 2: window = Windows.DatabaseForm<SkillMainForm>(); break;
				case 3: window = Windows.DatabaseForm<ItemMainForm>(); break;
				case 4: window = Windows.DatabaseForm<WeaponMainForm>(); break;
				case 5: window = Windows.DatabaseForm<ArmorMainForm>(); break;
				case 6: window = Windows.DatabaseForm<EnemyMainForm>(); break;
				case 7: window = Windows.DatabaseForm<TroopMainForm>(); break;
				case 8: window = Windows.DatabaseForm<StateMainForm>(); break;
				case 9: window = Windows.DatabaseForm<AnimationMainForm>(); break;
				case 10: window = Windows.DatabaseForm<TilesetsMainForm>(); break;
				case 11: window = Windows.DatabaseForm<CommonEventMainForm>(); break;
				case 12: window = Windows.DatabaseForm<SystemMainForm>(); break;
			}
			if (window != null)
				window.Show(MainDock);
		}
	}
}
