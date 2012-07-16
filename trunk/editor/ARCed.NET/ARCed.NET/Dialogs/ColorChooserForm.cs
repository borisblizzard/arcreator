#region Using Directives

using System;
using System.Drawing;
using System.Globalization;
using System.Threading;
using System.Windows.Forms;
using ARCed.Core;

#endregion

namespace ARCed.Dialogs
{
	/// <summary>
	///   Summary description for ColorChooser.
	/// </summary>
	public partial class ColorChooserForm : Form
    {

        #region Public Properties

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

        /// <summary>
        /// Gets or sets the selected <see cref="Color"/> of the form.
        /// </summary>
        public Color Color
        {
            get { return myColorWheel.Color; }
            set
            {
                this._changeType = ChangeStyle.RGB;
                this._argb = new ColorHandler.ARGB(value.A, value.R, value.G, value.B);
                this._hsv = ColorHandler.RGBtoHSV(this._argb);
            }
        }

        #endregion

        #region Constructor

        /// <summary>
        /// Default constructor
        /// </summary>
		public ColorChooserForm()
		{
			InitializeComponent();
		}

        #endregion

        #region Private Methods

        private void ColorChooserLoad(object sender, EventArgs e)
		{
			SetStyle(ControlStyles.AllPaintingInWmPaint, true);
			SetStyle(ControlStyles.UserPaint, true);
			SetStyle(ControlStyles.DoubleBuffer, true);
			pnlSelectedColor.Visible = false;
			pnlBrightness.Visible = false;
			pnlColor.Visible = false;
			var selectedColorRectangle = new Rectangle(pnlSelectedColor.Location, pnlSelectedColor.Size);
			var brightnessRectangle = new Rectangle(pnlBrightness.Location, pnlBrightness.Size);
			var colorRectangle = new Rectangle(pnlColor.Location, pnlColor.Size);
			myColorWheel = new ColorWheel(colorRectangle, brightnessRectangle, selectedColorRectangle);
			myColorWheel.ColorChanged += MyColorWheelColorChanged;
			if (!panelAlpha.Enabled)
			{
				if (this.Color.A != 255)
					this.Color = Color.FromArgb(255, this.Color);
			}
			SetRGB(this._argb);
			SetHSV(this._hsv);
			SetRGBLabels(this._argb);
			SetHSVLabels(this._hsv);
		}

		private void HandleMouse(object sender, MouseEventArgs e)
		{
			if (e.Button != MouseButtons.Left)
				return;
			this._changeType = ChangeStyle.MouseMove;
			selectedPoint = new Point(e.X, e.Y);
			Invalidate();
		}

		private void FormMainMouseUp(object sender, MouseEventArgs e)
		{
			myColorWheel.SetMouseUp();
			this._changeType = ChangeStyle.None;
		}

		private void SetRGBLabels(ColorHandler.ARGB argb)
		{
			RefreshText(lblRed, argb.Red);
			RefreshText(lblBlue, argb.Blue);
			RefreshText(lblGreen, argb.Green);
			RefreshText(lblAlpha, argb.Alpha);
			tbHexCode.Text = string.Format("{0:X2}{1:X2}{2:X2}{3:X2}", argb.Alpha, argb.Red, argb.Green, argb.Blue);
		}

		private void SetHSVLabels(ColorHandler.HSV hsv)
		{
			RefreshText(lblHue, hsv.Hue);
			RefreshText(lblSaturation, hsv.Saturation);
			RefreshText(lblValue, hsv.Value);
			RefreshText(lblAlpha, hsv.Alpha);
		}

		private void SetRGB(ColorHandler.ARGB argb)
		{
			RefreshValue(tbRed, argb.Red);
			RefreshValue(tbBlue, argb.Blue);
			RefreshValue(tbGreen, argb.Green);
			RefreshValue(tbAlpha, argb.Alpha);
			SetRGBLabels(argb);
		}

		private void SetHSV(ColorHandler.HSV hsv)
		{
			RefreshValue(tbHue, hsv.Hue);
			RefreshValue(tbSaturation, hsv.Saturation);
			RefreshValue(tbValue, hsv.Value);
			RefreshValue(tbAlpha, hsv.Alpha);
			SetHSVLabels(hsv);
		}

