#region Using Directives

using System;
using System.Collections.Generic;
using System.Globalization;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using ARCed.Helpers;
using ARCed.UI;
using RPG;

#endregion

namespace ARCed.Database.Actors
{
	/// <summary>
	/// Form to provide functionality of using an interactive chart to modify actor parameter values.
	/// </summary>
	public partial class ActorParametersForm : DockContent
	{
		#region Private Fields

		Actor _actor;
		Chart[] _charts;
		bool _mouseDown, _suppressEvent;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the associated actor of the control.
		/// </summary>
		public Actor Actor
		{
			get { return _actor; }
			set { RefreshActor(value); }
		}

		/// <summary>
		/// Gets or sets the index of the associated parameter.
		/// </summary>
		public int ParameterIndex
		{
			get { return tabControlParameters.SelectedIndex; }
			set { tabControlParameters.SelectedIndex = value; }
		}
				
		/// <summary>
		/// Gets the current chart.
		/// </summary>
		internal Chart CurrentChart { get { return _charts[tabControlParameters.SelectedIndex]; } }

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		/// <param name="actor">Actor to associate with this control.</param>
		/// <param name="index">Index of the parameter to activate on the control.</param>
		public ActorParametersForm(Actor actor, int index)
		{
			InitializeComponent();
			numericValue.Maximum = Project.Settings.GetMaxValue(index);
			_actor = actor;
			numericLevel.Minimum = _actor.initial_level;
			numericLevel.Maximum = _actor.final_level;
			TabText = String.Format("Parameters: {0}", _actor.name);
			GenerateCharts();
			Windows.ChartSettingsForm.SetCharts(ref _charts);
			tabControlParameters.SelectedIndex = index;
		}

		#endregion

		#region Mouse Events

		private void ChartMouseEnter(object sender, EventArgs e)
		{
			Cursor = Cursors.Cross;
		}

		private void ChartMouseLeave(object sender, EventArgs e)
		{
			Cursor = Cursors.Default;
			_mouseDown = false;
		}

		private void ChartMouseUp(object sender, MouseEventArgs e)
		{
			_mouseDown = false;
		}

		private void ChartMouseDown(object sender, MouseEventArgs e)
		{
			_mouseDown = true;
		}

		void ChartMouseMove(object sender, MouseEventArgs e)
		{
			var result = (sender as Chart).HitTest(e.X, e.Y);
			if (result.ChartElementType == ChartElementType.PlottingArea ||
				result.ChartElementType == ChartElementType.DataPoint ||
				result.ChartElementType == ChartElementType.Gridlines)
			{

				Tuple<int, int> point = GetAxisValuesFromMouse(sender as Chart, e.X, e.Y);
				labelCoordX.Text = "X: " + point.Item1.ToString(CultureInfo.InvariantCulture);
				labelCoordY.Text = "Y: " + point.Item2.ToString(CultureInfo.InvariantCulture);
				if (_mouseDown)
				{
					int index = tabControlParameters.SelectedIndex;
					Table parameters = _actor.parameters;

					if (parameters[index, point.Item1] != point.Item2)
					{
						_actor.parameters[index, point.Item1] = point.Item2;
						RefreshChart(index);
					}
				}
			}
			else
			{
				labelCoordX.Text = "X: ";
				labelCoordY.Text = "Y: ";
			}
		}

		private Tuple<int, int> GetAxisValuesFromMouse(Chart chart, int x, int y)
		{
			var chartArea = chart.ChartAreas[0];
			var xValue = chartArea.AxisX.PixelPositionToValue(x);
			var yValue = chartArea.AxisY.PixelPositionToValue(y);
			return new Tuple<int, int>(
				(int)xValue.Clamp(1, Project.Settings.MaxLevel),
				(int)yValue.Clamp(0, Project.Settings.GetMaxValue(tabControlParameters.SelectedIndex)));
		}

		#endregion

		#region Form Private Functions

		private void RefreshActor(Actor actor)
		{
			_suppressEvent = true;
			_actor = actor;
			numericLevel.Minimum = _actor.initial_level;
			numericLevel.Maximum = _actor.final_level;
			TabText = String.Format("Parameters: {0}", _actor.name);
			RefreshChart(tabControlParameters.SelectedIndex);
		}

