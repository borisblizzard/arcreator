using System;
using System.IO;
using System.Text;
using ARCed.Core.Win32;

namespace ARCed.Helpers
{
	public static class Ini
	{
		#region Private Fields
		private static string _filename;
		private static StringBuilder _buffer;
		#endregion

		/// <summary>
		/// Prepares the file to be read by the parser
		/// </summary>
		/// <param name="path">The path to be parsed</param>
		/// <returns>Flag is file was successfully loaded</returns>
		public static bool Load(string filename)
		{
			if (_buffer == null)
				_buffer = new StringBuilder(256);
			_filename = File.Exists(filename) ? filename : null;
			return _filename != null;
		}

		/// <summary>
		/// Writes a value to the .ini file
		/// </summary>
		/// <param name="section">The section of the .ini file</param>
		/// <param name="key">A key name in the .ini file</param>
		/// <param name="value">The value to write</param>
		public static void Write(string section, string key, string value)
		{
			if (_filename != null)
				NativeMethods.WritePrivateProfileString(section, key, value, _filename);
		}

		/// <summary>
		/// Returns a string value read from the file
		/// </summary>
		/// <param name="section">The section of the .ini file</param>
		/// <param name="key">A key name in the .ini file</param>
		/// <returns>The read value</returns>
		public static string ReadString(string section, string key)
		{
			if (_filename != null)
			{
				_buffer.Clear();
				NativeMethods.GetPrivateProfileString(section, key, "", _buffer, 256, _filename);
				return _buffer.ToString();
			}
			return "";
		}

		/// <summary>
		/// Returns an integer value read from the file
		/// </summary>
		/// <param name="section">The section of the .ini file</param>
		/// <param name="key">A key name in the .ini file</param>
		/// <returns>A value converted to a integer</returns>
		public static int ReadInteger(string section, string key)
		{
			return Convert.ToInt32(ReadString(section, key));
		}

		/// <summary>
		/// Returns a float value read from the file
		/// </summary>
		/// <param name="section">The section of the .ini file</param>
		/// <param name="key">A key name in the .ini file</param>
		/// <returns>A value converted to a float</returns>
		public static float ReadFloat(string section, string key)
		{
			return Convert.ToSingle(ReadString(section, key));
		}

		/// <summary>
		/// Returns an array of values from splitting a string
		/// </summary>
		/// <param name="section">The section of the .ini file</param>
		/// <param name="key">A key name in the .ini file</param>
		/// <param name="separator">The separator string used for splitting</param>
		/// <returns>An string array of read values</returns>
		public static string[] ReadStringSplit(string section, string key, char separator)
		{
			return ReadString(section, key).Split(separator);
		}

	}
}
