#region Using Directives

using System.Collections.ObjectModel;

#endregion


namespace ARCed.Scintilla.Configuration
{
    public class IndicatorConfigList : KeyedCollection<int, IndicatorConfig>
    {
        #region Fields

        private bool? _inherit;

        #endregion Fields


        #region Methods

        protected override int GetKeyForItem(IndicatorConfig item)
        {
            return item.Number;
        }

        #endregion Methods


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

        #endregion Properties
    }
}
