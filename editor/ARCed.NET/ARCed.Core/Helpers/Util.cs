using System;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Text;
using System.Text.RegularExpressions;
using System.Windows.Forms;
using System.Xml.Serialization;

namespace ARCed.Helpers
{
	public static class Util
	{
		private static Random random;
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
                    foreach (Type type in GetTypesInNamespace(ARCedCoreAssembly, "RPG"))
                        _rpgTypes[type.ToString()] = type;
                    _rpgTypes.Add("Table", typeof(Table));
                    _rpgTypes.Add("Color", typeof(RPG.Color));
                    //_rpgTypes.Add("Tone", typeof(RPG.Tone));
                }
                return _rpgTypes;
            }
        }

        public static Type[] GetTypesInNamespace(Assembly assembly, string nameSpace)
        {
            return assembly.GetTypes().Where(t => 
                String.Equals(t.Namespace, nameSpace, StringComparison.Ordinal)).ToArray();
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

        public static Assembly XnaAssembly
        {
            get
            {
                if (_xnaAssembly == null)
                {
                    string path = Path.Combine(PathHelper.AssemblyDir, "ARCed.Xna.dll");
                    _xnaAssembly = Assembly.LoadFile(path);
                }
                return _xnaAssembly;
            }
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
			speed = speed.Clamp(-10, 10);
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
                XmlSerializer serializer = new XmlSerializer(typeof(T));
                using (TextWriter writer = new StreamWriter(path, false, Encoding.UTF8))
                    serializer.Serialize(writer, data);
            }
            catch (Exception error) { ShowErrorBox(error, path); }
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
        /// <param name="path">Path to the file that will be written to</param>
        /// <param name="data">Object to save</param>
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
        /// <typeparam name="T">Object type that will be restored</typeparam>
        /// <param name="path">Path to the binary formatted file to load</param>
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
