#region Using Directives

using System;
using System.Drawing;
using System.Xml.Serialization;
using ARCed.Core;
using ARCed.Helpers;

#endregion

namespace ARCed.Settings
{
	/// <summary>
	/// Class containing settings for how the headers in the database will be rendered
	/// </summary>
	[Serializable]
	public class HeaderSettings
	{
		/// <summary>
		/// Gets or sets the left gradient color
		/// </summary>
		[XmlIgnore]
		public Color GradientLeft { get; set; }

		/// <summary>
		/// Gets or sets the right gradient color
		/// </summary>
		[XmlIgnore]
		public Color GradientRight { get; set; }

		/// <summary>
		/// Gets or sets the text color
		/// </summary>
		[XmlIgnore]
		public Color TextColor { get; set; }

		/// <summary>
		/// Gets or sets the left gradient color using an Html formatted color string
		/// </summary>
		[XmlElement("GradientLeft")]
		public string GradientLeftHtml 
		{
			get { return ColorTranslator.ToHtml(GradientLeft); }
			set { GradientLeft = ColorTranslator.FromHtml(value); }
		}

		/// <summary>
		/// Gets or sets the right gradient color using an Html formatted color string
		/// </summary>
		[XmlElement("GradientRight")]
		public string GradientRightHtml
		{
			get { return ColorTranslator.ToHtml(GradientRight); }
			set { GradientRight = ColorTranslator.FromHtml(value); }
		}

		/// <summary>
		/// Gets or sets the text color using an Html formatted color string
		/// </summary>
		[XmlElement("TextColor")]
		public string TextColorHtml
		{
			get { return ColorTranslator.ToHtml(TextColor); }
			set { TextColor = ColorTranslator.FromHtml(value); }
		}

		/// <summary>
		/// Get or set the font used to draw the text
		/// </summary>
		public SerializableFont Font { get; set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		public HeaderSettings()
		{
			GradientLeft = Color.Gray;
			GradientRight = Color.DarkGray;
			TextColor = Color.White;
			Font = FontHelper.GetMemoryFont("Ethnocentric", 10, FontStyle.Regular);
		}
	}
}
