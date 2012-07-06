﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Reflection;
using System.IO;
using System.Text.RegularExpressions;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;

namespace ARCed.Helpers
{
	public static class Util
	{
		private static Random random;

		/// <summary>
		/// Clamp to values of type T within a defined range
		/// </summary>
		/// <typeparam name="T">The <see cref="System.Type"/> of the that will be passed and returned. Must implement the <see cref="System.IComparable"/> interface</typeparam>
		/// <param name="val">The value to clamp</param>
		/// <param name="min">The minimum allowed value</param>
		/// <param name="_maxBackups">The maximum allowed value</param>
		/// <returns>The value clamped between the minimum and maximum</returns>
		public static T Clamp<T>(T val, T min, T max) where T : IComparable<T>
		{
			if (val.CompareTo(min) < 0) return min;
			else if (val.CompareTo(max) > 0) return max;
			else return val;
		}

		/// <summary>
		/// Calculates the parameter value of a curve at the given level
		/// </summary>
		/// <param name="min">The lowest value value at the starting point of the curve</param>
		/// <param name="_maxBackups">The greatest value at the end of the curve</param>
		/// <param name="speed">The "pitch" of the curve</param>
		/// <param name="level">The level to calculate the value for (x coordinate)</param>
		/// <param name="initial">The initial level that the curve begins generation</param>
		/// <param name="final">The final level that the curve ends generation</param>
		/// <returns>The calculated value for the curve at the given level</returns>
		public static int GenerateParameter
			(int min, int max, int speed, int level, int initial, int final)
		{
			speed = Clamp<int>(speed, -10, 10);
			float curve;
			int pRange = max - min;
			float lRange = Convert.ToSingle(final - initial);
			int linear = Convert.ToInt32(min + pRange * ((level - initial) / lRange));
			if (speed == 0)
				return linear;
			else if (speed < 0)
				curve = min + pRange * (float)Math.Pow(((level - initial) / lRange), 2);
			else
				curve = max - pRange * (float)Math.Pow(((final - level) / lRange), 2);
			return ((Convert.ToInt32(curve) * Math.Abs(speed) + linear * (10 - Math.Abs(speed))) / 10);
		}

		/// <summary>
		/// Gets a random number between two given values
		/// </summary>
		/// <param name="minimum">The minimum threshold</param>
		/// <param name="maximum">The maximum threshold</param>
		/// <returns>A randomly generated number</returns>
		public static double GetRandomBetween(double minimum, double maximum)
		{
			if (random == null)
				random = new Random();
			return random.NextDouble() * (maximum - minimum) + minimum;
		}

		/// <summary>
		/// Copies an embedded resource to an external place on the hard-drive
		/// </summary>
		/// <param name="path">The path the resource will be saved to</param>
		public static void ExtractResource(string resource, string path)
		{
			using (Stream s = Assembly.GetExecutingAssembly().GetManifestResourceStream(resource))
			using (FileStream resourceFile = new FileStream(path, FileMode.Create))
			{
				byte[] b = new byte[s.Length + 1];
				s.Read(b, 0, Convert.ToInt32(s.Length));
				resourceFile.Write(b, 0, Convert.ToInt32(b.Length - 1));
				resourceFile.Flush();
			}
		}

		/// <summary>
		/// Validates a string by replacing any illegal path characters
		/// </summary>
		/// <param name="name">The text of the path</param>
		/// <param name="replace">Replacement string for invalid characters</param>
		/// <returns>A santized string valid for a path</returns>
		public static string ValidateFilename(string name, string replace = "")
		{
			string invalidChars = Regex.Escape(new string(Path.GetInvalidFileNameChars()));
			string invalidReStr = string.Format(@"[{0}]+", invalidChars);
			return Regex.Replace(name, invalidReStr, replace);
		}

		/// <summary>
		/// Ensures that all characters in the textbox field are valid for a path
		/// </summary>
		/// <param name="textBox">The textbox to check</param>
		/// <param name="replace">Replacement string for invalid characters</param>
		/// <param name="beep">Flag to play system beep if invalid characters are found</param>
		public static void ValidateTextBox(System.Windows.Forms.TextBox textBox, 
			string replace = "", bool beep = true)
		{
			string text = ValidateFilename(textBox.Text, replace);
			if (text != textBox.Text)
			{
				int pos = textBox.SelectionStart - 1;
				textBox.Text = text;
				if (beep)
					System.Media.SystemSounds.Beep.Play();
				textBox.SelectionStart = pos;
			}
		}

		/// <summary>
		/// Creates an deep clone of an object
		/// </summary>
		/// <typeparam name="T">The object type</typeparam>
		/// <param name="obj">The object to create an exact copy of</param>
		/// <returns>A deep clone of the object</returns>
		public static T CloneObject<T>(T obj)
		{
			using (MemoryStream memStream = new MemoryStream())
			{
				BinaryFormatter binaryFormatter = new BinaryFormatter(null,
					 new StreamingContext(StreamingContextStates.Clone));
				binaryFormatter.Serialize(memStream, obj);
				memStream.Seek(0, SeekOrigin.Begin);
				return (T)binaryFormatter.Deserialize(memStream);
			}
		}

		public static double GetRandomNumber(double minimum, double maximum)
		{
			if (random == null)
				random = new Random();
			return random.NextDouble() * (maximum - minimum) + minimum;
		}
	}
}