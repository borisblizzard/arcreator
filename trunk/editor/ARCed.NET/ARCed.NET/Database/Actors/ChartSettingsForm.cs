using System;
using System.Drawing;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;
using ARCed.Dialogs;
using ARCed.UI;
using ARCed;

namespace ARCed.Database.Actors
{
	public partial class ChartSettingsForm : DockContent
	{

		Chart[] _charts;


		Chart CurrentChart { get { return (this.Parent as ActorParametersForm).CurrentChart; } }

		public ChartSettingsForm()
		{
			InitializeComponent();
			AddDataBinding();
			this.Icon = Icon.FromHandle(Properties.Resources.Chart.GetHicon());
		}

		public void SetCharts(ref Chart[] charts)
		{
			_charts = charts;
		}

		public void ClearCharts()
		{
			_charts = null;
		}

		private void AddDataBinding()
		{
			listBoxColors.DataSource = Editor.Settings.Charting.ColorsHtml;
			//comboBoxType.DataBindings.Add("SelectedIndex", Editor.Settings.Charting, "Type",
				//false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
			numericTension.DataBindings.Add("Value", Editor.Settings.Charting, "SplineTension",
				false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
			numericInclination.DataBindings.Add("Value", Editor.Settings.Charting, "Inclination",
				false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
			numericDepth.DataBindings.Add("Value", Editor.Settings.Charting, "Depth",
				false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
			comboBoxLighting.DataBindings.Add("SelectedIndex", Editor.Settings.Charting, "Lighting",
				false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
			numericPerspective.DataBindings.Add("Value", Editor.Settings.Charting, "Perspective",
				false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
			numericRotation.DataBindings.Add("Value", Editor.Settings.Charting, "Rotation",
				false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
			checkBox3D.DataBindings.Add("Checked", Editor.Settings.Charting, "ThreeD",
				false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
			checkBoxMarkerLines.DataBindings.Add("Checked", Editor.Settings.Charting, "Markers",
				false, DataSourceUpdateMode.OnValidation | DataSourceUpdateMode.OnPropertyChanged);
		}

		#region Setting Controls

		private void comboBoxType_SelectedIndexChanged(object sender, EventArgs e)
		{
			SeriesChartType type;
			switch (comboBoxType.SelectedIndex)
			{
				case 1: type = SeriesChartType.SplineArea; break;
				case 2: type = SeriesChartType.Spline; break;
				case 3: type = SeriesChartType.StepLine; break;
				case 4: type = SeriesChartType.RangeColumn; break;
				case 5: type = SeriesChartType.Point; break;
				default: type = SeriesChartType.SplineRange; break;
			}
			Editor.Settings.Charting.Type = type;
			if (_charts != null)
				SetChartType(type, ref _charts);
		}

		private void numericTension_ValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.SplineTension = numericTension.Value;
			if (_charts != null)
			{
				foreach (Chart chart in _charts)
					chart.Series[0]["LineTension"] = numericTension.Value.ToString();
			}
		}

		private void comboBoxLighting_SelectedIndexChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Lighting = (LightStyle)comboBoxLighting.SelectedIndex;
			if (_charts != null)
			{
				SetChartLighting((LightStyle)comboBoxLighting.SelectedIndex, ref _charts);
			}
		}

		private void numericInclination_ValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Inclination = numericInclination.Value;
			if (_charts != null)
			{
				foreach (Chart chart in _charts)
					chart.ChartAreas[0].Area3DStyle.Inclination = (int)numericInclination.Value;
			}
		}

		private void numericRotation_ValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Rotation = numericRotation.Value;
			if (_charts != null)
			{
				foreach (Chart chart in _charts)
					chart.ChartAreas[0].Area3DStyle.Rotation = (int)numericRotation.Value;
			}
		}

		private void numericPerspective_ValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Perspective = numericPerspective.Value;
			if (_charts != null)
			{
				foreach (Chart chart in _charts)
					chart.ChartAreas[0].Area3DStyle.Perspective = (int)numericPerspective.Value;
			}
		}

		private void checkBoxMarkerLines_CheckedChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Markers = checkBoxMarkerLines.Checked;
			if (_charts != null)
			{
				foreach (Chart chart in _charts)
					chart.Series[0]["ShowMarkerLines"] = checkBoxMarkerLines.Checked.ToString();
			}
		}

		private void comboBoxType_KeyDown(object sender, KeyEventArgs e)
		{
			e.SuppressKeyPress = true;
		}

		private void numericDepth_ValueChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.Depth = numericDepth.Value;
			if (_charts != null)
			{
				foreach (Chart chart in _charts)
					chart.ChartAreas[0].Area3DStyle.PointDepth = (int)numericDepth.Value;
			}
		}

