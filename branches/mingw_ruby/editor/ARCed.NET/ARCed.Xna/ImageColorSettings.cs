#region Using Directives

using System;
using System.Drawing;
using System.Xml.Serialization;
using XnaColor = Microsoft.Xna.Framework.Color;

#endregion

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
			get { return ColorTranslator.ToHtml(this.BackgroundColor.ToSystemColor()); }
			set { this.BackgroundColor = ColorTranslator.FromHtml(value).ToXnaColor(); }
		}

		/// <summary>
		/// Gets or sets the color of the selector as an HTML formatted string.
		/// </summary>
		[XmlElement("SelectorColor")]
		public string SelectorColorHtml
		{
			get { return ColorTranslator.ToHtml(this.SelectorColor.ToSystemColor()); }
			set { this.SelectorColor = ColorTranslator.FromHtml(value).ToXnaColor(); }
		}

		/// <summary>
		/// Gets or sets the color of the grid lines as an HTML formatted string.
		/// </summary>
		[XmlElement("GridColor")]
		public string GridColorHtml
		{
			get { return ColorTranslator.ToHtml(this.GridColor.ToSystemColor()); }
			set { this.GridColor = ColorTranslator.FromHtml(value).ToXnaColor(); }
		}

		/// <summary>
		/// Gets or sets the flag to display grid lines on the tileset.
		/// </summary>
		public bool ShowGrid { get; set; }

		public ImageColorSettings()
		{
			this.BackgroundColor = XnaColor.White;
			this.SelectorColor = XnaColor.White;
			this.GridColor = XnaColor.Black;
			this.SelectorThickness = 2;
			this.ShowGrid = true;
		}
	}
}
