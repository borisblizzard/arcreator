using System.ComponentModel;
using System.Windows.Forms;
using System.Drawing;

namespace ARCed.Controls
{
	/// <summary>
	/// ListBox control with double-buffering
	/// </summary>
	[ToolboxBitmap(typeof(ListBox))]
	[Description("ListBox control with double-buffering.")]
	public partial class DoubleBufferedListBox : ListBox
	{
		public DoubleBufferedListBox() : base()
		{
			this.DoubleBuffered = true;
		}
	}
}
