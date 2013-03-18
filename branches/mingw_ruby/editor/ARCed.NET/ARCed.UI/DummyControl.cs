#region Using Directives

using System.Windows.Forms;

#endregion

namespace ARCed.UI
{
	internal class DummyControl : Control
	{
		public DummyControl()
		{
			SetStyle(ControlStyles.Selectable, false);
		}
	}
}
