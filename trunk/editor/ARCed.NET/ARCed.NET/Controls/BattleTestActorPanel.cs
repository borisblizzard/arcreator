using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
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
			DatabaseHelper.Populate(comboBoxActor, Project.Data.Actors, false);
			comboBoxActor.SelectedIndex = 0;
		}
	}
}
