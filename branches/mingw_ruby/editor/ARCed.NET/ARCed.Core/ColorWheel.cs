#region Using Directives

using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;

#endregion

namespace ARCed.Core
{
    /// <summary>
    /// Color wheel for getting a user-selected color
    /// </summary>
	public class ColorWheel : IDisposable
	{

		#region Delegates

        /// <summary>
        /// Handler for color changing events
        /// </summary>
        /// <param name="sender">Delegate invoker</param>
        /// <param name="e">Event arguments</param>
		public delegate void ColorChangedEventHandler(object sender, ColorChangedEventArgs e);

		#endregion

		#region MouseState enum

        /// <summary>
        /// Enum for tracking current mouse state
        /// </summary>
		public enum MouseState
		{
            /// <summary>
            /// Mouse up state
            /// </summary>
			MouseUp,
            /// <summary>
            /// Mouse click on color state
            /// </summary>
			ClickOnColor,
            /// <summary>
            /// Mouse drag in color state
            /// </summary>
			DragInColor,
            /// <summary>
            /// Mouse click on brightness state
            /// </summary>
			ClickOnBrightness,
            /// <summary>
            /// Mouse drag in brightness state
            /// </summary>
			DragInBrightness,
            /// <summary>
            /// Mouse click outside region state
            /// </summary>
			ClickOutsideRegion,
            /// <summary>
            /// Mouse drag outside region state.
            /// </summary>
			DragOutsideRegion,
		}

		#endregion

        #region Private Fields

        private Image _alphaImage;
        private const double DEGREES_PER_RADIAN = 180.0 / Math.PI;

		private const int COLOR_COUNT = 6 * 256;
		private readonly int _brightnessMax, _brightnessMin, _brightnessX, _radius;
		private readonly Rectangle _brightnessRectangle, _selectedColorRectangle;
		private readonly Region _brightnessRegion, _colorRegion;
		private readonly double _brightnessScaling;

        private ColorHandler.HSV _hsv;
        private ColorHandler.ARGB _argb;
        private int _brightness;
        private Point _brightnessPoint, _centerPoint, _colorPoint;
        private Bitmap _colorImage;
        private Rectangle _colorRectangle;
        private MouseState _currentState = MouseState.MouseUp;
        private Graphics _graphics;
        private Color _selectedColor = Color.White, _fullColor;

        #endregion

        #region Public Properties

        internal TextureBrush AlphaBrush
        {
            get
            {
                if (this._alphaImage == null)
                {
                    this._alphaImage = new Bitmap(16, 16);
                    using (var g = Graphics.FromImage(this._alphaImage))
                    {
                        g.FillRectangle(Brushes.Gray, 0, 0, 8, 8);
                        g.FillRectangle(Brushes.Gray, 8, 8, 8, 8);
                    }
                }
                return new TextureBrush(this._alphaImage, WrapMode.Tile, new Rectangle(0, 0, 16, 16));
            }
        }

        /// <summary>
        /// Handler for color change events
        /// </summary>
		public ColorChangedEventHandler ColorChanged;

        /// <summary>
        /// Gets the selected color
        /// </summary>
        public Color Color
        {
            get { return this._selectedColor; }
        }

        #endregion

        #region Constructor

        /// <summary>
        /// Default constructor
        /// </summary>
        /// <param name="colorRectangle">Rectangle for the color wheel image</param>
        /// <param name="brightnessRectangle">Rectangle for the brightness control</param>
        /// <param name="selectedColorRectangle">Rectangle for the selected color control</param>
		public ColorWheel(Rectangle colorRectangle, Rectangle brightnessRectangle, Rectangle selectedColorRectangle)
		{
			using (var path = new GraphicsPath())
			{
				this._colorRectangle = colorRectangle;
				this._brightnessRectangle = brightnessRectangle;
				this._selectedColorRectangle = selectedColorRectangle;
				this._radius = Math.Min(colorRectangle.Width, colorRectangle.Height) / 2;
				this._centerPoint = colorRectangle.Location;
				this._centerPoint.Offset(this._radius, this._radius);
				this._colorPoint = this._centerPoint;
				path.AddEllipse(colorRectangle);
				this._colorRegion = new Region(path);
				this._brightnessMin = this._brightnessRectangle.Top;
				this._brightnessMax = this._brightnessRectangle.Bottom;
				path.AddRectangle(new Rectangle(brightnessRectangle.Left, brightnessRectangle.Top - 10,
					brightnessRectangle.Width + 10, brightnessRectangle.Height + 20));
				this._brightnessRegion = new Region(path);
				this._brightnessX = brightnessRectangle.Left + brightnessRectangle.Width;
				this._brightnessScaling = (double)255 / (this._brightnessMax - this._brightnessMin);
				this._brightnessPoint = new Point(this._brightnessX, this._brightnessMax);
				this.CreateGradient();
			}
		}

