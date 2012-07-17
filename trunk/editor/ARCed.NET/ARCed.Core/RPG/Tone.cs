#region Using Directives

using ARCed;

#endregion

namespace RPG
{
    /// <summary>
    /// The color tone class. Each component is handled with a <see langword="float"/> value.
    /// </summary>
    public class Tone
    {
        #region Private Fields

        private float _red, _green, _blue, _gray;

        #endregion

        #region Public Properties

        /// <summary>
        /// The red value (-255-255). Values out of range are automatically corrected.
        /// </summary>
        public float red
        {
            get { return _red; }
            set { _red = value.Clamp(-255, 255); }
        }

        /// <summary>
        /// The green value (-255-255). Values out of range are automatically corrected.
        /// </summary>
        public float green
        {
            get { return _green; }
            set { _green = value.Clamp(-255, 255); }
        }
        /// <summary>
        /// The blue value (-255-255). Values out of range are automatically corrected.
        /// </summary>
        public float blue
        {
            get { return _blue; }
            set { _blue = value.Clamp(-255, 255); }
        }

        /// <summary>
        /// The gray value (0-255). Values out of range are automatically corrected.
        /// </summary>
        public float gray
        {
            get { return this._gray; }
            set { this._gray = value.Clamp(0, 255); }
        }

        #endregion

        #region Constructors

        /// <summary>
        /// Creates a Tone object with all values initialized as 0.0.
        /// </summary>
        public Tone() : this(0.0f, 0.0f, 0.0f) { }

        /// <summary>
        /// Creates a Tone object. If gray is omitted, it is assumed at 0.
        /// </summary>
        /// <param name="red">The red value (-255-255)</param>
        /// <param name="green">The green value (-255-255)</param>
        /// <param name="blue">The blue value (-255-255)</param>
        /// <param name="gray">The gray value (0-255)</param>
        public Tone(float red, float green, float blue, float gray = 0.0f)
        {
            this.red = red;
            this.green = green;
            this.blue = blue;
            this.gray = gray;
        }

        #endregion

        #region Public Methods

        /// <summary>
        /// Sets all components at once. Gray remains the same.
        /// </summary>
        /// <param name="red">The red value (-255-255)</param>
        /// <param name="green">The green value (-255-255)</param>
        /// <param name="blue">The blue value (-255-255)</param>
        public void set(float red, float green, float blue)
        {
            set(red, green, blue, this.gray);
        }

        /// <summary>
        /// Sets all components at once. 
        /// </summary>
        /// <param name="red">The red value (-255-255)</param>
        /// <param name="green">The green value (-255-255)</param>
        /// <param name="blue">The blue value (-255-255)</param>
        /// <param name="gray">The gray value (0-255)</param>
        public void set(float red, float green, float blue, float gray)
        {
            this.red = red;
            this.green = green;
            this.blue = blue;
            this.gray = gray;
        }

        /// <summary>
        /// Returns a <see langword="string"/> that represents the current object.
        /// </summary>
        /// <returns>String representation of object.</returns>
        public override string ToString()
        {
            return string.Format("{0}, {1}, {2}, {3}", red, green, blue, gray);
        }

        #endregion
    }
}
