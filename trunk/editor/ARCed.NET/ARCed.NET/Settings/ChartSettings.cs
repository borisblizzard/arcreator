#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms.DataVisualization.Charting;
using System.Xml.Serialization;

#endregion

namespace ARCed.Settings
{
	[Serializable]
	public class ChartSettings
	{
		/// <summary>
		/// Gets or sets the type of the chart
		/// </summary>
		public SeriesChartType Type { get; set; }
		/// <summary>
		/// Gets or sets the lighting of the chart
		/// </summary>
		public LightStyle Lighting { get; set; }
		/// <summary>
		/// Gets or sets the spline tension of the chart
		/// </summary>
		public decimal SplineTension { get; set; }
		/// <summary>
		/// Gets or sets the perspective of the chart (3D only)
		/// </summary>
		public decimal Perspective { get; set; }
		/// <summary>
		/// Gets or sets the inclination of the chart (3D only)
		/// </summary>
		public decimal Inclination { get; set; }
		/// <summary>
		/// Gets or sets the rotation of the chart (3D only)
		/// </summary>
		public decimal Rotation { get; set; }
		/// <summary>
		/// Gets or sets the depth of the chart (3D only)
		/// </summary>
		public decimal Depth { get; set; }
		/// <summary>
		/// Gets or sets the flag to display chart as 3D
		/// </summary>
		public bool ThreeD { get; set; }
		/// <summary>
		/// Gets or sets the flag to display point markers
		/// </summary>
		public bool Markers { get; set; }
		/// <summary>
		/// Gets or sets the colors used for various charts
		/// </summary>
		[XmlIgnore]
		public List<Color> Colors { get; set; }
		/// <summary>
		/// Gets or sets the list of HTML string colors
		/// </summary>
		[XmlElement("Colors")]
		public List<string> ColorsHtml 
		{ 
			get
			{
				var colors = new List<string>();
				foreach (Color c in Colors)
					colors.Add(ColorTranslator.ToHtml(c));
				return colors;
			}
			set
			{
				var colors = new List<Color>();
				foreach (string color in value)
					colors.Add(ColorTranslator.FromHtml(color));
				Colors = colors;
			}
		}

		/// <summary>
		/// Default constructor
		/// </summary>
		public ChartSettings()
		{
			Type = SeriesChartType.SplineRange;
			Lighting = LightStyle.Realistic;
			SplineTension = 0.4M;
			Perspective = 0;
			Inclination = 0;
			Rotation = 0;
			Depth = 200;
			Markers = false;
			ThreeD = true;
			Colors = DefaultColors;
		}

		/// <summary>
		/// Default list of 8 colors used for charts
		/// </summary>
		/// <remarks>Tomato, Slate Blue, Forest Green, Orange, Thistle, Cadet Blue, Yellow-Green, and Violet</remarks>
		public static List<Color> DefaultColors
		{
			get
			{
				return new List<Color>
				{
					Color.Tomato,
					Color.SlateBlue,
					Color.ForestGreen,
					Color.Orange,
					Color.Thistle,
					Color.CadetBlue,
					Color.YellowGreen,
					Color.Violet
				};
			}
		}
	}
}
