﻿#region Using Directives

using System;
using System.Drawing;
using System.Globalization;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using ARCed.Dialogs;
using ARCed.Properties;
using ARCed.Settings;
using ARCed.UI;

#endregion

namespace ARCed.Database.Actors
{
	/// <summary>
	/// Form with controls for allowing modification of user-defined chart settings.
	/// </summary>
	public partial class ChartSettingsForm : DockContent
	{
		#region Private Fields

		Chart[] _charts;

		#endregion

		#region Constructor

		/// <summary>
		/// Default constuctor
		/// </summary>
		public ChartSettingsForm()
		{
			this.InitializeComponent();
			this.AddDataBinding();
			Icon = Icon.FromHandle(Resources.Chart.GetHicon());
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Sets the forms chart controls
		/// </summary>
		/// <param name="charts">Reference to an array of <see cref="Chart"/> object.</param>
		public void SetCharts(ref Chart[] charts)
		{
			this._charts = charts;
		}

		/// <summary>
		/// Clears the charts
		/// </summary>
		public void ClearCharts()
		{
			this._charts = null;
		}

		/// <summary>
		/// Sets the <see cref="SeriesChartType"/> type for the charts.
		/// </summary>
		/// <param name="type">Chart type to set</param>
		/// <param name="charts">Reference to an array of <see cref="Chart"/> object.</param>
		public static void SetChartType(SeriesChartType type, ref Chart[] charts)
		{
			if (charts == null) return;
			foreach (Chart chart in charts)
				chart.Series[0].ChartType = type;
		}

		/// <summary>
		/// Gets the user-defined <see cref="Color"/> used for the chart with the given index.
		/// </summary>
		/// <param name="index">Index of the color to retrieve.</param>
		/// <returns>User-defined color</returns>
		public static Color GetUserColor(int index)
		{
			index %= Editor.Settings.Charting.Colors.Count;
			return Editor.Settings.Charting.Colors[index];
		}

		/// <summary>
		/// Gets the user-defined <see cref="Color"/> used for the chart with the given index.
		/// </summary>
		/// <param name="index">Index of the color to retrieve.</param>
		/// <param name="color">User-defined color</param>
		public static void SetUserColor(int index, Color color)
		{
			index %= Editor.Settings.Charting.Colors.Count;
			Editor.Settings.Charting.Colors[index] = color;
		}

		/// <summary>
		/// Gets the user-defined <see cref="LightStyle"/> setting for the given index. 
		/// </summary>
		/// <param name="index">Index to retrieve the style for.</param>
		/// <returns>LightStyle setting for index.</returns>
		public static LightStyle GetChartLighting(int index)
		{
			return (LightStyle)index;
		}

		/// <summary>
		/// Sets the user-defined <see cref="LightStyle"/> setting for the given index. 
		/// </summary>
		/// <param name="style">Style to set</param>
		/// <param name="charts">Reference to an array of <see cref="Chart"/> object.</param>
		public static void SetChartLighting(LightStyle style, ref Chart[] charts)
		{
			if (charts == null) return;
			foreach (Chart chart in charts)
				chart.ChartAreas[0].Area3DStyle.LightStyle = style;
		}

		#endregion

		#region Private Methods

		private void AddDataBinding()
		{
			this.listBoxColors.DataSource = Editor.Settings.Charting.ColorsHtml;
			//comboBoxType.DataBindings.Add("SelectedIndex", Editor.Settings.Charting, "Type",
			//false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
			this.numericTension.DataBindings.Add("Value", Editor.Settings.Charting, "SplineTension",
				false, DataSourceUpdateMode.OnPropertyChanged);
			this.numericInclination.DataBindings.Add("Value", Editor.Settings.Charting, "Inclination",
				false, DataSourceUpdateMode.OnPropertyChanged);
			this.numericDepth.DataBindings.Add("Value", Editor.Settings.Charting, "Depth",
				false, DataSourceUpdateMode.OnPropertyChanged);
			this.comboBoxLighting.DataBindings.Add("SelectedIndex", Editor.Settings.Charting, "Lighting",
				false, DataSourceUpdateMode.OnPropertyChanged);
			this.numericPerspective.DataBindings.Add("Value", Editor.Settings.Charting, "Perspective",
				false, DataSourceUpdateMode.OnPropertyChanged);
			this.numericRotation.DataBindings.Add("Value", Editor.Settings.Charting, "Rotation",
				false, DataSourceUpdateMode.OnPropertyChanged);
			this.checkBox3D.DataBindings.Add("Checked", Editor.Settings.Charting, "ThreeD",
				false, DataSourceUpdateMode.OnPropertyChanged);
			this.checkBoxMarkerLines.DataBindings.Add("Checked", Editor.Settings.Charting, "Markers",
				false, DataSourceUpdateMode.OnPropertyChanged);
		}

		private void ComboBoxTypeSelectedIndexChanged(object sender, EventArgs e)
		{
			SeriesChartType type;
			switch (this.comboBoxType.SelectedIndex)
			{
				case 1: type = SeriesChartType.SplineArea; break;
				case 2: type = SeriesChartType.Spline; break;
				case 3: type = SeriesChartType.StepLine; break;
				case 4: type = SeriesChartType.RangeColumn; break;
				case 5: type = SeriesChartType.Point; break;
				default: type = SeriesChartType.SplineRange; break;
			}
			Editor.Settings.Charting.Type = type;
			if (this._charts != null)
				SetChartType(type, ref this._charts);
		}

		private void NumericTensionValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.SplineTension = this.numericTension.Value;
			if (this._charts != null)
			{
				foreach (Chart chart in this._charts)
					chart.Series[0]["LineTension"] = this.numericTension.Value.ToString(CultureInfo.InvariantCulture);
			}
		}

		private void ComboBoxLightingSelectedIndexChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Lighting = (LightStyle)this.comboBoxLighting.SelectedIndex;
			if (this._charts != null)
			{
				SetChartLighting((LightStyle)this.comboBoxLighting.SelectedIndex, ref this._charts);
			}
		}

		private void NumericInclinationValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Inclination = this.numericInclination.Value;
			if (this._charts != null)
			{
				foreach (Chart chart in this._charts)
					chart.ChartAreas[0].Area3DStyle.Inclination = (int)this.numericInclination.Value;
			}
		}

		private void NumericRotationValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Rotation = this.numericRotation.Value;
			if (this._charts != null)
			{
				foreach (Chart chart in this._charts)
					chart.ChartAreas[0].Area3DStyle.Rotation = (int)this.numericRotation.Value;
			}
		}

		private void NumericPerspectiveValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Perspective = this.numericPerspective.Value;
			if (this._charts != null)
			{
				foreach (Chart chart in this._charts)
					chart.ChartAreas[0].Area3DStyle.Perspective = (int)this.numericPerspective.Value;
			}
		}

		private void CheckBoxMarkerLinesCheckedChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Markers = this.checkBoxMarkerLines.Checked;
			if (this._charts != null)
			{
				foreach (Chart chart in this._charts)
					chart.Series[0]["ShowMarkerLines"] = this.checkBoxMarkerLines.Checked.ToString();
			}
		}

		private void NumericDepthValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Depth = this.numericDepth.Value;
			if (this._charts == null) return;
			foreach (Chart chart in this._charts)
				chart.ChartAreas[0].Area3DStyle.PointDepth = (int)this.numericDepth.Value;
		}

		private void CheckBox3DCheckedChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.ThreeD = this.checkBox3D.Checked;
			if (this._charts == null) return;
			foreach (Chart chart in this._charts)
				chart.ChartAreas[0].Area3DStyle.Enable3D = this.checkBox3D.Checked;
		}

		private void ListBoxColorsDoubleClick(object sender, EventArgs e)
		{
			var index = this.listBoxColors.SelectedIndex;
			if (index < 0) return;
			using (var dialog = new ColorChooserForm())
			{
				dialog.Color = Editor.Settings.Charting.Colors[index];
				dialog.AlphaEnabled = false;
				if (dialog.ShowDialog(Windows.ChartSettingsForm) != DialogResult.OK) return;
				this.listBoxColors.DataSource = null;
				Editor.Settings.Charting.Colors[index] = dialog.Color;
				this.RefreshColors();
			}
		}

		private void ButtonAddClick(object sender, EventArgs e)
		{
			using (var dialog = new ColorChooserForm())
			{
				dialog.Color = Color.White;
				if (dialog.ShowDialog() != DialogResult.OK) return;
				Editor.Settings.Charting.Colors.Add(dialog.Color);
				this.RefreshColors();
			}
		}

		private void ButtonRemoveClick(object sender, EventArgs e)
		{
			int index = this.listBoxColors.SelectedIndex;
			if (index > 0)
			{
				this.listBoxColors.DataSource = null;
				Editor.Settings.Charting.Colors.RemoveAt(index);
				this.RefreshColors();
			}
			this.listBoxColors.SelectedIndex = index.Clamp(0, Editor.Settings.Charting.Colors.Count - 1);
		}

		private void ButtonUpClick(object sender, EventArgs e)
		{
			int index = this.listBoxColors.SelectedIndex;
			if (index <= 0) return;
			this.listBoxColors.DataSource = null;
			Color color = Editor.Settings.Charting.Colors[index % Editor.Settings.Charting.Colors.Count];
			Editor.Settings.Charting.Colors.RemoveAt(index);
			Editor.Settings.Charting.Colors.Insert(index - 1, color);
			this.RefreshColors();
			this.listBoxColors.SelectedIndex = index - 1;
		}

		private void ButtonDownClick(object sender, EventArgs e)
		{
			int index = this.listBoxColors.SelectedIndex;
			if (index < Editor.Settings.Charting.Colors.Count - 1)
			{
				this.listBoxColors.DataSource = null;
				Color color = Editor.Settings.Charting.Colors[index];
				Editor.Settings.Charting.Colors.RemoveAt(index);
				Editor.Settings.Charting.Colors.Insert(index + 1, color);
				this.RefreshColors();
				this.listBoxColors.SelectedIndex = index + 1;
			}
		}

		private void RefreshColors()
		{
			this.listBoxColors.BeginUpdate();
			this.listBoxColors.DataSource = Editor.Settings.Charting.ColorsHtml;
			this.listBoxColors.EndUpdate();
		}

		private void ListBoxColorsSelectedIndexChanged(object sender, EventArgs e)
		{
			bool enable = this.listBoxColors.SelectedIndex >= 0 && this.listBoxColors.Items.Count > 1;
			this.buttonDown.Enabled = enable;
			this.buttonUp.Enabled = enable;
			this.buttonRemove.Enabled = enable;
		}

		private void ButtonDefaultColorsClick(object sender, EventArgs e)
		{
			this.listBoxColors.DataSource = null;
			Editor.Settings.Charting.Colors = ChartSettings.DefaultColors;
			this.RefreshColors();
		}

		#endregion
	}
}
