﻿#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla
{
    public enum CaretPolicy
    {
        Slop = 0x01,
        Strict = 0x04,
        Jumps = 0x10,
        Even = 0x08,
    }
}
