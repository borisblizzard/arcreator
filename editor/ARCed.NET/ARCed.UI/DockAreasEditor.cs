#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Drawing.Design;
using System.Windows.Forms;
using System.Windows.Forms.Design;

#endregion

namespace ARCed.UI
{	
	internal class DockAreasEditor : UITypeEditor
	{
		private class DockAreasEditorControl : UserControl
		{
            private readonly CheckBox _checkBoxFloat;
            private readonly CheckBox _checkBoxDockLeft;
            private readonly CheckBox _checkBoxDockRight;
            private readonly CheckBox _checkBoxDockTop;
            private readonly CheckBox _checkBoxDockBottom;
            private readonly CheckBox _checkBoxDockFill;
			private DockAreas _mOldDockAreas;

			public DockAreas DockAreas
			{
				get
				{
					DockAreas dockAreas = 0;
					if (this._checkBoxFloat.Checked)
						dockAreas |= DockAreas.Float;
					if (this._checkBoxDockLeft.Checked)
						dockAreas |= DockAreas.DockLeft;
					if (this._checkBoxDockRight.Checked)
						dockAreas |= DockAreas.DockRight;
					if (this._checkBoxDockTop.Checked)
						dockAreas |= DockAreas.DockTop;
					if (this._checkBoxDockBottom.Checked)
						dockAreas |= DockAreas.DockBottom;
					if (this._checkBoxDockFill.Checked)
						dockAreas |= DockAreas.Document;

					if (dockAreas == 0)
						return this._mOldDockAreas;
					else
						return dockAreas;
				}
			}

			public DockAreasEditorControl()
			{
				this._checkBoxFloat = new CheckBox();
				this._checkBoxDockLeft = new CheckBox();
				this._checkBoxDockRight = new CheckBox();
				this._checkBoxDockTop = new CheckBox();
				this._checkBoxDockBottom = new CheckBox();
				this._checkBoxDockFill = new CheckBox();

				SuspendLayout();

				this._checkBoxFloat.Appearance = Appearance.Button;
				this._checkBoxFloat.Dock = DockStyle.Top;
				this._checkBoxFloat.Height = 24;
				this._checkBoxFloat.Text = Strings.DockAreaEditor_FloatCheckBoxText;
				this._checkBoxFloat.TextAlign = ContentAlignment.MiddleCenter;
				this._checkBoxFloat.FlatStyle = FlatStyle.System;
			
				this._checkBoxDockLeft.Appearance = Appearance.Button;
				this._checkBoxDockLeft.Dock = DockStyle.Left;
				this._checkBoxDockLeft.Width = 24;
				this._checkBoxDockLeft.FlatStyle = FlatStyle.System;

				this._checkBoxDockRight.Appearance = Appearance.Button;
				this._checkBoxDockRight.Dock = DockStyle.Right;
				this._checkBoxDockRight.Width = 24;
				this._checkBoxDockRight.FlatStyle = FlatStyle.System;

				this._checkBoxDockTop.Appearance = Appearance.Button;
				this._checkBoxDockTop.Dock = DockStyle.Top;
				this._checkBoxDockTop.Height = 24;
				this._checkBoxDockTop.FlatStyle = FlatStyle.System;

				this._checkBoxDockBottom.Appearance = Appearance.Button;
				this._checkBoxDockBottom.Dock = DockStyle.Bottom;
				this._checkBoxDockBottom.Height = 24;
				this._checkBoxDockBottom.FlatStyle = FlatStyle.System;
			
				this._checkBoxDockFill.Appearance = Appearance.Button;
				this._checkBoxDockFill.Dock = DockStyle.Fill;
				this._checkBoxDockFill.FlatStyle = FlatStyle.System;

				Controls.AddRange(new Control[] {
														 this._checkBoxDockFill,
														 this._checkBoxDockBottom,
														 this._checkBoxDockTop,
														 this._checkBoxDockRight,
														 this._checkBoxDockLeft,
														 this._checkBoxFloat});

				Size = new Size(160, 144);
				BackColor = SystemColors.Control;
				ResumeLayout();
			}

			public void SetStates(DockAreas dockAreas)
			{
				this._mOldDockAreas = dockAreas;
				if ((dockAreas & DockAreas.DockLeft) != 0)
					this._checkBoxDockLeft.Checked = true;
				if ((dockAreas & DockAreas.DockRight) != 0)
					this._checkBoxDockRight.Checked = true;
				if ((dockAreas & DockAreas.DockTop) != 0)
					this._checkBoxDockTop.Checked = true;
				if ((dockAreas & DockAreas.DockTop) != 0)
					this._checkBoxDockTop.Checked = true;
				if ((dockAreas & DockAreas.DockBottom) != 0)
					this._checkBoxDockBottom.Checked = true;
				if ((dockAreas & DockAreas.Document) != 0)
					this._checkBoxDockFill.Checked = true;
				if ((dockAreas & DockAreas.Float) != 0)
					this._checkBoxFloat.Checked = true;
			}
		}

		private DockAreasEditorControl m_ui;

		public override UITypeEditorEditStyle GetEditStyle(ITypeDescriptorContext context)
		{
			return UITypeEditorEditStyle.DropDown;
		}

		public override object EditValue(ITypeDescriptorContext context, IServiceProvider sp, object value)
		{
			if (this.m_ui == null)
				this.m_ui = new DockAreasEditorControl();

			this.m_ui.SetStates((DockAreas)value);

            var edSvc = (IWindowsFormsEditorService)sp.GetService(typeof(IWindowsFormsEditorService));
			edSvc.DropDownControl(this.m_ui);

			return this.m_ui.DockAreas;
		}
	}
}
