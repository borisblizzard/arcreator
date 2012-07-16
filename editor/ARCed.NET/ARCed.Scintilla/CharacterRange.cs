#region Using Directives

using System.Runtime.InteropServices;

#endregion


namespace ARCed.Scintilla
{
    // TODO Make internal
    [StructLayout(LayoutKind.Sequential)]
    public struct CharacterRange
    {
        public int cpMin;
        public int cpMax;
    }
}
