﻿#region Using Directives

using System;
using System.Windows.Forms;
using RPG;

#endregion

namespace ARCed.Database.Actors
{
	/// <summary>
	/// Dialog for getting user-defined values used to 
	/// generate curves for <see cref="RPG.Actor"/> parameters.
	/// </summary>
	public partial class ParamGenerateCurveDialog : Form
	{
		#region Public Properties

		/// <summary>
		/// Gets the initial value to start the curve on.
		/// </summary>
		public int InitialValue { get { return (int)this.numericInitial.Value; } }
		/// <summary>
		/// Gets the final value to end the curve on.
		/// </summary>
		public int FinalValue { get { return (int)this.numericFinal.Value; } }
		/// <summary>
		/// Gets the speed at which the curve increases.
		/// </summary>
		public int Speed { get { return this.trackBarSpeed.Value; } }

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor.
		/// </summary>
		/// <param name="actor">Reference to an <see cref="RPG.Actor"/> object.</param>
		/// <param name="paramIndex">Index of the parameter to change</param>
		public ParamGenerateCurveDialog(ref Actor actor, int paramIndex)
		{
			this.InitializeComponent();
			var max = Project.Settings.GetMaxValue(paramIndex);
			this.numericInitial.Maximum = max;
			this.numericFinal.Maximum = max;
			this.numericFinal.Value = actor.parameters[paramIndex, actor.final_level];
			this.numericInitial.Value = actor.parameters[paramIndex, actor.initial_level];
		}

		#endregion

		#region Private Methods

		private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}

		private void NumericValueChanged(object sender, EventArgs e)
		{
			if (this.numericInitial.Value > this.numericFinal.Value)
				this.numericInitial.Value = this.numericFinal.Value;
		}

		#endregion
	}
}
