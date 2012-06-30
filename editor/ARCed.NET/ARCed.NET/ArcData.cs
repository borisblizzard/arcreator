using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

namespace ARCed
{
	/// <summary>
	/// Wrapper for standard Dictionary with dynamic key-value pairs
	/// </summary>
	public class Hash : Dictionary<dynamic, dynamic> { }

	/// <summary>
	/// Wrapper for a dictionary containing name-type pairs
	/// </summary>
	public class TypeMap : Dictionary<string, Type> { }

	/// <summary>
	/// Static class for serialization of .arc format
	/// </summary>
	public static class ArcData
	{

		/// <summary>
		/// Enum representing flags for type-identifying byte markers 
		/// </summary>
		public enum RubyTypes
		{
			/// <summary>
			/// Byte marker for NilClass value: 0x10 (16)
			/// </summary>
			NilClass = 0x10,
			/// <summary>
			/// Byte marker for FalseClass value: 0x11 (17)
			/// </summary>
			FalseClass = 0x11,
			/// <summary>
			/// Byte marker for TrueClass value: 0x12 (18)
			/// </summary>
			TrueClass = 0x12,
			/// <summary>
			/// Byte marker for Fixnum value: 0x21 (33)
			/// </summary>
			Fixnum = 0x21,
			/// <summary>
			/// Byte marker for Bignum value: 0x22 (34)
			/// </summary>
			Bignum = 0x22,
			/// <summary>
			/// Byte marker for Float value: 0x23 (35)
			/// </summary>
			Float = 0x23,
			/// <summary>
			/// Byte marker for String value: 0x30 (48)
			/// </summary>
			String = 0x30,
			/// <summary>
			/// Byte marker for Array value: 0x40 (64)
			/// </summary>
			Array = 0x40,
			/// <summary>
			/// Byte marker for Hash value: 0x41 (65)
			/// </summary>
			Hash = 0x41,
			/// <summary>
			/// Byte marker for Object value: 0x00 (0)
			/// </summary>
			Object = 0x00
		}

		#region Constants

		const string HEADER = "\x41\x52\x43\x44";  // ARCD
		const string VERSION = "\x01\x00";         // 1.0

		#endregion

		#region Private Fields

		private static Stream _stream = Stream.Null;
		private static byte[] _buffer = new byte[0];
		private static List<object> _strings = new List<object>() { null };
		private static List<object> _arrays = new List<object>() { null };
		private static List<object> _hashes = new List<object>() { null };
		private static List<object> _objects = new List<object>() { null };
		private static TypeMap _mappedTypes;
		private static TypeMap _assemblyTypes;

		#endregion

		#region Public Methods

		/// <summary>
		/// Serializes the given object and writes it to the stream
		/// </summary>
		/// <param name="stream">IO stream to write to</param>
		/// <param name="obj">Object to write</param>
		public static void dump(Stream stream, object obj)
		{
			Reset();
			_mappedTypes = new TypeMap();
			_stream = stream;
			_stream.Write(HEADER.GetBytes(), 0, 4);
			_stream.Write(VERSION.GetBytes(), 0, 2);
			try { _dump(obj); }
			catch { Console.WriteLine("ERROR: Failed to dump \"{0}\".", obj); }
			finally { Reset(); }
		}

		/// <summary>
		/// Loads an object from the stream
		/// </summary>
		/// <param name="stream">Stream to read</param>
		/// <returns>Deserialized object</returns>
		public static object load(Stream stream)
		{
			return load(stream, Assembly.GetExecutingAssembly());
		}

		/// <summary>
		/// Loads an object from the stream
		/// </summary>
		/// <param name="stream">Stream to read</param>
		/// <param name="assemblies">Assemblies that will be searched for known types</param>
		/// <returns>Deserialized object</returns>
		public static object load(Stream stream, params Assembly[] assemblies)
		{
			TypeMap map = new TypeMap();
			foreach (Assembly assembly in assemblies)
			{
				foreach (Type type in assembly.GetTypes())
					map[type.ToString()] = type;
			}
			return load(stream, map);
		}

