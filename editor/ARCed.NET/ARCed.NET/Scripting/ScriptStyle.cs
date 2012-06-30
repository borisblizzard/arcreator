using System;
using System.Drawing;
using System.Xml.Serialization;
using ARCed.Data;

namespace ARCed.Scripting
{
	/// <summary>
	/// Represents a lexer style used by the script editor
	/// </summary>
	[Serializable]
	public class ScriptStyle
	{
		#region Public Properties

		/// <summary>
		/// Gets or sets the foreground color of the style
		/// </summary>
		[XmlIgnore]
		public Color ForeColor { get; set; }
		/// <summary>
		/// Gets or sets the foreground color using an Html formatted color string
		/// </summary>
		[XmlElement("ForeColor")]
		public string ForeColorHtml
		{
			get { return ColorTranslator.ToHtml(ForeColor); }
			set { ForeColor = ColorTranslator.FromHtml(value); }
		}
		/// <summary>
		/// Gets or sets the background color of the style
		/// </summary>
		[XmlIgnore]
		public Color BackColor { get; set; }
		/// <summary>
		/// Gets or sets the background color using an Html formatted color string
		/// </summary>
		[XmlElement("BackColor")]
		public string BackColorHtml
		{
			get { return ColorTranslator.ToHtml(BackColor); }
			set { BackColor = ColorTranslator.FromHtml(value); }
		}
		/// <summary>
		/// Gets or sets the font used for the style
		/// </summary> 
		public SerializableFont Font { get; set; }
		/// <summary>
		/// Gets or sets the name of the style
		/// </summary>
		[XmlAttribute(AttributeName = "Name")]
		public string Name { get; set; }

		#endregion

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public ScriptStyle() : this("", Color.Black, Color.Transparent, SystemFonts.DefaultFont) {}

		/// <summary>
		/// Constructor with parameters
		/// </summary>
		/// <param name="name">The name of the style</param>
		/// <param name="fore">The foreground color of the style</param>
		/// <param name="back">The background color of the style</param>
		/// <param name="font">The font used for the style</param>
		public ScriptStyle(string name, Color fore, Color back, Font font)
		{
			Name = name;
			ForeColor = fore;
			BackColor = back;
			Font = font;
		}

		#endregion
	}
}