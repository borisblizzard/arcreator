#region Using Directives

using System.Collections.Generic;
using System.Linq;
using System.Reflection;

#endregion

namespace ARCed.Plugins
{
	/// <summary>
    /// Container for <see crefe="Plugin"/> objects
	/// </summary>
	public class PluginCollection : List<Plugin>
	{
		#region Public Properties

		/// <summary>
		/// Returns a list of all loaded assemblies
		/// </summary>
		public List<Assembly> Assemblies
		{
			get { return this.Select(plugin => plugin.Assembly).ToList(); }
		}

		/// <summary>
		/// Gets a list of all filenames in the collection
		/// </summary>
		public List<string> Filenames
		{
			get { return this.Select(plugin => plugin.Filename).ToList(); }
		}

		/// <summary>
		/// Returns a sorted list of all plugin names
		/// </summary>
		public List<string> Names
		{
			get
			{
				var names = new List<string>(Count);
			    names.AddRange(this.Select(plugin => plugin.Name));
			    names.Sort();
				return names;
			}
		}

		#endregion
	}
}