        #endregion

        #region IDisposable Members

        void IDisposable.Dispose()
		{
			if (this._colorImage != null)
				this._colorImage.Dispose();
			if (this._colorRegion != null)
				this._colorRegion.Dispose();
			if (this._brightnessRegion != null)
				this._brightnessRegion.Dispose();
			if (this._graphics != null)
				this._graphics.Dispose();
		}

		#endregion

        #region Public Methods

        /// <summary>
        /// Sets the mouse state to MouseState.MouseUp
        /// </summary>
        public void SetMouseUp()
        {
            this._currentState = MouseState.MouseUp;
        }

        /// <summary>
        /// Draws the images
        /// </summary>
        /// <param name="g">Graphics context to draw with</param>
        /// <param name="hsv">HSV color to draw</param>
        public void Draw(Graphics g, ColorHandler.HSV hsv)
        {
            this._graphics = g;
            this._hsv = hsv;
            this.CalcCoordsAndUpdate(this._hsv);
            this.UpdateDisplay();
        }

        /// <summary>
        /// Draws the images
        /// </summary>
        /// <param name="g">Graphics context to draw with</param>
        /// <param name="argb">ARGB color to draw</param>
        public void Draw(Graphics g, ColorHandler.ARGB argb)
        {
            this._graphics = g;
            this._hsv = ColorHandler.RGBtoHSV(argb);
            this.CalcCoordsAndUpdate(this._hsv);
            this.UpdateDisplay();
        }

        /// <summary>
        /// Draws the images
        /// </summary>
        /// <param name="g">Graphics context to draw with</param>
        /// <param name="mousePoint">MousePoint to draw</param>
        public void Draw(Graphics g, Point mousePoint)
        {
            var newColorPoint = this._colorPoint;
            var newBrightnessPoint = this._brightnessPoint;
            this._graphics = g;
            if (this._currentState == MouseState.MouseUp)
            {
                if (!mousePoint.IsEmpty)
                {
                    if (this._colorRegion.IsVisible(mousePoint))
                        this._currentState = MouseState.ClickOnColor;
                    else if (this._brightnessRegion.IsVisible(mousePoint))
                        this._currentState = MouseState.ClickOnBrightness;
                    else
                        this._currentState = MouseState.ClickOutsideRegion;
                }
            }
            switch (this._currentState)
            {
                case MouseState.ClickOnBrightness:
                case MouseState.DragInBrightness:
                    var newPoint = mousePoint;
                    if (newPoint.Y < this._brightnessMin)
                    {
                        newPoint.Y = this._brightnessMin;
                    }
                    else if (newPoint.Y > this._brightnessMax)
                    {
                        newPoint.Y = this._brightnessMax;
                    }
                    newBrightnessPoint = new Point(this._brightnessX, newPoint.Y);
                    this._brightness = (int)((this._brightnessMax - newPoint.Y) * this._brightnessScaling);
                    this._hsv.Value = this._brightness;
                    this._argb = ColorHandler.HSVtoRGB(this._hsv);
                    break;

                case MouseState.ClickOnColor:
                case MouseState.DragInColor:
                    newColorPoint = mousePoint;
                    var delta = new Point(mousePoint.X - this._centerPoint.X, mousePoint.Y - this._centerPoint.Y);
                    var degrees = CalcDegrees(delta);
                    var distance = Math.Sqrt(delta.X * delta.X + delta.Y * delta.Y) / this._radius;
                    if (this._currentState == MouseState.DragInColor)
                    {
                        if (distance > 1)
                        {
                            distance = 1;
                            newColorPoint = GetPoint(degrees, this._radius, this._centerPoint);
                        }
                    }
                    this._hsv.Hue = (degrees * 255 / 360);
                    this._hsv.Saturation = (int)(distance * 255);
                    this._hsv.Value = this._brightness;
                    this._argb = ColorHandler.HSVtoRGB(this._hsv);
                    this._fullColor = ColorHandler.HSVtoColor(this._hsv.Alpha, this._hsv.Hue, this._hsv.Saturation, 255);
                    break;
            }
            this._selectedColor = ColorHandler.HSVtoColor(this._hsv);
            this.OnColorChanged(this._argb, this._hsv);
            switch (this._currentState)
            {
                case MouseState.ClickOnBrightness:
                    this._currentState = MouseState.DragInBrightness;
                    break;
                case MouseState.ClickOnColor:
                    this._currentState = MouseState.DragInColor;
                    break;
                case MouseState.ClickOutsideRegion:
                    this._currentState = MouseState.DragOutsideRegion;
                    break;
            }
            this._colorPoint = newColorPoint;
            this._brightnessPoint = newBrightnessPoint;
            this.UpdateDisplay();
        }

        #endregion

