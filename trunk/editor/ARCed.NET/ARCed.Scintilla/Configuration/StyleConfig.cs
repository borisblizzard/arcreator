#region Using Directives

using System.Drawing;

#endregion


namespace ARCed.Scintilla.Configuration
{
    public class StyleConfig
    {
        #region Fields

        private Color _backColor;
        private bool? _bold;
        private StyleCase? _case;
        private CharacterSet? _characterSet;
        private string _fontName;
        private Color _foreColor;
        private bool? _inherit;
        private bool? _isChangeable;
        private bool? _isHotspot;
        private bool? _isSelectionEolFilled;
        private bool? _isVisible;
        private bool? _italic;
        private string _name;
        private int? _number;
        private int? _size;
        private bool? _underline;

        #endregion Fields


        #region Methods

        public override string ToString()
        {
            return "Name = \"" + this._name + "\" Number=" + this._number.ToString();
        }

        #endregion Methods


        #region Properties

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


        public bool? Bold
        {
            get
            {
                return this._bold;
            }
            set
            {
                this._bold = value;
            }
        }


        public StyleCase? Case
        {
            get
            {
                return this._case;
            }
            set
            {
                this._case = value;
            }
        }


        public CharacterSet? CharacterSet
        {
            get
            {
                return this._characterSet;
            }
            set
            {
                this._characterSet = value;
            }
        }


        public string FontName
        {
            get
            {
                return this._fontName;
            }
            set
            {
                this._fontName = value;
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


        public bool? IsChangeable
        {
            get
            {
                return this._isChangeable;
            }
            set
            {
                this._isChangeable = value;
            }
        }


        public bool? IsHotspot
        {
            get
            {
                return this._isHotspot;
            }
            set
            {
                this._isHotspot = value;
            }
        }


        public bool? IsSelectionEolFilled
        {
            get
            {
                return this._isSelectionEolFilled;
            }
            set
            {
                this._isSelectionEolFilled = value;
            }
        }


        public bool? IsVisible
        {
            get
            {
                return this._isVisible;
            }
            set
            {
                this._isVisible = value;
            }
        }


        public bool? Italic
        {
            get
            {
                return this._italic;
            }
            set
            {
                this._italic = value;
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


        public int? Size
        {
            get
            {
                return this._size;
            }
            set
            {
                this._size = value;
            }
        }


        public bool? Underline
        {
            get
            {
                return this._underline;
            }
            set
            {
                this._underline = value;
            }
        }

        #endregion Properties
    }
}
