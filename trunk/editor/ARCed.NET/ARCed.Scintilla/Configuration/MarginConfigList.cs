#region Using Directives

using System.Collections.Generic;
using System.Drawing;

#endregion


namespace ARCed.Scintilla.Configuration
{
    public class MarginConfigList : List<MarginConfig>
    {
        #region Fields

        private Color _foldMarginColor;
        private Color _foldMarginHighlightColor;
        private bool? _inherit;
        private int? _left;
        private int? _right;

        #endregion Fields


        #region Properties

        public Color FoldMarginColor
        {
            get
            {
                return this._foldMarginColor;
            }
            set
            {
                this._foldMarginColor = value;
            }
        }


        public Color FoldMarginHighlightColor
        {
            get
            {
                return this._foldMarginHighlightColor;
            }
            set
            {
                this._foldMarginHighlightColor = value;
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


        public int? Left
        {
            get
            {
                return this._left;
            }
            set
            {
                this._left = value;
            }
        }


        public int? Right
        {
            get
            {
                return this._right;
            }
            set
            {
                this._right = value;
            }
        }

        #endregion Properties
    }
}
