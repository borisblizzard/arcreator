#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Text;
using System.Threading;
using System.Windows.Forms;
using ARCed.Data;
using ARCed.Dialogs;
using ARCed.Forms.Splash;
using ARCed.Helpers;
using ARCed.Plugins;
using ARCed.Scripting;
using ARCed.Settings;
using ARCed.UI;
using System.Diagnostics;
using System.Security.Principal;
using System.Security.Permissions;

#endregion

namespace ARCed
{
	public partial class Editor : Form, IPluginHost
	{
		/// <summary>
		/// Possible editor modes
		/// </summary>
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

		private DeserializeDockContent _deserializeDockContent;

		#endregion

		#region Properties

		public DockPanel DockPanel { get { return dockMain; } }

		#endregion

		#region Constructor

		/// <summary>
		/// Constructs a new Editor, automatically opening a a project if filename is given
		/// </summary>
		/// <param name="filename"></param>
		public Editor(string filename = null)
		{
			ARCed.Helpers.ResourceHelper.Initialize();
			FontHelper.LoadUserFonts();
			LoadSettings();
			//Log.AppendFormat("ARCed Log File: {0}\n\n", DateTime.Now);
			// Create editor form and set the icon to match the executable
			InitializeComponent();
			Editor.MainInstance = this;
			Editor.MainDock = dockMain;
			Editor.StatusBar = this.statusStripMain;
			Editor.ProgressBar = this.toolStripProgressBar;
			Windows.ScriptTabContextMenu = this.contextMenuScriptTab;
			dockMain.Skin = Editor.Settings.WindowSkin;
			try
			{
				this.Icon = Icon.ExtractAssociatedIcon(PathHelper.EditorPath);
				if (Editor.Mode.HasFlag(EditorMode.Debug))
					new Thread(lamda => NativeMethods.SetConsoleIcon(this.Icon.Handle)).Start();
			}
			catch { }
			// Show the splash screen
			if (Editor.Settings.ShowSplash)
			{
				this.Hide();
				Thread splashthread = new Thread(new ThreadStart(SplashScreen.ShowSplashScreen));
				splashthread.IsBackground = true;
				splashthread.Start();
				StartSplash(filename);
			}
			else
			{
				RestoreWindowLocation();
				if (File.Exists(filename) && Path.GetExtension(filename) == ".arcproj")
					LoadProject(filename);
			}



			Registry.LoadAll();
			// Set deserializer for restoring window layout.
			_deserializeDockContent = new DeserializeDockContent(GetContentFromPersistString);

			Project.Settings = new ProjectSettings();

// TEST /////////////////////////////////////////////////////////////////////////////////////

			string testPath = Path.Combine(PathHelper.EditorDirectory, 
				@"Chronicles of Sir Lag-A-Lot\Chronicles of Sir Lag-A-Lot.arcproj");
			if (File.Exists(testPath))
				LoadProject(testPath);
			dockMain.SuspendPainting();
			SuspendLayout();
			new Database.Troops.TroopMainForm().Show(Editor.MainDock);
			dockMain.ResumePainting(true);
			ResumeLayout(true);

// TEST /////////////////////////////////////////////////////////////////////////////////////

			// Suspend child controls from resizing every pixel
			this.ResizeBegin += (s, e) => { SuspendLayout(); };
			this.ResizeEnd += (s, e) => { ResumeLayout(true); };

		}

		/// <summary>
		/// Restores the window size, state, and location it was in from the last save
		/// </summary>
		private void RestoreWindowLocation()
		{
			if (Editor.Settings.WindowState.HasFlag(FormWindowState.Maximized))
				this.WindowState = FormWindowState.Maximized;
			else
			{
				this.Size = Editor.Settings.Size;
				this.Location = Editor.Settings.Location;
			}
		}

