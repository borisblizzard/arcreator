#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using ARCed.Database.Actors;
using RPG;
using Color = System.Drawing.Color;

#endregion

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
			get { return this.chartParameter; }
		}

		/// <summary>
		/// Gets or sets the color of the chart on the control
		/// </summary>
		[Category("ARCed"), Description("Defines the color of the chart."), DefaultValue(typeof(Color), "Tomato")]
		public Color ChartColor
		{
			get { return this.chartParameter.Series[0].Color; }
			set { this.chartParameter.Series[0].Color = value; this.RefreshChart(); }
		}

		/// <summary>
		/// Gets or sets the index of the associated parameter
		/// </summary>
		[DefaultValue(0)]
		[Browsable(false)]
		public int ParameterIndex
		{
			get { return this._paramIndex; }
			set { this.SetParameterIndex(value); }
		}

		/// <summary>
		/// Gets or sets the label of the control
		/// </summary>
		[Category("ARCed"), Description("Defines the label for the control."), DefaultValue("MaxHP")]
		public string ParameterLabel
		{
			get { return Text; }
			set { Text = value; }
		}

		#endregion

		#region Private Fields

		private Actor _actor;
	    private int _paramIndex;

		#endregion

		#region Constructors

		/// <summary>
		/// Default constructor
		/// </summary>
		public ParameterMiniChart()
		{
			this.InitializeComponent();
			Controls.Add(this.chartParameter);
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
			if (this._actor != null)
			{
				this.chartParameter.BeginInit();
				this.chartParameter.Series[0].Points.Clear();
				this.chartParameter.ChartAreas[0].AxisY.Minimum = 0;
				this.chartParameter.ChartAreas[0].AxisY.Maximum = Project.Settings.GetMaxValue(this._paramIndex);
				for (int lvl = 1; lvl < this._actor.final_level; lvl++)
					this.chartParameter.Series[0].Points.AddXY(lvl, this._actor.parameters[this._paramIndex, lvl]);
				this.chartParameter.EndInit();
			}
		}

		/// <summary>
		/// Changes the actor the chart is displaying information of.
		/// </summary>
		/// <param name="actor"></param>
		public void ChangeActor(Actor actor)
		{
			this._actor = actor;
			this.RefreshChart();
		}

		#endregion

		#region Private Methods

		private void ParameterMiniChartDoubleClick(object sender, EventArgs e)
		{
		    var window = Windows.ChartForms.Find(f => f.Actor == this._actor) ??
		        new ActorParametersForm(this._actor, this._paramIndex);
		    window.ParameterIndex = this._paramIndex;
		    window.Show(Editor.MainDock);
		}

	    private void SetParameterIndex(int index)
		{
			this._paramIndex = index % Project.Settings.Parameters.Count;
			Text = Project.Settings.Parameters[this._paramIndex];
			this.chartParameter.Series[0].Color = Editor.Settings.Charting.Colors[this._paramIndex];
			this.RefreshChart();
		}

		#endregion
	}
}
