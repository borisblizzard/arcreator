namespace ARCed
{
	partial class Editor
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			foreach (var proc in ChildProcesses)
				proc.Kill();
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.components = new System.ComponentModel.Container();
			this.menuStripMain = new System.Windows.Forms.MenuStrip();
			this.menuStripFile = new System.Windows.Forms.ToolStripMenuItem();
			this.fileMenuNewProject = new System.Windows.Forms.ToolStripMenuItem();
			this.fileMenuOpenProject = new System.Windows.Forms.ToolStripMenuItem();
			this.fileMenuOpenRecent = new System.Windows.Forms.ToolStripMenuItem();
			this.fileMenuCloseProject = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator = new System.Windows.Forms.ToolStripSeparator();
			this.fileMenuSaveProject = new System.Windows.Forms.ToolStripMenuItem();
			this.fileMenuSaveTemplate = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator1 = new System.Windows.Forms.ToolStripSeparator();
			this.fileMenuExit = new System.Windows.Forms.ToolStripMenuItem();
			this.menuStripEdit = new System.Windows.Forms.ToolStripMenuItem();
			this.editMenuUndo = new System.Windows.Forms.ToolStripMenuItem();
			this.editMenuRedo = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator3 = new System.Windows.Forms.ToolStripSeparator();
			this.editMenuCut = new System.Windows.Forms.ToolStripMenuItem();
			this.editMenuCopy = new System.Windows.Forms.ToolStripMenuItem();
			this.editMenuPaste = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator4 = new System.Windows.Forms.ToolStripSeparator();
			this.menuStripView = new System.Windows.Forms.ToolStripMenuItem();
			this.menuStripTools = new System.Windows.Forms.ToolStripMenuItem();
			this.toolMenuDatabaseManager = new System.Windows.Forms.ToolStripMenuItem();
			this.toolMenuScriptManager = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator2 = new System.Windows.Forms.ToolStripSeparator();
			this.toolMenuPlugins = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator6 = new System.Windows.Forms.ToolStripSeparator();
			this.rMXPProjectConverterToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.toolMenuARChiveUtility = new System.Windows.Forms.ToolStripMenuItem();
			this.toolMenuSkinManager = new System.Windows.Forms.ToolStripMenuItem();
			this.toolMenuScriptSettings = new System.Windows.Forms.ToolStripMenuItem();
			this.toolScriptMenuStyleSettings = new System.Windows.Forms.ToolStripMenuItem();
			this.toolScriptMenuAutoComplete = new System.Windows.Forms.ToolStripMenuItem();
			this.toolScriptMenuSnippetManager = new System.Windows.Forms.ToolStripMenuItem();
			this.toolMenuEditorOptions = new System.Windows.Forms.ToolStripMenuItem();
			this.menuStripGame = new System.Windows.Forms.ToolStripMenuItem();
			this.menuStripHelp = new System.Windows.Forms.ToolStripMenuItem();
			this.helpMenuHelp = new System.Windows.Forms.ToolStripMenuItem();
			this.helpMenuAbout = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenFolder = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenGraphics = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenAudio = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenData = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenScripts = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenTemplates = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenProjectTemplates = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenScriptTemplates = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenPlugins = new System.Windows.Forms.ToolStripMenuItem();
			this.gameMenuOpenSettings = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator5 = new System.Windows.Forms.ToolStripSeparator();
			this.statusStripMain = new System.Windows.Forms.StatusStrip();
			this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
			this.toolStripStatusLabel2 = new System.Windows.Forms.ToolStripStatusLabel();
			this.toolStripStatusLabel3 = new System.Windows.Forms.ToolStripStatusLabel();
			this.toolStripProgressBar = new System.Windows.Forms.ToolStripProgressBar();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			this.contextMenuScriptTab = new System.Windows.Forms.ContextMenuStrip(this.components);
			this.saveToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.closeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.closeAllButThisToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator7 = new System.Windows.Forms.ToolStripSeparator();
			this.floatToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripSeparator8 = new System.Windows.Forms.ToolStripSeparator();
			this.newHorizontalTabGroupToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.newVerticalTabGroupToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
			this.dockMain = new ARCed.UI.DockPanel();
			this.menuStripMain.SuspendLayout();
			this.statusStripMain.SuspendLayout();
			this.contextMenuScriptTab.SuspendLayout();
			this.SuspendLayout();
			// 
			// menuStripMain
			// 
			this.menuStripMain.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.menuStripFile,
            this.menuStripEdit,
            this.menuStripView,
            this.menuStripTools,
            this.menuStripGame,
            this.menuStripHelp});
			this.menuStripMain.Location = new System.Drawing.Point(0, 0);
			this.menuStripMain.Name = "menuStripMain";
			this.menuStripMain.Size = new System.Drawing.Size(829, 24);
			this.menuStripMain.TabIndex = 0;
			this.menuStripMain.Text = "menuStrip1";
			// 
			// menuStripFile
			// 
			this.menuStripFile.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.fileMenuNewProject,
            this.fileMenuOpenProject,
            this.fileMenuOpenRecent,
            this.fileMenuCloseProject,
            this.toolStripSeparator,
            this.fileMenuSaveProject,
            this.fileMenuSaveTemplate,
            this.toolStripSeparator1,
            this.fileMenuExit});
			this.menuStripFile.Name = "menuStripFile";
			this.menuStripFile.Size = new System.Drawing.Size(37, 20);
			this.menuStripFile.Text = "&File";
			this.menuStripFile.DropDownOpening += new System.EventHandler(this.menuItemFile_DropDownOpening);
			// 
			// fileMenuNewProject
			// 
			this.fileMenuNewProject.Image = global::ARCed.Properties.Resources.NewDocument;
			this.fileMenuNewProject.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.fileMenuNewProject.Name = "fileMenuNewProject";
			this.fileMenuNewProject.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.N)));
			this.fileMenuNewProject.Size = new System.Drawing.Size(217, 22);
			this.fileMenuNewProject.Text = "&New Project...";
			this.fileMenuNewProject.Click += new System.EventHandler(this.fileMenuNewProject_Clicked);
			// 
			// fileMenuOpenProject
			// 
			this.fileMenuOpenProject.Image = global::ARCed.Properties.Resources.FolderOpen;
			this.fileMenuOpenProject.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.fileMenuOpenProject.Name = "fileMenuOpenProject";
			this.fileMenuOpenProject.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.O)));
			this.fileMenuOpenProject.Size = new System.Drawing.Size(217, 22);
			this.fileMenuOpenProject.Text = "&Open Project...";
			this.fileMenuOpenProject.Click += new System.EventHandler(this.fileMenuOpenProject_Click);
			// 
			// fileMenuOpenRecent
			// 
			this.fileMenuOpenRecent.Name = "fileMenuOpenRecent";
			this.fileMenuOpenRecent.Size = new System.Drawing.Size(217, 22);
			this.fileMenuOpenRecent.Text = "Recent Projects";
			// 
			// fileMenuCloseProject
			// 
			this.fileMenuCloseProject.Image = global::ARCed.Properties.Resources.Close;
			this.fileMenuCloseProject.Name = "fileMenuCloseProject";
			this.fileMenuCloseProject.Size = new System.Drawing.Size(217, 22);
			this.fileMenuCloseProject.Text = "Close Project";
			this.fileMenuCloseProject.Click += new System.EventHandler(this.fileMenuCloseProject_Click);
			// 
			// toolStripSeparator
			// 
			this.toolStripSeparator.Name = "toolStripSeparator";
			this.toolStripSeparator.Size = new System.Drawing.Size(214, 6);
			// 
			// fileMenuSaveProject
			// 
			this.fileMenuSaveProject.Image = global::ARCed.Properties.Resources.Save;
			this.fileMenuSaveProject.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.fileMenuSaveProject.Name = "fileMenuSaveProject";
			this.fileMenuSaveProject.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.S)));
			this.fileMenuSaveProject.Size = new System.Drawing.Size(217, 22);
			this.fileMenuSaveProject.Text = "&Save Project";
			this.fileMenuSaveProject.Click += new System.EventHandler(this.fileMenuSaveProject_Click);
			// 
			// fileMenuSaveTemplate
			// 
			this.fileMenuSaveTemplate.Image = global::ARCed.Properties.Resources.SaveTemplate;
			this.fileMenuSaveTemplate.Name = "fileMenuSaveTemplate";
			this.fileMenuSaveTemplate.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.T)));
			this.fileMenuSaveTemplate.Size = new System.Drawing.Size(217, 22);
			this.fileMenuSaveTemplate.Text = "Save As &Template...";
			this.fileMenuSaveTemplate.Click += new System.EventHandler(this.fileMenuSaveTemplate_Click);
			// 
			// toolStripSeparator1
			// 
			this.toolStripSeparator1.Name = "toolStripSeparator1";
			this.toolStripSeparator1.Size = new System.Drawing.Size(214, 6);
			// 
			// fileMenuExit
			// 
			this.fileMenuExit.Name = "fileMenuExit";
			this.fileMenuExit.Size = new System.Drawing.Size(217, 22);
			this.fileMenuExit.Text = "E&xit";
			this.fileMenuExit.Click += new System.EventHandler(this.fileMenuExit_Click);
			// 
			// menuStripEdit
			// 
			this.menuStripEdit.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.editMenuUndo,
            this.editMenuRedo,
            this.toolStripSeparator3,
            this.editMenuCut,
            this.editMenuCopy,
            this.editMenuPaste,
            this.toolStripSeparator4});
			this.menuStripEdit.Name = "menuStripEdit";
			this.menuStripEdit.Size = new System.Drawing.Size(39, 20);
			this.menuStripEdit.Text = "&Edit";
			this.menuStripEdit.DropDownOpening += new System.EventHandler(this.menuStripEdit_DropDownOpening);
			// 
			// editMenuUndo
			// 
			this.editMenuUndo.Image = global::ARCed.Properties.Resources.Undo;
			this.editMenuUndo.Name = "editMenuUndo";
			this.editMenuUndo.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Z)));
			this.editMenuUndo.Size = new System.Drawing.Size(144, 22);
			this.editMenuUndo.Text = "&Undo";
			// 
			// editMenuRedo
			// 
			this.editMenuRedo.Image = global::ARCed.Properties.Resources.Redo;
			this.editMenuRedo.Name = "editMenuRedo";
			this.editMenuRedo.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.Y)));
			this.editMenuRedo.Size = new System.Drawing.Size(144, 22);
			this.editMenuRedo.Text = "&Redo";
			// 
			// toolStripSeparator3
			// 
			this.toolStripSeparator3.Name = "toolStripSeparator3";
			this.toolStripSeparator3.Size = new System.Drawing.Size(141, 6);
			// 
			// editMenuCut
			// 
			this.editMenuCut.Image = global::ARCed.Properties.Resources.Cut;
			this.editMenuCut.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.editMenuCut.Name = "editMenuCut";
			this.editMenuCut.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.X)));
			this.editMenuCut.Size = new System.Drawing.Size(144, 22);
			this.editMenuCut.Text = "Cu&t";
			// 
			// editMenuCopy
			// 
			this.editMenuCopy.Image = global::ARCed.Properties.Resources.Copy;
			this.editMenuCopy.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.editMenuCopy.Name = "editMenuCopy";
			this.editMenuCopy.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.C)));
			this.editMenuCopy.Size = new System.Drawing.Size(144, 22);
			this.editMenuCopy.Text = "&Copy";
			// 
			// editMenuPaste
			// 
			this.editMenuPaste.Image = global::ARCed.Properties.Resources.Paste;
			this.editMenuPaste.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.editMenuPaste.Name = "editMenuPaste";
			this.editMenuPaste.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Control | System.Windows.Forms.Keys.V)));
			this.editMenuPaste.Size = new System.Drawing.Size(144, 22);
			this.editMenuPaste.Text = "&Paste";
			// 
			// toolStripSeparator4
			// 
			this.toolStripSeparator4.Name = "toolStripSeparator4";
			this.toolStripSeparator4.Size = new System.Drawing.Size(141, 6);
			// 
			// menuStripView
			// 
			this.menuStripView.Name = "menuStripView";
			this.menuStripView.Size = new System.Drawing.Size(44, 20);
			this.menuStripView.Text = "View";
			// 
			// menuStripTools
			// 
			this.menuStripTools.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolMenuDatabaseManager,
            this.toolMenuScriptManager,
            this.toolStripSeparator2,
            this.toolMenuPlugins,
            this.toolStripSeparator6,
            this.rMXPProjectConverterToolStripMenuItem,
            this.toolMenuARChiveUtility,
            this.toolMenuSkinManager,
            this.toolMenuScriptSettings,
            this.toolMenuEditorOptions});
			this.menuStripTools.Name = "menuStripTools";
			this.menuStripTools.Size = new System.Drawing.Size(48, 20);
			this.menuStripTools.Text = "&Tools";
			this.menuStripTools.DropDownOpening += new System.EventHandler(this.menuStripTools_DropDownOpening);
			// 
			// toolMenuDatabaseManager
			// 
			this.toolMenuDatabaseManager.Image = global::ARCed.Properties.Resources.Database;
			this.toolMenuDatabaseManager.Name = "toolMenuDatabaseManager";
			this.toolMenuDatabaseManager.Size = new System.Drawing.Size(210, 22);
			this.toolMenuDatabaseManager.Text = "&Database Manager";
			// 
			// toolMenuScriptManager
			// 
			this.toolMenuScriptManager.Image = global::ARCed.Properties.Resources.Ruby;
			this.toolMenuScriptManager.Name = "toolMenuScriptManager";
			this.toolMenuScriptManager.Size = new System.Drawing.Size(210, 22);
			this.toolMenuScriptManager.Text = "&Script Manager";
			this.toolMenuScriptManager.Click += new System.EventHandler(this.toolMenuScriptManager_Click);
			// 
			// toolStripSeparator2
			// 
			this.toolStripSeparator2.Name = "toolStripSeparator2";
			this.toolStripSeparator2.Size = new System.Drawing.Size(207, 6);
			// 
			// toolMenuPlugins
			// 
			this.toolMenuPlugins.Name = "toolMenuPlugins";
			this.toolMenuPlugins.Size = new System.Drawing.Size(210, 22);
			this.toolMenuPlugins.Text = "&Plugins";
			// 
			// toolStripSeparator6
			// 
			this.toolStripSeparator6.Name = "toolStripSeparator6";
			this.toolStripSeparator6.Size = new System.Drawing.Size(207, 6);
			// 
			// rMXPProjectConverterToolStripMenuItem
			// 
			this.rMXPProjectConverterToolStripMenuItem.Image = global::ARCed.Properties.Resources.RMXP;
			this.rMXPProjectConverterToolStripMenuItem.Name = "rMXPProjectConverterToolStripMenuItem";
			this.rMXPProjectConverterToolStripMenuItem.Size = new System.Drawing.Size(210, 22);
			this.rMXPProjectConverterToolStripMenuItem.Text = "RMXP Project Converter...";
			// 
			// toolMenuARChiveUtility
			// 
			this.toolMenuARChiveUtility.Image = global::ARCed.Properties.Resources.SevenZip;
			this.toolMenuARChiveUtility.Name = "toolMenuARChiveUtility";
			this.toolMenuARChiveUtility.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Alt | System.Windows.Forms.Keys.B)));
			this.toolMenuARChiveUtility.Size = new System.Drawing.Size(210, 22);
			this.toolMenuARChiveUtility.Text = "&ARChive Utility...";
			this.toolMenuARChiveUtility.Click += new System.EventHandler(this.backupUtilityToolStripMenuItem_Click);
			// 
			// toolMenuSkinManager
			// 
			this.toolMenuSkinManager.Image = global::ARCed.Properties.Resources.Theme;
			this.toolMenuSkinManager.Name = "toolMenuSkinManager";
			this.toolMenuSkinManager.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Alt | System.Windows.Forms.Keys.K)));
			this.toolMenuSkinManager.Size = new System.Drawing.Size(210, 22);
			this.toolMenuSkinManager.Text = "S&kin Manager...";
			this.toolMenuSkinManager.Click += new System.EventHandler(this.toolMenuSkinManager_Click);
			// 
			// toolMenuScriptSettings
			// 
			this.toolMenuScriptSettings.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolScriptMenuStyleSettings,
            this.toolScriptMenuAutoComplete,
            this.toolScriptMenuSnippetManager});
			this.toolMenuScriptSettings.Name = "toolMenuScriptSettings";
			this.toolMenuScriptSettings.Size = new System.Drawing.Size(210, 22);
			this.toolMenuScriptSettings.Text = "Script Settings";
			// 
			// toolScriptMenuStyleSettings
			// 
			this.toolScriptMenuStyleSettings.Image = global::ARCed.Properties.Resources.Scintilla;
			this.toolScriptMenuStyleSettings.Name = "toolScriptMenuStyleSettings";
			this.toolScriptMenuStyleSettings.Size = new System.Drawing.Size(211, 22);
			this.toolScriptMenuStyleSettings.Text = "Style Settings...";
			this.toolScriptMenuStyleSettings.Click += new System.EventHandler(this.styleManagerToolStripMenuItem_Click);
			// 
			// toolScriptMenuAutoComplete
			// 
			this.toolScriptMenuAutoComplete.Image = global::ARCed.Properties.Resources.AutoComplete;
			this.toolScriptMenuAutoComplete.Name = "toolScriptMenuAutoComplete";
			this.toolScriptMenuAutoComplete.Size = new System.Drawing.Size(211, 22);
			this.toolScriptMenuAutoComplete.Text = "Auto-Complete Settings...";
			this.toolScriptMenuAutoComplete.Click += new System.EventHandler(this.toolScriptMenuAutoComplete_Click);
			// 
			// toolScriptMenuSnippetManager
			// 
			this.toolScriptMenuSnippetManager.Name = "toolScriptMenuSnippetManager";
			this.toolScriptMenuSnippetManager.Size = new System.Drawing.Size(211, 22);
			this.toolScriptMenuSnippetManager.Text = "Snippet Manager...";
			// 
			// toolMenuEditorOptions
			// 
			this.toolMenuEditorOptions.Image = global::ARCed.Properties.Resources.Settings;
			this.toolMenuEditorOptions.Name = "toolMenuEditorOptions";
			this.toolMenuEditorOptions.ShortcutKeys = ((System.Windows.Forms.Keys)((System.Windows.Forms.Keys.Alt | System.Windows.Forms.Keys.O)));
			this.toolMenuEditorOptions.Size = new System.Drawing.Size(210, 22);
			this.toolMenuEditorOptions.Text = "&Options...";
			this.toolMenuEditorOptions.Click += new System.EventHandler(this.toolMenuEditorOptions_Click);
			// 
			// menuStripGame
			// 
			this.menuStripGame.Name = "menuStripGame";
			this.menuStripGame.Size = new System.Drawing.Size(50, 20);
			this.menuStripGame.Text = "&Game";
			// 
			// menuStripHelp
			// 
			this.menuStripHelp.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.helpMenuHelp,
            this.helpMenuAbout});
			this.menuStripHelp.Name = "menuStripHelp";
			this.menuStripHelp.Size = new System.Drawing.Size(44, 20);
			this.menuStripHelp.Text = "&Help";
			// 
			// helpMenuHelp
			// 
			this.helpMenuHelp.Image = global::ARCed.Properties.Resources.Help;
			this.helpMenuHelp.Name = "helpMenuHelp";
			this.helpMenuHelp.Size = new System.Drawing.Size(116, 22);
			this.helpMenuHelp.Text = "&Help";
			// 
			// helpMenuAbout
			// 
			this.helpMenuAbout.Name = "helpMenuAbout";
			this.helpMenuAbout.Size = new System.Drawing.Size(116, 22);
			this.helpMenuAbout.Text = "&About...";
			this.helpMenuAbout.Click += new System.EventHandler(this.helpMenuAbout_Click);
			// 
			// gameMenuOpenFolder
			// 
			this.gameMenuOpenFolder.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.gameMenuOpenGraphics,
            this.gameMenuOpenAudio,
            this.gameMenuOpenData,
            this.gameMenuOpenTemplates,
            this.gameMenuOpenPlugins,
            this.gameMenuOpenSettings});
			this.gameMenuOpenFolder.Image = global::ARCed.Properties.Resources.FolderOpen;
			this.gameMenuOpenFolder.Name = "gameMenuOpenFolder";
			this.gameMenuOpenFolder.Size = new System.Drawing.Size(173, 22);
			this.gameMenuOpenFolder.Tag = "Game";
			this.gameMenuOpenFolder.Text = "Open Game Folder";
			this.gameMenuOpenFolder.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// gameMenuOpenGraphics
			// 
			this.gameMenuOpenGraphics.Name = "gameMenuOpenGraphics";
			this.gameMenuOpenGraphics.Size = new System.Drawing.Size(129, 22);
			this.gameMenuOpenGraphics.Tag = "Graphics";
			this.gameMenuOpenGraphics.Text = "Graphics";
			this.gameMenuOpenGraphics.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// gameMenuOpenAudio
			// 
			this.gameMenuOpenAudio.Name = "gameMenuOpenAudio";
			this.gameMenuOpenAudio.Size = new System.Drawing.Size(129, 22);
			this.gameMenuOpenAudio.Tag = "Audio";
			this.gameMenuOpenAudio.Text = "Audio";
			this.gameMenuOpenAudio.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// gameMenuOpenData
			// 
			this.gameMenuOpenData.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.gameMenuOpenScripts});
			this.gameMenuOpenData.Name = "gameMenuOpenData";
			this.gameMenuOpenData.Size = new System.Drawing.Size(129, 22);
			this.gameMenuOpenData.Tag = "Data";
			this.gameMenuOpenData.Text = "Data";
			this.gameMenuOpenData.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// gameMenuOpenScripts
			// 
			this.gameMenuOpenScripts.Name = "gameMenuOpenScripts";
			this.gameMenuOpenScripts.Size = new System.Drawing.Size(109, 22);
			this.gameMenuOpenScripts.Tag = "Scripts";
			this.gameMenuOpenScripts.Text = "Scripts";
			this.gameMenuOpenScripts.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// gameMenuOpenTemplates
			// 
			this.gameMenuOpenTemplates.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.gameMenuOpenProjectTemplates,
            this.gameMenuOpenScriptTemplates});
			this.gameMenuOpenTemplates.Name = "gameMenuOpenTemplates";
			this.gameMenuOpenTemplates.Size = new System.Drawing.Size(129, 22);
			this.gameMenuOpenTemplates.Tag = "Templates";
			this.gameMenuOpenTemplates.Text = "Templates";
			this.gameMenuOpenTemplates.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// gameMenuOpenProjectTemplates
			// 
			this.gameMenuOpenProjectTemplates.Name = "gameMenuOpenProjectTemplates";
			this.gameMenuOpenProjectTemplates.Size = new System.Drawing.Size(116, 22);
			this.gameMenuOpenProjectTemplates.Tag = "TemplatesProjects";
			this.gameMenuOpenProjectTemplates.Text = "Projects";
			this.gameMenuOpenProjectTemplates.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// gameMenuOpenScriptTemplates
			// 
			this.gameMenuOpenScriptTemplates.Name = "gameMenuOpenScriptTemplates";
			this.gameMenuOpenScriptTemplates.Size = new System.Drawing.Size(116, 22);
			this.gameMenuOpenScriptTemplates.Tag = "TemplatesProjects";
			this.gameMenuOpenScriptTemplates.Text = "Scripts";
			this.gameMenuOpenScriptTemplates.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// gameMenuOpenPlugins
			// 
			this.gameMenuOpenPlugins.Name = "gameMenuOpenPlugins";
			this.gameMenuOpenPlugins.Size = new System.Drawing.Size(129, 22);
			this.gameMenuOpenPlugins.Tag = "Plugins";
			this.gameMenuOpenPlugins.Text = "Plugins";
			this.gameMenuOpenPlugins.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// gameMenuOpenSettings
			// 
			this.gameMenuOpenSettings.Name = "gameMenuOpenSettings";
			this.gameMenuOpenSettings.Size = new System.Drawing.Size(129, 22);
			this.gameMenuOpenSettings.Tag = "Settings";
			this.gameMenuOpenSettings.Text = "Settings";
			this.gameMenuOpenSettings.Click += new System.EventHandler(this.buttonOpenGameDirectory_Click);
			// 
			// toolStripSeparator5
			// 
			this.toolStripSeparator5.Name = "toolStripSeparator5";
			this.toolStripSeparator5.Size = new System.Drawing.Size(149, 6);
			// 
			// statusStripMain
			// 
			this.statusStripMain.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1,
            this.toolStripStatusLabel2,
            this.toolStripStatusLabel3});
			this.statusStripMain.Location = new System.Drawing.Point(0, 475);
			this.statusStripMain.Name = "statusStripMain";
			this.statusStripMain.Size = new System.Drawing.Size(829, 22);
			this.statusStripMain.TabIndex = 1;
			this.statusStripMain.Text = "statusStrip";
			// 
			// toolStripStatusLabel1
			// 
			this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
			this.toolStripStatusLabel1.Size = new System.Drawing.Size(118, 17);
			this.toolStripStatusLabel1.Text = "toolStripStatusLabel1";
			// 
			// toolStripStatusLabel2
			// 
			this.toolStripStatusLabel2.Name = "toolStripStatusLabel2";
			this.toolStripStatusLabel2.Size = new System.Drawing.Size(578, 17);
			this.toolStripStatusLabel2.Spring = true;
			this.toolStripStatusLabel2.Text = "toolStripStatusLabel2";
			// 
			// toolStripStatusLabel3
			// 
			this.toolStripStatusLabel3.Name = "toolStripStatusLabel3";
			this.toolStripStatusLabel3.Size = new System.Drawing.Size(118, 17);
			this.toolStripStatusLabel3.Text = "toolStripStatusLabel3";
			this.toolStripStatusLabel3.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
			// 
			// toolStripProgressBar
			// 
			this.toolStripProgressBar.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
			this.toolStripProgressBar.Name = "toolStripProgressBar";
			this.toolStripProgressBar.Size = new System.Drawing.Size(96, 16);
			this.toolStripProgressBar.Step = 1;
			this.toolStripProgressBar.Style = System.Windows.Forms.ProgressBarStyle.Continuous;
			this.toolStripProgressBar.ToolTipText = "Current progress...";
			this.toolStripProgressBar.Visible = false;
			// 
			// contextMenuScriptTab
			// 
			this.contextMenuScriptTab.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.saveToolStripMenuItem,
            this.closeToolStripMenuItem,
            this.closeAllButThisToolStripMenuItem,
            this.toolStripSeparator7,
            this.floatToolStripMenuItem,
            this.toolStripSeparator8,
            this.newHorizontalTabGroupToolStripMenuItem,
            this.newVerticalTabGroupToolStripMenuItem});
			this.contextMenuScriptTab.Name = "contextMenuScriptTab";
			this.contextMenuScriptTab.Size = new System.Drawing.Size(216, 148);
			// 
			// saveToolStripMenuItem
			// 
			this.saveToolStripMenuItem.Image = global::ARCed.Properties.Resources.Save;
			this.saveToolStripMenuItem.Name = "saveToolStripMenuItem";
			this.saveToolStripMenuItem.Size = new System.Drawing.Size(215, 22);
			this.saveToolStripMenuItem.Text = "Save ";
			this.saveToolStripMenuItem.Click += new System.EventHandler(this.saveToolStripMenuItem_Click);
			// 
			// closeToolStripMenuItem
			// 
			this.closeToolStripMenuItem.Image = global::ARCed.Properties.Resources.Close;
			this.closeToolStripMenuItem.Name = "closeToolStripMenuItem";
			this.closeToolStripMenuItem.Size = new System.Drawing.Size(215, 22);
			this.closeToolStripMenuItem.Text = "Close";
			this.closeToolStripMenuItem.Click += new System.EventHandler(this.closeToolStripMenuItem_Click);
			// 
			// closeAllButThisToolStripMenuItem
			// 
			this.closeAllButThisToolStripMenuItem.Name = "closeAllButThisToolStripMenuItem";
			this.closeAllButThisToolStripMenuItem.Size = new System.Drawing.Size(215, 22);
			this.closeAllButThisToolStripMenuItem.Text = "Close All But This";
			this.closeAllButThisToolStripMenuItem.Click += new System.EventHandler(this.closeAllButThisToolStripMenuItem_Click);
			// 
			// toolStripSeparator7
			// 
			this.toolStripSeparator7.Name = "toolStripSeparator7";
			this.toolStripSeparator7.Size = new System.Drawing.Size(212, 6);
			// 
			// floatToolStripMenuItem
			// 
			this.floatToolStripMenuItem.Name = "floatToolStripMenuItem";
			this.floatToolStripMenuItem.Size = new System.Drawing.Size(215, 22);
			this.floatToolStripMenuItem.Text = "Float";
			this.floatToolStripMenuItem.Click += new System.EventHandler(this.floatToolStripMenuItem_Click);
			// 
			// toolStripSeparator8
			// 
			this.toolStripSeparator8.Name = "toolStripSeparator8";
			this.toolStripSeparator8.Size = new System.Drawing.Size(212, 6);
			// 
			// newHorizontalTabGroupToolStripMenuItem
			// 
			this.newHorizontalTabGroupToolStripMenuItem.Name = "newHorizontalTabGroupToolStripMenuItem";
			this.newHorizontalTabGroupToolStripMenuItem.Size = new System.Drawing.Size(215, 22);
			this.newHorizontalTabGroupToolStripMenuItem.Text = "New Horizontal Tab Group";
			// 
			// newVerticalTabGroupToolStripMenuItem
			// 
			this.newVerticalTabGroupToolStripMenuItem.Name = "newVerticalTabGroupToolStripMenuItem";
			this.newVerticalTabGroupToolStripMenuItem.Size = new System.Drawing.Size(215, 22);
			this.newVerticalTabGroupToolStripMenuItem.Text = "New Vertical Tab Group";
			// 
			// dockMain
			// 
			this.dockMain.ActiveAutoHideContent = null;
			this.dockMain.Dock = System.Windows.Forms.DockStyle.Fill;
			this.dockMain.DockBackColor = System.Drawing.SystemColors.AppWorkspace;
			this.dockMain.Location = new System.Drawing.Point(0, 24);
			this.dockMain.Name = "dockMain";
			this.dockMain.Size = new System.Drawing.Size(829, 451);
			this.dockMain.TabIndex = 3;
			// 
			// Editor
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(829, 497);
			this.Controls.Add(this.dockMain);
			this.Controls.Add(this.statusStripMain);
			this.Controls.Add(this.menuStripMain);
			this.IsMdiContainer = true;
			this.MainMenuStrip = this.menuStripMain;
			this.Name = "Editor";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "ARCed.NET";
			this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.Editor_FormClosing);
			this.menuStripMain.ResumeLayout(false);
			this.menuStripMain.PerformLayout();
			this.statusStripMain.ResumeLayout(false);
			this.statusStripMain.PerformLayout();
			this.contextMenuScriptTab.ResumeLayout(false);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.MenuStrip menuStripMain;
		private System.Windows.Forms.ToolStripMenuItem menuStripFile;
		private System.Windows.Forms.ToolStripMenuItem fileMenuNewProject;
		private System.Windows.Forms.ToolStripMenuItem fileMenuOpenProject;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator;
		private System.Windows.Forms.ToolStripMenuItem fileMenuSaveProject;
		private System.Windows.Forms.ToolStripMenuItem fileMenuSaveTemplate;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator1;
		private System.Windows.Forms.ToolStripMenuItem fileMenuExit;
		private System.Windows.Forms.ToolStripMenuItem menuStripEdit;
		private System.Windows.Forms.ToolStripMenuItem editMenuUndo;
		private System.Windows.Forms.ToolStripMenuItem editMenuRedo;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator3;
		private System.Windows.Forms.ToolStripMenuItem editMenuCut;
		private System.Windows.Forms.ToolStripMenuItem editMenuCopy;
		private System.Windows.Forms.ToolStripMenuItem editMenuPaste;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator4;
		private System.Windows.Forms.ToolStripMenuItem menuStripTools;
		private System.Windows.Forms.ToolStripMenuItem menuStripHelp;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator5;
		private System.Windows.Forms.ToolStripMenuItem helpMenuAbout;
		private System.Windows.Forms.StatusStrip statusStripMain;
		private System.Windows.Forms.ToolStripMenuItem fileMenuCloseProject;
		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.ToolStripMenuItem toolMenuARChiveUtility;
		private System.Windows.Forms.ToolStripMenuItem toolMenuSkinManager;
		private System.Windows.Forms.ToolStripMenuItem toolMenuScriptSettings;
		private System.Windows.Forms.ToolStripMenuItem toolScriptMenuStyleSettings;
		private System.Windows.Forms.ToolStripMenuItem toolScriptMenuAutoComplete;
		private System.Windows.Forms.ToolStripMenuItem toolScriptMenuSnippetManager;
		private System.Windows.Forms.ToolStripMenuItem toolMenuEditorOptions;
		private System.Windows.Forms.ToolStripMenuItem menuStripGame;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenFolder;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenGraphics;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenAudio;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenData;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenTemplates;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenProjectTemplates;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenScriptTemplates;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenPlugins;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenSettings;
		private System.Windows.Forms.ToolStripMenuItem gameMenuOpenScripts;
		private System.Windows.Forms.ToolStripProgressBar toolStripProgressBar;
		private System.Windows.Forms.ToolStripMenuItem toolMenuScriptManager;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator2;
		private System.Windows.Forms.ToolStripMenuItem toolMenuPlugins;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator6;
		private System.Windows.Forms.ToolStripMenuItem menuStripView;
		private System.Windows.Forms.ToolStripMenuItem helpMenuHelp;
		private System.Windows.Forms.ToolStripMenuItem toolMenuDatabaseManager;
		private System.Windows.Forms.ToolStripMenuItem saveToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem closeToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem closeAllButThisToolStripMenuItem;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator7;
		private System.Windows.Forms.ToolStripMenuItem floatToolStripMenuItem;
		private System.Windows.Forms.ToolStripSeparator toolStripSeparator8;
		private System.Windows.Forms.ToolStripMenuItem newHorizontalTabGroupToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem newVerticalTabGroupToolStripMenuItem;
		private System.Windows.Forms.ContextMenuStrip contextMenuScriptTab;
		private UI.DockPanel dockMain;
		private System.Windows.Forms.ToolStripMenuItem fileMenuOpenRecent;
		private System.Windows.Forms.ToolStripMenuItem rMXPProjectConverterToolStripMenuItem;
		private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel1;
		private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel2;
		private System.Windows.Forms.ToolStripStatusLabel toolStripStatusLabel3;
	}
}

