using System;
using System.Windows.Forms;
using RPG;

namespace ARCed.Database.Actors
{
	public partial class ParamGenerateCurveDialog : Form
	{
		public int InitialValue { get { return (int)numericInitial.Value; } }
		public int FinalValue { get { return (int)numericFinal.Value; } }
		public int Speed { get { return trackBarSpeed.Value; } }

		public ParamGenerateCurveDialog(ref Actor actor, int paramIndex)
		{
			InitializeComponent();
			int max = Project.Settings.GetMaxValue(paramIndex);
			numericInitial.Maximum = max;
			numericFinal.Maximum = max;
			numericFinal.Value = actor.parameters[paramIndex, actor.final_level];
			numericInitial.Value = actor.parameters[paramIndex, actor.initial_level];
		}

		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}

		private void numeric_ValueChanged(object sender, EventArgs e)
		{
			if (numericInitial.Value > numericFinal.Value)
				numericInitial.Value = numericFinal.Value;
		}
	}
}
