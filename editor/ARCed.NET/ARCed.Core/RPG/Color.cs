#region Using Directives

using ARCed;
using SysColor = System.Drawing.Color;

#endregion

namespace RPG
{
    /// <summary>
    /// The RGBA color class. Each component is handled with a <see langword="float"/> value.
    /// </summary>
    public class Color
    {
        #region Private Fields

        private float _red, _green, _blue, _alpha;

        #endregion

        #region Public Properties

        /// <summary>
        /// The red value (0-255). Values out of range are automatically corrected.
        /// </summary>
        public float red
        {
            get { return _red; } 
            set { _red = value.Clamp(0, 255); }
        }

        /// <summary>
        /// The green value (0-255). Values out of range are automatically corrected.
        /// </summary>
        public float green
        {
            get { return _green; }
            set { _green = value.Clamp(0, 255); }
        }
        /// <summary>
        /// The blue value (0-255). Values out of range are automatically corrected.
        /// </summary>
        public float blue
        {
            get { return _blue; }
            set { _blue = value.Clamp(0, 255); }
        }

        /// <summary>
        /// The alpha value (0-255). Values out of range are automatically corrected.
        /// </summary>
        public float alpha
        {
            get { return _alpha; }
            set { _alpha = value.Clamp(0, 255); }
        }

        #endregion

        #region Constructors

        /// <summary>
        /// Creates a Color object with all values initialized as 0.0.
        /// </summary>
        public Color() : this(0.0f, 0.0f, 0.0f, 0.0f) { }

        /// <summary>
        /// Creates a Color object. If alpha is omitted, it is assumed at 255.
        /// </summary>
        /// <param name="red">The red value (0-255)</param>
        /// <param name="green">The green value (0-255)</param>
        /// <param name="blue">The blue value (0-255)</param>
        /// <param name="alpha">The alpha value (0-255)</param>
        public Color(float red, float green, float blue, float alpha = 255.0f)
        {
            this.red = red;
            this.green = green;
            this.blue = blue;
            this.alpha = alpha;
        }

        #endregion

        #region Public Methods

        /// <summary>
        /// Sets all components at once. Alpha remains the same.
        /// </summary>
        /// <param name="red">The red value (0-255)</param>
        /// <param name="green">The green value (0-255)</param>
        /// <param name="blue">The blue value (0-255)</param>
        public void set(float red, float green, float blue)
        {
            set(red, green, blue, this.alpha);
        }

        /// <summary>
        /// Sets all components at once. 
        /// </summary>
        /// <param name="red">The red value (0-255)</param>
        /// <param name="green">The green value (0-255)</param>
        /// <param name="blue">The blue value (0-255)</param>
        /// <param name="alpha">The alpha value (0-255)</param>
        public void set(float red, float green, float blue, float alpha)
        {
            this.red = red;
            this.green = green;
            this.blue = blue;
            this.alpha = alpha;
        }

        /// <summary>
        /// Returns a <see langword="string"/> that represents the current object.
        /// </summary>
        /// <returns>String representation of object.</returns>
        public override string ToString()
        {
            return string.Format("{0}, {1}, {2}, {3}", red, green, blue, alpha);
        }

        #endregion

        #region Operators

        /// <summary>
        /// Implicit operator to convert a <see cref="Color"/> to a <see cref="SysColor"/>.
        /// </summary>
        /// <param name="color">Color to convert</param>
        /// <returns>A System.Drawing.Color representation of the object.</returns>
        public static implicit operator SysColor(Color color)
        {
            return SysColor.FromArgb((int)color.alpha, (int)color.red,
                (int)color.green, (int)color.blue);
        }

        /// <summary>
        /// Implicit operator to convert a <see cref="SysColor"/> to a <see cref="Color"/>.
        /// </summary>
        /// <param name="color">Color to convert</param>
        /// <returns>Color representation of the object.</returns>
        public static implicit operator Color(SysColor color)
        {
            return new Color(color.R, color.G, color.B, color.A);
        }

        #endregion
    }
}
