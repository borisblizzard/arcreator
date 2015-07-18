﻿#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using System.Windows.Forms;
using System.Xml.Serialization;
using ARCed.Core;
using ARCed.Helpers;
using ARCed.UI;

#endregion

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
			get { return this._maxRecent; }
			set { this._maxRecent = value.Clamp(0, 16); }
		}
		/// <summary>
		/// Gets or sets the <see cref="DockPanelSkin"/> property. These 
		/// settings are used for the styling of the editor windows
		/// </summary>
		/// <remarks>These settings are stored their own file.</remarks>
		[XmlIgnore]
		public DockPanelSkin WindowSkin { get; set; }
		/// <summary>
		/// Gets or sets the <see cref="ScriptSettings"/> property. These 
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
			get { return this.SerializedNoteFont; }
			set { this.SerializedNoteFont = value; }
		}
		/// <summary>
		/// Gets or sets the font used for notepads
		/// </summary>
		[XmlElement("NoteFont")]
		public SerializableFont SerializedNoteFont { get; set; }
		/// <summary>
		/// Gets or sets the settings used for tileset editor.
		/// </summary>
		public ImageColorSettings ImageColorSettings { get; set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		public EditorSettings()
		{
			this._maxRecent = 8;
			this.Location = new Point();
			this.Size = new Size(800, 600);
			this.WindowState = FormWindowState.Maximized;
			this.ShowSplash = false; // TODO: Change back to "true"
			this.RecentlyOpened = new List<string>(16);
			this.WindowSkin = new DockPanelSkin();
			this.Scripting = new ScriptSettings();
			this.Charting = new ChartSettings();
			this.SerializedNoteFont = FontHelper.MonoFont;
			this.ImageColorSettings = new ImageColorSettings();
		}

		/// <summary>
		/// Adds a value to the "Recently Opened" list and trims the list to the max allowed items
		/// </summary>
		/// <param name="filename">The filename to add</param>
		public void AddToRecent(string filename)
		{
			if (this.RecentlyOpened.Contains(filename))
				this.RecentlyOpened.Remove(filename);
			this.RecentlyOpened.Insert(0, filename);
			if (this.RecentlyOpened.Count > this.MaxRecent)
				this.RecentlyOpened.RemoveRange(this.MaxRecent - 1, this.RecentlyOpened.Count - this.MaxRecent);
		}

		/// <summary>
		/// Saves the settings files to disk in the AppData folder.
		/// </summary>
		/// <seealso cref="ARCed.Helpers.PathHelper"/>
		/// <seealso cref="ScriptSettings"/>
		/// <seealso cref="ARCed.UI.DockPanelSkin"/>
		public void Save()
		{
			try
			{
				Util.SaveXML(PathHelper.EditorSettings, this);
				Util.SaveXML(PathHelper.SkinSettings, this.WindowSkin);
				Util.SaveXML(PathHelper.ScriptSettings, this.Scripting);
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
		/// <seealso cref="ScriptSettings"/>
		/// <seealso cref="ARCed.UI.DockPanelSkin"/>
		public static EditorSettings Load()
		{
			var settings = new EditorSettings();
			if (File.Exists(PathHelper.EditorSettings))
				settings = Util.LoadXML<EditorSettings>(PathHelper.EditorSettings);
			if (File.Exists(PathHelper.SkinSettings))
				settings.WindowSkin = Util.LoadXML<DockPanelSkin>(PathHelper.SkinSettings);
			if (File.Exists(PathHelper.ScriptSettings))
				settings.Scripting = Util.LoadXML<ScriptSettings>(PathHelper.ScriptSettings);
			return settings;
		}

	}
}
