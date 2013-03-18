#region Using Directives

using System.Drawing;

#endregion


namespace ARCed.Scintilla.Configuration
{
    public class IndicatorConfig
    {
        #region Fields

        private Color _color;
        private bool? _inherit;
        private bool? _isDrawnUnder;
        private int _number;
        private IndicatorStyle? _style;

        #endregion Fields


        #region Properties

        public Color Color
        {
            get
            {
                return this._color;
            }
            set
            {
                this._color = value;
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


        public bool? IsDrawnUnder
        {
            get
            {
                return this._isDrawnUnder;
            }
            set
            {
                this._isDrawnUnder = value;
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


        public IndicatorStyle? Style
        {
            get
            {
                return this._style;
            }
            set
            {
                this._style = value;
            }
        }

        #endregion Properties
    }
}
