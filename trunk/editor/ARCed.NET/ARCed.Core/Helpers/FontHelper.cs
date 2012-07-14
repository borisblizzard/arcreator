using System;
using System.Collections.Generic;
using System.Drawing;
using System.Drawing.Text;
using System.IO;
using System.Reflection;
using System.Runtime.InteropServices;
using ARCed.Core.Win32;

namespace ARCed.Helpers
{
	/// <summary>
	/// Static class for loading and creating Fonts in memory without the need to 
	/// have them installed.
	/// </summary>
	/// <remarks>In order for a memory font to be drawn on a control, it must be 
	/// rendered with GDI+, so "SetCompatibleTextRenderingDefault" must be set for  
	/// the application, or "UseCompatibleTextRendering" for individual controls.</remarks>
	public static class FontHelper
	{
		private static List<string> _loadedPaths = new List<string>();
		private static PrivateFontCollection _fonts;
		private static Font _monoFont;
		private static List<string> _installedFonts;

		/// <summary>
		/// Loads all TrueType fonts found in the application's "Fonts" folder into memory.
		/// </summary>
		/// <remarks>This method also loads resource fonts embedded into the application.</remarks>
		public static void LoadUserFonts()
		{
			string fontDir = Path.Combine(PathHelper.EditorDirectory, "Fonts");
            if (Directory.Exists(fontDir))
            {
                foreach (string filename in Directory.GetFiles(fontDir, "*.ttf"))
                    AddFileFont(filename);
            }
		}

		/// <summary>
		/// Creates and returns a font, first checking memorized fonts.
		/// </summary>
		/// <param _frames="familyName">Name of the font family</param>
		/// <param _frames="size">Size of the font</param>
		/// <param _frames="style">Style to apply to the font</param>
		/// <returns>Loaded font object</returns>
		public static Font GetFont(string familyName, float size, FontStyle style)
		{
			Font font = GetMemoryFont(familyName, size, style);
			if (font != null)
				return font;
			return new Font(new FontFamily(familyName), size, style);
		}	
	
		/// <summary>
		/// Adds a font from an array of bytes
		/// </summary>
		/// <param _frames="bytes">Array of bytes to read</param>
		public static void AddResourceFont(byte[] bytes)
		{
			int dataLength = bytes.Length;
			IntPtr ptrData = Marshal.AllocCoTaskMem(dataLength);
			Marshal.Copy(bytes, 0, ptrData, dataLength);
			uint cFonts = 0;
			NativeMethods.AddFontMemResourceEx(ptrData, (uint)dataLength, IntPtr.Zero, ref cFonts);
			FontCollection.AddMemoryFont(ptrData, dataLength);
			Marshal.FreeCoTaskMem(ptrData);
		}

		/// <summary>
		/// Returns the system's default monospace font
		/// </summary>
		public static Font MonoFont 
		{
			get
			{
				if (_monoFont == null)
				{
					FontFamily family = new FontFamily(GenericFontFamilies.Monospace);
					float size = SystemFonts.MessageBoxFont.Size;
					_monoFont = new Font(family, size);
				}
				return _monoFont;
			}
		}

		/// <summary>
		/// Finds and creates a font from a font family previously loaded into memory
		/// </summary>
		/// <param _frames="familyName">Name of the font family</param>
		/// <param _frames="size">Size of the font</param>
		/// <param _frames="style">Style to apply to the font</param>
		/// <returns>Font loaded from memory, or null if font family could not be found.</returns>
		public static Font GetMemoryFont(string familyName, float size, FontStyle style)
		{
			foreach (FontFamily family in Families)
			{
				if (family.Name == familyName)
					return new Font(family, size, style);
			}
			return null;
		}

		/// <summary>
		/// Gets a list of names of the system's installed fonts
		/// </summary>
		public static List<string> InstalledFonts
		{
			get
			{
				if (_installedFonts == null)
				{
					_installedFonts = new List<string>();
					using (InstalledFontCollection fonts = new InstalledFontCollection())
					{
						foreach (var family in fonts.Families)
							_installedFonts.Add(family.Name);
					}
				}
				return _installedFonts;
			}
		}

		/// <summary>
		/// Gets the private collection of fonts loaded into memory
		/// </summary>
		public static PrivateFontCollection FontCollection
		{
			get
			{
				if (_fonts == null)
					_fonts = new PrivateFontCollection();
				return _fonts;
			}
		}

		/// <summary>
		/// Gets an array of loaded font families in memory
		/// </summary>
		public static FontFamily[] Families
		{
			get { return FontCollection.Families; }
		}

		/// <summary>
		/// Adds a private memory font from a file
		/// </summary>
		/// <param _frames="filename">The path of the file</param>
		public static void AddFileFont(string filename)
		{
			if (!_loadedPaths.Contains(filename))
			{
				AddFont(File.OpenRead(filename));
				NativeMethods.AddFontResourceEx(filename, 0x10, IntPtr.Zero);
			}
		}

		/// <summary>
		/// Adds a private memory font from an embedded resource
		/// </summary>
		/// <param _frames="resourceName">The full _frames, including namespaces, of the resource file</param>
		public static void AddResourceFont(string resourceName)
		{
			if (!_loadedPaths.Contains(resourceName))
			{
				Assembly assembly = Assembly.GetExecutingAssembly();
				AddFont(assembly.GetManifestResourceStream(resourceName));
			}
		}

		/// <summary>
		/// Adds a private memory font from a stream
		/// </summary>
		/// <param _frames="stream">The stream to load the font from</param>
		/// <remarks>The stream will be closed automatically after the font is loaded</remarks>
		public static void AddFont(Stream stream)
		{
			IntPtr ptr;
			ptr = Marshal.AllocCoTaskMem((int)stream.Length);
			byte[] data = new byte[stream.Length];
			stream.Read(data, 0, (int)stream.Length);
			Marshal.Copy(data, 0, ptr, (int)stream.Length);
			FontCollection.AddMemoryFont(ptr, (int)stream.Length);
			stream.Close();
			Marshal.FreeCoTaskMem(ptr);
		}

		/// <summary>
		/// Checks if a font is installed on the machine and returns the result
		/// </summary>
		/// <param _frames="fontName">The _frames of the font to check for</param>
		/// <returns>The result of the check</returns>
		public static bool IsInstalled(string fontName)
		{
			using (Font testFont = new Font(fontName, 8))
			{
				return 0 == string.Compare(
				  fontName,
				  testFont.Name,
				  StringComparison.InvariantCultureIgnoreCase);
			}
		}
	}
}