        #region Private/Protected Methods

        protected void OnColorChanged(ColorHandler.ARGB argb, ColorHandler.HSV hsv)
		{
			var e = new ColorChangedEventArgs(argb, hsv);
			this.ColorChanged(this, e);
		}

		private Point CalcBrightnessPoint(int brightness)
		{
			return new Point(this._brightnessX,
				(int)(this._brightnessMax - brightness / this._brightnessScaling));
		}

		private void UpdateDisplay()
		{
			using (Brush selectedBrush = new SolidBrush(this._selectedColor))
			{
				this._graphics.DrawImage(this._colorImage, this._colorRectangle);
                this._graphics.FillRectangle(this.AlphaBrush, this._selectedColorRectangle);
				this._graphics.FillRectangle(selectedBrush, this._selectedColorRectangle);
				this._graphics.DrawRectangle(Pens.Black, this._selectedColorRectangle);
				this.DrawLinearGradient(this._fullColor);
				this.DrawColorPointer(this._colorPoint);
				this.DrawBrightnessPointer(this._brightnessPoint);
			}
		}

		private void CalcCoordsAndUpdate(ColorHandler.HSV hsv)
		{
			this._colorPoint = GetPoint((double)hsv.Hue / 255 * 360,
				(double)hsv.Saturation / 255 * this._radius,
				this._centerPoint);
			this._brightnessPoint = this.CalcBrightnessPoint(hsv.Value);
			this._brightness = hsv.Value;
			this._selectedColor = ColorHandler.HSVtoColor(hsv);
			this._argb = ColorHandler.HSVtoRGB(hsv);
			this._fullColor = ColorHandler.HSVtoColor(hsv.Alpha, hsv.Hue, hsv.Saturation, 255);
		}

		private void DrawLinearGradient(Color topColor)
		{
			using (var lgb =
				new LinearGradientBrush(this._brightnessRectangle, topColor,
					Color.Black, LinearGradientMode.Vertical))
			{
				this._graphics.FillRectangle(lgb, this._brightnessRectangle);
			}
		}

		private static int CalcDegrees(Point pt)
		{
			int degrees;
			if (pt.X == 0)
			{
				degrees = pt.Y > 0 ? 270 : 90;
			}
			else
			{
				degrees = (int)(-Math.Atan((double)pt.Y / pt.X) * DEGREES_PER_RADIAN);
				if (pt.X < 0)
				{
					degrees += 180;
				}
				degrees = (degrees + 360) % 360;
			}
			return degrees;
		}

		private void CreateGradient()
		{
			using (var pgb =
				new PathGradientBrush(GetPoints(this._radius, new Point(this._radius, this._radius))))
			{
				pgb.CenterColor = Color.White;
				pgb.CenterPoint = new PointF(this._radius, this._radius);
				pgb.SurroundColors = GetColors();
				this._colorImage = new Bitmap(
					this._colorRectangle.Width, this._colorRectangle.Height,
					PixelFormat.Format32bppArgb);
				using (var newGraphics = Graphics.FromImage(this._colorImage))
				{
					newGraphics.FillEllipse(pgb, 0, 0,
						this._colorRectangle.Width, this._colorRectangle.Height);
				}
			}
		}

		private static Color[] GetColors()
		{
			var colors = new Color[COLOR_COUNT];
			for (int i = 0; i <= COLOR_COUNT - 1; i++)
				colors[i] = ColorHandler.HSVtoColor(255, (int)((double)(i * 255) / COLOR_COUNT), 255, 255);
			return colors;
		}

		private static Point[] GetPoints(double radius, Point centerPoint)
		{
			var points = new Point[COLOR_COUNT];
			for (var i = 0; i <= COLOR_COUNT - 1; i++)
				points[i] = GetPoint((double)(i * 360) / COLOR_COUNT, radius, centerPoint);
			return points;
		}

		private static Point GetPoint(double degrees, double radius, Point centerPoint)
		{
			var radians = degrees / DEGREES_PER_RADIAN;
			return new Point((int)(centerPoint.X + Math.Floor(radius * Math.Cos(radians))),
				(int)(centerPoint.Y - Math.Floor(radius * Math.Sin(radians))));
		}

		private void DrawColorPointer(Point pt)
		{
			const int size = 3;
			this._graphics.DrawRectangle(Pens.Black,
				pt.X - size, pt.Y - size, size * 2, size * 2);
		}

		private void DrawBrightnessPointer(Point pt)
		{
			const int height = 10;
			const int width = 7;
			var points = new Point[3];
			points[0] = pt;
			points[1] = new Point(pt.X + width, pt.Y + height / 2);
			points[2] = new Point(pt.X + width, pt.Y - height / 2);
			this._graphics.FillPolygon(Brushes.Black, points);
        }

        #endregion
    }
}
