#region Using Directives

using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Represents the Binding Combination of a Keyboard Key + Modifiers
    /// </summary>
    public struct KeyBinding
    {
        #region Fields

        private Keys _keycode;
        private Keys _modifiers;

        #endregion Fields


        #region Methods

        /// <summary>
        ///     Overridden.
        /// </summary>
        /// <param name="obj">Another KeyBinding struct</param>
        /// <returns>True if the Keycode and Modifiers are equal</returns>
        public override bool Equals(object obj)
        {
            if (!(obj is KeyBinding))
                return false;

            var kb = (KeyBinding)obj;

            return this._keycode == kb._keycode && this._modifiers == kb._modifiers;
        }

        /// <summary>
        ///     Overridden
        /// </summary>
        /// <returns>Hashcode of ToString()</returns>
        public override int GetHashCode()
        {
            return this.ToString().GetHashCode();
        }


        /// <summary>
        ///     Overridden. Returns string representation of the Keyboard shortcut
        /// </summary>
        /// <returns>Returns string representation of the Keyboard shortcut</returns>
        public override string ToString()
        {
            return ((int)this._keycode).ToString() + ((int)this._modifiers).ToString();
        }

        #endregion Methods


        #region Properties

        /// <summary>
        ///     Gets/Sets Key to trigger command
        /// </summary>
        public Keys KeyCode
        {
            get
            {
                return this._keycode;
            }
            set
            {
                this._keycode = value;
            }
        }


        /// <summary>
        ///     Gets sets key modifiers to the Keyboard shortcut
        /// </summary>
        public Keys Modifiers
        {
            get
            {
                return this._modifiers;
            }
            set
            {
                this._modifiers = value;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the KeyBinding structure.
        /// </summary>
        /// <param name="keycode">Key to trigger command</param>
        /// <param name="modifiers"> key modifiers to the Keyboard shortcut</param>
        public KeyBinding(Keys keycode, Keys modifiers)
        {
            this._keycode = keycode;
            this._modifiers = modifiers;
        }

        #endregion Constructors
    }
}
