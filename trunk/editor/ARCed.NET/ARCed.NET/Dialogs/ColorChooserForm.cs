using System;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Core;

namespace ARCed.Dialogs
{
	/// <summary>
	///   Summary description for ColorChooser.
	/// </summary>
	public partial class ColorChooserForm : Form
	{
		/// <summary>
		///   Required designer variable.
		/// </summary>

		public ColorChooserForm()
		{
			//
			// Required for Windows Form Designer support
			//
			InitializeComponent();
		}

		/// <summary>
		/// Gets or sets the ability to adjust alpha values
		/// </summary>
		public bool AlphaEnabled
		{
			get { return panelAlpha.Enabled; }
			set
			{ 
				panelAlpha.Enabled = value;
			}
		}

		public Color Color
		{
			// Get or set the color to be
			// displayed in the color wheel.
			get { return myColorWheel.Color; }

			set
			{
				// Indicate the color change type. Either RGB or HSV
				// will cause the color wheel to update the position
				// of the pointer.
				changeType = ChangeStyle.RGB;
				argb = new ColorHandler.ARGB(value.A, value.R, value.G, value.B);
				hsv = ColorHandler.RGBtoHSV(argb);
			}
		}

		private void ColorChooserLoad(object sender, EventArgs e)
		{
			// Turn on double-buffering, so the form looks better. 
			SetStyle(ControlStyles.AllPaintingInWmPaint, true);
			SetStyle(ControlStyles.UserPaint, true);
			SetStyle(ControlStyles.DoubleBuffer, true);

			// These properties are set in design view, as well, but they
			// have to be set to false in order for the Paint
			// event to be able to display their contents.
			// Never hurts to make sure they're invisible.
			pnlSelectedColor.Visible = false;
			pnlBrightness.Visible = false;
			pnlColor.Visible = false;

			// Calculate the coordinates of the three
			// required regions on the form.
			Rectangle selectedColorRectangle = new Rectangle(pnlSelectedColor.Location, pnlSelectedColor.Size);
			Rectangle brightnessRectangle = new Rectangle(pnlBrightness.Location, pnlBrightness.Size);
			Rectangle colorRectangle = new Rectangle(pnlColor.Location, pnlColor.Size);

			// Create the new ColorWheel class, indicating
			// the locations of the color wheel itself, the
			// brightness area, and the position of the selected color.
			myColorWheel = new ColorWheel(colorRectangle, brightnessRectangle, selectedColorRectangle);
			myColorWheel.ColorChanged += MyColorWheelColorChanged;

			if (!panelAlpha.Enabled)
			{
				if (this.Color.A != 255)
					this.Color = Color.FromArgb(255, this.Color);
			}

			// Set the RGB and HSV values 
			// of the NumericUpDown controls.
			SetRGB(argb);
			SetHSV(hsv);
			SetRGBLabels(argb);
			SetHSVLabels(hsv);
		}

		private void HandleMouse(object sender, MouseEventArgs e)
		{
			// If you have the left mouse button down, 
			// then update the selectedPoint value and 
			// force a repaint of the color wheel.
			if (e.Button != MouseButtons.Left)
				return;
			changeType = ChangeStyle.MouseMove;
			selectedPoint = new Point(e.X, e.Y);
			Invalidate();
		}

		private void FormMainMouseUp(object sender, MouseEventArgs e)
		{
			myColorWheel.SetMouseUp();
			changeType = ChangeStyle.None;
		}

		private void SetRGBLabels(ColorHandler.ARGB argb)
		{
			RefreshText(lblRed, argb.Red);
			RefreshText(lblBlue, argb.Blue);
			RefreshText(lblGreen, argb.Green);
			RefreshText(lblAlpha, argb.Alpha);
			tbHexCode.Text = string.Format("{0:X2}{1:X2}{2:X2}{3:X2}", argb.Alpha, argb.Red, argb.Green, argb.Blue);
		}

		private void SetHSVLabels(ColorHandler.HSV HSV)
		{
			RefreshText(lblHue, HSV.Hue);
			RefreshText(lblSaturation, HSV.Saturation);
			RefreshText(lblValue, HSV.Value);
			RefreshText(lblAlpha, HSV.Alpha);
		}

		private void SetRGB(ColorHandler.ARGB argb)
		{
			// Update the RGB values on the form.
			RefreshValue(tbRed, argb.Red);
			RefreshValue(tbBlue, argb.Blue);
			RefreshValue(tbGreen, argb.Green);
			RefreshValue(tbAlpha, argb.Alpha);
			SetRGBLabels(argb);
		}

		private void SetHSV(ColorHandler.HSV HSV)
		{
			// Update the HSV values on the form.
			RefreshValue(tbHue, HSV.Hue);
			RefreshValue(tbSaturation, HSV.Saturation);
			RefreshValue(tbValue, HSV.Value);
			RefreshValue(tbAlpha, HSV.Alpha);
			SetHSVLabels(HSV);
		}