		/// <summary>
		/// Loads an object from the stream
		/// </summary>
		/// <param name="stream">Stream to read</param>
		/// <param name="assemblyTypes">Dictionary map for containing known types</param>
		/// <returns>Deserialized object</returns>
		public static object load(Stream stream, TypeMap assemblyTypes)
		{
			_stream = stream;
			CheckHeader();
			_assemblyTypes = assemblyTypes;
			_mappedTypes = new TypeMap();
			object data = null;
			data = _load();
			try { }
			catch { Console.WriteLine("ERROR: Stream Position: {0}", _stream.Position); }
			finally { Reset(); }
			return data;
		}

		#endregion

		#region Private Methods

		/// <summary>
		/// Checks formatting of header and version data at the beginning of the stream
		/// </summary>
		/// <exception cref="InvalidDataException">Thrown if header and version do not match proper format</exception>
		private static void CheckHeader()
		{
			_stream.Seek(0, SeekOrigin.Begin);
			string header = _stream.ReadByteString(4);
			if (header != HEADER)
			{
				string msg = String.Format("Incorrect header information. Looking for\"{0}\", found: \"{1}\"",
					HEADER, header);
				throw new InvalidDataException(msg);
			}
			string version = _stream.ReadByteString(2);
			if (version != VERSION)
			{
				string msg = String.Format("Incorrect version information. Looking for\"{0}\", found: \"{1}\"",
					VERSION, version);
				throw new InvalidDataException(msg);
			}
		}

		/// <summary>
		/// Closes the stream if open, and clears all mappings
		/// </summary>
		private static void Reset()
		{
			if (_stream != null)
				_stream.Dispose();
			_stream = Stream.Null;
			_strings.Clear();
			_strings.Add(null);
			_arrays.Clear();
			_arrays.Add(null);
			_hashes.Clear();
			_arrays.Add(null);
			_objects.Clear();
			_objects.Add(null);
		}

		/// <summary>
		/// Identifies the object type and dumps it to the stream accordingly
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dump(object obj)
		{
			if (obj == null) _dumpNilClass(obj);
			else if (obj is bool)
			{
				if ((bool)obj) _dumpTrueClass(obj);
				else _dumpFalseClass(obj);
			}
			else if (IsRubyFixnum(obj)) _dumpFixnum(obj);
			else if (IsRubyBignum(obj)) _dumpBignum(obj);
			else if (IsRubyFloat(obj)) _dumpFloat(obj);
			else if (obj is String) _dumpString(obj);
			else if (obj is Array) _dumpArray(obj);
			else if (obj is DictionaryBase) _dumpHash(obj);
			else
			{
				try { _dumpObject(obj); }
				catch
				{
					string msg = String.Format("Objects of type \"{0}\" cannot be dumped.", obj.GetType());
					throw new System.Runtime.Serialization.SerializationException(msg);
				}
			}
		}

		/// <summary>
		/// Reads the type identifying byte marker from the current stream position, and loads the data accordingly
		/// </summary>
		/// <returns>Deserialized object</returns>
		private static dynamic _load()
		{
			RubyTypes type = (RubyTypes)_stream.ReadByte();
			switch (type)
			{
				case RubyTypes.NilClass: return _loadNilClass();
				case RubyTypes.FalseClass: return _loadFalseClass();
				case RubyTypes.TrueClass: return _loadTrueClass();
				case RubyTypes.Fixnum: return _loadFixnum();
				case RubyTypes.Bignum: return _loadBignum();
				case RubyTypes.Float: return _loadFloat();
				case RubyTypes.String: return _loadString();
				case RubyTypes.Array: return _loadArray();
				case RubyTypes.Hash: return _loadHash();
				case RubyTypes.Object: return _loadObject();
			}
			string msg = String.Format("Unknown byte identifier: {0}", type);
			throw new TypeLoadException(msg);
		}

		/// <summary>
		/// Checks an object if it us a numerical type falling in range of a Ruby Fixnum
		/// </summary>
		/// <param name="value">Object to check</param>
		/// <returns>Flag if object is Fixnum or not</returns>
		private static bool IsRubyFixnum(object value)
		{
			if (value is sbyte) return true;
			if (value is byte) return true;
			if (value is short) return true;
			if (value is ushort) return true;
			if (value is int) return true;
			if (value is uint) return true;
			return false;
		}

