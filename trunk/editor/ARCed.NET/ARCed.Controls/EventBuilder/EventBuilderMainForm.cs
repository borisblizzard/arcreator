#region Using Directives

using System;
using System.Windows.Forms;

#endregion

namespace ARCed.EventBuilder
{
	public partial class EventBuilderMainForm : Form
	{
		public EventBuilderMainForm()
		{
			InitializeComponent();
		}

		private void buttonCommand_Clicked(object sender, EventArgs e)
		{
			int code = Convert.ToInt32((sender as Button).Tag);
			var commands = EventCommandEditor.CreateCommand(code, 0);
		}
	}
}