		private static void RefreshValue(TrackBar hsv, int value)
		{
			hsv.Value = value;
		}

		private static void RefreshText(Control lbl, int value)
		{
			lbl.Text = value.ToString();
		}

		private void MyColorWheelColorChanged(object sender, ColorChangedEventArgs e)
		{
			SetRGB(e.ARGB);
			SetHSV(e.HSV);
		}

		private void HandleHSVScroll(object sender, EventArgs e)
		// If the H, S, or V values change, use this 
		// code to update the RGB values and invalidate
		// the color wheel (so it updates the pointers).
		// Check the isInUpdate flag to avoid recursive events
		// when you update the NumericUpdownControls.
		{
			changeType = ChangeStyle.HSV;
			hsv = new ColorHandler.HSV(tbAlpha.Value, tbHue.Value, tbSaturation.Value, tbValue.Value);
			SetRGB(ColorHandler.HSVtoRGB(hsv));
			SetHSVLabels(hsv);
			Invalidate();
		}

		private void HandleRGBScroll(object sender, EventArgs e)
		{
			// If the R, G, or B values change, use this 
			// code to update the HSV values and invalidate
			// the color wheel (so it updates the pointers).
			// Check the isInUpdate flag to avoid recursive events
			// when you update the NumericUpdownControls.
			changeType = ChangeStyle.RGB;
			argb = new ColorHandler.ARGB(tbAlpha.Value, tbRed.Value, tbGreen.Value, tbBlue.Value);
			SetHSV(ColorHandler.RGBtoHSV(argb));
			SetRGBLabels(argb);
			Invalidate();
		}

		private void TbAlphaScroll(object sender, EventArgs e)
		{
			changeType = ChangeStyle.RGB;
			argb = new ColorHandler.ARGB(tbAlpha.Value, tbRed.Value, tbGreen.Value, tbBlue.Value);
			RefreshText(lblAlpha, tbAlpha.Value);
			tbHexCode.Text = string.Format("{0:X2}{1:X2}{2:X2}{3:X2}", argb.Alpha, argb.Red, argb.Green, argb.Blue);
			Invalidate();
		}

		private void ColorChooserPaint(object sender, PaintEventArgs e)
		{
			// Depending on the circumstances, force a repaint
			// of the color wheel passing different information.
			switch (changeType)
			{
				case ChangeStyle.HSV:
					myColorWheel.Draw(e.Graphics, hsv);
					break;
				case ChangeStyle.MouseMove:
				case ChangeStyle.None:
					myColorWheel.Draw(e.Graphics, selectedPoint);
					break;
				case ChangeStyle.RGB:
					myColorWheel.Draw(e.Graphics, argb);
					break;
			}
		}

		private void TbHexCodeMouseDown(object sender, MouseEventArgs e)
		{
			tbHexCode.SelectionStart = 0;
			tbHexCode.SelectionLength = tbHexCode.Text.Length;
		}


		#region Nested type: ChangeStyle

		private enum ChangeStyle
		{
			MouseMove,
			RGB,
			HSV,
			None
		}

		#endregion

		private void buttonCapture_Click(object sender, EventArgs e)
		{
			FormWindowState currentState = Editor.MainInstance.WindowState;
			Editor.MainInstance.Visible = false;
			this.Visible = false;
			System.Threading.Thread.Sleep(500);
			using (CaptureForm captureForm = new CaptureForm())
			{
				captureForm.TakeSnapShot();
				captureForm.ShowDialog();
				this.Color = captureForm.CaptureColor;
				SetRGBLabels(argb);
				SetHSVLabels(hsv);
				SetRGB(argb);
				SetHSV(hsv);
			}
			Editor.MainInstance.Visible = true;
			this.Visible = true;

		}

		private void groupBoxRGB_CollapseBoxClickedEvent(object sender)
		{
			int y = (groupBoxRGB.FullHeight - groupBoxRGB.CollapsedHeight);
			if (groupBoxRGB.IsCollapsed) y *= -1;
			this.Size = new Size(this.Width, this.Height + y);
			groupBoxHSV.Location = new Point(groupBoxHSV.Location.X,
				groupBoxHSV.Location.Y + y);
			panelAlpha.Location = new Point(panelAlpha.Location.X,
				panelAlpha.Location.Y + y);
		}

		private void groupBoxHSV_CollapseBoxClickedEvent(object sender)
		{
			int y = (groupBoxHSV.FullHeight - groupBoxHSV.CollapsedHeight);
			if (groupBoxHSV.IsCollapsed) y *= -1;
			this.Size = new Size(this.Width, this.Height + y);
			panelAlpha.Location = new Point(panelAlpha.Location.X,
				panelAlpha.Location.Y + y);
		}
	}
}
