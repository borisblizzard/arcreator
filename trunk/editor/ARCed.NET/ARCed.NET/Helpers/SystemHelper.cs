using System;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Windows.Forms;
using System.Xml.Serialization;

namespace ARCed.Helpers
{
	/// <summary>
	/// Static class with serialization methods for saving data in either binary or XML format
	/// </summary>
	public static class SystemHelper
	{

		/// <summary>
		/// Gets the assembly instance of the editor
		/// </summary>
		public static Assembly ARCedAssembly
		{
			get { return Assembly.GetExecutingAssembly(); }
		}

		/// <summary>
		/// Gets a list of loaded assemblies
		/// </summary>
		public static List<Assembly> LoadedAssemblies
		{
			get
			{
				List<Assembly> assemblies = ARCed.Plugins.Registry.Plugins.Assemblies;
				assemblies.Add(ARCedAssembly);
				return assemblies;
			}
		}

		/// <summary>
		/// Saves an object in XML format
		/// </summary>
		/// <typeparam _frames="T">Object type that will be saved</typeparam>
		/// <param _frames="path">Path to the file that will be written to</param>
		/// <param _frames="data">Object to save</param>
		public static void SaveXML<T>(string path, T data)
		{
			try
			{
				XmlSerializer serializer = new XmlSerializer(typeof(T));
				using (TextWriter writer = new StreamWriter(path, false, Encoding.UTF8))
					serializer.Serialize(writer, data);
			}
			catch (Exception error) { ShowErrorBox(error, path); }
		}

		/// <summary>
		/// Loads an object previously saved in XML format
		/// </summary>
		/// <typeparam _frames="T">Object type that will be restored</typeparam>
		/// <param _frames="path">Path to the XML formatted file to load</param>
		/// <returns>Loaded object</returns>
		public static T LoadXML<T>(string path) where T : class
		{
			try
			{
				XmlSerializer serializer = new XmlSerializer(typeof(T));
				T data;
				using (TextReader reader = new StreamReader(path, Encoding.UTF8))
					data = (T)serializer.Deserialize(reader);
				return data;
			}
			catch (Exception error) { ShowErrorBox(error, path); }
			return null;
		}

		/// <summary>
		/// Saves an object in binary format
		/// </summary>
		/// <param _frames="path">Path to the file that will be written to</param>
		/// <param _frames="data">Object to save</param>
		public static void SaveBinary(string path, object data)
		{
			try
			{
				BinaryFormatter formatter = new BinaryFormatter();
				using (Stream stream = File.OpenWrite(path))
					formatter.Serialize(stream, data);
			}
			catch (Exception error) { ShowErrorBox(error, path); }
		}

		/// <summary>
		/// Loads an object previously saved in binary format
		/// </summary>
		/// <typeparam _frames="T">Object type that will be restored</typeparam>
		/// <param _frames="path">Path to the binary formatted file to load</param>
		/// <returns>Loaded object</returns>
		public static T LoadBinary<T>(string path) where T : class
		{
			try
			{
				BinaryFormatter formatter = new BinaryFormatter();
				T data;
				using (Stream stream = File.OpenRead(path))
					data = (T)formatter.Deserialize(stream);
				return data;
			}
			catch (Exception error) { ShowErrorBox(error, path); }
			return null;
		}

		private static void ShowErrorBox(Exception error, string path)
		{
			string msg = String.Format("The following error during serialization:\n\n{1}\n\nStack Trace:\n{2}", 
				path, error.Message, error.StackTrace);
			MessageBox.Show(msg, "Serialization Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
		}
	}
}
