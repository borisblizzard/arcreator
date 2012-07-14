using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;

using System.Linq;
using System.Text;
using System.Windows.Forms;
using ARCed.Helpers;

namespace ARCed.Controls
{
	public partial class BattleTestActorPanel : UserControl
	{
		public BattleTestActorPanel()
		{
			InitializeComponent();
			
			comboBoxActor.SelectedIndex = 0;
		}
	}
}