		/// <summary>
		/// Checks an object if it us a numerical type falling in range of a Ruby Bignum
		/// </summary>
		/// <param name="value">Object to check</param>
		/// <returns>Flag if object is Bignum or not</returns>
		private static bool IsRubyBignum(object value)
		{
			if (value is long) return true;
			if (value is ulong) return true;
			return false;
		}

		/// <summary>
		/// Checks an object if it us a numerical type falling in range of a Ruby Float
		/// </summary>
		/// <param name="value">Object to check</param>
		/// <returns>Flag if object is Float or not</returns>
		private static bool IsRubyFloat(object value)
		{
			if (value is float) return true;
			if (value is double) return true;
			if (value is decimal) return true;
			return false;
		}

		#endregion

		#region Mapping

		/// <summary>
		/// Checks if object is already mapped using equality comparison, mapping object if not found
		/// </summary>
		/// <param name="data">Reference to a list of objects</param>
		/// <param name="obj">Object to map</param>
		/// <returns>Flag if object was mapped</returns>
		/// <remarks>If object is already mapped, the index it was found in is dumped instead of the
		/// the whole object</remarks>
		private static bool TryMapEquality(ref List<object> data, object obj) 
		{
			int index = -1;
			for (int i = 0; i < data.Count; i++)
			{
				if (data[i] == obj)
				{
					index = i;
					break;
				}
			}
			if (index < 0)
			{
				_dumpInt32(data.Count);
				data.Add(obj);
				return true;
			}
			_dumpInt32(index);
			return false;
		}

		/// <summary>
		/// Checks if object is already mapped using identity comparison, mapping object if not found
		/// </summary>
		/// <param name="data">Reference to a list of objects</param>
		/// <param name="obj">Object to map</param>
		/// <returns>Flag if object was mapped</returns>
		/// <remarks>If object is already mapped, the index it was found in is dumped instead of the
		/// the whole object</remarks>
		private static bool TryMapIdentity(ref List<object> data, object obj) 
		{
			int index = data.IndexOf(obj);
			if (index < 0)
			{
				_dumpInt32(data.Count);
				data.Add(obj);
				return true;
			}
			_dumpInt32(index);
			return false;
		}

		/// <summary>
		/// Retrieves a <paramref name="System.Type"/> that was previously mapped, or if not found, 
		/// finds the type and maps it.
		/// </summary>
		/// <param name="classPath">Path of the class</param>
		/// <returns>Object type</returns>
		/// <exception cref="TypeLoadException">Thrown when type cannot be found in the assembly</exception>
		private static Type GetMappedType(string classPath)
		{
			if (_mappedTypes.ContainsKey(classPath))
				return _mappedTypes[classPath];
			else
			{
				Regex regex = new Regex(String.Join(@"[\+|\.]", Regex.Split(classPath, "::")));
				foreach (string typeName in _assemblyTypes.Keys)
				{
					if (regex.Match(typeName).Success)
					{
						_mappedTypes[classPath] = _assemblyTypes[typeName];
						return _mappedTypes[classPath];
					}
				}
			}
			throw new TypeLoadException(String.Format("Type of \"{0}\" cannot be found in loaded assemblies.", classPath));
		}

		/// <summary>
		/// Retrieves the object with the given ID in the map, or null if not found
		/// </summary>
		/// <param name="list">Reference to the map to search</param>
		/// <param name="id">ID of the object</param>
		/// <returns>Object found with the given ID, or null if not found</returns>
		private static object FindMapping(ref List<object> list, int id)
		{
			return id < list.Count ? list[id] : null;
		}

		/// <summary>
		/// Maps an object to the given list
		/// </summary>
		/// <typeparam name="T">Object type</typeparam>
		/// <param name="list">Reference to the map</param>
		/// <param name="obj">Object to map</param>
		private static void MapObject<T>(ref List<object> list, T obj)
		{
			list.Add(obj);
		}

		#endregion

		#region Int32

