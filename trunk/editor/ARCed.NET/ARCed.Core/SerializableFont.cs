#region Using Directives

using System;
using System.ComponentModel;
using System.Diagnostics;
using System.Drawing;
using System.Xml.Serialization;
using ARCed.Helpers;

#endregion

namespace ARCed.Core
{
    /// <summary>
    /// Class that handles conversions to/from a serializable string to a <see cref="Font"/> object.
    /// </summary>
	[Serializable]
	public class SerializableFont
    {
        #region Constructor

        /// <summary>
        /// Default constructor.
        /// </summary>
		public SerializableFont()
		{
			FontValue = null;
		}

        /// <summary>
        /// Constructor specifying <seealso cref="Font"/> to create object from. 
        /// </summary>
        /// <param name="font"></param>
		public SerializableFont(Font font)
		{
			FontValue = font;
		}

        #endregion

        #region Public Properties

        /// <summary>
        /// Gets or sets the <see cref="Font"/> object associated with object.
        /// </summary>
        [XmlIgnore]
		public Font FontValue { get; set; }

        /// <summary>
        /// Gets or sets the <see langword="string"/> attribute of the <see cref="Font"/> that will 
        /// be serialized.
        /// </summary>
		[XmlElement("Font")]
		public string SerializeFontAttribute
		{
            get { return FontXmlConverter.ConvertToString(FontValue); }
            set { FontValue = FontXmlConverter.ConvertToFont(value); }
		}

        #endregion

        #region Operators

        /// <summary>
        /// Implicit cast from a <see cref="SerializableFont"/> to a <see cref="Font"/>.
        /// </summary>
        /// <param name="serializeableFont">SerializableFont to cast from.</param>
        /// <returns>Font representation of the object.</returns>
		public static implicit operator Font(SerializableFont serializeableFont)
		{
			if (serializeableFont == null)
				return null;
			return serializeableFont.FontValue;
		}

        /// <summary>
        /// Implicit cast from a <see cref="Font"/> to a <see cref="SerializableFont"/>.
        /// </summary>
        /// <param name="font">Font to cast from.</param>
        /// <returns>Font representation of the object.</returns>
		public static implicit operator SerializableFont(Font font)
		{
			return new SerializableFont(font);
        }

        #endregion
    }

    /// <summary>
    /// Static class that handles conversion of XML serialized Fonts to/from <see cref="Font"/> objects.
    /// </summary>
	public static class FontXmlConverter
	{
        /// <summary>
        /// Converts a <see cref="Font"/> to a <see cref="String"/>
        /// </summary>
        /// <param name="font">Font to convert</param>
        /// <returns>String representation of the font.</returns>
		public static string ConvertToString(Font font)
		{
			try
			{
				if (font != null)
				{
					TypeConverter converter = TypeDescriptor.GetConverter(typeof(Font));
					return converter.ConvertToString(font);
				}
				return null;
			}
			catch { Debug.WriteLine("Unable to convert"); }
			return null;
		}

        /// <summary>
        /// Converts a <see cref="String"/> to a <see cref="Font"/> object.
        /// </summary>
        /// <param name="fontString">String to convert</param>
        /// <returns>Font representation of the string.</returns>
		public static Font ConvertToFont(string fontString)
        {
            Font font = null;
            try
            {
                var converter = TypeDescriptor.GetConverter(typeof(Font));
                font = (Font)converter.ConvertFromString(fontString) ?? (SystemFonts.DefaultFont);
                var fontName = fontString.Split(',')[0];
                var memFont = FontHelper.GetMemoryFont(fontName, font.Size, font.Style);
                if (memFont != null)
                    return memFont;
            }
            catch { Debug.WriteLine("Unable to convert font.");}
            return font;
        }
	}
}