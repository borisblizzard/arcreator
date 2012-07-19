#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla.Configuration
{
    public class MarginConfig
    {
        #region Fields

        private int? _autoToggleMarkerNumber;
        private bool? _inherit;
        private bool? _isClickable;
        private bool? _isFoldMargin;
        private bool? _isMarkerMargin;
        private int _number;
        private MarginType? _type;
        private int? _width;

        #endregion Fields


        #region Properties

        public int? AutoToggleMarkerNumber
        {
            get
            {
                return this._autoToggleMarkerNumber;
            }
            set
            {
                this._autoToggleMarkerNumber = value;
            }
        }


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


        public bool? IsClickable
        {
            get
            {
                return this._isClickable;
            }
            set
            {
                this._isClickable = value;
            }
        }


        public bool? IsFoldMargin
        {
            get
            {
                return this._isFoldMargin;
            }
            set
            {
                this._isFoldMargin = value;
            }
        }


        public bool? IsMarkerMargin
        {
            get
            {
                return this._isMarkerMargin;
            }
            set
            {
                this._isMarkerMargin = value;
            }
        }


        public int Number
        {
            get
            {
                return this._number;
            }
            set
            {
                this._number = value;
            }
        }


        public MarginType? Type
        {
            get
            {
                return this._type;
            }
            set
            {
                this._type = value;
            }
        }


        public int? Width
        {
            get
            {
                return this._width;
            }
            set
            {
                this._width = value;
            }
        }

        #endregion Properties
    }
}
