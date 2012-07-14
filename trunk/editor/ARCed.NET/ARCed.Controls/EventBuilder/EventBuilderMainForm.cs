using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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
