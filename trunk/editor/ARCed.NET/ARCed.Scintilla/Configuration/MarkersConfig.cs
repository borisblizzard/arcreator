#region Using Directives

using System.Drawing;

#endregion

namespace ARCed.Scintilla.Configuration
{
    public class MarkersConfig
    {
        #region Fields

        private int? _alpha;
        private Color _backColor;
        private Color _foreColor;
        private bool? _inherit;
        private string _name;
        private int? _number;
        private MarkerSymbol? _symbol;

        #endregion Fields


        #region Properties

        public int? Alpha
        {
            get
            {
                return this._alpha;
            }
            set
            {
                this._alpha = value;
            }
        }


        public Color BackColor
        {
            get
            {
                return this._backColor;
            }
            set
            {
                this._backColor = value;
            }
        }


        public Color ForeColor
        {
            get
            {
                return this._foreColor;
            }
            set
            {
                this._foreColor = value;
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


        public string Name
        {
            get
            {
                return this._name;
            }
            set
            {
                this._name = value;
            }
        }


        public int? Number
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


        public MarkerSymbol? Symbol
        {
            get
            {
                return this._symbol;
            }
            set
            {
                this._symbol = value;
            }
        }

        #endregion Properties
    }
}
