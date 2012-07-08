using System;
using System.Drawing;
using System.Xml.Serialization;
using XnaColor = Microsoft.Xna.Framework.Color;

namespace ARCed.Settings
{
	[Serializable]
	public class ImageColorSettings
	{
		/// <summary>
		/// Gets or sets the color of the background.
		/// </summary>
		[XmlIgnore]
		public XnaColor BackgroundColor { get; set; }

		/// <summary>
		/// Gets or sets the color of the selector.
		/// </summary>
		[XmlIgnore]
		public XnaColor SelectorColor { get; set; }

		/// <summary>
		/// Gets or sets the color of the grid lines.
		/// </summary>
		[XmlIgnore]
		public XnaColor GridColor { get; set; }

		/// <summary>
		/// Gets or sets the thickness of the selector rectangle.
		/// </summary>
		public int SelectorThickness { get; set; }

		/// <summary>
		/// Gets or sets the color of the background as an HTML formatted string.
		/// </summary>
		[XmlElement("BackgroundColor")]
		public string BackgroundColorHtml
		{
			get { return ColorTranslator.ToHtml(BackgroundColor.ToSystemColor()); }
			set { BackgroundColor = ColorTranslator.FromHtml(value).ToXnaColor(); }
		}

		/// <summary>
		/// Gets or sets the color of the selector as an HTML formatted string.
		/// </summary>
		[XmlElement("SelectorColor")]
		public string SelectorColorHtml
		{
			get { return ColorTranslator.ToHtml(SelectorColor.ToSystemColor()); }
			set { SelectorColor = ColorTranslator.FromHtml(value).ToXnaColor(); }
		}

		/// <summary>
		/// Gets or sets the color of the grid lines as an HTML formatted string.
		/// </summary>
		[XmlElement("GridColor")]
		public string GridColorHtml
		{
			get { return ColorTranslator.ToHtml(GridColor.ToSystemColor()); }
			set { GridColor = ColorTranslator.FromHtml(value).ToXnaColor(); }
		}

		/// <summary>
		/// Gets or sets the flag to display grid lines on the tileset.
		/// </summary>
		public bool ShowGrid { get; set; }

		public ImageColorSettings()
		{
			BackgroundColor = XnaColor.LightGray;
			SelectorColor = XnaColor.White;
			GridColor = XnaColor.Black;
			SelectorThickness = 2;
			ShowGrid = true;
		}
	}
}
