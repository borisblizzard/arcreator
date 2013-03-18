#region Using Directives

using System;
using System.Collections.Generic;
using System.Linq;
using ARCed.UI;

#endregion

namespace ARCed.Plugins
{
	/// <summary>
    /// Container for <see cref="RegistryEntry"/> objects
	/// </summary>
	public class RegistryEntryCollection : List<RegistryEntry>
	{
		#region Public Properties

		/// <summary>
		/// Gets a sorted list of all names found in the collection
		/// </summary>
		public List<string> Names
		{
			get
			{
				var names = this.Select(entry => entry.Name).ToList();
			    names.Sort();
				return names;
			}
		}
		/// <summary>
		/// Gets a sorted list of all class names found in the collection
		/// </summary>
		public List<string> ClassNames
		{
			get
			{
				var names = this.Select(entry => entry.ClassName).ToList();
			    names.Sort();
				return names;
			}
		}
		/// <summary>
		/// Gets a list of all types found in the collection
		/// </summary>
		public List<Type> Types
		{
			get { return this.Select(entry => entry.ClassType).ToList(); }
		}
		/// <summary>
		/// Gets a collection of all associated DockContent for the entries
		/// </summary>
		public DockContentCollection Contents
		{
			get
			{
				var contents = new DockContentCollection();
				foreach (var entry in this)
					contents.Add(entry.Content);
				return contents;
			}
		}

		#endregion
	}
}
