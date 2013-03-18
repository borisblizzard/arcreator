#region Using Directives

using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Security.Principal;
using System.Windows.Forms;
using ARCed.Core;
using ARCed.Core.Win32;
using ARCed.Database;
using ARCed.Helpers;
using ARCed.Plugins;
using ARCed.Scripting;
using ARCed.Settings;
using ARCed.UI;

#endregion

namespace ARCed
{
	partial class Editor
	{
		#region Private Fields

		private static readonly Logger _logger = new Logger();

		/// <summary>
		/// List of all processes attached to the editor
		/// </summary>
		private static List<Process> _childProcesses;

		#endregion

		#region Public Properties

        /// <summary>
        /// Gets a collection of assemblies used for the editor, as well as loaded plugin assemblies.
        /// </summary>
        public static List<Assembly> ARCedAssemblies
        {
            get
            {
                string dir = Path.Combine(Path.GetDirectoryName(Application.ExecutablePath), "Assemblies");
                var assemblies = Directory.GetFiles(dir, "*.dll").Select(Assembly.LoadFile).ToList();
                assemblies.AddRange(Registry.Plugins.Select(plugin => plugin.Assembly));
                return assemblies;
            }
        }
		/// <summary>
		/// Gets or sets the main status bar instance of the editor
		/// </summary>
		public static StatusStrip StatusBar { get; set; }
		/// <summary>
		/// Gets or sets the editor settings.
		/// </summary>
		public static EditorSettings Settings { get; set; }
		/// <summary>
		/// The main dock panel instance of the editor
		/// </summary>
		public static DockPanel MainDock { get; private set; }
		/// <summary>
		/// Deserializer used for recreating windows from persist strings
		/// </summary>
		public static DeserializeDockContent DeserializeContent { get; set; }
		/// <summary>
		/// Gets the flag indicating if the program is being run as an administrator
		/// </summary>
		public static bool IsAdministrator { get { return IsRunAsAdmin(); } }
		/// <summary>
		/// Gets the flag indicating if the current platform has a 64-bit CPU architecture
		/// </summary>
		public static bool Is64bit { get { return IntPtr.Size == 8; } }
		/// <summary>
		/// Returns the main editor instance
		/// </summary>
		public static Editor MainInstance { get; set; }
		/// <summary>
		/// Gets the current mode of the editor
		/// </summary>
		public static EditorMode Mode
		{
			get
			{
				var mode = EditorMode.Normal;
				if (Runtime.Debug)
				{
					mode |= EditorMode.Debug;
					mode &= ~EditorMode.Normal;
				}
				if (Runtime.Logging)
				{
					mode |= EditorMode.Logging;
					mode &= ~EditorMode.Normal;
				}
				return mode;
			}
		}
		/// <summary>
		/// Gets a list of all processes attached to the Editor
		/// </summary>
		public static List<Process> ChildProcesses
		{
			get { return _childProcesses ?? (_childProcesses = new List<Process>()); }
		}
		/// <summary>
		/// Notifies all open database windows that objects of a given type need refreshed
		/// </summary>
		/// <param name="type">Flag for type of object to refresh</param>
		public static void DatabaseNotify(RefreshType type)
		{
			foreach (DatabaseWindow window in Windows.DatabaseForms)
				window.NotifyRefresh(type);
		}

		#endregion

		#region Internal Properties

		internal static Logger Log { get { return _logger; } }

		#endregion

		#region Public Methods

		/// <summary>
		/// Adds and activates a window to the main editor's dock panel
		/// </summary>
		/// <param name="window">The dockable window</param>
		/// <param name="state">The initial state of the window</param>
		public static void Show(DockContent window, DockState state = DockState.Unknown)
		{
			if (state == DockState.Unknown)
				window.Show(MainDock);
			else
				window.Show(MainDock, state);
		}

		public static void Show(IPluginClient plugin, DockState state = DockState.Unknown)
		{

		}

		/// <summary>
		/// Creates a script editor panel and puts it in the opened script list
		/// </summary>
		/// <param name="file">The path of the script</param>
		/// <param name="show">Flag to display the script window</param>
		/// <returns>The instance of the associated script window</returns>
		public static ScriptEditorForm OpenScript(string file, bool show = false)
		{
		    Script script = Project.ScriptManager.WithPath(file) ?? new Script(file);
		    ScriptEditorForm editor = Windows.ScriptEditors.Find(e => e.Script == script);
			if (editor == null)
			{
				editor = new ScriptEditorForm(script);
				Windows.ScriptEditors.Add(editor);
			}
			if (show)
			{
				if (editor.DockPanel == null && !editor.IsFloat)
				{
					editor.Show(MainDock);
					editor.DockPanel.ContextMenuStrip = Windows.ScriptTabContextMenu;
				}
				MainDock.ActiveContent.DockHandler.Activate();
				editor.Activate();
			}
			return editor;
		}

		/// <summary>
		/// Creates a script editor panel and puts it in the opened script list
		/// </summary>
		/// <param name="script">The script to open</param>
		/// <param name="show">Flag to display the script window</param>
		/// <returns>The instance of the associated script window</returns>
		public static ScriptEditorForm OpenScript(Script script, bool show = false)
		{
			return OpenScript(script.Filename, show);
		}

		/// <summary>
		/// Starts a process and attaches it to the editor.
		/// </summary>
		/// <param name="filename">The path to the process</param>
		/// <param name="hidden">Flag to start hidden or not</param>
		/// <remarks>All child processes will be killed automatically when Editor exits</remarks>
		public static void AttachProcess(string filename, bool hidden = false)
		{
			var info = new ProcessStartInfo(filename);

			Process found = ChildProcesses.Find(p => p.StartInfo.FileName == filename);
			if (found != null && !hidden)
			{
				NativeMethods.SetForegroundWindow(found.MainWindowHandle);
				return;
			}
			info.UseShellExecute = false;
			info.RedirectStandardOutput = true;
			if (hidden)
			{
				info.CreateNoWindow = true;
				info.WindowStyle = ProcessWindowStyle.Hidden;
			}
			Process proc = Process.Start(info);
			ChildProcesses.Add(proc);
		}

		public static void AssociateFiles()
		{
			FileAssociator.Associate(".arcproj", "ARCed Project File",
				Path.Combine(PathHelper.EditorDirectory, "Resources", "icon.ico"),
				PathHelper.EditorPath);
			Console.WriteLine("Associated");
		}

		#endregion

		#region Private Methods

		private static bool IsRunAsAdmin()
		{
			WindowsIdentity curIdentity = WindowsIdentity.GetCurrent();
			var principal = new WindowsPrincipal(curIdentity);
			return principal.IsInRole(WindowsBuiltInRole.Administrator);
		}

		#endregion

	}
}
