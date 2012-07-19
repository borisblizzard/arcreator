#region Using Directives

using System.Collections.Generic;

#endregion


namespace ARCed.Scintilla.Configuration
{
    public class CommandBindingConfigList : List<CommandBindingConfig>
    {
        #region Fields

        private bool? _allowDuplicateBindings;
        private bool? _inherit;

        #endregion Fields


        #region Properties

        public bool? AllowDuplicateBindings
        {
            get
            {
                return this._allowDuplicateBindings;
            }
            set
            {
                this._allowDuplicateBindings = value;
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
