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
			get { return this._actor; }
			set { this.RefreshActor(value); }
		}

		/// <summary>
		/// Gets or sets the index of the associated parameter.
		/// </summary>
		public int ParameterIndex
		{
			get { return this.tabControlParameters.SelectedIndex; }
			set { this.tabControlParameters.SelectedIndex = value; }
		}
				
		/// <summary>
		/// Gets the current chart.
		/// </summary>
		internal Chart CurrentChart { get { return this._charts[this.tabControlParameters.SelectedIndex]; } }

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		/// <param name="actor">Actor to associate with this control.</param>
		/// <param name="index">Index of the parameter to activate on the control.</param>
		public ActorParametersForm(Actor actor, int index)
		{
			this.InitializeComponent();
			this.numericValue.Maximum = Project.Settings.GetMaxValue(index);
			this._actor = actor;
			this.numericLevel.Minimum = this._actor.initial_level;
			this.numericLevel.Maximum = this._actor.final_level;
			TabText = String.Format("Parameters: {0}", this._actor.name);
			this.GenerateCharts();
			Windows.ChartSettingsForm.SetCharts(ref this._charts);
			this.tabControlParameters.SelectedIndex = index;
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
			this._mouseDown = false;
		}

		private void ChartMouseUp(object sender, MouseEventArgs e)
		{
			this._mouseDown = false;
		}

		private void ChartMouseDown(object sender, MouseEventArgs e)
		{
			this._mouseDown = true;
		}

		void ChartMouseMove(object sender, MouseEventArgs e)
		{
			var result = (sender as Chart).HitTest(e.X, e.Y);
			if (result.ChartElementType == ChartElementType.PlottingArea ||
				result.ChartElementType == ChartElementType.DataPoint ||
				result.ChartElementType == ChartElementType.Gridlines)
			{

				Tuple<int, int> point = this.GetAxisValuesFromMouse(sender as Chart, e.X, e.Y);
				this.labelCoordX.Text = "X: " + point.Item1.ToString(CultureInfo.InvariantCulture);
				this.labelCoordY.Text = "Y: " + point.Item2.ToString(CultureInfo.InvariantCulture);
				if (this._mouseDown)
				{
					int index = this.tabControlParameters.SelectedIndex;
					Table parameters = this._actor.parameters;

					if (parameters[index, point.Item1] != point.Item2)
					{
						this._actor.parameters[index, point.Item1] = point.Item2;
						this.RefreshChart(index);
					}
				}
			}
			else
			{
				this.labelCoordX.Text = "X: ";
				this.labelCoordY.Text = "Y: ";
			}
		}

		private Tuple<int, int> GetAxisValuesFromMouse(Chart chart, int x, int y)
		{
			var chartArea = chart.ChartAreas[0];
			var xValue = chartArea.AxisX.PixelPositionToValue(x);
			var yValue = chartArea.AxisY.PixelPositionToValue(y);
			return new Tuple<int, int>(
				(int)xValue.Clamp(1, Project.Settings.MaxLevel),
				(int)yValue.Clamp(0, Project.Settings.GetMaxValue(this.tabControlParameters.SelectedIndex)));
		}

		#endregion

		#region Form Private Functions

		private void RefreshActor(Actor actor)
		{
			this._suppressEvent = true;
			this._actor = actor;
			this.numericLevel.Minimum = this._actor.initial_level;
			this.numericLevel.Maximum = this._actor.final_level;
			TabText = String.Format("Parameters: {0}", this._actor.name);
			this.RefreshChart(this.tabControlParameters.SelectedIndex);
		}

		private void GenerateCharts()
		{
			List<string> parameterNames = Project.Settings.Parameters;
			Table parameters = this._actor.parameters;
			this._charts = new Chart[parameterNames.Count];
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
				chart.ChartAreas[0].AxisX.Minimum = this._actor.initial_level;
				chart.ChartAreas[0].AxisX.Maximum = this._actor.final_level;
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
				for (int lvl = this._actor.initial_level; lvl < this._actor.final_level + 1; lvl++)
					chart.Series[0].Points.AddXY(lvl, parameters[i, lvl]);
				// Label styling
				chart.ChartAreas[0].AxisX.LabelStyle.Interval =
					(this._actor.final_level - this._actor.initial_level) / 10.0d;
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
				this._charts[i] = chart;
				this.tabControlParameters.TabPages.Add(page);
			}
			ChartSettingsForm.SetChartType(Editor.Settings.Charting.Type, ref this._charts);
			ChartSettingsForm.SetChartLighting(Editor.Settings.Charting.Lighting, ref this._charts);
		}

		private void ButtonGenerateClick(object sender, EventArgs e)
		{
			int index = this.tabControlParameters.SelectedIndex;
			using (var dialog = new ParamGenerateCurveDialog(ref this._actor, index))
			{
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					int init = dialog.InitialValue;
					int final = dialog.FinalValue;
					int spd = dialog.Speed;
					int iLvl = this._actor.initial_level;
					int fLvl = this._actor.final_level;
					for (int i = iLvl; i < fLvl + 1; i++)
					{
						this._actor.parameters[index, i] =
							Util.GenerateParameter(init, final, spd, i, iLvl, fLvl);
					}
					this.RefreshChart(index);
				}
			}
		}

		private void RefreshChart(int index)
		{
			Table parameters = this._actor.parameters;
			this._charts[index].Series[0].Points.Clear();
			for (int i = this._actor.initial_level; i < this._actor.final_level + 1; i++)
				this._charts[index].Series[0].Points.AddXY(i, parameters[index, i]);
		}

		private void ButtonQuickCurveClick(object sender, EventArgs e)
		{
			int index = this.tabControlParameters.SelectedIndex;
			int max = Project.Settings.GetMaxValue(index);
			int init = Convert.ToInt32(Util.GetRandomNumber(0.045, 0.10) * max);
			int final = Convert.ToInt32(Util.GetRandomNumber(0.75, 0.95) * max);
			int spd = Convert.ToInt32((sender as Control).Tag);
			int iLvl = this._actor.initial_level;
			int fLvl = this._actor.final_level;
			for (int i = iLvl; i < fLvl + 1; i++)
			{
				this._actor.parameters[index, i] =
					Util.GenerateParameter(init, final, spd, i, iLvl, fLvl);
			}
			this.RefreshChart(index);
		}

		private void TabControlParametersSelectedIndexChanged(object sender, EventArgs e)
		{
			this.numericValue.Maximum = Project.Settings.GetMaxValue(this.tabControlParameters.SelectedIndex);
			this.NumericLevelValueChanged(null, null);
		}

		private void NumericLevelValueChanged(object sender, EventArgs e)
		{
			int index = this.tabControlParameters.SelectedIndex;
			this._suppressEvent = true;
			this.numericValue.Value = this._actor.parameters[index, (int)this.numericLevel.Value];
			this._suppressEvent = false;
		}

		private void NumericValueValueChanged(object sender, EventArgs e)
		{
			if (!this._suppressEvent)
			{
				int index = this.tabControlParameters.SelectedIndex;
				var level = (int)this.numericLevel.Value;
				this._actor.parameters[index, level] = (int)this.numericValue.Value;
			}
		}

		private void ButtonSettingsClick(object sender, EventArgs e)
		{
			Windows.ChartSettingsForm.Show(Editor.MainDock);
			Windows.ChartSettingsForm.SetCharts(ref this._charts);
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
