#region Using Directives

using System;
using System.Drawing;

#endregion

namespace ARCed.Core
{
    /// <summary>
    /// Handle conversions between RGB and HSV color spaces.
    /// </summary>
	public class ColorHandler
    {
        #region Public Methods

        /// <summary>
        /// Converts a HSV color values to an RGB color
        /// </summary>
        /// <param name="a">Alpha value</param>
        /// <param name="h">Hue value</param>
        /// <param name="s">Saturation value</param>
        /// <param name="v">Value value</param>
        /// <returns>RGB color equivalent</returns>
		public static ARGB HSVtoRGB(int a, int h, int s, int v)
		{
            return HSVtoRGB(new HSV(a, h, s, v));
		}

        /// <summary>
        /// Converts a HSV color to a System.Drawing.Color
        /// </summary>
        /// <param name="hsv">HSV color to convert</param>
        /// <returns>System.Drawing.Color equivalent</returns>
		public static Color HSVtoColor(HSV hsv)
		{
			var argb = HSVtoRGB(hsv);
			return Color.FromArgb(argb.Alpha, argb.Red, argb.Green, argb.Blue);
		}

        /// <summary>
        /// Converts a HSV color values to a System.Drawing.Color.
        /// </summary>
        /// <param name="a">Alpha value</param>
        /// <param name="h">Hue value</param>
        /// <param name="s">Saturation value</param>
        /// <param name="v">Value value</param>
        /// <returns>System.Drawing.Color equivalent</returns>
		public static Color HSVtoColor(int a, int h, int s, int v)
		{
            return HSVtoColor(new HSV(a, h, s, v));
		}

        /// <summary>
        /// Converts a HSV color values to an RGB color
        /// </summary>
        /// <param name="hsv">HSV color to convert</param>
        /// <returns>RGB color equivalent</returns>
		public static ARGB HSVtoRGB(HSV hsv)
        {
            double r = 0.0d, g = 0.0d, b = 0.0d;
			var h = ((double)hsv.Hue / 255 * 360) % 360;
			var s = (double)hsv.Saturation / 255;
			var v = (double)hsv.Value / 255;

			if (Equals(s, 0.0d))
			{
				r = v;
				g = v;
				b = v;
			}
			else
			{
				var sectorPos = h / 60;
				var sectorNumber = (int)(Math.Floor(sectorPos));
				var fractionalSector = sectorPos - sectorNumber;
				var p = v * (1 - s);
				var q = v * (1 - (s * fractionalSector));
				var t = v * (1 - (s * (1 - fractionalSector)));
				switch (sectorNumber)
				{
					case 0:
						r = v;
						g = t;
						b = p;
						break;

					case 1:
						r = q;
						g = v;
						b = p;
						break;

					case 2:
						r = p;
						g = v;
						b = t;
						break;

					case 3:
						r = p;
						g = q;
						b = v;
						break;

					case 4:
						r = t;
						g = p;
						b = v;
						break;

					case 5:
						r = v;
						g = p;
						b = q;
						break;
				}
			}
			return new ARGB(hsv.Alpha, (int)(r * 255), (int)(g * 255), (int)(b * 255));
		}

		/// <summary>
		/// Converts an ARGB color to a HSV color.
		/// </summary>
		/// <param name="argb">ARGB color to convert</param>
		/// <returns>HSV color equivalent</returns>
		public static HSV RGBtoHSV(ARGB argb)
		{
            double h, s;
			var r = (double)argb.Red / 255;
			var g = (double)argb.Green / 255;
			var b = (double)argb.Blue / 255;
		    var min = Math.Min(Math.Min(r, g), b);
			var max = Math.Max(Math.Max(r, g), b);
			var v = max;
			var delta = max - min;
			if (Equals(max, 0.0d) || Equals(delta, 0.0d))
			{
				s = 0;
				h = 0;
			}
			else
			{
				s = delta / max;
				if (Equals(r, max))
					h = (g - b) / delta;
				else if (Equals(g, max))
					h = 2 + (b - r) / delta;
				else
					h = 4 + (r - g) / delta;
			}
			h *= 60;
			if (h < 0)
				h += 360;
			return new HSV(argb.Alpha, (int)(h / 360 * 255), (int)(s * 255), (int)(v * 255));
		}