		private void GenerateCharts()
		{
			List<string> parameterNames = Project.Settings.Parameters;
			Table parameters = _actor.parameters;
			_charts = new Chart[parameterNames.Count];
			for (int i = 0; i < parameterNames.Count; i++)
			{
				var page = new TabPage(parameterNames[i]);
				var chart = new Chart();
				// ChartArea styling
				chart.ChartAreas.Add(new ChartArea(parameterNames[i]));
				chart.ChartAreas[0].Area3DStyle.Enable3D = Editor.Settings.Charting.ThreeD;
				chart.ChartAreas[0].Area3DStyle.Inclination =
					(int)Editor.Settings.Charting.Inclination;
				chart.ChartAreas[0].Area3DStyle.Rotation =
					(int)Editor.Settings.Charting.Rotation;
				chart.ChartAreas[0].Area3DStyle.PointDepth =
					(int)Editor.Settings.Charting.Depth;
				chart.ChartAreas[0].AxisX.Minimum = _actor.initial_level;
				chart.ChartAreas[0].AxisX.Maximum = _actor.final_level;
				chart.ChartAreas[0].AxisY.Minimum = 0;
				chart.ChartAreas[0].AxisY.Maximum = Project.Settings.GetMaxValue(i);
				chart.ChartAreas[0].AxisX.IsMarginVisible = false;
				chart.ChartAreas[0].AxisY.IsMarginVisible = false;
				// Series styling
				chart.Series.Add(new Series());
				chart.Series[0].Color = Editor.Settings.Charting.Colors[i];
				chart.Series[0].IsVisibleInLegend = false;
				chart.Series[0]["LineTension"] =
					Editor.Settings.Charting.SplineTension.ToString(CultureInfo.InvariantCulture);
				// Plot points
				for (int lvl = _actor.initial_level; lvl < _actor.final_level + 1; lvl++)
					chart.Series[0].Points.AddXY(lvl, parameters[i, lvl]);
				// Label styling
				chart.ChartAreas[0].AxisX.LabelStyle.Interval =
					(_actor.final_level - _actor.initial_level) / 10.0d;
				chart.ChartAreas[0].AxisY.LabelStyle.Interval = Project.Settings.GetMaxValue(i) / 10.0d;
				chart.ChartAreas[0].AxisX.LabelStyle.IntervalOffset = -1;
				chart.ChartAreas[0].AxisX.LabelStyle.IsEndLabelVisible = true;
				// Bind events
				chart.MouseMove += this.ChartMouseMove;
				chart.MouseDown += this.ChartMouseDown;
				chart.MouseUp += this.ChartMouseUp;
				chart.MouseEnter += this.ChartMouseEnter;
				chart.MouseLeave += this.ChartMouseLeave;
				// Add page and chart to tab control
				page.Controls.Add(chart);
				chart.Dock = DockStyle.Fill;
				_charts[i] = chart;
				tabControlParameters.TabPages.Add(page);
			}
			ChartSettingsForm.SetChartType(Editor.Settings.Charting.Type, ref _charts);
			ChartSettingsForm.SetChartLighting(Editor.Settings.Charting.Lighting, ref _charts);
		}

		private void ButtonGenerateClick(object sender, EventArgs e)
		{
			int index = tabControlParameters.SelectedIndex;
			using (var dialog = new ParamGenerateCurveDialog(ref _actor, index))
			{
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					int init = dialog.InitialValue;
					int final = dialog.FinalValue;
					int spd = dialog.Speed;
					int iLvl = _actor.initial_level;
					int fLvl = _actor.final_level;
					for (int i = iLvl; i < fLvl + 1; i++)
					{
						_actor.parameters[index, i] =
							Util.GenerateParameter(init, final, spd, i, iLvl, fLvl);
					}
					RefreshChart(index);
				}
			}
		}

		private void RefreshChart(int index)
		{
			Table parameters = _actor.parameters;
			_charts[index].Series[0].Points.Clear();
			for (int i = _actor.initial_level; i < _actor.final_level + 1; i++)
				_charts[index].Series[0].Points.AddXY(i, parameters[index, i]);
		}

		private void ButtonQuickCurveClick(object sender, EventArgs e)
		{
			int index = tabControlParameters.SelectedIndex;
			int max = Project.Settings.GetMaxValue(index);
			int init = Convert.ToInt32(Util.GetRandomNumber(0.045, 0.10) * max);
			int final = Convert.ToInt32(Util.GetRandomNumber(0.75, 0.95) * max);
			int spd = Convert.ToInt32((sender as Control).Tag);
			int iLvl = _actor.initial_level;
			int fLvl = _actor.final_level;
			for (int i = iLvl; i < fLvl + 1; i++)
			{
				_actor.parameters[index, i] =
					Util.GenerateParameter(init, final, spd, i, iLvl, fLvl);
			}
			RefreshChart(index);
		}

		private void TabControlParametersSelectedIndexChanged(object sender, EventArgs e)
		{
			numericValue.Maximum = Project.Settings.GetMaxValue(tabControlParameters.SelectedIndex);
			this.NumericLevelValueChanged(null, null);
		}

		private void NumericLevelValueChanged(object sender, EventArgs e)
		{
			int index = tabControlParameters.SelectedIndex;
			_suppressEvent = true;
			numericValue.Value = _actor.parameters[index, (int)numericLevel.Value];
			_suppressEvent = false;
		}

		private void NumericValueValueChanged(object sender, EventArgs e)
		{
			if (!_suppressEvent)
			{
				int index = tabControlParameters.SelectedIndex;
				var level = (int)numericLevel.Value;
				_actor.parameters[index, level] = (int)numericValue.Value;
			}
		}

		private void ButtonSettingsClick(object sender, EventArgs e)
		{
			Windows.ChartSettingsForm.Show(Editor.MainDock);
			Windows.ChartSettingsForm.SetCharts(ref _charts);
		}

        private void ActorParametersFormLoad(object sender, EventArgs e)
        {
            Windows.ChartForms.Add(this);
        }

		private void ActorParametersFormFormClosing(object sender, FormClosingEventArgs e)
		{
		    Windows.ChartForms.Remove(this);
			Windows.ChartSettingsForm.ClearCharts();
		}

		#endregion
	}
}
