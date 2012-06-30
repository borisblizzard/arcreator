using System.Collections.Generic;
using System.Reflection;

namespace ARCed.Plugins
{
	/// <summary>
	/// Container for <paramref name="Plugin"/> objects
	/// </summary>
	public class PluginCollection : List<Plugin>
	{
		#region Public Properties

		/// <summary>
		/// Returns a list of all loaded assemblies
		/// </summary>
		public List<Assembly> Assemblies
		{
			get
			{
				List<Assembly> assemblies = new List<Assembly>();
				foreach (Plugin plugin in this)
					assemblies.Add(plugin.Assembly);
				return assemblies;
			}
		}

		/// <summary>
		/// Gets a list of all filenames in the collection
		/// </summary>
		public List<string> Filenames
		{
			get
			{
				List<string> filenames = new List<string>();
				foreach (Plugin plugin in this)
					filenames.Add(plugin.Filename);
				return filenames;
			}
		}

		/// <summary>
		/// Returns a sorted list of all plugin names
		/// </summary>
		public List<string> Names
		{
			get
			{
				List<string> names = new List<string>(Count);
				foreach (Plugin plugin in this)
					names.Add(plugin.Name);
				names.Sort();
				return names;
			}
		}

		#endregion
	}
}
