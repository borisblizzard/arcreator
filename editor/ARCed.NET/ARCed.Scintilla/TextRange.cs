﻿#region Using Directives

using System;
using System.Runtime.InteropServices;

#endregion


namespace ARCed.Scintilla
{
	// TODO Make internal
	[StructLayout(LayoutKind.Sequential)]
	public struct TextRange
	{
		public CharacterRange chrg;
		public IntPtr lpstrText;
	}
}
