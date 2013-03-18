#region Using Directives

using System.Drawing;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed.UI
{
	internal static class Win32Helper
	{
		public static Control ControlAtPoint(Point pt)
		{
			return Control.FromChildHandle(NativeMethods.WindowFromPoint(pt));
		}

		public static uint MakeLong(int low, int high)
		{
			return (uint)((high << 16) + low);
		}
	}
}
