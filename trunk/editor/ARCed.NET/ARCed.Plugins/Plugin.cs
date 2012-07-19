#region Using Directives

using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Resources;

#endregion

namespace ARCed.Plugins
{
	/// <summary>
	/// This class is used for loading and processing of plugins.
	/// It acts as a handle for control between the assemblies.
	/// </summary>
	/// <seealso cref="IPluginClient"/>
	/// <seealso cref="IPluginHost"/>
	public class Plugin
	{
		#region Public Properties

		/// <summary>
		/// Gets the filename to the plugin assembly
		/// </summary>
		public string Filename { get { return this._assembly.Location; } }
		/// <summary>
		/// Gets a flag indicating the plugin loaded without errors
		/// </summary>
		public bool IsLoaded { get; private set; }
		/// <summary>
		/// The associated <see cref="System.Reflection.Assembly"/> instance of the plugin
		/// </summary>
		public Assembly Assembly { get { return this._assembly; } }
		/// <summary>
        /// The associated <see cref="System.Reflection.AssemblyName"/> instance of the plugin
		/// </summary>
		public AssemblyName AssemblyName { get { return this._assembly.GetName(); } }
		/// <summary>
        /// Gets the file <see cref="System.Version"/> of the associated assembly 
		/// </summary>
		public Version Version { get { return this._assembly.GetName().Version; } }
		/// <summary>
		/// Gets the simple name of the associated assembly
		/// </summary>
		public string Name { get { return this._assembly.GetName().Name; } }
		/// <summary>
		/// Gets the plugin's host
		/// </summary>
		public IPluginHost Host { get { return this._host; } }

		#endregion

		#region Private Fields

		private readonly Assembly _assembly;
		private readonly IPluginHost _host;
		private readonly Dictionary<string, string> _data;

		#endregion

		#region Construction

		/// <summary>
		/// Creates a new Plugin instance
		/// </summary>
		/// <param name="filename">The filename to the assembly that contains the plugin</param>
		/// <param name="host">The host form that will be using the plugin</param>
		public Plugin(string filename, IPluginHost host)
		{
			try
			{
				this._host = host;
				this._assembly = Assembly.LoadFile(filename);
				var config = ReadResourceConfiguration(this._assembly);
				this._data = GetRegistryClasses(config);
				this.GetEntries();
				this.IsLoaded = true;
			}
			catch { this.IsLoaded = false; }
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Generates and returns a list of entries to be added to the ARCed Registry
		/// </summary>
		/// <returns>The list of entries</returns>
		public List<RegistryEntry> GetEntries()
		{
			var entries = new List<RegistryEntry>(this._data.Count);
		    entries.AddRange(from kvp in this._data
		        let type = this._assembly.GetType(kvp.Value)
		        select new RegistryEntry(this, type, kvp.Key, kvp.Value));
		    return entries;
		}

		#endregion

		#region Private Methods

		/// <summary>
		/// Reads the assembly's resource files for the configuration strings used in 
		/// creating the windows
		/// </summary>
		/// <param name="assembly">The assembly to check for resource files</param>
		/// <returns>A list of key/values pairs, the keys being the simple name to display
		/// in the GUI, and the values being the full name of the type including namespaces</returns>
		private static IEnumerable<DictionaryEntry> ReadResourceConfiguration(Assembly assembly)
		{
			var config = new List<DictionaryEntry>();
		    foreach (var resName in assembly.GetManifestResourceNames())
		        using (var stream = assembly.GetManifestResourceStream(resName))
		            if (stream != null)
		                using (var reader = new ResourceReader(stream))
		                {
		                    var kvp = reader.GetEnumerator();
		                    while (kvp.MoveNext())
		                        config.Add(kvp.Entry);
		                }
		    return config;
		}

		/// <summary>
		/// Generates a dictionary of simple and full names of registerable windows found
		/// </summary>
		/// <param name="config">A list of resource key/value pairs, the key being the name of
		/// the resouce, and the value being the value of the resouce</param>
		/// <returns>A dictionary of key/values pairs, the keys being the simple name to display
		/// in the GUI, and the values being the full name of the type including namespaces</returns>
		private static Dictionary<string, string> GetRegistryClasses(IEnumerable<DictionaryEntry> config)
		{
			var data = new Dictionary<string,string>();
			foreach (var classNames in from entry in config
			    where entry.Key.ToString().StartsWith("RegistyPlugin")
			    select entry.Value.ToString().Split('|'))
			{
			    data[classNames[0]] = classNames[1];
			}
			return data;
		}

		#endregion
	}
}

