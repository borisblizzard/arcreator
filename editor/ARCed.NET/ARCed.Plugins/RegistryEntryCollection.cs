using System;
using System.Collections.Generic;
using ARCed.UI;

namespace ARCed.Plugins
{
	/// <summary>
	/// Container for <paramref name="RegistryEntry"/> objects
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
				List<string> names = new List<string>();
				foreach (RegistryEntry entry in this)
					names.Add(entry.Name);
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
				List<string> names = new List<string>();
				foreach (RegistryEntry entry in this)
					names.Add(entry.ClassName);
				names.Sort();
				return names;
			}
		}
		/// <summary>
		/// Gets a list of all types found in the collection
		/// </summary>
		public List<Type> Types
		{
			get
			{
				List<Type> types = new List<Type>();
				foreach (RegistryEntry entry in this)
					types.Add(entry.ClassType);
				return types;
			}
		}
		/// <summary>
		/// Gets a collection of all associated DockContent for the entries
		/// </summary>
		public DockContentCollection Contents
		{
			get
			{
				DockContentCollection contents = new DockContentCollection();
				foreach (RegistryEntry entry in this)
					contents.Add(entry.Content);
				return contents;
			}
		}

		#endregion
	}
}
