using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Windows.Forms;
using System.Xml.Serialization;
using ARCed.Data;
using ARCed.Helpers;
using ARCed.UI;

namespace ARCed.Settings
{
	/// <summary>
	/// Represents all settings that are not project related. These settings are the
	/// same globally for the editor under the current user no matter the current project.
	/// </summary>
	[Serializable]
	public class EditorSettings
	{
		private int _maxRecent;

		/// <summary>
		/// Gets or sets the editor's window location on startup
		/// </summary>
		public Point Location { get; set; }
		/// <summary>
		/// Gets or sets the editor's window size on startup
		/// </summary>
		public Size Size { get; set; }
		/// <summary>
		/// Gets or sets the editor's window state on startup
		/// </summary>
		public FormWindowState WindowState { get; set; }
		/// <summary>
		/// Gets or sets the flag to display the splash screen on startup
		/// </summary>
		public bool ShowSplash { get; set; }
		/// <summary>
		/// Gets or sets a list of recently opened projects
		/// </summary>
		public List<string> RecentlyOpened { get; set; }
		/// <summary>
		/// Gets or sets the maximum number of recently opened projects to display
		/// </summary>
		/// <remarks>The maximum number of recently items is 16</remarks>
		public int MaxRecent 
		{
			get { return _maxRecent; }
			set { _maxRecent = Util.Clamp<int>(value, 0, 16); }
		}
		/// <summary>
		/// Gets or sets the <paramref name="DockPanelSkin"/> property. These 
		/// settings are used for the styling of the editor windows
		/// </summary>
		/// <remarks>These settings are stored their own file.</remarks>
		[XmlIgnore]
		public DockPanelSkin WindowSkin { get; set; }
		/// <summary>
		/// Gets or sets the <paramref name="ScriptSettings"/> property. These 
		/// settings are used for all the styling and behavior of the script editor.
		/// </summary>
		/// <remarks>These settings are stored their own file.</remarks>
		[XmlIgnore]
		public ScriptSettings Scripting { get; set; }
		/// <summary>
		/// Settings used for chart styling in the _actor database panel
		/// </summary>
		public ChartSettings Charting { get; set; }
		/// <summary>
		/// Gets or sets the font used for notepads
		/// </summary>
		[XmlIgnore]
		public Font NoteFont 
		{ 
			get { return SerializedNoteFont; }
			set { SerializedNoteFont = value; }
		}
		/// <summary>
		/// Gets or sets the font used for notepads
		/// </summary>
		[XmlElement("NoteFont")]
		public SerializableFont SerializedNoteFont { get; set; }
		/// <summary>
		/// Gets or sets the settings used for rendering header images
		/// </summary>
		public HeaderSettings HeaderImage { get; set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		public EditorSettings()
		{
			_maxRecent = 8;
			Location = new Point();
			Size = new Size(800, 600);
			WindowState = FormWindowState.Maximized;
			ShowSplash = false; // TODO: Change back to "true"
			RecentlyOpened = new List<string>(16);
			WindowSkin = new DockPanelSkin();
			Scripting = new ScriptSettings();
			Charting = new ChartSettings();
			SerializedNoteFont = FontHelper.MonoFont;
			HeaderImage = new HeaderSettings();
		}

		/// <summary>
		/// Adds a value to the "Recently Opened" list and trims the list to the max allowed items
		/// </summary>
		/// <param name="filename">The filename to add</param>
		public void AddToRecent(string filename)
		{
			if (RecentlyOpened.Contains(filename))
				RecentlyOpened.Remove(filename);
			RecentlyOpened.Insert(0, filename);
			if (RecentlyOpened.Count > MaxRecent)
				RecentlyOpened.RemoveRange(MaxRecent - 1, RecentlyOpened.Count - MaxRecent);
		}

		/// <summary>
		/// Saves the settings files to disk in the AppData folder.
		/// </summary>
		/// <seealso cref="ARCed.Helpers.PathHelper"/>
		/// <seealso cref="ARCed.Scripting.ScriptSettings"/>
		/// <seealso cref="ARCed.UI.DockPanelSkin"/>
		public void Save()
		{
			try
			{
				SystemHelper.SaveXML<EditorSettings>(PathHelper.EditorSettings, this);
				SystemHelper.SaveXML<DockPanelSkin>(PathHelper.SkinSettings, WindowSkin);
				SystemHelper.SaveXML<ScriptSettings>(PathHelper.ScriptSettings, Scripting);
			}
			catch (IOException)
			{
				MessageBox.Show("Failed to save ARCed.NET settings.\nFile(s) are locked by another process.", 
					"Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
		}

		/// <summary>
		/// Initializes a new instance the ARCed.NET settings. User defined settings are
		/// loaded so long as each file exists, else the default values will be used.
		/// </summary>
		/// <returns>The created settings</returns>
		/// <seealso cref="ARCed.Helpers.PathHelper"/>
		/// <seealso cref="ARCed.Scripting.ScriptSettings"/>
		/// <seealso cref="ARCed.UI.DockPanelSkin"/>
		public static EditorSettings Load()
		{
			EditorSettings settings = new EditorSettings();
			if (File.Exists(PathHelper.EditorSettings))
				settings = SystemHelper.LoadXML<EditorSettings>(PathHelper.EditorSettings);
			if (File.Exists(PathHelper.SkinSettings))
				settings.WindowSkin = SystemHelper.LoadXML<DockPanelSkin>(PathHelper.SkinSettings);
			if (File.Exists(PathHelper.ScriptSettings))
				settings.Scripting = SystemHelper.LoadXML<ScriptSettings>(PathHelper.ScriptSettings);
			return settings;
		}

	}
}
