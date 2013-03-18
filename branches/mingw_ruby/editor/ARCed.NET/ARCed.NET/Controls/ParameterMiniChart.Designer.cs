namespace ARCed.Controls
{
	partial class ParameterMiniChart
	{
		/// <summary> 
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary> 
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Component Designer generated code

		/// <summary> 
		/// Required method for Designer support - do not modify 
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.components = new System.ComponentModel.Container();
			System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
			System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
			System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
			this.chartParameter = new System.Windows.Forms.DataVisualization.Charting.Chart();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			((System.ComponentModel.ISupportInitialize)(this.chartParameter)).BeginInit();
			this.SuspendLayout();
			// 
			// chartParameter
			// 
			chartArea1.AlignmentOrientation = ((System.Windows.Forms.DataVisualization.Charting.AreaAlignmentOrientations)((System.Windows.Forms.DataVisualization.Charting.AreaAlignmentOrientations.Vertical | System.Windows.Forms.DataVisualization.Charting.AreaAlignmentOrientations.Horizontal)));
			chartArea1.AxisX.IsMarginVisible = false;
			chartArea1.AxisX.IsMarksNextToAxis = false;
			chartArea1.AxisX.LabelStyle.Enabled = false;
			chartArea1.AxisX.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisX.MajorGrid.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisX.MajorTickMark.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisX.MinorGrid.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisX.MinorTickMark.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisX2.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisY.IsMarginVisible = false;
			chartArea1.AxisY.IsMarksNextToAxis = false;
			chartArea1.AxisY.LabelStyle.Enabled = false;
			chartArea1.AxisY.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisY.MajorGrid.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisY.MajorTickMark.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisY.MinorGrid.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisY.MinorTickMark.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.AxisY2.LineDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			chartArea1.Name = "ChartArea";
			this.chartParameter.ChartAreas.Add(chartArea1);
			this.chartParameter.Dock = System.Windows.Forms.DockStyle.Fill;
			legend1.Name = "Legend1";
			this.chartParameter.Legends.Add(legend1);
			this.chartParameter.Location = new System.Drawing.Point(0, 0);
			this.chartParameter.Name = "chartParameter";
			this.chartParameter.Padding = new System.Windows.Forms.Padding(3);
			series1.BackGradientStyle = System.Windows.Forms.DataVisualization.Charting.GradientStyle.DiagonalRight;
			series1.BackSecondaryColor = System.Drawing.Color.Silver;
			series1.BorderDashStyle = System.Windows.Forms.DataVisualization.Charting.ChartDashStyle.NotSet;
			series1.ChartArea = "ChartArea";
			series1.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.SplineArea;
			series1.IsVisibleInLegend = false;
			series1.Legend = "Legend1";
			series1.Name = "Series";
			this.chartParameter.Series.Add(series1);
			this.chartParameter.Size = new System.Drawing.Size(300, 300);
			this.chartParameter.TabIndex = 0;
			this.chartParameter.Text = "chart1";
			this.toolTip.SetToolTip(this.chartParameter, "Double-click to edit parameter");
			this.chartParameter.DoubleClick += new System.EventHandler(this.ParameterMiniChartDoubleClick);
			// 
			// ParameterMiniChart
			// 
			this.Padding = new System.Windows.Forms.Padding(6);
			this.Size = new System.Drawing.Size(273, 208);
			((System.ComponentModel.ISupportInitialize)(this.chartParameter)).EndInit();
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.DataVisualization.Charting.Chart chartParameter;
		private System.Windows.Forms.ToolTip toolTip;

	}
}
