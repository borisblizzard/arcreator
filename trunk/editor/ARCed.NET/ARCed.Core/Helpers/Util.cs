#region Using Directives

using System;
using System.IO;
using System.Linq;
using System.Media;
using System.Reflection;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Text.RegularExpressions;
using System.Windows.Forms;
using System.Xml.Serialization;
using RPG;

#endregion

namespace ARCed.Helpers
{
    /// <summary>
    /// Static class that provides functions that are shared across tha ARCed assemblies.
    /// </summary>
	public static class Util
	{
		private static Random _random;
        private static TypeMap _rpgTypes;
        private static Assembly _xnaAssembly, _coreAssembly;

        /// <summary>
        /// Gets a mapping of all RPG types.
        /// </summary>
        public static TypeMap RpgTypes
        {
            get
            {
                if (_rpgTypes == null)
                {
                    _rpgTypes = new TypeMap();
                    foreach (var type in GetTypesInNamespace(ARCedCoreAssembly, "RPG"))
                        _rpgTypes[type.ToString()] = type;
                    _rpgTypes.Add("Table", typeof(Table));
                    _rpgTypes.Add("Color", typeof(Color));
                    //_rpgTypes.Add("Tone", typeof(RPG.Tone));
                }
                return _rpgTypes;
            }
        }

        /// <summary>
        /// Gets an array of all types found in the given namespace.
        /// </summary>
        /// <param name="assembly">Assembly to search for the namespace.</param>
        /// <param name="namespace">The namespace to search</param>
        /// <returns>Array of found types</returns>
        public static Type[] GetTypesInNamespace(Assembly assembly, string @namespace)
        {
            return assembly.GetTypes().Where(t => 
                String.Equals(t.Namespace, @namespace, StringComparison.Ordinal)).ToArray();
        }

        /// <summary>
        /// Gets the assembly instance of the editor
        /// </summary>
        public static Assembly ARCedAssembly
        {
            get { return Assembly.LoadFile(PathHelper.EditorPath); }
        }

        /// <summary>
        /// Gets the assembly instance of the editor
        /// </summary>
        public static Assembly ARCedCoreAssembly
        {
            get
            {
                if (_coreAssembly == null)
                {
                    string path = Path.Combine(PathHelper.AssemblyDir, "ARCed.Core.dll");
                    _coreAssembly = Assembly.LoadFile(path);
                }
                return _coreAssembly;
            }
        }

        /// <summary>
        /// Gets the instance of the ARCed.Xna assembly.
        /// </summary>
        public static Assembly XnaAssembly
        {
            get
            {
                if (_xnaAssembly == null)
                {
                    var path = Path.Combine(PathHelper.AssemblyDir, "ARCed.Xna.dll");
                    _xnaAssembly = Assembly.LoadFile(path);
                }
                return _xnaAssembly;
            }
        }

		/// <summary>
		/// Calculates the parameter value of a curve at the given level
		/// </summary>
		/// <param name="min">The lowest value value at the starting point of the curve</param>
		/// <param name="max">The greatest value at the end of the curve</param>
		/// <param name="speed">The "pitch" of the curve</param>
		/// <param name="level">The level to calculate the value for (x coordinate)</param>
		/// <param name="initial">The initial level that the curve begins generation</param>
		/// <param name="final">The final level that the curve ends generation</param>
		/// <returns>The calculated value for the curve at the given level</returns>
		public static int GenerateParameter
			(int min, int max, int speed, int level, int initial, int final)
		{
			speed = speed.Clamp(-10, 10);
			float curve;
			var pRange = max - min;
			var lRange = Convert.ToSingle(final - initial);
			var linear = Convert.ToInt32(min + pRange * ((level - initial) / lRange));
			if (speed == 0)
				return linear;
		    if (speed < 0)
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
			if (_random == null)
				_random = new Random();
			return _random.NextDouble() * (maximum - minimum) + minimum;
		}