		/// <summary>
		/// Creates a window from a string representation of the original and returns it
		/// </summary>
		/// <param name="persistString">The string representation of the window</param>
		/// <returns>The created window</returns>
		/// <remarks>It is important that any plugin have a parameterless constructor, else
		/// it will fail to load from a saved layout.</remarks>
		private IDockContent GetContentFromPersistString(string persistString)
		{
			if (persistString == typeof(ARCed.Scripting.ScriptEditorForm).ToString())
			{
				if (Project.Settings.OpenScripts.Count > 0)
				{
					string file = Project.Settings.OpenScripts[0];
					Project.Settings.OpenScripts.RemoveAt(0);
					return OpenScript(file, false);
				}
				return null;
			}
			else if (persistString == typeof(ARCed.Scintilla.FindReplaceDialog).ToString())
				return Windows.ScintillaFindReplace;
			else if (persistString == typeof(ARCed.Scripting.ScriptStyleForm).ToString())
				return Windows.ScriptStyleMenu;
			else if (persistString == typeof(ARCed.Scripting.ScriptMenuForm).ToString())
				return Windows.ScriptMenu;
			else if (persistString == typeof(ARCed.Forms.ARChiveForm).ToString())
				return Windows.ARChiveForm;
			else if (persistString == typeof(ARCed.Forms.EditorOptionsForm).ToString())
				return Windows.EditorOptionsMenu;
			else if (persistString == typeof(ARCed.Forms.SkinSettingsForm).ToString())
				return Windows.SkinSettingForm;
			else if (persistString == typeof(ARCed.Scripting.AutoCompleteForm).ToString())
				return Windows.AutoCompleteWindow;

			// Attempt to create windows not defined, searching plugin assemblies
			try
			{
				Type type = null;
				foreach (var assembly in SystemHelper.LoadedAssemblies)
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
			if (Editor.Settings.ShowSplash)
			{
				SplashScreen.UdpateStatusText("Initializing Ruby engine...");
				Thread.Sleep(500);
				RestoreWindowLocation();
				if (File.Exists(filename) && Path.GetExtension(filename) == ".arcproj")
				{
					LoadProject(filename);
					SplashScreen.UdpateStatusText("Opening project...");
					Thread.Sleep(500);
				}
				SplashScreen.UdpateStatusText("Restoring layout...");
				Thread.Sleep(500);
				this.Show();
				SplashScreen.CloseSplashScreen();
				this.Activate();
			}
		}

		#endregion

		/// <summary>
		/// Loads the settings of the editor or initializes new ones if not found.
		/// </summary>
		private void LoadSettings()
		{
			Editor.Settings = EditorSettings.Load();
		}
	
		/// <summary>
		/// Loads the project file at the given path.
		/// </summary>
		/// <param name="path">Full path to the project file</param>
		private void LoadProject(string path)
		{
			dockMain.SuspendPainting();
			if (Project.IsLoaded)
				Project.Close();
			Project.NeedSaved = false;
			Project.Load(path);
			try
			{
				
				if (File.Exists(Project.LayoutSettings))
					dockMain.LoadFromXml(Project.LayoutSettings, _deserializeDockContent);
				Windows.ScriptMenu.ScriptsDirectory = Project.ScriptsDirectory;
				Windows.ARChiveForm.RefreshSettings();
				this.Text = Project.Title;
				Editor.Settings.AddToRecent(path);
			}
			catch
			{
				CloseProject();
				MessageBox.Show("Error loading project.", 
					"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
			dockMain.ResumePainting(true);
		}

		/// <summary>
		/// Closes the project and resets the Editor back to default
		/// </summary>
		private void CloseProject()
		{
			var contents = dockMain.Contents;
			for (int i = 0; i < contents.Count; i++)
				dockMain.RemoveContent(contents[i]);
			Project.Close();
			this.Text = "ARCed.NET";
			Windows.DisposeAll();
		}

		private void SaveProject()
		{
			try
			{
				Project.Save();
				Project.ScriptManager.SaveAll();
				dockMain.SaveAsXml(Project.LayoutSettings, Encoding.UTF8);
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
				"Advanced RPG Creator", MessageBoxButtons.YesNoCancel, MessageBoxIcon.Exclamation);
			if (result == DialogResult.Yes)
			{
				SaveProject();
				return true;
			}
			else if (result == DialogResult.No) return true;
			else return false;
		}

		private void Editor_FormClosing(object sender, FormClosingEventArgs e)
		{
			Editor.Settings.Location = this.Location;
			Editor.Settings.Size = this.Size;
			Editor.Settings.WindowState = this.WindowState;
			Editor.Settings.Save();
			ARCed.Properties.Settings.Default.Save();
		}

		private void buttonOpenGameDirectory_Click(object sender, EventArgs e)
		{
			string tag = (sender as ToolStripMenuItem).Tag.ToString();
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
			System.Diagnostics.Process.Start(dir + @"\");

		}

		private void styleManagerToolStripMenuItem_Click(object sender, EventArgs e)
		{
			if (Windows.ScriptStyleMenu.IsHidden)
				Windows.ScriptStyleMenu.Show(dockMain);
			Windows.ScriptStyleMenu.Show();
		}

		private void backupUtilityToolStripMenuItem_Click(object sender, EventArgs e)
		{
			Windows.ARChiveForm.RefreshSettings();
			Show(Windows.ARChiveForm);
		}

		private void toolMenuScriptManager_Click(object sender, EventArgs e)
		{
			Show(Windows.ScriptMenu);
		}

		private void toolMenuEditorOptions_Click(object sender, EventArgs e)
		{
			Show(Windows.EditorOptionsMenu);
		}

		#region Menu Strip: File

		/// <summary>
		/// Invoked when "File" drop-down is opening on menu strip, 
		/// enabling/disabling specific options as needed.
		/// </summary>
		private void menuItemFile_DropDownOpening(object sender, EventArgs e)
		{
			bool enable = Project.IsLoaded;
			fileMenuSaveProject.Enabled = enable;
			fileMenuSaveTemplate.Enabled = enable;
			fileMenuCloseProject.Enabled = enable;
			fileMenuOpenRecent.DropDownItems.Clear();
			foreach (string filename in Editor.Settings.RecentlyOpened)
			{
				// TODO: Implement custom game icon to tool item?
				var item = new ToolStripMenuItem(Path.GetFileNameWithoutExtension(filename));
				item.Click += new EventHandler(openRecentFile_Click);
				item.ToolTipText = filename;
				fileMenuOpenRecent.DropDownItems.Add(item);
			}
			//
		}

		private void openRecentFile_Click(object sender, EventArgs e)
		{
			string filename = (sender as ToolStripMenuItem).ToolTipText;
			if (File.Exists(filename))
				LoadProject(filename);
			else
			{
				MessageBox.Show("Project cannot be found.", 
					"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
				Editor.Settings.RecentlyOpened.Remove(filename);
			}
		}

		/// <summary>
		/// Menu: File -> New Project...
		/// </summary>
		private void fileMenuNewProject_Clicked(object sender, EventArgs e)
		{
			if (ConfirmProjectClose())
			{
				using (NewProjectForm dialog = new NewProjectForm())
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
						string proj = Project.CreateProject(dir, dialog.ProjectTitle, template);
						LoadProject(proj);
					}
				}
			}
		}

		/// <summary>
		/// Menu: File -> Open Project...
		/// </summary>
		private void fileMenuOpenProject_Click(object sender, EventArgs e)
		{
			if (ConfirmProjectClose())
			{
				using (OpenFileDialog loadDialog = new OpenFileDialog())
				{
					loadDialog.DefaultExt = "";
					loadDialog.Filter = "ARC Project File|*.arcproj|All Documents|*.*";
					loadDialog.InitialDirectory = PathHelper.DefaultSaveDirectory;
					loadDialog.Title = "Open ARC Project...";
					if (loadDialog.ShowDialog() == DialogResult.OK)
					{
						if (Project.IsLoaded && !ConfirmProjectClose())
							return;
						CloseProject();
						LoadProject(loadDialog.FileName);
					}
				}
			}
		}

		/// <summary>
		/// Menu: File -> Close Project
		/// </summary>
		private void fileMenuCloseProject_Click(object sender, EventArgs e)
		{
			if (ConfirmProjectClose())
				CloseProject();
		}

		/// <summary>
		/// Menu: File -> Save Project
		/// </summary>
		private void fileMenuSaveProject_Click(object sender, EventArgs e)
		{
			SaveProject();
		}

		/// <summary>
		/// Menu: File -> Save As Template...
		/// </summary>
		private void fileMenuSaveTemplate_Click(object sender, EventArgs e)
		{
			string title = "Save Project Template";
			string label = "Template Name:";
			string text = Project.Title;
			using (UserStringForm dialog = new UserStringForm(title, text, label, true))
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
		private void fileMenuExit_Click(object sender, EventArgs e)
		{
			if (ConfirmProjectClose())
				this.Close();
		}

		#endregion

		#region Menu Strip: Edit

		/// <summary>
		/// Invoked when the "Tools" drop-down is opening on menu strip, 
		/// enabling/disabling specific options as needed.
		/// </summary>
		private void menuStripEdit_DropDownOpening(object sender, EventArgs e)
		{
			bool enable = Project.IsLoaded;

		}

		#endregion

		#region Menu Strip: Tools

		private void menuStripTools_DropDownOpening(object sender, EventArgs e)
		{
			bool enable = Project.IsLoaded;
			toolMenuARChiveUtility.Enabled = enable;
			toolMenuDatabaseManager.Enabled = enable;
			toolMenuPlugins.Enabled = enable;
			toolMenuScriptManager.Enabled = enable;
			toolMenuSkinManager.Enabled = enable;

			// Add plugins to dropdown
			toolMenuPlugins.DropDownItems.Clear();
			foreach (RegistryEntry entry in Registry.Entries)
			{
				ToolStripMenuItem item = new ToolStripMenuItem(entry.Name);
				item.Image = Icon.ExtractAssociatedIcon(entry.Plugin.Filename).ToBitmap();
				item.ToolTipText = entry.Description;
				item.Tag = entry;
				item.Click += new EventHandler(menuStripPlugins_Clicked);
				toolMenuPlugins.DropDownItems.Add(item);
			}
		}

		private void menuStripPlugins_Clicked(object sender, EventArgs e)
		{
			((sender as ToolStripMenuItem).Tag as RegistryEntry).Show();
		}

		#endregion

		#region Script Context Menu

		private void saveToolStripMenuItem_Click(object sender, EventArgs e)
		{
			(Editor.MainDock.ActivePane.ActiveContent as ScriptEditorForm).Script.Save();
		}

		private void closeToolStripMenuItem_Click(object sender, EventArgs e)
		{
			Editor.MainDock.ActivePane.CloseActiveContent();
		}

		private void closeAllButThisToolStripMenuItem_Click(object sender, EventArgs e)
		{
			var keepForm = dockMain.ActiveDocumentPane.ActiveContent;
			if (dockMain.DocumentStyle == DocumentStyle.SystemMdi)
			{
				foreach (Form form in MdiChildren)
					if (form != keepForm)
						form.Close();
			}
			else
			{
                IDockContent[] documents = dockMain.DocumentsToArray();
				foreach (IDockContent content in documents)
					if (content != keepForm)
						content.DockHandler.Close();
			}
		}

		private void floatToolStripMenuItem_Click(object sender, EventArgs e)
		{
			Size size = new Size(720, 512);
			Rectangle screenRect = Screen.FromControl(this).Bounds;
			Point point = new Point((screenRect.Width - 720) / 2, (screenRect.Height - 512) / 2);
			Editor.MainDock.ActivePane.ActiveContent.DockHandler.FloatAt(new Rectangle(point, size));
		}

		#endregion

		private void toolMenuSkinManager_Click(object sender, EventArgs e)
		{
			Show(Windows.SkinSettingForm);
		}

		private void toolScriptMenuAutoComplete_Click(object sender, EventArgs e)
		{
			Show(Windows.AutoCompleteWindow);
		}

		private void helpMenuAbout_Click(object sender, EventArgs e)
		{
			using (AboutBox aboutDialog = new AboutBox())
				aboutDialog.ShowDialog(this);
		}

		/// <summary>
		/// TEST PURPOSES ONLY
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void toolComboDatabaseItem_Click(object sender, EventArgs e)
		{
			int index = Convert.ToInt32((sender as ToolStripMenuItem).Tag);
			Database.DatabaseWindow window = null;
			switch (index)
			{
				case 0: window = Windows.DatabaseForm<Database.Actors.ActorMainForm>(); break;
				case 1: window = Windows.DatabaseForm<Database.Classes.ClassMainForm>(); break;
				case 2: window = Windows.DatabaseForm<Database.Skills.SkillMainForm>(); break;
				case 3: window = Windows.DatabaseForm<Database.Items.ItemMainForm>(); break;
				case 4: window = Windows.DatabaseForm<Database.Weapons.WeaponMainForm>(); break;
				case 5: window = Windows.DatabaseForm<Database.Armors.ArmorMainForm>(); break;
				case 6: window = Windows.DatabaseForm<Database.Enemies.EnemyMainForm>(); break;
				case 7: window = Windows.DatabaseForm<Database.Troops.TroopMainForm>(); break;
				case 8: window = Windows.DatabaseForm<Database.Actors.ActorMainForm>(); break;
				case 9: window = Windows.DatabaseForm<Database.Actors.ActorMainForm>(); break;
				case 10: window = Windows.DatabaseForm<Database.Actors.ActorMainForm>(); break;
				case 11: window = Windows.DatabaseForm<Database.Actors.ActorMainForm>(); break;
				case 12: window = Windows.DatabaseForm<Database.Actors.ActorMainForm>(); break;
			}
			if (window != null)
				window.Show(Editor.MainDock);
		}
	}
}
