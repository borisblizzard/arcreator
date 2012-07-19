#region Using Directives

using System;
using System.Globalization;
using System.IO;
using System.Reflection;
using System.Text;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed
{
	/// <summary>
	/// Static class that extends functionality of various data types
	/// </summary>
	public static class ExtensionMethods
	{
		#region Private Fields

		/// <summary>
		/// UTF-8 encoding instance used for byte-string conversions
		/// </summary>
		private static readonly UTF8Encoding _utf8 = new UTF8Encoding();
		/// <summary>
		/// Byte array used as a buffer for reading streams
		/// </summary>
		private static byte[] _buffer;

		#endregion

        /// <summary>
        /// Rounds an <seealso langword="int"/> down to the nearest multiple.
        /// </summary>
        /// <param name="value">Integer to round</param>
        /// <param name="multiple">Multiple to round down to.</param>
        /// <returns>The rounded number</returns>
		public static int RoundFloor(this int value, int multiple)
		{
			return ((int)Math.Floor(value / Convert.ToSingle(multiple))) * multiple;
		}

        /// <summary>
        /// Rounds an <seealso langword="int"/> up to the nearest multiple.
        /// </summary>
        /// <param name="value">Integer to round</param>
        /// <param name="multiple">Multiple to round up to.</param>
        /// <returns>The rounded number</returns>
		public static int RoundCeil(this int value, int multiple)
		{
			return ((int)Math.Ceiling(value / Convert.ToSingle(multiple))) * multiple;
		}

		/// <summary>
		/// Suspends painting of control until ResumePainting() is called.
		/// </summary>
		/// <param name="control">Control to suspend painting</param>
		public static void SuspendPainting(this Control control)
		{
			NativeMethods.SendMessage(control.Handle, NativeMethods.WM_SETREDRAW, false, 0);
		}

		/// <summary>
		/// Resumes painting of the control that was suspended with SuspendPainting().
		/// </summary>
		/// <param name="control">Control to resume painting</param>
		/// <param name="refresh">Flag to refresh control.</param>
		public static void ResumePainting(this Control control, bool refresh)
		{
			NativeMethods.SendMessage(control.Handle, NativeMethods.WM_SETREDRAW, true, 0);
			if (refresh)
				control.Refresh();
		}

		/// <summary>
		/// Pads the center of a string with the given character
		/// </summary>
		/// <param name="str">String to pad</param>
		/// <param name="width">The width of the string</param>
		/// <param name="chr">Character to pad with</param>
		/// <returns>The string padded in the center</returns>
		public static string PadCenter(this string str, int width, char chr)
		{
			if (str == null || width <= str.Length) return str;
			int padding = width - str.Length;
			return str.PadLeft(str.Length + padding / 2, chr).PadRight(width, chr);
		}

		/// <summary>
		/// Gets the number of digits in a number
		/// </summary>
		/// <param name="value">Integer to get digits of</param>
		/// <returns>Number of digits counted</returns>
		public static int NumberDigits(this int value)
		{
			return value.ToString(CultureInfo.InvariantCulture).Length;
		}

		/// <summary>
		/// Reads the specified number of bytes from the stream and returns it as a UTF-8 encoded string
		/// </summary>
		/// <param name="stream">Stream to read</param>
		/// <param name="numBytes">Number of bytes to read</param>
		/// <returns>UTF-8 encoded string</returns>
		public static string ReadByteString(this Stream stream, int numBytes)
		{
			return stream.ReadBytes(numBytes).GetString();
		}

		/// <summary>
		/// Reads the specified number of bytes from the current position if the stream
		/// </summary>
		/// <param name="stream">Stream to read</param>
		/// <param name="numBytes">Number of bytes to read</param>
		/// <returns>Array of bytes that were read</returns>
		public static byte[] ReadBytes(this Stream stream, int numBytes)
		{
			_buffer = new byte[numBytes];
			stream.Read(_buffer, 0, numBytes);
			return _buffer;
		}

		/// <summary>
		/// Returns a UTF-8 encoded string from an array of bytes
		/// </summary>
		/// <param name="value">Array of bytes to convert</param>
		/// <returns>UTF-8 encoded string</returns>
		public static string GetString(this byte[] value)
		{
			return _utf8.GetString(value);
		}

		/// <summary>
		/// Returns the string as an array of bytes
		/// </summary>
		/// <param name="value">String value to convert</param>
		/// <returns>Array of bytes</returns>
		/// <remarks>The string is assumed to be encoded using UTF-8</remarks>
		public static byte[] GetBytes(this string value)
		{
			return _utf8.GetBytes(value);
		}

		/// <summary>
		/// Gets a byte array of the value
		/// </summary>
		/// <param name="value">Short value</param>
		/// <returns>Two element byte array</returns>
		public static byte[] GetBytes(this short value)
		{
			byte[] bytes = BitConverter.GetBytes(value);
			if (!BitConverter.IsLittleEndian)
				Array.Reverse(bytes);
			return bytes;
		}

		/// <summary>
		/// Gets a byte array of the value
		/// </summary>
		/// <param name="value">Integer value</param>
		/// <returns>Four element byte array</returns>
		public static byte[] GetBytes(this int value)
		{
			byte[] bytes = BitConverter.GetBytes(value);
			if (!BitConverter.IsLittleEndian)
				Array.Reverse(bytes);
			return bytes;
		}

		/// <summary>
		/// Checks if integer is between an upper and lower range
		/// </summary>
		/// <param name="value">Integer value to compare</param>
		/// <param name="lower">Lower limit to check</param>
		/// <param name="upper">Upper limit to check</param>
		/// <returns>True if value is withing range, otherwise false</returns>
		/// <remarks>Comparison is inclusive for upper and lower</remarks>
		public static bool IsBetween(this int value, int lower, int upper) 
		{
			return value <= upper && value >= lower;
		}

		/// <summary>
		/// Clamps a value within a given minimum and maximum
		/// </summary>
		/// <typeparam name="T">Type of object that interfaces IComparable</typeparam>
		/// <param name="value">Value of object</param>
		/// <param name="min">Minimum value that will be returned</param>
		/// <param name="max">Maximum value that will be returned</param>
		/// <returns>Value clamped between the minimum and maximum</returns>
		public static T Clamp<T>(this T value, T min, T max) where T : IComparable
		{
			if (value.CompareTo(min) < 0) return min;
			return value.CompareTo(max) > 0 ? max : value;
		}

		/// <summary>
		/// Checks an object if it us a numerical type
		/// </summary>
		/// <param name="value">Object to check</param>
		/// <returns>Flag if object is numerical or not</returns>
		public static bool IsNumber(this object value)
		{
			if (value is sbyte) return true;
			if (value is byte) return true;
			if (value is short) return true;
			if (value is ushort) return true;
			if (value is int) return true;
			if (value is uint) return true;
			if (value is long) return true;
			if (value is ulong) return true;
			if (value is float) return true;
			if (value is double) return true;
			return value is decimal;
		}

		/// <summary>
		/// Checks if a type has the given method and returns the result
		/// </summary>
		/// <param name="objectToCheck">Object to check for the method</param>
		/// <param name="methodName">String name of the method</param>
		/// <returns>Flag if object type has given method</returns>
		/// <remarks>CharacterStance case of the string will be ignored</remarks>
		public static bool HasMethod(this object objectToCheck, string methodName)
		{
			var type = objectToCheck.GetType();
			return type.GetMethod(methodName, BindingFlags.IgnoreCase) != null;
		} 
	}
}
