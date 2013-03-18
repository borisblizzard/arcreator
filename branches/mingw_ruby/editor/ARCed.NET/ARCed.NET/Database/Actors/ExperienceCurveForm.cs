#region Using Directives

using System;
using System.Drawing;
using System.Globalization;
using System.Windows.Forms;
using ARCed.Helpers;
using ARCed.UI;
using RPG;

#endregion

namespace ARCed.Database.Actors
{
    /// <summary>
    /// Form for displaying and configuring experience tables for an <see cref="RPG.Actor"/>.
    /// </summary>
	public partial class ExperienceCurveForm : DockContent
    {
        #region Private Fields

        private Actor _actor;
        private string _fStr;
        private long[] _expList;
        private int[] _startValues;

        #endregion

        #region Constructor

        /// <summary>
        /// Default constructor
        /// </summary>
		public ExperienceCurveForm()
		{
			this.InitializeComponent();
			this.listBoxExperience.Font = new Font(FontHelper.MonoFont.FontFamily, 7.5f, FontStyle.Regular);
			this.numericBasis.DataBindings.Add("Value", this.trackBarBasis, "Value",
				false, DataSourceUpdateMode.OnPropertyChanged);
			this.numericInflation.DataBindings.Add("Value", this.trackBarInflation, "Value",
				false, DataSourceUpdateMode.OnPropertyChanged);
		}

        #endregion

        #region Public Methods

        /// <summary>
        /// Changes the form's associated <see cref="RPG.Actor"/> to represent.
        /// </summary>
        /// <param name="actor">RPG.Actor instance</param>
        public void ChangeActor(Actor actor)
		{
			this._actor = actor;
			this.listBoxExperience.ColumnWidth = this._actor.final_level <= 100 ? 96 : 136;
			this._expList = new long[this._actor.final_level + 1];
			this.trackBarBasis.Value = this._actor.exp_basis;
			this.trackBarInflation.Value = this._actor.exp_inflation;
			this._startValues = new[] { this._actor.exp_basis, this._actor.exp_inflation };
		}

        /// <summary>
        /// Calculates experience levels based on the given basis and inflation rate.
        /// </summary>
        /// <param name="basis">Base value</param>
        /// <param name="inflation">Rate of inflation</param>
		public void CalculateInflation(int basis, int inflation)
		{
			this._expList = new long[this._actor.final_level + 1];
			double powI = 2.4d + inflation / 100.0d;
			double n;
			for (int i = 2; i <= this._actor.final_level; i++)
			{
				n = basis * (Math.Pow(i + 3, powI) / Math.Pow(5, powI));
				this._expList[i] = this._expList[i - 1] + Convert.ToInt64(n);
			}
			var digits = this._expList[this._expList.Length - 1].ToString(CultureInfo.InvariantCulture).Length + 5;
			this._fStr = @"{0," + digits.ToString(CultureInfo.InvariantCulture) + @"}";
		}

        /// <summary>
        /// Refreshes the table to display current values.
        /// </summary>
		public void RefreshTable()
		{
			if (this._actor != null)
			{
				int topIndex = this.listBoxExperience.TopIndex;
				this.listBoxExperience.BeginUpdate();
				this.listBoxExperience.Items.Clear();
				this.CalculateInflation((int)this.numericBasis.Value, (int)this.numericInflation.Value);
				if (this.radioButtonNext.Checked)
				{
					for (int i = 1; i < this._actor.final_level; i++)
						this.listBoxExperience.Items.Add(this._expList[i + 1] - this._expList[i]);
				}
				else
				{
					for (int i = 1; i <= this._actor.final_level; i++)
						this.listBoxExperience.Items.Add(this._expList[i]);
				}
				this.listBoxExperience.TopIndex = topIndex;
				this.listBoxExperience.EndUpdate();
			}
			else
				this.listBoxExperience.Items.Clear();
		}

        #endregion

        #region Private Methods

        private void NumericBasisValueChanged(object sender, EventArgs e)
		{
			this.RefreshTable();
			if (this._actor != null)
				this._actor.exp_basis = (int)this.numericBasis.Value;
		}

		private void NumericInflationValueChanged(object sender, EventArgs e)
		{
			this.RefreshTable();
			if (this._actor != null)
				this._actor.exp_inflation = (int)this.numericInflation.Value;
		}

		private void ButtonApplyClick(object sender, EventArgs e)
		{
			this._actor.exp_basis = (int)this.numericBasis.Value;
			this._actor.exp_inflation = (int)this.numericInflation.Value;
		}

		private void ListBoxExperienceDrawItem(object sender, DrawItemEventArgs e)
		{
			using (e.Graphics)
			{
				string lvl = String.Format("{0,3}:", "L" + (e.Index + 1));
				string exp = String.Format(this._fStr, this.listBoxExperience.Items[e.Index]);
				e.Graphics.DrawString(lvl, e.Font, Brushes.Black, e.Bounds);
				e.Graphics.DrawString(exp, e.Font, 
					this.radioButtonNext.Checked ? Brushes.Green : Brushes.Red, e.Bounds);
			}
		}

		private void RadioButtonCheckedChanged(object sender, EventArgs e)
		{
			this.RefreshTable();
		}

		private void ButtonCancelClick(object sender, EventArgs e)
		{
			this.trackBarBasis.Value = this._startValues[0];
			this.trackBarInflation.Value = this._startValues[1];
        }

        #endregion
    }
}
