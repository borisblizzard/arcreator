#region Using Directives

using System;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Dialogs;
using ARCed.Properties;
using ARCed.Settings;
using ARCed.UI;

#endregion

namespace ARCed.Scripting
{
	public partial class ScriptStyleForm : DockContent
	{
		private bool _suppressEvents = true;

		private ScriptStyle CurrentStyle
		{
			get { return Editor.Settings.Scripting.ScriptStyles[this.listBoxStyles.SelectedIndex]; }
		}

		public ScriptStyleForm()
		{
			this.InitializeComponent();
			Icon = Icon.FromHandle(Resources.Scintilla.GetHicon());
			this.listBoxStyles.Items.Clear();
			this.listBoxStyles.BeginUpdate();
			foreach (ScriptStyle style in Editor.Settings.Scripting.ScriptStyles)
				this.listBoxStyles.Items.Add(style.Name);
			this.listBoxStyles.EndUpdate();
			this.panelCaretColor.BackColor = Editor.Settings.Scripting.CaretColor;
			this.listBoxStyles.SelectedIndex = 0;
		}

		private static Color ShowColorDialog(Color color)
		{
			using (var dialog = new ColorChooserForm())
			{
				dialog.Color = color;
				return dialog.ShowDialog() == DialogResult.OK ? dialog.Color : color;
			}
		}

		private static void UpdateOpenScripts()
		{
			foreach (ScriptEditorForm form in Windows.ScriptEditors)
			{
				form.SetStyle(Editor.Settings.Scripting.ScriptStyles);
				form.ScintillaControl.Caret.Color = Editor.Settings.Scripting.CaretColor;
			}
		}

		#region Form Controls

		private void UpdateFont(object sender, EventArgs e)
		{
			if (!this._suppressEvents)
			{
				this.CurrentStyle.Font = this.fontSelector.UserFont;
				UpdateOpenScripts();
			}
		}

		private void panelCaretColor_DoubleClick(object sender, EventArgs e)
		{
			if (!this._suppressEvents)
			{
				Editor.Settings.Scripting.CaretColor = 
					ShowColorDialog(Editor.Settings.Scripting.CaretColor);
				this.panelCaretColor.BackColor = Editor.Settings.Scripting.CaretColor;
				UpdateOpenScripts();
			}
		}

		private void panelColorFore_DoubleClick(object sender, EventArgs e)
		{
			if (!this._suppressEvents)
			{
				this.CurrentStyle.ForeColor = ShowColorDialog(this.CurrentStyle.ForeColor);
				this.panelColorFore.BackColor = this.CurrentStyle.ForeColor;
				UpdateOpenScripts();
			}
		}

		private void panelColorBack_DoubleClick(object sender, EventArgs e)
		{
			if (!this._suppressEvents)
			{
				this.CurrentStyle.BackColor = ShowColorDialog(this.CurrentStyle.BackColor);
				this.panelColorFore.BackColor = this.CurrentStyle.BackColor;
				UpdateOpenScripts();
			}
		}

		private void listBoxStyles_SelectedIndexChanged(object sender, EventArgs e)
		{
			this._suppressEvents = true;
			ScriptStyle style = this.CurrentStyle;
			this.fontSelector.UserFont = style.Font;
			this.panelColorFore.BackColor = style.ForeColor;
			this.panelColorBack.BackColor = style.BackColor;
			this._suppressEvents = false;
		}

		private void buttonDefault_Click(object sender, EventArgs e)
		{
			Editor.Settings.Scripting.ScriptStyles = ScriptSettings.DefaultStyles;
			this.listBoxStyles_SelectedIndexChanged(null, null);
			UpdateOpenScripts();
		}

		#endregion

		private void panelColor_OnPaint(object sender, PaintEventArgs e)
		{
			using (e.Graphics)
			{
				e.Graphics.DrawImage(Resources.Alpha, e.ClipRectangle);
				using (var brush = new SolidBrush((sender as Panel).BackColor))
					e.Graphics.FillRectangle(brush, e.ClipRectangle);	
			}
		}
	}
}
