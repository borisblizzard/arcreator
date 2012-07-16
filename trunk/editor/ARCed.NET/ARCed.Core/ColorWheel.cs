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
                if (_alphaImage == null)
                {
                    _alphaImage = new Bitmap(16, 16);
                    using (var g = Graphics.FromImage(_alphaImage))
                    {
                        g.FillRectangle(Brushes.Gray, 0, 0, 8, 8);
                        g.FillRectangle(Brushes.Gray, 8, 8, 8, 8);
                    }
                }
                return new TextureBrush(_alphaImage, WrapMode.Tile, new Rectangle(0, 0, 16, 16));
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
            get { return _selectedColor; }
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
				_colorRectangle = colorRectangle;
				_brightnessRectangle = brightnessRectangle;
				_selectedColorRectangle = selectedColorRectangle;
				_radius = Math.Min(colorRectangle.Width, colorRectangle.Height) / 2;
				_centerPoint = colorRectangle.Location;
				_centerPoint.Offset(_radius, _radius);
				_colorPoint = _centerPoint;
				path.AddEllipse(colorRectangle);
				_colorRegion = new Region(path);
				_brightnessMin = _brightnessRectangle.Top;
				_brightnessMax = _brightnessRectangle.Bottom;
				path.AddRectangle(new Rectangle(brightnessRectangle.Left, brightnessRectangle.Top - 10,
					brightnessRectangle.Width + 10, brightnessRectangle.Height + 20));
				_brightnessRegion = new Region(path);
				_brightnessX = brightnessRectangle.Left + brightnessRectangle.Width;
				_brightnessScaling = (double)255 / (_brightnessMax - _brightnessMin);
				_brightnessPoint = new Point(_brightnessX, _brightnessMax);
				CreateGradient();
			}
		}

        #endregion

        #region IDisposable Members

        void IDisposable.Dispose()
		{
			if (_colorImage != null)
				_colorImage.Dispose();
			if (_colorRegion != null)
				_colorRegion.Dispose();
			if (_brightnessRegion != null)
				_brightnessRegion.Dispose();
			if (_graphics != null)
				_graphics.Dispose();
		}

		#endregion

        #region Public Methods

        /// <summary>
        /// Sets the mouse state to MouseState.MouseUp
        /// </summary>
        public void SetMouseUp()
        {
            _currentState = MouseState.MouseUp;
        }

        /// <summary>
        /// Draws the images
        /// </summary>
        /// <param name="g">Graphics context to draw with</param>
        /// <param name="hsv">HSV color to draw</param>
        public void Draw(Graphics g, ColorHandler.HSV hsv)
        {
            _graphics = g;
            _hsv = hsv;
            CalcCoordsAndUpdate(_hsv);
            UpdateDisplay();
        }

        /// <summary>
        /// Draws the images
        /// </summary>
        /// <param name="g">Graphics context to draw with</param>
        /// <param name="argb">ARGB color to draw</param>
        public void Draw(Graphics g, ColorHandler.ARGB argb)
        {
            _graphics = g;
            _hsv = ColorHandler.RGBtoHSV(argb);
            CalcCoordsAndUpdate(_hsv);
            UpdateDisplay();
        }

        /// <summary>
        /// Draws the images
        /// </summary>
        /// <param name="g">Graphics context to draw with</param>
        /// <param name="mousePoint">MousePoint to draw</param>
        public void Draw(Graphics g, Point mousePoint)
        {
            var newColorPoint = _colorPoint;
            var newBrightnessPoint = _brightnessPoint;
            _graphics = g;
            if (_currentState == MouseState.MouseUp)
            {
                if (!mousePoint.IsEmpty)
                {
                    if (_colorRegion.IsVisible(mousePoint))
                        _currentState = MouseState.ClickOnColor;
                    else if (_brightnessRegion.IsVisible(mousePoint))
                        _currentState = MouseState.ClickOnBrightness;
                    else
                        _currentState = MouseState.ClickOutsideRegion;
                }
            }
            switch (_currentState)
            {
                case MouseState.ClickOnBrightness:
                case MouseState.DragInBrightness:
                    var newPoint = mousePoint;
                    if (newPoint.Y < _brightnessMin)
                    {
                        newPoint.Y = _brightnessMin;
                    }
                    else if (newPoint.Y > _brightnessMax)
                    {
                        newPoint.Y = _brightnessMax;
                    }
                    newBrightnessPoint = new Point(_brightnessX, newPoint.Y);
                    _brightness = (int)((_brightnessMax - newPoint.Y) * _brightnessScaling);
                    _hsv.Value = _brightness;
                    _argb = ColorHandler.HSVtoRGB(_hsv);
                    break;

                case MouseState.ClickOnColor:
                case MouseState.DragInColor:
                    newColorPoint = mousePoint;
                    var delta = new Point(mousePoint.X - _centerPoint.X, mousePoint.Y - _centerPoint.Y);
                    var degrees = CalcDegrees(delta);
                    var distance = Math.Sqrt(delta.X * delta.X + delta.Y * delta.Y) / _radius;
                    if (_currentState == MouseState.DragInColor)
                    {
                        if (distance > 1)
                        {
                            distance = 1;
                            newColorPoint = GetPoint(degrees, _radius, _centerPoint);
                        }
                    }
                    _hsv.Hue = (degrees * 255 / 360);
                    _hsv.Saturation = (int)(distance * 255);
                    _hsv.Value = _brightness;
                    _argb = ColorHandler.HSVtoRGB(_hsv);
                    _fullColor = ColorHandler.HSVtoColor(_hsv.Alpha, _hsv.Hue, _hsv.Saturation, 255);
                    break;
            }
            _selectedColor = ColorHandler.HSVtoColor(_hsv);
            OnColorChanged(_argb, _hsv);
            switch (_currentState)
            {
                case MouseState.ClickOnBrightness:
                    _currentState = MouseState.DragInBrightness;
                    break;
                case MouseState.ClickOnColor:
                    _currentState = MouseState.DragInColor;
                    break;
                case MouseState.ClickOutsideRegion:
                    _currentState = MouseState.DragOutsideRegion;
                    break;
            }
            _colorPoint = newColorPoint;
            _brightnessPoint = newBrightnessPoint;
            UpdateDisplay();
        }

        #endregion

        #region Private/Protected Methods

        protected void OnColorChanged(ColorHandler.ARGB argb, ColorHandler.HSV hsv)
		{
			var e = new ColorChangedEventArgs(argb, hsv);
			ColorChanged(this, e);
		}

		private Point CalcBrightnessPoint(int brightness)
		{
			return new Point(_brightnessX,
				(int)(_brightnessMax - brightness / _brightnessScaling));
		}

		private void UpdateDisplay()
		{
			using (Brush selectedBrush = new SolidBrush(_selectedColor))
			{
				_graphics.DrawImage(_colorImage, _colorRectangle);
                _graphics.FillRectangle(AlphaBrush, _selectedColorRectangle);
				_graphics.FillRectangle(selectedBrush, _selectedColorRectangle);
				_graphics.DrawRectangle(Pens.Black, _selectedColorRectangle);
				DrawLinearGradient(_fullColor);
				DrawColorPointer(_colorPoint);
				DrawBrightnessPointer(_brightnessPoint);
			}
		}

		private void CalcCoordsAndUpdate(ColorHandler.HSV hsv)
		{
			_colorPoint = GetPoint((double)hsv.Hue / 255 * 360,
				(double)hsv.Saturation / 255 * _radius,
				_centerPoint);
			_brightnessPoint = CalcBrightnessPoint(hsv.Value);
			_brightness = hsv.Value;
			_selectedColor = ColorHandler.HSVtoColor(hsv);
			_argb = ColorHandler.HSVtoRGB(hsv);
			_fullColor = ColorHandler.HSVtoColor(hsv.Alpha, hsv.Hue, hsv.Saturation, 255);
		}

		private void DrawLinearGradient(Color topColor)
		{
			using (var lgb =
				new LinearGradientBrush(_brightnessRectangle, topColor,
					Color.Black, LinearGradientMode.Vertical))
			{
				_graphics.FillRectangle(lgb, _brightnessRectangle);
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
				new PathGradientBrush(GetPoints(_radius, new Point(_radius, _radius))))
			{
				pgb.CenterColor = Color.White;
				pgb.CenterPoint = new PointF(_radius, _radius);
				pgb.SurroundColors = GetColors();
				_colorImage = new Bitmap(
					_colorRectangle.Width, _colorRectangle.Height,
					PixelFormat.Format32bppArgb);
				using (var newGraphics = Graphics.FromImage(_colorImage))
				{
					newGraphics.FillEllipse(pgb, 0, 0,
						_colorRectangle.Width, _colorRectangle.Height);
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
			_graphics.DrawRectangle(Pens.Black,
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
			_graphics.FillPolygon(Brushes.Black, points);
        }

        #endregion
    }
}
