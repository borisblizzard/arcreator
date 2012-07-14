#region Using Directives

using System;

#endregion Using Directives


namespace ARCed.Scintilla.Configuration
{
    public enum ConfigurationLoadOrder
    {
        BuiltInCustomUser,
        BuiltInUserCustom,
        CustomBuiltInUser,
        CustomUserBuiltIn,
        UserBuiltInCustom,
        UserCustomBuiltIn
    }
}