		private static void RefreshValue(TrackBar hsv, int value)
		{
			hsv.Value = value;
		}

		private static void RefreshText(Control lbl, int value)
		{
			lbl.Text = value.ToString(CultureInfo.InvariantCulture);
		}

		private void MyColorWheelColorChanged(object sender, ColorChangedEventArgs e)
		{
			SetRGB(e.ARGB);
			SetHSV(e.HSV);
		}

		private void HandleHSVScroll(object sender, EventArgs e)
		{
			this._changeType = ChangeStyle.HSV;
			this._hsv = new ColorHandler.HSV(tbAlpha.Value, tbHue.Value, tbSaturation.Value, tbValue.Value);
			SetRGB(ColorHandler.HSVtoRGB(this._hsv));
			SetHSVLabels(this._hsv);
			Invalidate();
		}

		private void HandleRGBScroll(object sender, EventArgs e)
		{
			this._changeType = ChangeStyle.RGB;
			this._argb = new ColorHandler.ARGB(tbAlpha.Value, tbRed.Value, tbGreen.Value, tbBlue.Value);
			SetHSV(ColorHandler.RGBtoHSV(this._argb));
			SetRGBLabels(this._argb);
			Invalidate();
		}

		private void TbAlphaScroll(object sender, EventArgs e)
		{
			this._changeType = ChangeStyle.RGB;
			this._argb = new ColorHandler.ARGB(tbAlpha.Value, tbRed.Value, tbGreen.Value, tbBlue.Value);
			RefreshText(lblAlpha, tbAlpha.Value);
			tbHexCode.Text = string.Format("{0:X2}{1:X2}{2:X2}{3:X2}", this._argb.Alpha, this._argb.Red, this._argb.Green, this._argb.Blue);
			Invalidate();
		}

		private void ColorChooserPaint(object sender, PaintEventArgs e)
		{
			switch (this._changeType)
			{
				case ChangeStyle.HSV:
					myColorWheel.Draw(e.Graphics, this._hsv);
					break;
				case ChangeStyle.MouseMove:
				case ChangeStyle.None:
					myColorWheel.Draw(e.Graphics, selectedPoint);
					break;
				case ChangeStyle.RGB:
					myColorWheel.Draw(e.Graphics, this._argb);
					break;
			}
		}

		private void TbHexCodeMouseDown(object sender, MouseEventArgs e)
		{
			tbHexCode.SelectionStart = 0;
			tbHexCode.SelectionLength = tbHexCode.Text.Length;
		}

		private void ButtonCaptureClick(object sender, EventArgs e)
		{
			Editor.MainInstance.Visible = false;
			Visible = false;
			Thread.Sleep(500);
			using (var captureForm = new CaptureForm())
			{
				captureForm.TakeSnapShot();
				captureForm.ShowDialog();
				this.Color = captureForm.CaptureColor;
				SetRGBLabels(this._argb);
				SetHSVLabels(this._hsv);
				SetRGB(this._argb);
				SetHSV(this._hsv);
			}
			Editor.MainInstance.Visible = true;
			Visible = true;
		}

		private void GroupBoxRGBCollapseBoxClickedEvent(object sender)
		{
			int y = (groupBoxRGB.FullHeight - groupBoxRGB.CollapsedHeight);
			if (groupBoxRGB.IsCollapsed) y *= -1;
			Size = new Size(Width, Height + y);
			groupBoxHSV.Location = new Point(groupBoxHSV.Location.X,
				groupBoxHSV.Location.Y + y);
			panelAlpha.Location = new Point(panelAlpha.Location.X,
				panelAlpha.Location.Y + y);
		}

		private void GroupBoxHSVCollapseBoxClickedEvent(object sender)
		{
			int y = (groupBoxHSV.FullHeight - groupBoxHSV.CollapsedHeight);
			if (groupBoxHSV.IsCollapsed) y *= -1;
			Size = new Size(Width, Height + y);
			panelAlpha.Location = new Point(panelAlpha.Location.X,
				panelAlpha.Location.Y + y);
		}

        #endregion

        #region Nested type: ChangeStyle

        /// <summary>
        /// Enum containing flags for change styles
        /// </summary>
        private enum ChangeStyle
        {
            MouseMove,
            RGB,
            HSV,
            None
        }

        #endregion
	}
}