		/// <summary>
		/// Converts an Int32 to a four-byte, little-endian array and writes it to the stream
		/// </summary>
		/// <param name="int32">Integer to dump</param>
		private static void _dumpInt32(int int32)
		{
			byte[] bytes = BitConverter.GetBytes(int32);
			if (!BitConverter.IsLittleEndian)
				Array.Reverse(bytes);
			_stream.Write(bytes, 0, 4);
		}

		/// <summary>
		/// Loads a 32-bit integer from the stream
		/// </summary>
		/// <returns>Integer value</returns>
		private static int _loadInt32()
		{
			return BitConverter.ToInt32(_stream.ReadBytes(4), 0);
		}

		#endregion

		#region NilClass

		/// <summary>
		/// Writes a null-type to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dumpNilClass(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.NilClass);
		}

		/// <summary>
		/// Returns null
		/// </summary>
		/// <returns>null</returns>
		private static object _loadNilClass() { return null; }

		#endregion

		#region FalseClass

		/// <summary>
		/// Writes bool-type to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dumpFalseClass(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.FalseClass);
		}

		/// <summary>
		/// Returns false
		/// </summary>
		/// <returns>false</returns>
		private static bool _loadFalseClass() { return false; }

		#endregion

		#region TrueClass

		/// <summary>
		/// Writes bool-type to the stram
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dumpTrueClass(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.TrueClass);
		}

		/// <summary>
		/// Returns true
		/// </summary>
		/// <returns>true</returns>
		private static bool _loadTrueClass() { return true; }

		#endregion

		#region Fixnum

		/// <summary>
		/// Writes an object to the string as a Ruby Fixnum
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dumpFixnum(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Fixnum);
			_dumpInt32((int)obj);
		}

		/// <summary>
		/// Reads a number from the stream
		/// </summary>
		/// <returns>Integer value</returns>
		private static int _loadFixnum()
		{
			return BitConverter.ToInt32(_stream.ReadBytes(4), 0);
		}

		#endregion

		#region Bignum

		/// <summary>
		/// Writes an object to the string as a Ruby Bignum
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dumpBignum(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Bignum);
			_dumpInt32((int)obj);
		}

		/// <summary>
		/// Reads a number from the stream
		/// </summary>
		/// <returns>Integer value</returns>
		private static int _loadBignum()
		{
			return BitConverter.ToInt32(_stream.ReadBytes(4), 0);
		}

		#endregion

		#region Float

		/// <summary>
		/// Writes a floating point decimal to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dumpFloat(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Float);
			byte[] bytes = BitConverter.GetBytes((float)obj);
			if (!BitConverter.IsLittleEndian)
				Array.Reverse(bytes);
			_stream.Write(bytes, 0, 4);
		}

		/// <summary>
		/// Reads a floating point decimal from the stream
		/// </summary>
		/// <returns>Float value</returns>
		private static float _loadFloat()
		{
			return BitConverter.ToSingle(_stream.ReadBytes(4), 0);
		}

		#endregion

		#region String

		/// <summary>
		/// Writes a string to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		/// <remarks>Strings are serialized in UTF-8 encoding</remarks>
		private static void _dumpString(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.String);
			if (!TryMapEquality(ref _strings, obj))
				return;
			string data = Convert.ToString(obj);
			_dumpInt32(data.Length);				// Dump length
			byte[] bytes = data.GetBytes();         // Get UTF-8 formatted string as byte array
			_stream.Write(bytes, 0, bytes.Length);  // Dump bytes
		}

		/// <summary>
		/// Reads a string from the stream
		/// </summary>
		/// <returns>String value</returns>
		private static string _loadString()
		{
			int id = _loadInt32();
			string obj = (string)FindMapping(ref _strings, id);
			if (obj != null)
				return String.Copy(obj);
			int size = _loadInt32();
			obj = _stream.ReadByteString(size);
			MapObject(ref _strings, obj);
			return obj;
		}

		#endregion

		#region Array

		/// <summary>
		/// Writes an array-type to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dumpArray(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Array);
			Array array = obj as Array;
			_dumpInt32(array.GetHashCode());        // Dump ID
			_dumpInt32(array.Length);				// Dump array size
			foreach (object data in array)			// Enumerate and dump each element
				_dump(data);
		}

		/// <summary>
		/// Reads an array from the stream
		/// </summary>
		/// <returns>Array value</returns>
		private static List<dynamic> _loadArray()
		{
			int id = _loadInt32();
			dynamic obj = FindMapping(ref _arrays, id);
			if (obj != null)
				return obj;
			int size = _loadInt32();
			List<dynamic> array = new List<dynamic>(size);
			for (int i = 0; i < size; i++)
				array.Add(_load());
			return array;
		}

		#endregion

		#region Hash

		/// <summary>
		/// Writes a dictionary-type to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dumpHash(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Hash);
			var dict = obj as Dictionary<object, object>;
			_dumpInt32(dict.GetHashCode());
			_dumpInt32(dict.Count);
			foreach (var pair in dict)
			{
				_dump(pair.Key);
				_dump(pair.Value);
			}
		}

		/// <summary>
		/// Reads a dictionary type from the stream
		/// </summary>
		/// <returns>Dictionary value</returns>
		private static Hash _loadHash()
		{
			int id = _loadInt32();
			object obj = FindMapping(ref _hashes, id);
			if (obj != null)
				return (Hash)obj;
			int size = _loadInt32();
			Hash hash = new Hash();
			object key;
			for (int i = 0; i < size; i++)
			{
				key = _load();
				hash[key] = _load();
			}
			return hash;
		}

		#endregion

		#region Object

		/// <summary>
		/// Writes an object to the stream
		/// </summary>
		/// <param name="obj">Object to serialize</param>
		private static void _dumpObject(object obj)
		{
			_stream.WriteByte((byte)RubyTypes.Object);
			Type objType = obj.GetType();
			string classe = Regex.Replace(objType.ToString(), @"[\+|\.]", "::");
			_dumpString(classe);
			if (!TryMapIdentity(ref _objects, obj))
				return;
			if (obj.HasMethod("_arc_dump"))
			{
				byte[] data = (byte[])objType.InvokeMember(
					"_arc_dump",
					BindingFlags.Public | BindingFlags.InvokeMethod,
					null,
					obj,
					null
				);
				_dumpInt32(data.Length);
				_stream.Write(data, 0, data.Length);
			}
			else
			{
				List<object> excludes = new List<object>();
				if (obj.HasMethod("_arc_exclude"))
				{
					excludes = (List<object>)objType.InvokeMember(
						"_arc_exclude",
						BindingFlags.Public | BindingFlags.GetProperty,
						null,
						obj,
						null
					);
				}
				PropertyInfo[] properties =
					objType.GetProperties(BindingFlags.Public | BindingFlags.Instance);
				List<string> variables = new List<string>();
				foreach (PropertyInfo info in properties)
				{
					string variable = info.Name;
					if (!excludes.Contains(variable))
						variables.Add(variable);
				}
				variables.Sort();
				_dumpInt32(variables.Count);
				foreach (string variable in variables)
				{
					_dumpString(variable);
					object value = objType.InvokeMember(
						variable,
						BindingFlags.Public | BindingFlags.GetProperty | BindingFlags.Instance,
						null,
						obj,
						null
					);
					_dump(value);
				}
			}
		}

		/// <summary>
		/// 
		/// </summary>
		/// <returns></returns>
		private static dynamic _loadObject()
		{
			string mapString = _load();
			int id = _loadInt32();
			dynamic obj = FindMapping(ref _objects, id);
			if (obj != null)
				return obj;
			int size = _loadInt32();
			Type type = GetMappedType(mapString);
			if (type.GetMethod("_arc_load") != null)
			{
				obj = type.InvokeMember(
					"_arc_load", BindingFlags.Public | BindingFlags.Static | BindingFlags.InvokeMethod,
					null, type, new object[] { _stream.ReadBytes(size) });
				return obj;
			}
			obj = Activator.CreateInstance(type);
			MapObject(ref _objects, obj);
			string propertyName;
			dynamic propertyValue;
			for (int i = 0; i < size; i++)
			{
				propertyName = _load();		
				propertyValue = _load();
				PropertyInfo info = type.GetProperty(propertyName);
				if (info != null)
					info.SetValue(obj, propertyValue, null);
			}
			return obj;
		}

		#endregion
	}
}
