#region Using Directives

using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	public partial class BattleTestActorPanel : UserControl
	{
		public BattleTestActorPanel()
		{
			this.InitializeComponent();
			
			this.comboBoxActor.SelectedIndex = 0;
		}
	}
}
