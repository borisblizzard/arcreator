#region Using Directives

using System;
using System.IO;
using System.Text;

#endregion

namespace ARCed.Scripting
{
	/// <summary>
	/// Represents a script file
	/// </summary>
	public class Script
	{
        /// <summary>
        /// Gets an empty script object.
        /// </summary>
        public static readonly Script DummyScript = new Script();

		#region Private Fields

		private string _text;
		private string _title;
		private int _index;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the associated text of the script
		/// </summary>
		public string Text { get { return this._text; } set { this.SetText(value); } }
		/// <summary>
		/// Gets or sets the title of the script.
		/// </summary>
		/// <remarks>Titles may not contain characters that are invalid for filenames</remarks>
		public string Title { get { return this._title; } set { this.SetTitle(value); } }
		/// <summary>
		/// Gets or sets the index of the script
		/// </summary>
		public int Index { get { return this._index; } set { this.SetIndex(value); } }
		/// <summary>
		/// Gets the path to the script file, relative to the main project folder
		/// </summary>
		public string Filename { get { return this.GetFullPath(); } }
		/// <summary>
		/// Gets the flag if the script has been altered and requires saving the changes
		/// </summary>
		public bool NeedSaved { get; private set; }
		/// <summary>
		/// Gets file information for this script, or null if file does not exist.
		/// </summary>
		public FileInfo FileInfo
		{
			get
			{
				try { return new FileInfo(this.Filename); }
				catch { return null; }
			}
		}

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public Script()
		{
			this._index = 0;
			this._title = "";
			this._text = "";
			this.NeedSaved = true;
		}

		/// <summary>
		/// Parametered constructor to load a script after construction
		/// </summary>
		/// <param name="filename">The filename of the script to load</param>
		public Script(string filename) : this()
		{
			this.Load(filename);
			filename = Path.GetFileName(filename);
            if (String.IsNullOrEmpty(filename))
                return;
			try { this._index = Convert.ToInt32(filename.Substring(0, 4)); }
			catch { this._index = 0; this.NeedSaved = true; }
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Saves the script to disk using generated filename
		/// </summary>
		/// <returns>Flag if save was successful or not</returns>
		public bool Save()
		{
			try 
			{ 
				File.WriteAllText(this.GetFullPath(), this._text, Encoding.UTF8);
				this.NeedSaved = false;
				return true;
			}
			catch (IOException) { return false; }
		}

		/// <summary>
		/// Loads a script file from the given path
		/// </summary>
		/// <param name="filename">The path to the script</param>
		/// <returns>Flag if script was successfully loaded or not</returns>
		public bool Load(string filename)
		{
			try
			{
				this._text = File.ReadAllText(filename, Encoding.UTF8).Replace("  ", "\t");
				filename = Path.GetFileNameWithoutExtension(filename);
                if (String.IsNullOrEmpty(filename))
                    return false;
				this._title = filename.Substring(5, filename.Length - 5);
				this.NeedSaved = false;
				return true;
			}
			catch 
			{
				this._text = "";
				this._title = "";
				this.NeedSaved = true;
				return false;
			}
		}

		/// <summary>
		/// Reloads the script from file
		/// </summary>
		public void Reload()
		{
			if (File.Exists(this.Filename))
				this.Load(this.Filename);
		}

		/// <summary>
		/// Uses the index and title of the script to create a unique filename
		/// </summary>
		/// <returns>The path for the script</returns>
		public string GetFullPath()
		{
			string filename = String.Format("{0:d4}-{1}.rb", this._index, this._title);
			return Path.Combine(Project.ScriptsDirectory, filename);
		}

		/// <summary>
		/// Checks if the script has a associated file
		/// </summary>
		/// <returns>Flag if script file exists for the script</returns>
		public bool Exists()
		{
			return File.Exists(this.GetFullPath());
		}

		#endregion

		#region Private Methods

		/// <summary>
		/// Sets the title of the script
		/// </summary>
		/// <param name="title">The title of the script</param>
		private void SetTitle(string title)
		{
			if (title != this._title)
			{
				this._title = title;
				this.NeedSaved = true;
			}
		}

		/// <summary>
		/// Sets the text of the script
		/// </summary>
		/// <param name="text">The text of the script</param>
		private void SetText(string text)
		{
			this._text = text;
			this.NeedSaved = true;
		}

		/// <summary>
		/// Sets the index of the script
		/// </summary>
		/// <param name="index">The script index</param>
		private void SetIndex(int index)
		{
			if (index != this._index)
			{
				this._index = index;
				this.NeedSaved = true;
			}
		}

		#endregion
	}
}
