#region Using Directives

using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
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
		public string Filename { get { return _assembly.Location; } }
		/// <summary>
		/// Gets a flag indicating the plugin loaded without errors
		/// </summary>
		public bool IsLoaded { get; private set; }
		/// <summary>
		/// The associated <paramref name="System.Reflection.Assembly"/> instance of the plugin
		/// </summary>
		public Assembly Assembly { get { return _assembly; } }
		/// <summary>
		/// The associated <paramref name="System.Reflection.AssemblyName"/> instance of the plugin
		/// </summary>
		public AssemblyName AssemblyName { get { return _assembly.GetName(); } }
		/// <summary>
		/// Gets the file <paramref name="System.Version"/> of the associated assembly 
		/// </summary>
		public Version Version { get { return _assembly.GetName().Version; } }
		/// <summary>
		/// Gets the simple name of the associated assembly
		/// </summary>
		public string Name { get { return _assembly.GetName().Name; } }
		/// <summary>
		/// Gets the plugin's host
		/// </summary>
		public IPluginHost Host { get { return _host; } }

		#endregion

		#region Private Fields

		private Assembly _assembly;
		private IPluginHost _host;
		private Dictionary<string, string> _data;

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
				_host = host;
				_assembly = Assembly.LoadFile(filename);
				List<DictionaryEntry> config = ReadResourceConfiguration(_assembly);
				_data = GetRegistryClasses(config);
				GetEntries();
				IsLoaded = true;
			}
			catch { IsLoaded = false; }
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Generates and returns a list of entries to be added to the ARCed Registry
		/// </summary>
		/// <returns>The list of entries</returns>
		public List<RegistryEntry> GetEntries()
		{
			List<RegistryEntry> entries = new List<RegistryEntry>(_data.Count);
			foreach (var kvp in _data)
			{
				Type type = _assembly.GetType(kvp.Value);
				RegistryEntry entry = new RegistryEntry(this, type, kvp.Key, kvp.Value);
				entries.Add(entry);
			}
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
		private static List<DictionaryEntry>  ReadResourceConfiguration(Assembly assembly)
		{
			List<DictionaryEntry> config = new List<DictionaryEntry>();
			foreach (string resName in assembly.GetManifestResourceNames())
			{
				using (Stream stream = assembly.GetManifestResourceStream(resName))
				{
					using (ResourceReader reader = new ResourceReader(stream))
					{
						IDictionaryEnumerator kvp = reader.GetEnumerator();
						while (kvp.MoveNext())
							config.Add(kvp.Entry);
					}
				}
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
		private static Dictionary<string, string> GetRegistryClasses(List<DictionaryEntry> config)
		{
			var data = new Dictionary<string,string>();
			foreach (DictionaryEntry entry in config)
			{
				if (entry.Key.ToString().StartsWith("RegistyPlugin"))
				{
					string[] classNames = entry.Value.ToString().Split('|');
					data[classNames[0]] = classNames[1];
				}
			}
			return data;
		}

		#endregion
	}
}

