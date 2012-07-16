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
			InitializeComponent();
			listBoxExperience.Font = new Font(FontHelper.MonoFont.FontFamily, 7.5f, FontStyle.Regular);
			numericBasis.DataBindings.Add("Value", trackBarBasis, "Value",
				false, DataSourceUpdateMode.OnPropertyChanged);
			numericInflation.DataBindings.Add("Value", trackBarInflation, "Value",
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
			_actor = actor;
			listBoxExperience.ColumnWidth = _actor.final_level <= 100 ? 96 : 136;
			_expList = new long[_actor.final_level + 1];
			trackBarBasis.Value = _actor.exp_basis;
			trackBarInflation.Value = _actor.exp_inflation;
			_startValues = new[] { _actor.exp_basis, _actor.exp_inflation };
		}

        /// <summary>
        /// Calculates experience levels based on the given basis and inflation rate.
        /// </summary>
        /// <param name="basis">Base value</param>
        /// <param name="inflation">Rate of inflation</param>
		public void CalculateInflation(int basis, int inflation)
		{
			_expList = new long[_actor.final_level + 1];
			double powI = 2.4d + inflation / 100.0d;
			double n;
			for (int i = 2; i <= _actor.final_level; i++)
			{
				n = basis * (Math.Pow(i + 3, powI) / Math.Pow(5, powI));
				_expList[i] = _expList[i - 1] + Convert.ToInt64(n);
			}
			var digits = _expList[_expList.Length - 1].ToString(CultureInfo.InvariantCulture).Length + 5;
			_fStr = @"{0," + digits.ToString(CultureInfo.InvariantCulture) + @"}";
		}

        /// <summary>
        /// Refreshes the table to display current values.
        /// </summary>
		public void RefreshTable()
		{
			if (_actor != null)
			{
				int topIndex = listBoxExperience.TopIndex;
				listBoxExperience.BeginUpdate();
				listBoxExperience.Items.Clear();
				CalculateInflation((int)numericBasis.Value, (int)numericInflation.Value);
				if (radioButtonNext.Checked)
				{
					for (int i = 1; i < _actor.final_level; i++)
						listBoxExperience.Items.Add(_expList[i + 1] - _expList[i]);
				}
				else
				{
					for (int i = 1; i <= _actor.final_level; i++)
						listBoxExperience.Items.Add(_expList[i]);
				}
				listBoxExperience.TopIndex = topIndex;
				listBoxExperience.EndUpdate();
			}
			else
				listBoxExperience.Items.Clear();
		}

        #endregion

        #region Private Methods

        private void NumericBasisValueChanged(object sender, EventArgs e)
		{
			RefreshTable();
			if (_actor != null)
				_actor.exp_basis = (int)numericBasis.Value;
		}

		private void NumericInflationValueChanged(object sender, EventArgs e)
		{
			RefreshTable();
			if (_actor != null)
				_actor.exp_inflation = (int)numericInflation.Value;
		}

		private void ButtonApplyClick(object sender, EventArgs e)
		{
			_actor.exp_basis = (int)numericBasis.Value;
			_actor.exp_inflation = (int)numericInflation.Value;
		}

		private void ListBoxExperienceDrawItem(object sender, DrawItemEventArgs e)
		{
			using (e.Graphics)
			{
				string lvl = String.Format("{0,3}:", "L" + (e.Index + 1));
				string exp = String.Format(_fStr, listBoxExperience.Items[e.Index]);
				e.Graphics.DrawString(lvl, e.Font, Brushes.Black, e.Bounds);
				e.Graphics.DrawString(exp, e.Font, 
					radioButtonNext.Checked ? Brushes.Green : Brushes.Red, e.Bounds);
			}
		}

		private void RadioButtonCheckedChanged(object sender, EventArgs e)
		{
			RefreshTable();
		}

		private void ButtonCancelClick(object sender, EventArgs e)
		{
			trackBarBasis.Value = _startValues[0];
			trackBarInflation.Value = _startValues[1];
        }

        #endregion
    }
}
