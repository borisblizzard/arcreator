#region Using Directives

using System.ComponentModel;
using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	public partial class StatusBarToolTip : ToolTip
	{
		public StatusBarToolTip()
		{
			InitializeComponent();
		}

		public StatusBarToolTip(IContainer container)
		{
			container.Add(this);
			InitializeComponent();
		}
		
		private void StatusBarToolTip_Popup(object sender, PopupEventArgs e)
		{
			Editor.StatusBar.Items[2].Text = GetToolTip(e.AssociatedControl);
			e.Cancel = true;
		}
	}
}
