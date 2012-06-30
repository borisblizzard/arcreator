using System;
using System.ComponentModel;
using System.Drawing;
using System.Xml.Serialization;
using ARCed.Helpers;

namespace ARCed.Data
{
	[Serializable]
	public class SerializableFont
	{
		public SerializableFont()
		{
			FontValue = null;
		}

		public SerializableFont(Font font)
		{
			FontValue = font;
		}

		[XmlIgnore]
		public Font FontValue { get; set; }

		[XmlElement("Font")]
		public string SerializeFontAttribute
		{
			get
			{
				return FontXmlConverter.ConvertToString(FontValue);
			}
			set
			{
				FontValue = FontXmlConverter.ConvertToFont(value);
			}
		}

		public static implicit operator Font(SerializableFont serializeableFont)
		{
			if (serializeableFont == null)
				return null;
			return serializeableFont.FontValue;
		}

		public static implicit operator SerializableFont(Font font)
		{
			return new SerializableFont(font);
		}
	}

	public static class FontXmlConverter
	{
		public static string ConvertToString(Font font)
		{
			try
			{
				if (font != null)
				{
					TypeConverter converter = TypeDescriptor.GetConverter(typeof(Font));
					return converter.ConvertToString(font);
				}
				else
					return null;
			}
			catch { System.Diagnostics.Debug.WriteLine("Unable to convert"); }
			return null;
		}

		public static Font ConvertToFont(string fontString)
		{
			try
			{
				TypeConverter converter = TypeDescriptor.GetConverter(typeof(Font));
				Font f = (Font)converter.ConvertFromString(fontString);
				// ------------------------------------------------------------
				// Bit of a hack since memory fonts are not included in search
				// ------------------------------------------------------------
				try
				{
					// TODO: Fix this mess
					string fontName = fontString.Split(',')[0];
					Font memFont = FontHelper.GetMemoryFont(fontName, f.Size, f.Style);
					if (memFont != null)
						return memFont;
				}
				catch {} // Nothing like an empty catch to make you feel the app is robust
				// -------------------------------------------------------------
				return f;
			}
			catch { System.Diagnostics.Debug.WriteLine("Unable to convert"); }
			return null;
		}
	}
}