        #endregion

        #region Nested type: ARGB

        /// <summary>
        /// Struct containing data for a color of the ARGB color space.
        /// </summary>
        public struct ARGB
		{
            #region Public Properties

            /// <summary>
            /// Gets or sets the alpha value
            /// </summary>
            public int Alpha { get; set; }

            /// <summary>
            /// Gets or sets the red value
            /// </summary>
            public int Red { get; set; }

            /// <summary>
            /// Gets or sets the green value
            /// </summary>
            public int Green { get; set; }

            /// <summary>
            /// Gets or sets the blue value
            /// </summary>
            public int Blue { get; set; }

            #endregion

			/// <summary>
			/// Default constructor
			/// </summary>
			/// <param name="a">Alpha value</param>
			/// <param name="r">Red value</param>
			/// <param name="g">Green value</param>
			/// <param name="b">Blue value</param>
			/// <remarks>Values are clamped between 0 and 255</remarks>
			public ARGB(int a, int r, int g, int b)
				: this()
			{
				Alpha = a.Clamp(0, 255);
                Red = r.Clamp(0, 255);
                Green = g.Clamp(0, 255);
                Blue = b.Clamp(0, 255);
			}

            /// <summary>
            /// Converts and returns the string representation of the object
            /// </summary>
            /// <returns>String representation</returns>
            public override string ToString()
			{
				return String.Format("({0}, {1}, {2} {3})", Alpha, Red, Green, Blue);
			}
		}

		#endregion

		#region Nested type: HSV

        /// <summary>
        /// Struct containing data for a color of the HSV color space.
        /// </summary>
		public struct HSV
		{
            #region Public Properties

            /// <summary>
            /// Gets or sets the alpha value
            /// </summary>
            public int Alpha { get; set; }

            /// <summary>
            /// Gets or sets the hue value
            /// </summary>
            public int Hue { get; set; }

            /// <summary>
            /// Gets or sets the saturation value
            /// </summary>
            public int Saturation { get; set; }

            /// <summary>
            /// Gets or sets the value value
            /// </summary>
            public int Value { get; set; }

            #endregion

            /// <summary>
            /// Default constructor
            /// </summary>
            /// <param name="a">Alpha value</param>
            /// <param name="h">Hue value</param>
            /// <param name="s">Saturation value</param>
            /// <param name="v">Value value</param>
			public HSV(int a, int h, int s, int v)
				: this()
			{
				Alpha = a;
				Hue = h;
				Saturation = s;
				Value = v;
			}

            /// <summary>
            /// Converts and returns the string representation of the object
            /// </summary>
            /// <returns>String representation</returns>
			public override string ToString()
			{
				return String.Format("({0}, {1}, {2})", Hue, Saturation, Value);
			}
		}

		#endregion
	}

    /// <summary>
    /// Arguments used when the color changes.
    /// </summary>
	public class ColorChangedEventArgs : EventArgs
	{
        /// <summary>
        /// Default constructor
        /// </summary>
        /// <param name="argb">ARGB color value</param>
        /// <param name="hsv">HSV color value</param>
		public ColorChangedEventArgs(ColorHandler.ARGB argb, ColorHandler.HSV hsv)
		{
			ARGB = argb;
			HSV = hsv;
		}

        /// <summary>
        /// Gets the color value in the ARGB color space.
        /// </summary>
		public ColorHandler.ARGB ARGB { get; private set; }

        /// <summary>
        /// Gets the color value in the HSV color space.
        /// </summary>
		public ColorHandler.HSV HSV { get; private set; }
	}
}
