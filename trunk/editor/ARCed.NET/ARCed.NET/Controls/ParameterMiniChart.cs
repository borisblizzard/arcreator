using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using ARCed.Database.Actors;

namespace ARCed.Controls
{
	/// <summary>
	/// Control for displaying actor parameters in a chart.
	/// </summary>
	[Description("Control for displaying actor parameters in a chart.")]
	[ToolboxBitmap(typeof(Chart))]
	public partial class ParameterMiniChart : GroupBox
	{
		#region Public Properties

		/// <summary>
		/// Gets the chart of the control
		/// </summary>
		[Browsable(false)]
		public Chart Chart 
		{
			get { return chartParameter; }
		}

		/// <summary>
		/// Gets or sets the color of the chart on the control
		/// </summary>
		[Category("ARCed"), Description("Defines the color of the chart."), DefaultValue(typeof(Color), "Tomato")]
		public Color ChartColor
		{
			get { return chartParameter.Series[0].Color; }
			set { chartParameter.Series[0].Color = value; RefreshChart(); }
		}

		/// <summary>
		/// Gets or sets the index of the associated parameter
		/// </summary>
		[DefaultValue(0)]
		[Browsable(false)]
		public int ParameterIndex
		{
			get { return _paramIndex; }
			set { SetParameterIndex(value); }
		}

		/// <summary>
		/// Gets or sets the label of the control
		/// </summary>
		[Category("ARCed"), Description("Defines the label for the control."), DefaultValue("MaxHP")]
		public string ParameterLabel
		{
			get { return this.Text; }
			set { this.Text = value; }
		}

		#endregion

		#region Private Fields

		private RPG.Actor _actor;
		private int _paramIndex = 0;

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public ParameterMiniChart()
		{
			InitializeComponent();
			this.Controls.Add(chartParameter);
			this.chartParameter.Series[0]["ShowMarkerLines"] = false.ToString();
			this.chartParameter.Series[0]["LineTension"] = "0.0";
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Forces the chart to refresh current parameters
		/// </summary>
		public void RefreshChart()
		{
			if (_actor != null)
			{
				this.chartParameter.BeginInit();
				this.chartParameter.Series[0].Points.Clear();
				this.chartParameter.ChartAreas[0].AxisY.Minimum = 0;
				this.chartParameter.ChartAreas[0].AxisY.Maximum = Project.Settings.GetMaxValue(_paramIndex);
				for (int lvl = 1; lvl < _actor.final_level; lvl++)
					chartParameter.Series[0].Points.AddXY(lvl, _actor.parameters[_paramIndex, lvl]);
				this.chartParameter.EndInit();
			}
		}

		/// <summary>
		/// Changes the actor the chart is displaying information of.
		/// </summary>
		/// <param name="actor"></param>
		public void ChangeActor(RPG.Actor actor)
		{
			_actor = actor;
			RefreshChart();
		}

		#endregion

		#region Private Methods

		private void ParameterMiniChart_DoubleClick(object sender, EventArgs e)
		{
			foreach (Form form in Windows.DatabaseForms)
			{
				if (form is ActorParametersForm && ((ActorParametersForm)form).Actor == _actor)
				{
					(form as ActorParametersForm).ParameterIndex = _paramIndex;
					form.Activate();
					return;
				}
			}
			ActorParametersForm window = new ActorParametersForm(_actor, _paramIndex);
			window.Show(Editor.MainDock);
		}

		private void SetParameterIndex(int index)
		{
			_paramIndex = index % Project.Settings.Parameters.Count;
			this.Text = Project.Settings.Parameters[_paramIndex];
			chartParameter.Series[0].Color = Editor.Settings.Charting.Colors[_paramIndex];
			RefreshChart();
		}

		#endregion
	}
}
