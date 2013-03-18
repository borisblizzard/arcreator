#region Using Directives

using System.Collections.Generic;
using System.Drawing;

#endregion


namespace ARCed.Scintilla.Configuration
{
    public class SnippetsConfigList : List<SnippetsConfig>
    {
        #region Fields

        private Color _activeSnippetColor;
        private int? _activeSnippetIndicator;
        private IndicatorStyle? _activeSnippetIndicatorStyle;
        private char? _defaultDelimeter;
        private Color _inactiveSnippetColor;
        private int? _inactiveSnippetIndicator;
        private IndicatorStyle? _inactiveSnippetIndicatorStyle;
        private bool? _inherit;
        private bool? _isEnabled;
        private bool? _isOneKeySelectionEmbedEnabled;

        #endregion Fields


        #region Properties

        public Color ActiveSnippetColor
        {
            get
            {
                return this._activeSnippetColor;
            }
            set
            {
                this._activeSnippetColor = value;
            }
        }


        public int? ActiveSnippetIndicator
        {
            get
            {
                return this._activeSnippetIndicator;
            }
            set
            {
                this._activeSnippetIndicator = value;
            }
        }


        public IndicatorStyle? ActiveSnippetIndicatorStyle
        {
            get
            {
                return this._activeSnippetIndicatorStyle;
            }
            set
            {
                this._activeSnippetIndicatorStyle = value;
            }
        }


        public char? DefaultDelimeter
        {
            get
            {
                return this._defaultDelimeter;
            }
            set
            {
                this._defaultDelimeter = value;
            }
        }


        public Color InactiveSnippetColor
        {
            get
            {
                return this._inactiveSnippetColor;
            }
            set
            {
                this._inactiveSnippetColor = value;
            }
        }


        public int? InactiveSnippetIndicator
        {
            get
            {
                return this._inactiveSnippetIndicator;
            }
            set
            {
                this._inactiveSnippetIndicator = value;
            }
        }


        public IndicatorStyle? InactiveSnippetIndicatorStyle
        {
            get
            {
                return this._inactiveSnippetIndicatorStyle;
            }
            set
            {
                this._inactiveSnippetIndicatorStyle = value;
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


        public bool? IsEnabled
        {
            get
            {
                return this._isEnabled;
            }
            set
            {
                this._isEnabled = value;
            }
        }


        public bool? IsOneKeySelectionEmbedEnabled
        {
            get
            {
                return this._isOneKeySelectionEmbedEnabled;
            }
            set
            {
                this._isOneKeySelectionEmbedEnabled = value;
            }
        }

        #endregion Properties
    }
}
