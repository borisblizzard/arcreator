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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Editor));
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
            this.menuStripHelp = new System.Windows.Forms.ToolStripMenuItem();
            this.helpMenuHelp = new System.Windows.Forms.ToolStripMenuItem();
            this.helpMenuAbout = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripMenuDatabase = new System.Windows.Forms.ToolStripMenuItem();
            this.actorsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.classesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.skillsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.itemsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.weaponsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.armorsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.enemiesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.troopsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.statesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.animationsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.tilesetsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.commonEventsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.systemToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.switchesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.variablesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.toolStripSeparator5 = new System.Windows.Forms.ToolStripSeparator();
            this.statusStripMain = new System.Windows.Forms.StatusStrip();
            this.toolStripStatusLabel1 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel2 = new System.Windows.Forms.ToolStripStatusLabel();
            this.toolStripStatusLabel3 = new System.Windows.Forms.ToolStripStatusLabel();
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
            this.languageToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
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
            this.menuStripHelp,
            this.toolStripMenuDatabase});
            resources.ApplyResources(this.menuStripMain, "menuStripMain");
            this.menuStripMain.Name = "menuStripMain";
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
            resources.ApplyResources(this.menuStripFile, "menuStripFile");
            this.menuStripFile.DropDownOpening += new System.EventHandler(this.MenuItemFileDropDownOpening);
            // 
            // fileMenuNewProject
            // 
            this.fileMenuNewProject.Image = global::ARCed.Properties.Resources.NewDocument;
            resources.ApplyResources(this.fileMenuNewProject, "fileMenuNewProject");
            this.fileMenuNewProject.Name = "fileMenuNewProject";
            this.fileMenuNewProject.Click += new System.EventHandler(this.FileMenuNewProjectClicked);
            // 
            // fileMenuOpenProject
            // 
            this.fileMenuOpenProject.Image = global::ARCed.Properties.Resources.FolderOpen;
            resources.ApplyResources(this.fileMenuOpenProject, "fileMenuOpenProject");
            this.fileMenuOpenProject.Name = "fileMenuOpenProject";
            this.fileMenuOpenProject.Click += new System.EventHandler(this.FileMenuOpenProjectClick);
            // 
            // fileMenuOpenRecent
            // 
            this.fileMenuOpenRecent.Name = "fileMenuOpenRecent";
            resources.ApplyResources(this.fileMenuOpenRecent, "fileMenuOpenRecent");
            // 
            // fileMenuCloseProject
            // 
            this.fileMenuCloseProject.Image = global::ARCed.Properties.Resources.Close;
            this.fileMenuCloseProject.Name = "fileMenuCloseProject";
            resources.ApplyResources(this.fileMenuCloseProject, "fileMenuCloseProject");
            this.fileMenuCloseProject.Click += new System.EventHandler(this.FileMenuCloseProjectClick);
            // 
            // toolStripSeparator
            // 
            this.toolStripSeparator.Name = "toolStripSeparator";
            resources.ApplyResources(this.toolStripSeparator, "toolStripSeparator");
            // 
            // fileMenuSaveProject
            // 
            this.fileMenuSaveProject.Image = global::ARCed.Properties.Resources.Save;
            resources.ApplyResources(this.fileMenuSaveProject, "fileMenuSaveProject");
            this.fileMenuSaveProject.Name = "fileMenuSaveProject";
            this.fileMenuSaveProject.Click += new System.EventHandler(this.FileMenuSaveProjectClick);
            // 
            // fileMenuSaveTemplate
            // 
            this.fileMenuSaveTemplate.Image = global::ARCed.Properties.Resources.SaveTemplate;
            this.fileMenuSaveTemplate.Name = "fileMenuSaveTemplate";
            resources.ApplyResources(this.fileMenuSaveTemplate, "fileMenuSaveTemplate");
            this.fileMenuSaveTemplate.Click += new System.EventHandler(this.FileMenuSaveTemplateClick);
            // 
            // toolStripSeparator1
            // 
            this.toolStripSeparator1.Name = "toolStripSeparator1";
            resources.ApplyResources(this.toolStripSeparator1, "toolStripSeparator1");
            // 
            // fileMenuExit
            // 
            this.fileMenuExit.Name = "fileMenuExit";
            resources.ApplyResources(this.fileMenuExit, "fileMenuExit");
            this.fileMenuExit.Click += new System.EventHandler(this.FileMenuExitClick);
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
            resources.ApplyResources(this.menuStripEdit, "menuStripEdit");
            this.menuStripEdit.DropDownOpening += new System.EventHandler(this.MenuStripEditDropDownOpening);
            // 
            // editMenuUndo
            // 
            this.editMenuUndo.Image = global::ARCed.Properties.Resources.Undo;
            this.editMenuUndo.Name = "editMenuUndo";
            resources.ApplyResources(this.editMenuUndo, "editMenuUndo");
            // 
            // editMenuRedo
            // 
            this.editMenuRedo.Image = global::ARCed.Properties.Resources.Redo;
            this.editMenuRedo.Name = "editMenuRedo";
            resources.ApplyResources(this.editMenuRedo, "editMenuRedo");
            // 
            // toolStripSeparator3
            // 
            this.toolStripSeparator3.Name = "toolStripSeparator3";
            resources.ApplyResources(this.toolStripSeparator3, "toolStripSeparator3");
            // 
            // editMenuCut
            // 
            this.editMenuCut.Image = global::ARCed.Properties.Resources.Cut;
            resources.ApplyResources(this.editMenuCut, "editMenuCut");
            this.editMenuCut.Name = "editMenuCut";
            // 
            // editMenuCopy
            // 
            this.editMenuCopy.Image = global::ARCed.Properties.Resources.Copy;
            resources.ApplyResources(this.editMenuCopy, "editMenuCopy");
            this.editMenuCopy.Name = "editMenuCopy";
            // 
            // editMenuPaste
            // 
            this.editMenuPaste.Image = global::ARCed.Properties.Resources.Paste;
            resources.ApplyResources(this.editMenuPaste, "editMenuPaste");
            this.editMenuPaste.Name = "editMenuPaste";
            // 
            // toolStripSeparator4
            // 
            this.toolStripSeparator4.Name = "toolStripSeparator4";
            resources.ApplyResources(this.toolStripSeparator4, "toolStripSeparator4");
            // 
            // menuStripView
            // 
            this.menuStripView.Name = "menuStripView";
            resources.ApplyResources(this.menuStripView, "menuStripView");
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
            resources.ApplyResources(this.menuStripTools, "menuStripTools");
            this.menuStripTools.DropDownOpening += new System.EventHandler(this.MenuStripToolsDropDownOpening);
            // 
            // toolMenuDatabaseManager
            // 
            this.toolMenuDatabaseManager.Image = global::ARCed.Properties.Resources.Database;
            this.toolMenuDatabaseManager.Name = "toolMenuDatabaseManager";
            resources.ApplyResources(this.toolMenuDatabaseManager, "toolMenuDatabaseManager");
            // 
            // toolMenuScriptManager
            // 
            this.toolMenuScriptManager.Image = global::ARCed.Properties.Resources.Ruby;
            this.toolMenuScriptManager.Name = "toolMenuScriptManager";
            resources.ApplyResources(this.toolMenuScriptManager, "toolMenuScriptManager");
            this.toolMenuScriptManager.Click += new System.EventHandler(this.ToolMenuScriptManagerClick);
            // 
            // toolStripSeparator2
            // 
            this.toolStripSeparator2.Name = "toolStripSeparator2";
            resources.ApplyResources(this.toolStripSeparator2, "toolStripSeparator2");
            // 
            // toolMenuPlugins
            // 
            this.toolMenuPlugins.Name = "toolMenuPlugins";
            resources.ApplyResources(this.toolMenuPlugins, "toolMenuPlugins");
            // 
            // toolStripSeparator6
            // 
            this.toolStripSeparator6.Name = "toolStripSeparator6";
            resources.ApplyResources(this.toolStripSeparator6, "toolStripSeparator6");
            // 
            // rMXPProjectConverterToolStripMenuItem
            // 
            this.rMXPProjectConverterToolStripMenuItem.Image = global::ARCed.Properties.Resources.RMXP;
            this.rMXPProjectConverterToolStripMenuItem.Name = "rMXPProjectConverterToolStripMenuItem";
            resources.ApplyResources(this.rMXPProjectConverterToolStripMenuItem, "rMXPProjectConverterToolStripMenuItem");
            // 
            // toolMenuARChiveUtility
            // 
            this.toolMenuARChiveUtility.Image = global::ARCed.Properties.Resources.SevenZip;
            this.toolMenuARChiveUtility.Name = "toolMenuARChiveUtility";
            resources.ApplyResources(this.toolMenuARChiveUtility, "toolMenuARChiveUtility");
            this.toolMenuARChiveUtility.Click += new System.EventHandler(this.BackupUtilityToolStripMenuItemClick);
            // 
            // toolMenuSkinManager
            // 
            this.toolMenuSkinManager.Image = global::ARCed.Properties.Resources.Theme;
            this.toolMenuSkinManager.Name = "toolMenuSkinManager";
            resources.ApplyResources(this.toolMenuSkinManager, "toolMenuSkinManager");
            this.toolMenuSkinManager.Click += new System.EventHandler(this.ToolMenuSkinManagerClick);
            // 
            // toolMenuScriptSettings
            // 
            this.toolMenuScriptSettings.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolScriptMenuStyleSettings,
            this.toolScriptMenuAutoComplete,
            this.toolScriptMenuSnippetManager});
            this.toolMenuScriptSettings.Name = "toolMenuScriptSettings";
            resources.ApplyResources(this.toolMenuScriptSettings, "toolMenuScriptSettings");
            // 
            // toolScriptMenuStyleSettings
            // 
            this.toolScriptMenuStyleSettings.Image = global::ARCed.Properties.Resources.Scintilla;
            this.toolScriptMenuStyleSettings.Name = "toolScriptMenuStyleSettings";
            resources.ApplyResources(this.toolScriptMenuStyleSettings, "toolScriptMenuStyleSettings");
            this.toolScriptMenuStyleSettings.Click += new System.EventHandler(this.StyleManagerToolStripMenuItemClick);
            // 
            // toolScriptMenuAutoComplete
            // 
            this.toolScriptMenuAutoComplete.Image = global::ARCed.Properties.Resources.AutoComplete;
            this.toolScriptMenuAutoComplete.Name = "toolScriptMenuAutoComplete";
            resources.ApplyResources(this.toolScriptMenuAutoComplete, "toolScriptMenuAutoComplete");
            this.toolScriptMenuAutoComplete.Click += new System.EventHandler(this.ToolScriptMenuAutoCompleteClick);
            // 
            // toolScriptMenuSnippetManager
            // 
            this.toolScriptMenuSnippetManager.Name = "toolScriptMenuSnippetManager";
            resources.ApplyResources(this.toolScriptMenuSnippetManager, "toolScriptMenuSnippetManager");
            // 
            // toolMenuEditorOptions
            // 
            this.toolMenuEditorOptions.Image = global::ARCed.Properties.Resources.Settings;
            this.toolMenuEditorOptions.Name = "toolMenuEditorOptions";
            resources.ApplyResources(this.toolMenuEditorOptions, "toolMenuEditorOptions");
            this.toolMenuEditorOptions.Click += new System.EventHandler(this.ToolMenuEditorOptionsClick);
            // 
            // menuStripGame
            // 
            this.menuStripGame.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.gameMenuOpenFolder});
            this.menuStripGame.Name = "menuStripGame";
            resources.ApplyResources(this.menuStripGame, "menuStripGame");
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
            resources.ApplyResources(this.gameMenuOpenFolder, "gameMenuOpenFolder");
            this.gameMenuOpenFolder.Tag = "Game";
            this.gameMenuOpenFolder.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // gameMenuOpenGraphics
            // 
            this.gameMenuOpenGraphics.Name = "gameMenuOpenGraphics";
            resources.ApplyResources(this.gameMenuOpenGraphics, "gameMenuOpenGraphics");
            this.gameMenuOpenGraphics.Tag = "Graphics";
            this.gameMenuOpenGraphics.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // gameMenuOpenAudio
            // 
            this.gameMenuOpenAudio.Name = "gameMenuOpenAudio";
            resources.ApplyResources(this.gameMenuOpenAudio, "gameMenuOpenAudio");
            this.gameMenuOpenAudio.Tag = "Audio";
            this.gameMenuOpenAudio.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // gameMenuOpenData
            // 
            this.gameMenuOpenData.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.gameMenuOpenScripts});
            this.gameMenuOpenData.Name = "gameMenuOpenData";
            resources.ApplyResources(this.gameMenuOpenData, "gameMenuOpenData");
            this.gameMenuOpenData.Tag = "Data";
            this.gameMenuOpenData.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // gameMenuOpenScripts
            // 
            this.gameMenuOpenScripts.Name = "gameMenuOpenScripts";
            resources.ApplyResources(this.gameMenuOpenScripts, "gameMenuOpenScripts");
            this.gameMenuOpenScripts.Tag = "Scripts";
            this.gameMenuOpenScripts.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // gameMenuOpenTemplates
            // 
            this.gameMenuOpenTemplates.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.gameMenuOpenProjectTemplates,
            this.gameMenuOpenScriptTemplates});
            this.gameMenuOpenTemplates.Name = "gameMenuOpenTemplates";
            resources.ApplyResources(this.gameMenuOpenTemplates, "gameMenuOpenTemplates");
            this.gameMenuOpenTemplates.Tag = "Templates";
            this.gameMenuOpenTemplates.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // gameMenuOpenProjectTemplates
            // 
            this.gameMenuOpenProjectTemplates.Name = "gameMenuOpenProjectTemplates";
            resources.ApplyResources(this.gameMenuOpenProjectTemplates, "gameMenuOpenProjectTemplates");
            this.gameMenuOpenProjectTemplates.Tag = "TemplatesProjects";
            this.gameMenuOpenProjectTemplates.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // gameMenuOpenScriptTemplates
            // 
            this.gameMenuOpenScriptTemplates.Name = "gameMenuOpenScriptTemplates";
            resources.ApplyResources(this.gameMenuOpenScriptTemplates, "gameMenuOpenScriptTemplates");
            this.gameMenuOpenScriptTemplates.Tag = "TemplatesProjects";
            this.gameMenuOpenScriptTemplates.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // gameMenuOpenPlugins
            // 
            this.gameMenuOpenPlugins.Name = "gameMenuOpenPlugins";
            resources.ApplyResources(this.gameMenuOpenPlugins, "gameMenuOpenPlugins");
            this.gameMenuOpenPlugins.Tag = "Plugins";
            this.gameMenuOpenPlugins.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // gameMenuOpenSettings
            // 
            this.gameMenuOpenSettings.Name = "gameMenuOpenSettings";
            resources.ApplyResources(this.gameMenuOpenSettings, "gameMenuOpenSettings");
            this.gameMenuOpenSettings.Tag = "Settings";
            this.gameMenuOpenSettings.Click += new System.EventHandler(this.ButtonOpenGameDirectoryClick);
            // 
            // menuStripHelp
            // 
            this.menuStripHelp.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.helpMenuHelp,
            this.helpMenuAbout,
            this.languageToolStripMenuItem});
            this.menuStripHelp.Name = "menuStripHelp";
            resources.ApplyResources(this.menuStripHelp, "menuStripHelp");
            // 
            // helpMenuHelp
            // 
            this.helpMenuHelp.Image = global::ARCed.Properties.Resources.Help;
            this.helpMenuHelp.Name = "helpMenuHelp";
            resources.ApplyResources(this.helpMenuHelp, "helpMenuHelp");
            // 
            // helpMenuAbout
            // 
            this.helpMenuAbout.Name = "helpMenuAbout";
            resources.ApplyResources(this.helpMenuAbout, "helpMenuAbout");
            this.helpMenuAbout.Click += new System.EventHandler(this.HelpMenuAboutClick);
            // 
            // toolStripMenuDatabase
            // 
            this.toolStripMenuDatabase.Alignment = System.Windows.Forms.ToolStripItemAlignment.Right;
            this.toolStripMenuDatabase.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.actorsToolStripMenuItem,
            this.classesToolStripMenuItem,
            this.skillsToolStripMenuItem,
            this.itemsToolStripMenuItem,
            this.weaponsToolStripMenuItem,
            this.armorsToolStripMenuItem,
            this.enemiesToolStripMenuItem,
            this.troopsToolStripMenuItem,
            this.statesToolStripMenuItem,
            this.animationsToolStripMenuItem,
            this.tilesetsToolStripMenuItem,
            this.commonEventsToolStripMenuItem,
            this.systemToolStripMenuItem,
            this.switchesToolStripMenuItem,
            this.variablesToolStripMenuItem});
            this.toolStripMenuDatabase.Name = "toolStripMenuDatabase";
            resources.ApplyResources(this.toolStripMenuDatabase, "toolStripMenuDatabase");
            // 
            // actorsToolStripMenuItem
            // 
            this.actorsToolStripMenuItem.Name = "actorsToolStripMenuItem";
            resources.ApplyResources(this.actorsToolStripMenuItem, "actorsToolStripMenuItem");
            this.actorsToolStripMenuItem.Tag = "0";
            this.actorsToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // classesToolStripMenuItem
            // 
            this.classesToolStripMenuItem.Name = "classesToolStripMenuItem";
            resources.ApplyResources(this.classesToolStripMenuItem, "classesToolStripMenuItem");
            this.classesToolStripMenuItem.Tag = "1";
            this.classesToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // skillsToolStripMenuItem
            // 
            this.skillsToolStripMenuItem.Name = "skillsToolStripMenuItem";
            resources.ApplyResources(this.skillsToolStripMenuItem, "skillsToolStripMenuItem");
            this.skillsToolStripMenuItem.Tag = "2";
            this.skillsToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // itemsToolStripMenuItem
            // 
            this.itemsToolStripMenuItem.Name = "itemsToolStripMenuItem";
            resources.ApplyResources(this.itemsToolStripMenuItem, "itemsToolStripMenuItem");
            this.itemsToolStripMenuItem.Tag = "3";
            this.itemsToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // weaponsToolStripMenuItem
            // 
            this.weaponsToolStripMenuItem.Name = "weaponsToolStripMenuItem";
            resources.ApplyResources(this.weaponsToolStripMenuItem, "weaponsToolStripMenuItem");
            this.weaponsToolStripMenuItem.Tag = "4";
            this.weaponsToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // armorsToolStripMenuItem
            // 
            this.armorsToolStripMenuItem.Name = "armorsToolStripMenuItem";
            resources.ApplyResources(this.armorsToolStripMenuItem, "armorsToolStripMenuItem");
            this.armorsToolStripMenuItem.Tag = "5";
            this.armorsToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // enemiesToolStripMenuItem
            // 
            this.enemiesToolStripMenuItem.Name = "enemiesToolStripMenuItem";
            resources.ApplyResources(this.enemiesToolStripMenuItem, "enemiesToolStripMenuItem");
            this.enemiesToolStripMenuItem.Tag = "6";
            this.enemiesToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // troopsToolStripMenuItem
            // 
            this.troopsToolStripMenuItem.Name = "troopsToolStripMenuItem";
            resources.ApplyResources(this.troopsToolStripMenuItem, "troopsToolStripMenuItem");
            this.troopsToolStripMenuItem.Tag = "7";
            this.troopsToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // statesToolStripMenuItem
            // 
            this.statesToolStripMenuItem.Name = "statesToolStripMenuItem";
            resources.ApplyResources(this.statesToolStripMenuItem, "statesToolStripMenuItem");
            this.statesToolStripMenuItem.Tag = "8";
            this.statesToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // animationsToolStripMenuItem
            // 
            this.animationsToolStripMenuItem.Name = "animationsToolStripMenuItem";
            resources.ApplyResources(this.animationsToolStripMenuItem, "animationsToolStripMenuItem");
            this.animationsToolStripMenuItem.Tag = "9";
            this.animationsToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // tilesetsToolStripMenuItem
            // 
            this.tilesetsToolStripMenuItem.Name = "tilesetsToolStripMenuItem";
            resources.ApplyResources(this.tilesetsToolStripMenuItem, "tilesetsToolStripMenuItem");
            this.tilesetsToolStripMenuItem.Tag = "10";
            this.tilesetsToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // commonEventsToolStripMenuItem
            // 
            this.commonEventsToolStripMenuItem.Name = "commonEventsToolStripMenuItem";
            resources.ApplyResources(this.commonEventsToolStripMenuItem, "commonEventsToolStripMenuItem");
            this.commonEventsToolStripMenuItem.Tag = "11";
            this.commonEventsToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // systemToolStripMenuItem
            // 
            this.systemToolStripMenuItem.Name = "systemToolStripMenuItem";
            resources.ApplyResources(this.systemToolStripMenuItem, "systemToolStripMenuItem");
            this.systemToolStripMenuItem.Tag = "12";
            this.systemToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // switchesToolStripMenuItem
            // 
            this.switchesToolStripMenuItem.Name = "switchesToolStripMenuItem";
            resources.ApplyResources(this.switchesToolStripMenuItem, "switchesToolStripMenuItem");
            this.switchesToolStripMenuItem.Tag = "13";
            this.switchesToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // variablesToolStripMenuItem
            // 
            this.variablesToolStripMenuItem.Name = "variablesToolStripMenuItem";
            resources.ApplyResources(this.variablesToolStripMenuItem, "variablesToolStripMenuItem");
            this.variablesToolStripMenuItem.Tag = "14";
            this.variablesToolStripMenuItem.Click += new System.EventHandler(this.ToolComboDatabaseItemClick);
            // 
            // toolStripSeparator5
            // 
            this.toolStripSeparator5.Name = "toolStripSeparator5";
            resources.ApplyResources(this.toolStripSeparator5, "toolStripSeparator5");
            // 
            // statusStripMain
            // 
            this.statusStripMain.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripStatusLabel1,
            this.toolStripStatusLabel2,
            this.toolStripStatusLabel3});
            resources.ApplyResources(this.statusStripMain, "statusStripMain");
            this.statusStripMain.Name = "statusStripMain";
            // 
            // toolStripStatusLabel1
            // 
            this.toolStripStatusLabel1.Name = "toolStripStatusLabel1";
            resources.ApplyResources(this.toolStripStatusLabel1, "toolStripStatusLabel1");
            // 
            // toolStripStatusLabel2
            // 
            this.toolStripStatusLabel2.Name = "toolStripStatusLabel2";
            resources.ApplyResources(this.toolStripStatusLabel2, "toolStripStatusLabel2");
            this.toolStripStatusLabel2.Spring = true;
            // 
            // toolStripStatusLabel3
            // 
            this.toolStripStatusLabel3.Name = "toolStripStatusLabel3";
            resources.ApplyResources(this.toolStripStatusLabel3, "toolStripStatusLabel3");
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
            resources.ApplyResources(this.contextMenuScriptTab, "contextMenuScriptTab");
            // 
            // saveToolStripMenuItem
            // 
            this.saveToolStripMenuItem.Image = global::ARCed.Properties.Resources.Save;
            this.saveToolStripMenuItem.Name = "saveToolStripMenuItem";
            resources.ApplyResources(this.saveToolStripMenuItem, "saveToolStripMenuItem");
            this.saveToolStripMenuItem.Click += new System.EventHandler(this.SaveToolStripMenuItemClick);
            // 
            // closeToolStripMenuItem
            // 
            this.closeToolStripMenuItem.Image = global::ARCed.Properties.Resources.Close;
            this.closeToolStripMenuItem.Name = "closeToolStripMenuItem";
            resources.ApplyResources(this.closeToolStripMenuItem, "closeToolStripMenuItem");
            this.closeToolStripMenuItem.Click += new System.EventHandler(this.CloseToolStripMenuItemClick);
            // 
            // closeAllButThisToolStripMenuItem
            // 
            this.closeAllButThisToolStripMenuItem.Name = "closeAllButThisToolStripMenuItem";
            resources.ApplyResources(this.closeAllButThisToolStripMenuItem, "closeAllButThisToolStripMenuItem");
            this.closeAllButThisToolStripMenuItem.Click += new System.EventHandler(this.CloseAllButThisToolStripMenuItemClick);
            // 
            // toolStripSeparator7
            // 
            this.toolStripSeparator7.Name = "toolStripSeparator7";
            resources.ApplyResources(this.toolStripSeparator7, "toolStripSeparator7");
            // 
            // floatToolStripMenuItem
            // 
            this.floatToolStripMenuItem.Name = "floatToolStripMenuItem";
            resources.ApplyResources(this.floatToolStripMenuItem, "floatToolStripMenuItem");
            this.floatToolStripMenuItem.Click += new System.EventHandler(this.FloatToolStripMenuItemClick);
            // 
            // toolStripSeparator8
            // 
            this.toolStripSeparator8.Name = "toolStripSeparator8";
            resources.ApplyResources(this.toolStripSeparator8, "toolStripSeparator8");
            // 
            // newHorizontalTabGroupToolStripMenuItem
            // 
            this.newHorizontalTabGroupToolStripMenuItem.Name = "newHorizontalTabGroupToolStripMenuItem";
            resources.ApplyResources(this.newHorizontalTabGroupToolStripMenuItem, "newHorizontalTabGroupToolStripMenuItem");
            // 
            // newVerticalTabGroupToolStripMenuItem
            // 
            this.newVerticalTabGroupToolStripMenuItem.Name = "newVerticalTabGroupToolStripMenuItem";
            resources.ApplyResources(this.newVerticalTabGroupToolStripMenuItem, "newVerticalTabGroupToolStripMenuItem");
            // 
            // dockMain
            // 
            this.dockMain.ActiveAutoHideContent = null;
            resources.ApplyResources(this.dockMain, "dockMain");
            this.dockMain.DockBackColor = System.Drawing.SystemColors.AppWorkspace;
            this.dockMain.Name = "dockMain";
            // 
            // languageToolStripMenuItem
            // 
            this.languageToolStripMenuItem.Name = "languageToolStripMenuItem";
            resources.ApplyResources(this.languageToolStripMenuItem, "languageToolStripMenuItem");
            // 
            // Editor
            // 
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.Controls.Add(this.dockMain);
            this.Controls.Add(this.statusStripMain);
            this.Controls.Add(this.menuStripMain);
            this.IsMdiContainer = true;
            this.MainMenuStrip = this.menuStripMain;
            this.Name = "Editor";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.EditorFormClosing);
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
		private System.Windows.Forms.ToolStripMenuItem toolStripMenuDatabase;
		private System.Windows.Forms.ToolStripMenuItem actorsToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem classesToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem skillsToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem itemsToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem weaponsToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem armorsToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem enemiesToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem troopsToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem statesToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem animationsToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem tilesetsToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem commonEventsToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem systemToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem switchesToolStripMenuItem;
		private System.Windows.Forms.ToolStripMenuItem variablesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem languageToolStripMenuItem;
	}
}

