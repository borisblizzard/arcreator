using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using RPG;
using ARCed.Helpers;
using System.Windows.Forms;

namespace ARCed.Database.Actors
{
	public partial class ExperienceCurveForm : ARCed.UI.DockContent
	{

		Actor _actor;
		string _fStr;
		long[] _expList;
		int[] _startValues;

		public ExperienceCurveForm()
		{
			InitializeComponent();
			listBoxExperience.Font = new Font(FontHelper.MonoFont.FontFamily, 7.5f, FontStyle.Regular);
			numericBasis.DataBindings.Add("Value", trackBarBasis, "Value",
				false, DataSourceUpdateMode.OnPropertyChanged | DataSourceUpdateMode.OnValidation);
			numericInflation.DataBindings.Add("Value", trackBarInflation, "Value",
				false, DataSourceUpdateMode.OnPropertyChanged | DataSourceUpdateMode.OnValidation);
		}

		public void ChangeActor(Actor actor)
		{
			_actor = actor;
			listBoxExperience.ColumnWidth = _actor.final_level <= 100 ? 96 : 136;
			_expList = new long[_actor.final_level + 1];
			trackBarBasis.Value = _actor.exp_basis;
			trackBarInflation.Value = _actor.exp_inflation;
			_startValues = new[] { _actor.exp_basis, _actor.exp_inflation };
		}

		public void CalculateInflation(int basis, int inflation)
		{
			_expList = new long[_actor.final_level + 1];
			double pow_i = 2.4d + inflation / 100.0d;
			double n;
			for (int i = 2; i <= _actor.final_level; i++)
			{
				n = basis * (Math.Pow(i + 3, pow_i) / Math.Pow(5, pow_i));
				_expList[i] = _expList[i - 1] + Convert.ToInt64(n);
			}
			int digits = _expList[_expList.Length - 1].ToString().Length + 5;
			_fStr = @"{0," + digits.ToString() + @"}";
		}

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

		private void numericBasis_ValueChanged(object sender, EventArgs e)
		{
			RefreshTable();
			if (_actor != null)
				_actor.exp_basis = (int)numericBasis.Value;
		}

		private void numericInflation_ValueChanged(object sender, EventArgs e)
		{
			RefreshTable();
			if (_actor != null)
				_actor.exp_inflation = (int)numericInflation.Value;
		}

		private void buttonApply_Click(object sender, EventArgs e)
		{
			_actor.exp_basis = (int)numericBasis.Value;
			_actor.exp_inflation = (int)numericInflation.Value;
		}

		private void listBoxExperience_DrawItem(object sender, DrawItemEventArgs e)
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

		private void radioButton_CheckedChanged(object sender, EventArgs e)
		{
			RefreshTable();
		}

		private void buttonCancel_Click(object sender, EventArgs e)
		{
			trackBarBasis.Value = _startValues[0];
			trackBarInflation.Value = _startValues[1];
		}
	}
}