		private void checkBox3D_CheckedChanged(object sender, EventArgs e)
		{
			Editor.Settings.Charting.ThreeD = checkBox3D.Checked;
			if (_charts != null)
			{
				foreach (Chart chart in _charts)
					chart.ChartAreas[0].Area3DStyle.Enable3D = checkBox3D.Checked;
			}
		}

		private void listBoxColors_DoubleClick(object sender, EventArgs e)
		{
			int index = listBoxColors.SelectedIndex;
			if (index >= 0)
			{
				using (ColorChooserForm dialog = new ColorChooserForm())
				{
					dialog.Color = Editor.Settings.Charting.Colors[index];
					dialog.AlphaEnabled = false;
					if (dialog.ShowDialog(Windows.ChartSettingsForm) == DialogResult.OK)
					{
						listBoxColors.DataSource = null;
						Editor.Settings.Charting.Colors[index] = dialog.Color;
						RefreshColors();
					}
				}
			}
		}

		#endregion

		public static void SetChartType(SeriesChartType type, ref Chart[] charts)
		{
			if (charts != null)
			{
				foreach (Chart chart in charts)
					chart.Series[0].ChartType = type;
			}
		}

		public static Color GetUserColor(int index)
		{
			index %= Editor.Settings.Charting.Colors.Count;
			return Editor.Settings.Charting.Colors[index];
		}

		public static void SetUserColor(int index, Color color)
		{
			index %= Editor.Settings.Charting.Colors.Count;
			Editor.Settings.Charting.Colors[index] = color;
		}

		public static LightStyle GetChartLighting(int index)
		{
			return (LightStyle)index;
		}

		public static void SetChartLighting(LightStyle style, ref Chart[] charts)
		{
			if (charts != null)
			{
				foreach (Chart chart in charts)
					chart.ChartAreas[0].Area3DStyle.LightStyle = style;
			}
		}

		private void buttonAdd_Click(object sender, EventArgs e)
		{
			using (ColorChooserForm dialog = new ColorChooserForm())
			{
				//dialog.AlphaEnabled = false;
				dialog.Color = Color.White;
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					Editor.Settings.Charting.Colors.Add(dialog.Color);
					RefreshColors();
				}
			}
		}

		private void buttonRemove_Click(object sender, EventArgs e)
		{
			int index = listBoxColors.SelectedIndex;
			if (index > 0)
			{
				listBoxColors.DataSource = null;
				Editor.Settings.Charting.Colors.RemoveAt(index);
				RefreshColors();
			}
			listBoxColors.SelectedIndex = index.Clamp(0, Editor.Settings.Charting.Colors.Count - 1);
		}

		private void buttonUp_Click(object sender, EventArgs e)
		{
			int index = listBoxColors.SelectedIndex;
			if (index > 0)
			{
				listBoxColors.DataSource = null;
				Color color = Editor.Settings.Charting.Colors[index % Editor.Settings.Charting.Colors.Count];
				Editor.Settings.Charting.Colors.RemoveAt(index);
				Editor.Settings.Charting.Colors.Insert(index - 1, color);
				RefreshColors();
				listBoxColors.SelectedIndex = index - 1;
			}
		}

		private void buttonDown_Click(object sender, EventArgs e)
		{
			int index = listBoxColors.SelectedIndex;
			if (index < Editor.Settings.Charting.Colors.Count - 1)
			{
				listBoxColors.DataSource = null;
				Color color = Editor.Settings.Charting.Colors[index];
				Editor.Settings.Charting.Colors.RemoveAt(index);
				Editor.Settings.Charting.Colors.Insert(index + 1, color);
				RefreshColors();
				listBoxColors.SelectedIndex = index + 1;
			}
		}

		private void RefreshColors()
		{
			listBoxColors.BeginUpdate();
			listBoxColors.DataSource = Editor.Settings.Charting.ColorsHtml;
			listBoxColors.EndUpdate();	
		}

		private void listBoxColors_SelectedIndexChanged(object sender, EventArgs e)
		{
			bool enable = listBoxColors.SelectedIndex >= 0 && listBoxColors.Items.Count > 1;
			buttonDown.Enabled = enable;
			buttonUp.Enabled = enable;
			buttonRemove.Enabled = enable;
		}

		private void buttonDefaultColors_Click(object sender, EventArgs e)
		{
			listBoxColors.DataSource = null;
			Editor.Settings.Charting.Colors = Settings.ChartSettings.DefaultColors;
			RefreshColors();
		}

	}
}
