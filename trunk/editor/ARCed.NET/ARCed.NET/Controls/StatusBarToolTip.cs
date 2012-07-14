using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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
			Console.WriteLine("POOP");
			Editor.StatusBar.Items[2].Text = GetToolTip(e.AssociatedControl);
			e.Cancel = true;
		}
	}
}
