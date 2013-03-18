#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla.Configuration
{
    public class KeyWordConfig
    {
        #region Fields

        private bool? _inherit;
        private int _list;
        private string _value;

        #endregion Fields


        #region Properties

        public bool? Inherit
        {
            get
            {
                return this._inherit;
            }
            set
            {
                this._inherit = value;
            }
        }


        public int List
        {
            get
            {
                return this._list;
            }
            set
            {
                this._list = value;
            }
        }


        public string Value
        {
            get
            {
                return this._value;
            }
            set
            {
                this._value = value;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the KeyWordConfig class.
        /// </summary>
        /// <param name="list"></param>
        /// <param name="value"></param>
        /// <param name="inherit"></param>
        public KeyWordConfig(int list, string value, bool? inherit)
        {
            this._list = list;
            this._value = value;
            this._inherit = inherit;
        }

        #endregion Constructors
    }
}
