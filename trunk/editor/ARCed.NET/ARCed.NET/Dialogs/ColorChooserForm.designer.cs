using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Core;

namespace ARCed.Dialogs
{
	public partial class ColorChooserForm 
	{
		private ColorHandler.ARGB _argb;
		private Button btnCancel;
		private Button btnOk;
		private ChangeStyle _changeType = ChangeStyle.None;
		private ColorHandler.HSV _hsv;
		private Label labelSaturation;
		private Label labelValue;
		private Label labelRed;
		private Label labelGreen;
		private Label labelHue;
		private Label labelBlue;
		private Label labelAlpha;
		private ColorWheel myColorWheel;
		private Panel pnlBrightness;
		private Panel pnlColor;
		private Panel pnlSelectedColor;
		private Point selectedPoint;
		private TrackBar tbAlpha;
		private TrackBar tbBlue;
		private TrackBar tbGreen;
		private TextBox tbHexCode;
		private TrackBar tbHue;
		private TrackBar tbRed;
		private TrackBar tbSaturation;
		private TrackBar tbValue;

		#region Windows Form Designer generated code

		/// <summary>
		///   Required method for Designer support - do not modify
		///   the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(ColorChooserForm));
            this.btnCancel = new System.Windows.Forms.Button();
            this.btnOk = new System.Windows.Forms.Button();
            this.tbHexCode = new System.Windows.Forms.TextBox();
            this.labelAlpha = new System.Windows.Forms.Label();
            this.tbAlpha = new System.Windows.Forms.TrackBar();
            this.pnlSelectedColor = new System.Windows.Forms.Panel();
            this.lblAlpha = new System.Windows.Forms.Label();
            this.pnlColor = new System.Windows.Forms.Panel();
            this.pnlBrightness = new System.Windows.Forms.Panel();
            this.buttonCapture = new System.Windows.Forms.Button();
            this.toolTip = new System.Windows.Forms.ToolTip(this.components);
            this.tbBlue = new System.Windows.Forms.TrackBar();
            this.tbGreen = new System.Windows.Forms.TrackBar();
            this.tbRed = new System.Windows.Forms.TrackBar();
            this.tbValue = new System.Windows.Forms.TrackBar();
            this.tbSaturation = new System.Windows.Forms.TrackBar();
            this.tbHue = new System.Windows.Forms.TrackBar();
            this.panelAlpha = new System.Windows.Forms.Panel();
            this.groupBoxRGB = new ARCed.Controls.CollapsibleGroupBox();
            this.labelRed = new System.Windows.Forms.Label();
            this.lblBlue = new System.Windows.Forms.Label();
            this.labelBlue = new System.Windows.Forms.Label();
            this.lblGreen = new System.Windows.Forms.Label();
            this.labelGreen = new System.Windows.Forms.Label();
            this.lblRed = new System.Windows.Forms.Label();
            this.groupBoxHSV = new ARCed.Controls.CollapsibleGroupBox();
            this.labelHue = new System.Windows.Forms.Label();
            this.labelValue = new System.Windows.Forms.Label();
            this.labelSaturation = new System.Windows.Forms.Label();
            this.lblValue = new System.Windows.Forms.Label();
            this.lblSaturation = new System.Windows.Forms.Label();
            this.lblHue = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.tbAlpha)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbBlue)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbGreen)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbRed)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbValue)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbSaturation)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbHue)).BeginInit();
            this.panelAlpha.SuspendLayout();
            this.groupBoxRGB.SuspendLayout();
            this.groupBoxHSV.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnCancel
            // 
            this.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            resources.ApplyResources(this.btnCancel, "btnCancel");
            this.btnCancel.Name = "btnCancel";
            this.toolTip.SetToolTip(this.btnCancel, resources.GetString("btnCancel.ToolTip"));
            // 
            // btnOk
            // 
            this.btnOk.DialogResult = System.Windows.Forms.DialogResult.OK;
            resources.ApplyResources(this.btnOk, "btnOk");
            this.btnOk.Name = "btnOk";
            this.toolTip.SetToolTip(this.btnOk, resources.GetString("btnOk.ToolTip"));
            // 
            // tbHexCode
            // 
            this.tbHexCode.BackColor = System.Drawing.Color.White;
            resources.ApplyResources(this.tbHexCode, "tbHexCode");
            this.tbHexCode.Name = "tbHexCode";
            this.toolTip.SetToolTip(this.tbHexCode, resources.GetString("tbHexCode.ToolTip"));
            this.tbHexCode.MouseDown += new System.Windows.Forms.MouseEventHandler(this.TbHexCodeMouseDown);
            // 
            // labelAlpha
            // 
            resources.ApplyResources(this.labelAlpha, "labelAlpha");
            this.labelAlpha.Name = "labelAlpha";
            // 
            // tbAlpha
            // 
            resources.ApplyResources(this.tbAlpha, "tbAlpha");
            this.tbAlpha.LargeChange = 16;
            this.tbAlpha.Maximum = 255;
            this.tbAlpha.Name = "tbAlpha";
            this.tbAlpha.TickFrequency = 32;
            this.toolTip.SetToolTip(this.tbAlpha, resources.GetString("tbAlpha.ToolTip"));
            this.tbAlpha.Scroll += new System.EventHandler(this.TbAlphaScroll);
            // 
            // pnlSelectedColor
            // 
            this.pnlSelectedColor.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
            resources.ApplyResources(this.pnlSelectedColor, "pnlSelectedColor");
            this.pnlSelectedColor.Name = "pnlSelectedColor";
            this.toolTip.SetToolTip(this.pnlSelectedColor, resources.GetString("pnlSelectedColor.ToolTip"));
            // 
            // lblAlpha
            // 
            resources.ApplyResources(this.lblAlpha, "lblAlpha");
            this.lblAlpha.Name = "lblAlpha";
            // 
            // pnlColor
            // 
            this.pnlColor.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            resources.ApplyResources(this.pnlColor, "pnlColor");
            this.pnlColor.MaximumSize = new System.Drawing.Size(160, 160);
            this.pnlColor.Name = "pnlColor";
            this.toolTip.SetToolTip(this.pnlColor, resources.GetString("pnlColor.ToolTip"));
            // 
            // pnlBrightness
            // 
            this.pnlBrightness.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            resources.ApplyResources(this.pnlBrightness, "pnlBrightness");
            this.pnlBrightness.Name = "pnlBrightness";
            this.toolTip.SetToolTip(this.pnlBrightness, resources.GetString("pnlBrightness.ToolTip"));
            // 
            // buttonCapture
            // 
            resources.ApplyResources(this.buttonCapture, "buttonCapture");
            this.buttonCapture.Name = "buttonCapture";
            this.toolTip.SetToolTip(this.buttonCapture, resources.GetString("buttonCapture.ToolTip"));
            this.buttonCapture.UseVisualStyleBackColor = true;
            this.buttonCapture.Click += new System.EventHandler(this.ButtonCaptureClick);
            // 
            // tbBlue
            // 
            resources.ApplyResources(this.tbBlue, "tbBlue");
            this.tbBlue.LargeChange = 16;
            this.tbBlue.Maximum = 255;
            this.tbBlue.Name = "tbBlue";
            this.tbBlue.TickFrequency = 32;
            this.toolTip.SetToolTip(this.tbBlue, resources.GetString("tbBlue.ToolTip"));
            this.tbBlue.Scroll += new System.EventHandler(this.HandleRGBScroll);
            // 
            // tbGreen
            // 
            resources.ApplyResources(this.tbGreen, "tbGreen");
            this.tbGreen.LargeChange = 16;
            this.tbGreen.Maximum = 255;
            this.tbGreen.Name = "tbGreen";
            this.tbGreen.TickFrequency = 32;
            this.toolTip.SetToolTip(this.tbGreen, resources.GetString("tbGreen.ToolTip"));
            this.tbGreen.Scroll += new System.EventHandler(this.HandleRGBScroll);
            // 
            // tbRed
            // 
            resources.ApplyResources(this.tbRed, "tbRed");
            this.tbRed.LargeChange = 16;
            this.tbRed.Maximum = 255;
            this.tbRed.Name = "tbRed";
            this.tbRed.TickFrequency = 32;
            this.toolTip.SetToolTip(this.tbRed, resources.GetString("tbRed.ToolTip"));
            this.tbRed.Scroll += new System.EventHandler(this.HandleRGBScroll);
            // 
            // tbValue
            // 
            resources.ApplyResources(this.tbValue, "tbValue");
            this.tbValue.LargeChange = 16;
            this.tbValue.Maximum = 255;
            this.tbValue.Name = "tbValue";
            this.tbValue.TickFrequency = 32;
            this.toolTip.SetToolTip(this.tbValue, resources.GetString("tbValue.ToolTip"));
            this.tbValue.Scroll += new System.EventHandler(this.HandleHSVScroll);
            // 
            // tbSaturation
            // 
            resources.ApplyResources(this.tbSaturation, "tbSaturation");
            this.tbSaturation.LargeChange = 16;
            this.tbSaturation.Maximum = 255;
            this.tbSaturation.Name = "tbSaturation";
            this.tbSaturation.TickFrequency = 32;
            this.toolTip.SetToolTip(this.tbSaturation, resources.GetString("tbSaturation.ToolTip"));
            this.tbSaturation.Scroll += new System.EventHandler(this.HandleHSVScroll);
            // 
            // tbHue
            // 
            resources.ApplyResources(this.tbHue, "tbHue");
            this.tbHue.LargeChange = 16;
            this.tbHue.Maximum = 255;
            this.tbHue.Name = "tbHue";
            this.tbHue.TickFrequency = 32;
            this.toolTip.SetToolTip(this.tbHue, resources.GetString("tbHue.ToolTip"));
            this.tbHue.Scroll += new System.EventHandler(this.HandleHSVScroll);
            // 
            // panelAlpha
            // 
            resources.ApplyResources(this.panelAlpha, "panelAlpha");
            this.panelAlpha.Controls.Add(this.labelAlpha);
            this.panelAlpha.Controls.Add(this.tbAlpha);
            this.panelAlpha.Controls.Add(this.lblAlpha);
            this.panelAlpha.Name = "panelAlpha";
            // 
            // groupBoxRGB
            // 
            resources.ApplyResources(this.groupBoxRGB, "groupBoxRGB");
            this.groupBoxRGB.Controls.Add(this.labelRed);
            this.groupBoxRGB.Controls.Add(this.lblBlue);
            this.groupBoxRGB.Controls.Add(this.labelBlue);
            this.groupBoxRGB.Controls.Add(this.lblGreen);
            this.groupBoxRGB.Controls.Add(this.labelGreen);
            this.groupBoxRGB.Controls.Add(this.lblRed);
            this.groupBoxRGB.Controls.Add(this.tbBlue);
            this.groupBoxRGB.Controls.Add(this.tbGreen);
            this.groupBoxRGB.Controls.Add(this.tbRed);
            this.groupBoxRGB.Name = "groupBoxRGB";
            this.groupBoxRGB.TabStop = false;
            this.groupBoxRGB.CollapseBoxClickedEvent += new ARCed.Controls.CollapsibleGroupBox.CollapseBoxClickedEventHandler(this.GroupBoxRGBCollapseBoxClickedEvent);
            // 
            // labelRed
            // 
            resources.ApplyResources(this.labelRed, "labelRed");
            this.labelRed.ForeColor = System.Drawing.Color.Red;
            this.labelRed.Name = "labelRed";
            // 
            // lblBlue
            // 
            resources.ApplyResources(this.lblBlue, "lblBlue");
            this.lblBlue.Name = "lblBlue";
            // 
            // labelBlue
            // 
            resources.ApplyResources(this.labelBlue, "labelBlue");
            this.labelBlue.ForeColor = System.Drawing.Color.Blue;
            this.labelBlue.Name = "labelBlue";
            // 
            // lblGreen
            // 
            resources.ApplyResources(this.lblGreen, "lblGreen");
            this.lblGreen.Name = "lblGreen";
            // 
            // labelGreen
            // 
            resources.ApplyResources(this.labelGreen, "labelGreen");
            this.labelGreen.ForeColor = System.Drawing.Color.Green;
            this.labelGreen.Name = "labelGreen";
            // 
            // lblRed
            // 
            resources.ApplyResources(this.lblRed, "lblRed");
            this.lblRed.Name = "lblRed";
            // 
            // groupBoxHSV
            // 
            resources.ApplyResources(this.groupBoxHSV, "groupBoxHSV");
            this.groupBoxHSV.Controls.Add(this.labelHue);
            this.groupBoxHSV.Controls.Add(this.labelValue);
            this.groupBoxHSV.Controls.Add(this.labelSaturation);
            this.groupBoxHSV.Controls.Add(this.tbValue);
            this.groupBoxHSV.Controls.Add(this.lblValue);
            this.groupBoxHSV.Controls.Add(this.tbSaturation);
            this.groupBoxHSV.Controls.Add(this.lblSaturation);
            this.groupBoxHSV.Controls.Add(this.tbHue);
            this.groupBoxHSV.Controls.Add(this.lblHue);
            this.groupBoxHSV.Name = "groupBoxHSV";
            this.groupBoxHSV.TabStop = false;
            this.groupBoxHSV.CollapseBoxClickedEvent += new ARCed.Controls.CollapsibleGroupBox.CollapseBoxClickedEventHandler(this.GroupBoxHSVCollapseBoxClickedEvent);
            // 
            // labelHue
            // 
            resources.ApplyResources(this.labelHue, "labelHue");
            this.labelHue.Name = "labelHue";
            // 
            // labelValue
            // 
            resources.ApplyResources(this.labelValue, "labelValue");
            this.labelValue.Name = "labelValue";
            // 
            // labelSaturation
            // 
            resources.ApplyResources(this.labelSaturation, "labelSaturation");
            this.labelSaturation.Name = "labelSaturation";
            // 
            // lblValue
            // 
            resources.ApplyResources(this.lblValue, "lblValue");
            this.lblValue.Name = "lblValue";
            // 
            // lblSaturation
            // 
            resources.ApplyResources(this.lblSaturation, "lblSaturation");
            this.lblSaturation.Name = "lblSaturation";
            // 
            // lblHue
            // 
            resources.ApplyResources(this.lblHue, "lblHue");
            this.lblHue.Name = "lblHue";
            // 
            // ColorChooserForm
            // 
            this.AcceptButton = this.btnOk;
            this.AccessibleRole = System.Windows.Forms.AccessibleRole.Dialog;
            resources.ApplyResources(this, "$this");
            this.CancelButton = this.btnCancel;
            this.Controls.Add(this.groupBoxRGB);
            this.Controls.Add(this.groupBoxHSV);
            this.Controls.Add(this.buttonCapture);
            this.Controls.Add(this.pnlBrightness);
            this.Controls.Add(this.tbHexCode);
            this.Controls.Add(this.btnCancel);
            this.Controls.Add(this.btnOk);
            this.Controls.Add(this.pnlSelectedColor);
            this.Controls.Add(this.pnlColor);
            this.Controls.Add(this.panelAlpha);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "ColorChooserForm";
            this.ShowIcon = false;
            this.ShowInTaskbar = false;
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.Load += new System.EventHandler(this.ColorChooserLoad);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.ColorChooserPaint);
            this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.HandleMouse);
            this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.HandleMouse);
            this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.FormMainMouseUp);
            ((System.ComponentModel.ISupportInitialize)(this.tbAlpha)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbBlue)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbGreen)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbRed)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbValue)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbSaturation)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.tbHue)).EndInit();
            this.panelAlpha.ResumeLayout(false);
            this.panelAlpha.PerformLayout();
            this.groupBoxRGB.ResumeLayout(false);
            this.groupBoxRGB.PerformLayout();
            this.groupBoxHSV.ResumeLayout(false);
            this.groupBoxHSV.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

		}
		#endregion

		private ARCed.Controls.CollapsibleGroupBox groupBoxRGB;
		private ARCed.Controls.CollapsibleGroupBox groupBoxHSV;
		private Label lblBlue;
		private Label lblGreen;
		private Label lblRed;
		private Label lblValue;
		private Label lblSaturation;
		private Label lblHue;
		private Label lblAlpha;
		private Button buttonCapture;
		private ToolTip toolTip;
		private IContainer components;
		private Panel panelAlpha;
	}
}