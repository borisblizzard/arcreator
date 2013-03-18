#region Using Directives

using System.Collections.Generic;

#endregion


namespace ARCed.Scintilla.Configuration
{
    public class StyleConfigList : List<StyleConfig>
    {
        #region Fields

        private int? _bits;
        private bool? _inherit;

        #endregion Fields


        #region Properties

        public int? Bits
        {
            get
            {
                return this._bits;
            }
            set
            {
                this._bits = value;
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

        #endregion Properties
    }
}
