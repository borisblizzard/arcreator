using System;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Dialogs;
using ARCed.Settings;
using ARCed.UI;

namespace ARCed.Scripting
{
	public partial class ScriptStyleForm : DockContent
	{
		private bool _suppressEvents = true;

		private ScriptStyle CurrentStyle
		{
			get { return Editor.Settings.Scripting.ScriptStyles[listBoxStyles.SelectedIndex]; }
		}

		public ScriptStyleForm()
		{
			InitializeComponent();
			this.Icon = Icon.FromHandle(Properties.Resources.Scintilla.GetHicon());
			listBoxStyles.Items.Clear();
			listBoxStyles.BeginUpdate();
			foreach (ScriptStyle style in Editor.Settings.Scripting.ScriptStyles)
				listBoxStyles.Items.Add(style.Name);
			listBoxStyles.EndUpdate();
			panelCaretColor.BackColor = Editor.Settings.Scripting.CaretColor;
			listBoxStyles.SelectedIndex = 0;
		}

		private Color ShowColorDialog(Color color)
		{
			using (ColorChooserForm dialog = new ColorChooserForm())
			{
				dialog.Color = color;
				if (dialog.ShowDialog() == DialogResult.OK)
					return dialog.Color;
				return color;
			}
		}

		private void UpdateOpenScripts()
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
			if (!_suppressEvents)
			{
				CurrentStyle.Font = fontSelector.UserFont;
				UpdateOpenScripts();
			}
		}

		private void panelCaretColor_DoubleClick(object sender, EventArgs e)
		{
			if (!_suppressEvents)
			{
				Editor.Settings.Scripting.CaretColor = 
					ShowColorDialog(Editor.Settings.Scripting.CaretColor);
				panelCaretColor.BackColor = Editor.Settings.Scripting.CaretColor;
				UpdateOpenScripts();
			}
		}

		private void panelColorFore_DoubleClick(object sender, EventArgs e)
		{
			if (!_suppressEvents)
			{
				CurrentStyle.ForeColor = ShowColorDialog(CurrentStyle.ForeColor);
				panelColorFore.BackColor = CurrentStyle.ForeColor;
				UpdateOpenScripts();
			}
		}

		private void panelColorBack_DoubleClick(object sender, EventArgs e)
		{
			if (!_suppressEvents)
			{
				CurrentStyle.BackColor = ShowColorDialog(CurrentStyle.BackColor);
				panelColorFore.BackColor = CurrentStyle.BackColor;
				UpdateOpenScripts();
			}
		}

		private void listBoxStyles_SelectedIndexChanged(object sender, EventArgs e)
		{
			_suppressEvents = true;
			ScriptStyle style = CurrentStyle;
			fontSelector.UserFont = style.Font;
			panelColorFore.BackColor = style.ForeColor;
			panelColorBack.BackColor = style.BackColor;
			_suppressEvents = false;
		}

		private void buttonDefault_Click(object sender, EventArgs e)
		{
			Editor.Settings.Scripting.ScriptStyles = ScriptSettings.DefaultStyles;
			listBoxStyles_SelectedIndexChanged(null, null);
			UpdateOpenScripts();
		}

		#endregion

		private void panelColor_OnPaint(object sender, PaintEventArgs e)
		{
			using (e.Graphics)
			{
				e.Graphics.DrawImage(Properties.Resources.Alpha, e.ClipRectangle);
				using (SolidBrush brush = new SolidBrush((sender as Panel).BackColor))
					e.Graphics.FillRectangle(brush, e.ClipRectangle);	
			}
		}
	}
}
