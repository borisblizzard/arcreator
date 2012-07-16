#region Using Directives

using System.Windows.Forms;

#endregion

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
