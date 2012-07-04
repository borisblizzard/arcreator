using System;
using System.Collections;
using System.IO;
using System.Linq;
using ARCed.Helpers;

namespace ARCed.Data
{
	/// <summary>
	/// Enum containing flags for various resource types
	/// </summary>
	public enum ResourceType
	{
		/// <summary>
		/// Unknown type
		/// </summary>
		Unknown,
		/// <summary>
		/// Flag for a graphic resource
		/// </summary>
		Graphics,
		/// <summary>
		/// Flag for an audio resource
		/// </summary>
		Audio,
		/// <summary>
		/// Flag for a script file
		/// </summary>
		Script
	}

	/// <summary>
	/// Enum containing flags for various of resource types
	/// </summary>
	public enum Location
	{
		/// <summary>
		/// Flag for an unknown/undefined location
		/// </summary>
		Unknown,
		/// <summary>
		/// Flag for a resource local to the project
		/// </summary>
		Local,
		/// <summary>
		/// Flag for a resource located in the host machine's RTP directory
		/// </summary>
		RTP
	}

	/// <summary>
	/// Base class for resource classes
	/// </summary>
	public class GameResource : IComparable
	{
		#region Public Properties

		/// <summary>
		/// Directory relative to the main directory the resource is found in
		/// </summary>
		public string Directory { get { return FileInfo.DirectoryName; } }
		/// <summary>
		/// FullPath of the resource
		/// </summary>
		public string FullPath { get { return FileInfo.FullName; } }
		/// <summary>
		/// The type of the resource
		/// </summary>
		public ResourceType ResourceType { get; protected set; }
		/// <summary>
		/// Gets or sets the location parameter determining if resource is local or ResourceHelper
		/// </summary>
		public Location Location { get; set; }
		/// <summary>
		/// Gets the name of the file without directory or extension
		/// </summary>
		public string Name { get { return Path.GetFileNameWithoutExtension(FileInfo.Name); } }
		/// <summary>
		/// Gets the extension of the file
		/// </summary>
		public string FileExtension { get { return FileInfo.Extension; } }
		/// <summary>
		/// Gets a path that is relative to both the project and RTP directory
		/// </summary>
		public string RelativePath
		{
			get 
			{
				string path;
				if (Location == Location.Local)
					path = FullPath.Replace(System.IO.Directory.GetCurrentDirectory(), "");
				else
					path = FullPath.Replace(Constants.RTP_PATH, "");
				return path.TrimStart('\\', '.');
			}
		}
		/// <summary>
		/// Returns the relative directory of the resource from the root folder
		/// </summary>
		public string RelativeDirectory { get { return Path.GetDirectoryName(RelativePath); } }

		/// <summary>
		/// Gets the FileInfo object for the file
		/// </summary>
		public FileInfo FileInfo { get; set; }

		#endregion

		#region Construction

		/// <summary>
		/// Constructor with parameters
		/// </summary>
		/// <param name="filename">Filename of the resource</param>
		/// <param name="location">Flag for resource location</param>
		/// <param name="type">Flag for resource type</param>
		public GameResource(string filename, Location location, ResourceType type)
		{
			if (!string.IsNullOrWhiteSpace(filename))
				FileInfo = new FileInfo(filename);
			Location = location;
			if (type == ResourceType.Unknown)
			{
				// Try to determine type based off file extension
				string ext = "*" + Path.GetExtension(filename);
				if (ResourceHelper.ImageFilters.Contains(ext)) type = ResourceType.Graphics;
				else if (ResourceHelper.AudioFilters.Contains(ext)) type = ResourceType.Audio;
			}
			ResourceType = type;
		}

		/// <summary>
		/// Compares two GameResource objects. Local resources are listed first, names are 
		/// sorted alphabetically within their location.
		/// </summary>
		/// <param name="other">GameResource object to compare</param>
		/// <returns>Integer comparison flag</returns>
		/// <exception cref="ArgumentException">Thrown when object to compare is not a GameResource</exception>
		public int CompareTo(object other)
		{
			GameResource rsx;
			if (other is GameResource)
				rsx = other as GameResource;
			else
				throw new ArgumentException("Object is not of type \"GameResource\"");
			if (this.Location == Location.Local && rsx.Location != Location.Local)
				return -1;
			else if (this.Location == Location.RTP && rsx.Location == Location.Local)
				return 1;
			else
				return this.Name.CompareTo(rsx.Name);
		}

		public static int Compare(object obj1, object obj2)
		{
			return new ResourceComparer().Compare(obj1, obj2);
		}

		private class ResourceComparer : IComparer
		{
			public int Compare(object obj1, object obj2)
			{
				GameResource rsx1, rsx2;
				if (obj1 is GameResource)
					rsx1 = obj1 as GameResource;
				else
					throw new ArgumentException("Object is not of type \"GameResource\"");
				if (obj2 is GameResource)
					rsx2 = obj2 as GameResource;
				else
					throw new ArgumentException("Object is not of type \"GameResource\"");
				return rsx1.CompareTo(rsx2);
			}
		}

		#endregion
	}

}
