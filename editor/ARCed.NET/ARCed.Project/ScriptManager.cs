using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using System.Linq;
using System.Windows.Forms;

namespace ARCed.Scripting
{
	/// <summary>
	/// Class used for managing <paramref name="ARCed.Scripting.Script"/> objects. The functionality
	/// is a very loose wrapper for a list.
	/// </summary>
	public class ScriptManager
	{
		private static List<Script> _scripts;

		/// <summary>
		/// Gets a list of all loaded scripts
		/// </summary>
		public List<Script> Scripts
		{
			get { return _scripts; }
		}

		/// <summary>
		/// Returns a new instance of the ScriptManager
		/// </summary>
		/// <param name="parentDirectory">The parent directory of the scripts</param>
		public ScriptManager(string parentDirectory)
		{
			_scripts = new List<Script>();
			LoadScripts(parentDirectory);
		}

		/// <summary>
		/// Loads scripts from the default directory
		/// </summary>
		public void LoadScripts() { LoadScripts(Project.ScriptsDirectory); }

		/// <summary>
		/// Loads scripts from the given directory
		/// </summary>
		/// <param name="directory"></param>
		public void LoadScripts(string directory)
		{
			_scripts.Clear();
			foreach (string file in Directory.GetFiles(directory, "*.rb"))
				_scripts.Add(new Script(file));
			RefreshScriptIndices();
		}

		/// <summary>
		/// Adds a script into the manager
		/// </summary>
		/// <param name="script">The script to add</param>
		public void Add(Script script)
		{
			Scripts.Add(script);
			RefreshScriptIndices();
		}

		/// <summary>
		/// Adds a script into the manager
		/// </summary>
		/// <param name="path">The path of the script</param>
		/// <remarks>Only files with an ".rb" extension will be added</remarks>
		public void Add(string filename)
		{
			if (Path.GetExtension(filename) == ".rb")
			{
				Scripts.Add(new Script(filename));
				RefreshScriptIndices();
			}
		}

		/// <summary>
		/// Creates and adds multiple scripts into the manager
		/// </summary>
		/// <param name="scripts">An array of scripts</param>
		public void AddRange(IEnumerable<Script> scripts)
		{
			foreach (Script script in scripts)
				Scripts.Add(script);
			RefreshScriptIndices();
		}

		/// <summary>
		/// Creates and adds multiple scripts into the manager
		/// </summary>
		/// <param name="filenames">The filenames of the scripts</param>
		/// <remarks>Only files with an ".rb" extension will be added</remarks>
		public void AddRange(IEnumerable<string> filenames)
		{
			foreach (string filename in filenames)
			{
				if (Path.GetExtension(filename) == ".rb")
					Scripts.Add(new Script(filename));
			}
			RefreshScriptIndices();
		}

		/// <summary>
		/// Inserts a script at the given index
		/// </summary>
		/// <param name="script">The script to insert</param>
		/// <param name="index">The index where it will be inserted</param>
		public void Insert(Script script, int index)
		{
			Scripts.Insert(index, script);
			RefreshScriptIndices();
		}

		/// <summary>
		/// Removes the script from the manager
		/// </summary>
		/// <param name="script">The script to remove</param>
		public void Remove(Script script)
		{
			Scripts.Remove(script);
			RefreshScriptIndices();
		}

		/// <summary>
		/// Removes the script at the given index
		/// </summary>
		/// <param name="index">The index of the script</param>
		public void Remove(int index)
		{
			Scripts.RemoveAt(index);
			RefreshScriptIndices();
		}

		/// <summary>
		/// Saves the script at the given index
		/// </summary>
		/// <param name="index">The index of the script</param>
		/// <returns>Truth value of successful save</returns>
		public bool Save(int index)
		{
			return Scripts[index].Save();
		}

		/// <summary>
		/// Applies changes and saves all scripts to disk
		/// </summary>
		public void SaveAll()
		{
			List<string> errors = new List<string>();
			for (int i = 0; i < Scripts.Count; i++)
			{
				Scripts[i].Index = i;
				if (!Scripts[i].Save())
					errors.Add(Scripts[i].Title);
			}
			if (errors.Count > 0)
			{
				string msg = String.Format("Failed to save the following script(s):\n{0}",
					String.Join("\n\t", errors));
				MessageBox.Show(msg, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
			}
		}

		/// <summary>
		/// Returns a binding list to be used with form controls
		/// </summary>
		public BindingList<Script> BindingList
		{
			get
			{
				var binding = new BindingList<Script>(Scripts);
				binding.AllowNew = true;
				return binding;
			}
			set { _scripts = value.ToList<Script>(); }
		}

		/// <summary>
		/// Refreshes the indices of all loaded scripts to match their current position in the list
		/// </summary>
		public void RefreshScriptIndices()
		{
			for (int i = 0; i < Scripts.Count; i++)
				Scripts[i].Index = i;
		}

		/// <summary>
		/// Finds a and returns the script with the given filename.
		/// </summary>
		/// <param name="path">The path to script to be found</param>
		/// <returns>The path to the script if found, null otherwise</returns>
		public Script WithPath(string path)
		{
			return _scripts.Find(delegate(Script s) { return s.Filename == path; });
		}
	}
}