		/// <summary>
		/// Copies an embedded resource to an external place on the hard-drive
		/// </summary>
        /// <param name="resource">The name of the resource</param>
		/// <param name="path">The path the resource will be saved to</param>
		public static void ExtractResource(string resource, string path)
		{
			using (var s = Assembly.GetExecutingAssembly().GetManifestResourceStream(resource))
			using (var resourceFile = new FileStream(path, FileMode.Create))
			{
			    if (s != null)
			    {
			        var b = new byte[s.Length + 1];
			        s.Read(b, 0, Convert.ToInt32(s.Length));
			        resourceFile.Write(b, 0, Convert.ToInt32(b.Length - 1));
			    }
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
			var invalidChars = Regex.Escape(new string(Path.GetInvalidFileNameChars()));
			var invalidReStr = string.Format(@"[{0}]+", invalidChars);
			return Regex.Replace(name, invalidReStr, replace);
		}

		/// <summary>
		/// Ensures that all characters in the textbox field are valid for a path
		/// </summary>
		/// <param name="textBox">The textbox to check</param>
		/// <param name="replace">Replacement string for invalid characters</param>
		/// <param name="beep">Flag to play system beep if invalid characters are found</param>
		public static void ValidateTextBox(TextBox textBox, string replace = "", bool beep = true)
		{
			var text = ValidateFilename(textBox.Text, replace);
		    if (text == textBox.Text) return;
		    int pos = textBox.SelectionStart - 1;
		    textBox.Text = text;
		    if (beep)
		        SystemSounds.Beep.Play();
		    textBox.SelectionStart = pos;
		}

		/// <summary>
		/// Creates an deep clone of an object
		/// </summary>
		/// <typeparam name="T">The object type</typeparam>
		/// <param name="obj">The object to create an exact copy of</param>
		/// <returns>A deep clone of the object</returns>
		public static T CloneObject<T>(T obj)
		{
			using (var memStream = new MemoryStream())
			{
				var binaryFormatter = new BinaryFormatter(null,
					 new StreamingContext(StreamingContextStates.Clone));
				binaryFormatter.Serialize(memStream, obj);
				memStream.Seek(0, SeekOrigin.Begin);
				return (T)binaryFormatter.Deserialize(memStream);
			}
		}

        /// <summary>
        /// Generates and returns a random number within the specified range
        /// </summary>
        /// <param name="minimum">Minimum value of the number to return</param>
        /// <param name="maximum">Maximum value of the number to return</param>
        /// <returns>Random number</returns>
		public static double GetRandomNumber(double minimum, double maximum)
		{
			if (_random == null)
				_random = new Random();
			return _random.NextDouble() * (maximum - minimum) + minimum;
		}

        /// <summary>
        /// Saves an object in XML format
        /// </summary>
        /// <typeparam name="T">Object type that will be saved</typeparam>
        /// <param name="path">Path to the file that will be written to</param>
        /// <param name="data">Object to save</param>
        public static void SaveXML<T>(string path, T data)
        {
            try
            {
                var serializer = new XmlSerializer(typeof(T));
                using (TextWriter writer = new StreamWriter(path, false, Encoding.UTF8))
                    serializer.Serialize(writer, data);
            }
            catch (Exception error) { ShowErrorBox(error); }
        }

        /// <summary>
        /// Loads an object previously saved in XML format
        /// </summary>
        /// <typeparam name="T">Object type that will be restored</typeparam>
        /// <param name="path">Path to the XML formatted file to load</param>
        /// <returns>Loaded object</returns>
        public static T LoadXML<T>(string path) where T : class
        {
            try
            {
                var serializer = new XmlSerializer(typeof(T));
                T data;
                using (TextReader reader = new StreamReader(path, Encoding.UTF8))
                    data = (T)serializer.Deserialize(reader);
                return data;
            }
            catch (Exception error) { ShowErrorBox(error); }
            return null;
        }

        /// <summary>
        /// Saves an object in binary format
        /// </summary>
        /// <param name="path">Path to the file that will be written to</param>
        /// <param name="data">Object to save</param>
        public static void SaveBinary(string path, object data)
        {
            try
            {
                var formatter = new BinaryFormatter();
                using (Stream stream = File.OpenWrite(path))
                    formatter.Serialize(stream, data);
            }
            catch (Exception error) { ShowErrorBox(error); }
        }

        /// <summary>
        /// Loads an object previously saved in binary format
        /// </summary>
        /// <typeparam name="T">Object type that will be restored</typeparam>
        /// <param name="path">Path to the binary formatted file to load</param>
        /// <returns>Loaded object</returns>
        public static T LoadBinary<T>(string path) where T : class
        {
            try
            {
                var formatter = new BinaryFormatter();
                T data;
                using (Stream stream = File.OpenRead(path))
                    data = (T)formatter.Deserialize(stream);
                return data;
            }
            catch (Exception error) { ShowErrorBox(error); }
            return null;
        }

        private static void ShowErrorBox(Exception error)
        {
            var msg = String.Format("The following error during serialization:\n\n{0}\n\nStack Trace:\n{1}",
                error.Message, error.StackTrace);
            MessageBox.Show(msg, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
        }
	}
}
