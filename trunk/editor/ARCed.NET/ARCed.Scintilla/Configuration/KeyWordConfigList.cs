#region Using Directives

using System.Collections.ObjectModel;

#endregion


namespace ARCed.Scintilla.Configuration
{
    public class KeyWordConfigList : KeyedCollection<int, KeyWordConfig>
    {
        #region Methods

        protected override int GetKeyForItem(KeyWordConfig item)
        {
            return item.List;
        }

        #endregion Methods
    }
}
