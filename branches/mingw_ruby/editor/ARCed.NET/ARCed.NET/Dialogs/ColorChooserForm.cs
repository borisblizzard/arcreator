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
            get { return this.panelAlpha.Enabled; }
            set
            {
                this.panelAlpha.Enabled = value;
            }
        }

        /// <summary>
        /// Gets or sets the selected <see cref="Color"/> of the form.
        /// </summary>
        public Color Color
        {
            get { return this.myColorWheel.Color; }
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
			this.InitializeComponent();
		}

        #endregion

        #region Private Methods

        private void ColorChooserLoad(object sender, EventArgs e)
		{
			SetStyle(ControlStyles.AllPaintingInWmPaint, true);
			SetStyle(ControlStyles.UserPaint, true);
			SetStyle(ControlStyles.DoubleBuffer, true);
			this.pnlSelectedColor.Visible = false;
			this.pnlBrightness.Visible = false;
			this.pnlColor.Visible = false;
			var selectedColorRectangle = new Rectangle(this.pnlSelectedColor.Location, this.pnlSelectedColor.Size);
			var brightnessRectangle = new Rectangle(this.pnlBrightness.Location, this.pnlBrightness.Size);
			var colorRectangle = new Rectangle(this.pnlColor.Location, this.pnlColor.Size);
			this.myColorWheel = new ColorWheel(colorRectangle, brightnessRectangle, selectedColorRectangle);
			this.myColorWheel.ColorChanged += this.MyColorWheelColorChanged;
			if (!this.panelAlpha.Enabled)
			{
				if (this.Color.A != 255)
					this.Color = Color.FromArgb(255, this.Color);
			}
			this.SetRGB(this._argb);
			this.SetHSV(this._hsv);
			this.SetRGBLabels(this._argb);
			this.SetHSVLabels(this._hsv);
		}

		private void HandleMouse(object sender, MouseEventArgs e)
		{
			if (e.Button != MouseButtons.Left)
				return;
			this._changeType = ChangeStyle.MouseMove;
			this.selectedPoint = new Point(e.X, e.Y);
			Invalidate();
		}

		private void FormMainMouseUp(object sender, MouseEventArgs e)
		{
			this.myColorWheel.SetMouseUp();
			this._changeType = ChangeStyle.None;
		}

		private void SetRGBLabels(ColorHandler.ARGB argb)
		{
			RefreshText(this.lblRed, argb.Red);
			RefreshText(this.lblBlue, argb.Blue);
			RefreshText(this.lblGreen, argb.Green);
			RefreshText(this.lblAlpha, argb.Alpha);
			this.tbHexCode.Text = string.Format("{0:X2}{1:X2}{2:X2}{3:X2}", argb.Alpha, argb.Red, argb.Green, argb.Blue);
		}

		private void SetHSVLabels(ColorHandler.HSV hsv)
		{
			RefreshText(this.lblHue, hsv.Hue);
			RefreshText(this.lblSaturation, hsv.Saturation);
			RefreshText(this.lblValue, hsv.Value);
			RefreshText(this.lblAlpha, hsv.Alpha);
		}

		private void SetRGB(ColorHandler.ARGB argb)
		{
			RefreshValue(this.tbRed, argb.Red);
			RefreshValue(this.tbBlue, argb.Blue);
			RefreshValue(this.tbGreen, argb.Green);
			RefreshValue(this.tbAlpha, argb.Alpha);
			this.SetRGBLabels(argb);
		}

		private void SetHSV(ColorHandler.HSV hsv)
		{
			RefreshValue(this.tbHue, hsv.Hue);
			RefreshValue(this.tbSaturation, hsv.Saturation);
			RefreshValue(this.tbValue, hsv.Value);
			RefreshValue(this.tbAlpha, hsv.Alpha);
			this.SetHSVLabels(hsv);
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
			this.SetRGB(e.ARGB);
			this.SetHSV(e.HSV);
		}

		private void HandleHSVScroll(object sender, EventArgs e)
		{
			this._changeType = ChangeStyle.HSV;
			this._hsv = new ColorHandler.HSV(this.tbAlpha.Value, this.tbHue.Value, this.tbSaturation.Value, this.tbValue.Value);
			this.SetRGB(ColorHandler.HSVtoRGB(this._hsv));
			this.SetHSVLabels(this._hsv);
			Invalidate();
		}

		private void HandleRGBScroll(object sender, EventArgs e)
		{
			this._changeType = ChangeStyle.RGB;
			this._argb = new ColorHandler.ARGB(this.tbAlpha.Value, this.tbRed.Value, this.tbGreen.Value, this.tbBlue.Value);
			this.SetHSV(ColorHandler.RGBtoHSV(this._argb));
			this.SetRGBLabels(this._argb);
			Invalidate();
		}

		private void TbAlphaScroll(object sender, EventArgs e)
		{
			this._changeType = ChangeStyle.RGB;
			this._argb = new ColorHandler.ARGB(this.tbAlpha.Value, this.tbRed.Value, this.tbGreen.Value, this.tbBlue.Value);
			RefreshText(this.lblAlpha, this.tbAlpha.Value);
			this.tbHexCode.Text = string.Format("{0:X2}{1:X2}{2:X2}{3:X2}", this._argb.Alpha, this._argb.Red, this._argb.Green, this._argb.Blue);
			Invalidate();
		}

		private void ColorChooserPaint(object sender, PaintEventArgs e)
		{
			switch (this._changeType)
			{
				case ChangeStyle.HSV:
					this.myColorWheel.Draw(e.Graphics, this._hsv);
					break;
				case ChangeStyle.MouseMove:
				case ChangeStyle.None:
					this.myColorWheel.Draw(e.Graphics, this.selectedPoint);
					break;
				case ChangeStyle.RGB:
					this.myColorWheel.Draw(e.Graphics, this._argb);
					break;
			}
		}

		private void TbHexCodeMouseDown(object sender, MouseEventArgs e)
		{
			this.tbHexCode.SelectionStart = 0;
			this.tbHexCode.SelectionLength = this.tbHexCode.Text.Length;
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
				this.SetRGBLabels(this._argb);
				this.SetHSVLabels(this._hsv);
				this.SetRGB(this._argb);
				this.SetHSV(this._hsv);
			}
			Editor.MainInstance.Visible = true;
			Visible = true;
		}

		private void GroupBoxRGBCollapseBoxClickedEvent(object sender)
		{
			int y = (this.groupBoxRGB.FullHeight - this.groupBoxRGB.CollapsedHeight);
			if (this.groupBoxRGB.IsCollapsed) y *= -1;
			Size = new Size(Width, Height + y);
			this.groupBoxHSV.Location = new Point(this.groupBoxHSV.Location.X,
				this.groupBoxHSV.Location.Y + y);
			this.panelAlpha.Location = new Point(this.panelAlpha.Location.X,
				this.panelAlpha.Location.Y + y);
		}

		private void GroupBoxHSVCollapseBoxClickedEvent(object sender)
		{
			int y = (this.groupBoxHSV.FullHeight - this.groupBoxHSV.CollapsedHeight);
			if (this.groupBoxHSV.IsCollapsed) y *= -1;
			Size = new Size(Width, Height + y);
			this.panelAlpha.Location = new Point(this.panelAlpha.Location.X,
				this.panelAlpha.Location.Y + y);
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
