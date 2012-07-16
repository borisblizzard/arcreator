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
                return _color;
            }
            set
            {
                _color = value;
            }
        }


        public bool? Inherit
        {
            get
            {
                return _inherit;
            }
            set
            {
                _inherit = value;
            }
        }


        public bool? IsDrawnUnder
        {
            get
            {
                return _isDrawnUnder;
            }
            set
            {
                _isDrawnUnder = value;
            }
        }


        public int Number
        {
            get
            {
                return _number;
            }
            set
            {
                _number = value;
            }
        }


        public IndicatorStyle? Style
        {
            get
            {
                return _style;
            }
            set
            {
                _style = value;
            }
        }

        #endregion Properties
    }
}
