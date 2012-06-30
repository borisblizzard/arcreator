using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Data;

namespace ARCed.Dialogs
{
	public partial class ColorChooserForm : Form
	{
		private ColorHandler.ARGB argb;
		private Button btnCancel;
		private Button btnOk;
		private ChangeStyle changeType = ChangeStyle.None;
		private ColorHandler.HSV hsv;
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
			this.panelAlpha = new System.Windows.Forms.Panel();
			this.groupBoxRGB = new ARCed.Controls.CollapsibleGroupBox();
			this.labelRed = new System.Windows.Forms.Label();
			this.lblBlue = new System.Windows.Forms.Label();
			this.labelBlue = new System.Windows.Forms.Label();
			this.lblGreen = new System.Windows.Forms.Label();
			this.labelGreen = new System.Windows.Forms.Label();
			this.lblRed = new System.Windows.Forms.Label();
			this.tbBlue = new System.Windows.Forms.TrackBar();
			this.tbGreen = new System.Windows.Forms.TrackBar();
			this.tbRed = new System.Windows.Forms.TrackBar();
			this.groupBoxHSV = new ARCed.Controls.CollapsibleGroupBox();
			this.labelHue = new System.Windows.Forms.Label();
			this.labelValue = new System.Windows.Forms.Label();
			this.labelSaturation = new System.Windows.Forms.Label();
			this.tbValue = new System.Windows.Forms.TrackBar();
			this.lblValue = new System.Windows.Forms.Label();
			this.tbSaturation = new System.Windows.Forms.TrackBar();
			this.lblSaturation = new System.Windows.Forms.Label();
			this.tbHue = new System.Windows.Forms.TrackBar();
			this.lblHue = new System.Windows.Forms.Label();
			((System.ComponentModel.ISupportInitialize)(this.tbAlpha)).BeginInit();
			this.panelAlpha.SuspendLayout();
			this.groupBoxRGB.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.tbBlue)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.tbGreen)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.tbRed)).BeginInit();
			this.groupBoxHSV.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.tbValue)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.tbSaturation)).BeginInit();
			((System.ComponentModel.ISupportInitialize)(this.tbHue)).BeginInit();
			this.SuspendLayout();
			// 
			// btnCancel
			// 
			this.btnCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.btnCancel.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.btnCancel.Location = new System.Drawing.Point(208, 118);
			this.btnCancel.Name = "btnCancel";
			this.btnCancel.Size = new System.Drawing.Size(72, 23);
			this.btnCancel.TabIndex = 42;
			this.btnCancel.Text = "Cancel";
			this.toolTip.SetToolTip(this.btnCancel, "Cancel and close");
			// 
			// btnOk
			// 
			this.btnOk.DialogResult = System.Windows.Forms.DialogResult.OK;
			this.btnOk.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.btnOk.Location = new System.Drawing.Point(208, 149);
			this.btnOk.Name = "btnOk";
			this.btnOk.Size = new System.Drawing.Size(72, 23);
			this.btnOk.TabIndex = 41;
			this.btnOk.Text = "OK";
			this.toolTip.SetToolTip(this.btnOk, "Confirm");
			// 
			// tbHexCode
			// 
			this.tbHexCode.BackColor = System.Drawing.Color.White;
			this.tbHexCode.Font = new System.Drawing.Font("Courier New", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.tbHexCode.Location = new System.Drawing.Point(208, 42);
			this.tbHexCode.MaxLength = 8;
			this.tbHexCode.Name = "tbHexCode";
			this.tbHexCode.Size = new System.Drawing.Size(71, 20);
			this.tbHexCode.TabIndex = 58;
			this.toolTip.SetToolTip(this.tbHexCode, "Hex value");
			this.tbHexCode.MouseDown += new System.Windows.Forms.MouseEventHandler(this.TbHexCodeMouseDown);
			// 
			// labelAlpha
			// 
			this.labelAlpha.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.labelAlpha.AutoSize = true;
			this.labelAlpha.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelAlpha.Location = new System.Drawing.Point(9, 8);
			this.labelAlpha.Margin = new System.Windows.Forms.Padding(3, 8, 3, 0);
			this.labelAlpha.Name = "labelAlpha";
			this.labelAlpha.Size = new System.Drawing.Size(19, 13);
			this.labelAlpha.TabIndex = 55;
			this.labelAlpha.Text = "A:";
			this.labelAlpha.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// tbAlpha
			// 
			this.tbAlpha.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.tbAlpha.AutoSize = false;
			this.tbAlpha.LargeChange = 16;
			this.tbAlpha.Location = new System.Drawing.Point(31, 3);
			this.tbAlpha.Margin = new System.Windows.Forms.Padding(0, 3, 3, 0);
			this.tbAlpha.Maximum = 255;
			this.tbAlpha.Name = "tbAlpha";
			this.tbAlpha.Size = new System.Drawing.Size(207, 32);
			this.tbAlpha.TabIndex = 56;
			this.tbAlpha.TickFrequency = 32;
			this.toolTip.SetToolTip(this.tbAlpha, "Alpha");
			this.tbAlpha.Scroll += new System.EventHandler(this.TbAlphaScroll);
			// 
			// pnlSelectedColor
			// 
			this.pnlSelectedColor.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))), ((int)(((byte)(0)))));
			this.pnlSelectedColor.Location = new System.Drawing.Point(208, 12);
			this.pnlSelectedColor.Name = "pnlSelectedColor";
			this.pnlSelectedColor.Size = new System.Drawing.Size(72, 24);
			this.pnlSelectedColor.TabIndex = 40;
			this.toolTip.SetToolTip(this.pnlSelectedColor, "Selected color");
			this.pnlSelectedColor.Visible = false;
			// 
			// lblAlpha
			// 
			this.lblAlpha.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.lblAlpha.AutoSize = true;
			this.lblAlpha.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblAlpha.Location = new System.Drawing.Point(243, 8);
			this.lblAlpha.Name = "lblAlpha";
			this.lblAlpha.Size = new System.Drawing.Size(25, 13);
			this.lblAlpha.TabIndex = 57;
			this.lblAlpha.Text = "000";
			this.lblAlpha.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// pnlColor
			// 
			this.pnlColor.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
			this.pnlColor.Location = new System.Drawing.Point(12, 12);
			this.pnlColor.MaximumSize = new System.Drawing.Size(160, 160);
			this.pnlColor.Name = "pnlColor";
			this.pnlColor.Size = new System.Drawing.Size(160, 160);
			this.pnlColor.TabIndex = 38;
			this.toolTip.SetToolTip(this.pnlColor, "Select color");
			this.pnlColor.Visible = false;
			// 
			// pnlBrightness
			// 
			this.pnlBrightness.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
			this.pnlBrightness.Location = new System.Drawing.Point(178, 12);
			this.pnlBrightness.Name = "pnlBrightness";
			this.pnlBrightness.Size = new System.Drawing.Size(16, 160);
			this.pnlBrightness.TabIndex = 39;
			this.toolTip.SetToolTip(this.pnlBrightness, "Value");
			this.pnlBrightness.Visible = false;
			// 
			// buttonCapture
			// 
			this.buttonCapture.Location = new System.Drawing.Point(207, 70);
			this.buttonCapture.Name = "buttonCapture";
			this.buttonCapture.Size = new System.Drawing.Size(72, 23);
			this.buttonCapture.TabIndex = 63;
			this.buttonCapture.Text = "Capture";
			this.toolTip.SetToolTip(this.buttonCapture, "Capture color on screen");
			this.buttonCapture.UseVisualStyleBackColor = true;
			this.buttonCapture.Click += new System.EventHandler(this.buttonCapture_Click);
			// 
			// panelAlpha
			// 
			this.panelAlpha.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.panelAlpha.Controls.Add(this.labelAlpha);
			this.panelAlpha.Controls.Add(this.tbAlpha);
			this.panelAlpha.Controls.Add(this.lblAlpha);
			this.panelAlpha.Location = new System.Drawing.Point(5, 406);
			this.panelAlpha.Name = "panelAlpha";
			this.panelAlpha.Size = new System.Drawing.Size(274, 40);
			this.panelAlpha.TabIndex = 64;
			// 
			// groupBoxRGB
			// 
			this.groupBoxRGB.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxRGB.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
			this.groupBoxRGB.Controls.Add(this.labelRed);
			this.groupBoxRGB.Controls.Add(this.lblBlue);
			this.groupBoxRGB.Controls.Add(this.labelBlue);
			this.groupBoxRGB.Controls.Add(this.lblGreen);
			this.groupBoxRGB.Controls.Add(this.labelGreen);
			this.groupBoxRGB.Controls.Add(this.lblRed);
			this.groupBoxRGB.Controls.Add(this.tbBlue);
			this.groupBoxRGB.Controls.Add(this.tbGreen);
			this.groupBoxRGB.Controls.Add(this.tbRed);
			this.groupBoxRGB.Location = new System.Drawing.Point(5, 178);
			this.groupBoxRGB.Name = "groupBoxRGB";
			this.groupBoxRGB.Size = new System.Drawing.Size(274, 108);
			this.groupBoxRGB.TabIndex = 61;
			this.groupBoxRGB.TabStop = false;
			this.groupBoxRGB.Text = "RGB";
			this.groupBoxRGB.CollapseBoxClickedEvent += new ARCed.Controls.CollapsibleGroupBox.CollapseBoxClickedEventHandler(this.groupBoxRGB_CollapseBoxClickedEvent);
			// 
			// labelRed
			// 
			this.labelRed.AutoSize = true;
			this.labelRed.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelRed.ForeColor = System.Drawing.Color.Red;
			this.labelRed.Location = new System.Drawing.Point(7, 23);
			this.labelRed.Margin = new System.Windows.Forms.Padding(3, 8, 3, 0);
			this.labelRed.Name = "labelRed";
			this.labelRed.Size = new System.Drawing.Size(20, 13);
			this.labelRed.TabIndex = 42;
			this.labelRed.Text = "R:";
			this.labelRed.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// lblBlue
			// 
			this.lblBlue.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.lblBlue.AutoSize = true;
			this.lblBlue.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblBlue.Location = new System.Drawing.Point(243, 75);
			this.lblBlue.Name = "lblBlue";
			this.lblBlue.Size = new System.Drawing.Size(25, 13);
			this.lblBlue.TabIndex = 54;
			this.lblBlue.Text = "000";
			this.lblBlue.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// labelBlue
			// 
			this.labelBlue.AutoSize = true;
			this.labelBlue.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelBlue.ForeColor = System.Drawing.Color.Blue;
			this.labelBlue.Location = new System.Drawing.Point(7, 75);
			this.labelBlue.Margin = new System.Windows.Forms.Padding(3, 8, 3, 0);
			this.labelBlue.Name = "labelBlue";
			this.labelBlue.Size = new System.Drawing.Size(19, 13);
			this.labelBlue.TabIndex = 46;
			this.labelBlue.Text = "B:";
			this.labelBlue.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// lblGreen
			// 
			this.lblGreen.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.lblGreen.AutoSize = true;
			this.lblGreen.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblGreen.Location = new System.Drawing.Point(243, 49);
			this.lblGreen.Name = "lblGreen";
			this.lblGreen.Size = new System.Drawing.Size(25, 13);
			this.lblGreen.TabIndex = 53;
			this.lblGreen.Text = "000";
			this.lblGreen.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// labelGreen
			// 
			this.labelGreen.AutoSize = true;
			this.labelGreen.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelGreen.ForeColor = System.Drawing.Color.Green;
			this.labelGreen.Location = new System.Drawing.Point(7, 49);
			this.labelGreen.Margin = new System.Windows.Forms.Padding(3, 8, 3, 0);
			this.labelGreen.Name = "labelGreen";
			this.labelGreen.Size = new System.Drawing.Size(20, 13);
			this.labelGreen.TabIndex = 44;
			this.labelGreen.Text = "G:";
			this.labelGreen.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// lblRed
			// 
			this.lblRed.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.lblRed.AutoSize = true;
			this.lblRed.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblRed.Location = new System.Drawing.Point(243, 23);
			this.lblRed.Name = "lblRed";
			this.lblRed.Size = new System.Drawing.Size(25, 13);
			this.lblRed.TabIndex = 52;
			this.lblRed.Text = "000";
			this.lblRed.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// tbBlue
			// 
			this.tbBlue.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.tbBlue.AutoSize = false;
			this.tbBlue.LargeChange = 16;
			this.tbBlue.Location = new System.Drawing.Point(29, 70);
			this.tbBlue.Margin = new System.Windows.Forms.Padding(0, 3, 3, 6);
			this.tbBlue.Maximum = 255;
			this.tbBlue.Name = "tbBlue";
			this.tbBlue.Size = new System.Drawing.Size(208, 32);
			this.tbBlue.TabIndex = 47;
			this.tbBlue.TickFrequency = 32;
			this.toolTip.SetToolTip(this.tbBlue, "Blue");
			this.tbBlue.Scroll += new System.EventHandler(this.HandleRGBScroll);
			// 
			// tbGreen
			// 
			this.tbGreen.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.tbGreen.AutoSize = false;
			this.tbGreen.LargeChange = 16;
			this.tbGreen.Location = new System.Drawing.Point(30, 44);
			this.tbGreen.Margin = new System.Windows.Forms.Padding(0, 3, 3, 0);
			this.tbGreen.Maximum = 255;
			this.tbGreen.Name = "tbGreen";
			this.tbGreen.Size = new System.Drawing.Size(207, 32);
			this.tbGreen.TabIndex = 45;
			this.tbGreen.TickFrequency = 32;
			this.toolTip.SetToolTip(this.tbGreen, "Green");
			this.tbGreen.Scroll += new System.EventHandler(this.HandleRGBScroll);
			// 
			// tbRed
			// 
			this.tbRed.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.tbRed.AutoSize = false;
			this.tbRed.LargeChange = 16;
			this.tbRed.Location = new System.Drawing.Point(30, 18);
			this.tbRed.Margin = new System.Windows.Forms.Padding(0, 3, 3, 0);
			this.tbRed.Maximum = 255;
			this.tbRed.Name = "tbRed";
			this.tbRed.Size = new System.Drawing.Size(207, 32);
			this.tbRed.TabIndex = 43;
			this.tbRed.TickFrequency = 32;
			this.toolTip.SetToolTip(this.tbRed, "Red");
			this.tbRed.Scroll += new System.EventHandler(this.HandleRGBScroll);
			// 
			// groupBoxHSV
			// 
			this.groupBoxHSV.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxHSV.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
			this.groupBoxHSV.Controls.Add(this.labelHue);
			this.groupBoxHSV.Controls.Add(this.labelValue);
			this.groupBoxHSV.Controls.Add(this.labelSaturation);
			this.groupBoxHSV.Controls.Add(this.tbValue);
			this.groupBoxHSV.Controls.Add(this.lblValue);
			this.groupBoxHSV.Controls.Add(this.tbSaturation);
			this.groupBoxHSV.Controls.Add(this.lblSaturation);
			this.groupBoxHSV.Controls.Add(this.tbHue);
			this.groupBoxHSV.Controls.Add(this.lblHue);
			this.groupBoxHSV.Location = new System.Drawing.Point(5, 292);
			this.groupBoxHSV.Name = "groupBoxHSV";
			this.groupBoxHSV.Size = new System.Drawing.Size(275, 108);
			this.groupBoxHSV.TabIndex = 62;
			this.groupBoxHSV.TabStop = false;
			this.groupBoxHSV.Text = "HSV";
			this.groupBoxHSV.CollapseBoxClickedEvent += new ARCed.Controls.CollapsibleGroupBox.CollapseBoxClickedEventHandler(this.groupBoxHSV_CollapseBoxClickedEvent);
			// 
			// labelHue
			// 
			this.labelHue.AutoSize = true;
			this.labelHue.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelHue.Location = new System.Drawing.Point(7, 24);
			this.labelHue.Margin = new System.Windows.Forms.Padding(3, 8, 3, 0);
			this.labelHue.Name = "labelHue";
			this.labelHue.Size = new System.Drawing.Size(20, 13);
			this.labelHue.TabIndex = 35;
			this.labelHue.Text = "H:";
			this.labelHue.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// labelValue
			// 
			this.labelValue.AutoSize = true;
			this.labelValue.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelValue.Location = new System.Drawing.Point(9, 74);
			this.labelValue.Margin = new System.Windows.Forms.Padding(3, 8, 3, 0);
			this.labelValue.Name = "labelValue";
			this.labelValue.Size = new System.Drawing.Size(19, 13);
			this.labelValue.TabIndex = 40;
			this.labelValue.Text = "V:";
			this.labelValue.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// labelSaturation
			// 
			this.labelSaturation.AutoSize = true;
			this.labelSaturation.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.labelSaturation.Location = new System.Drawing.Point(8, 48);
			this.labelSaturation.Margin = new System.Windows.Forms.Padding(3, 8, 3, 0);
			this.labelSaturation.Name = "labelSaturation";
			this.labelSaturation.Size = new System.Drawing.Size(19, 13);
			this.labelSaturation.TabIndex = 38;
			this.labelSaturation.Text = "S:";
			this.labelSaturation.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
			// 
			// tbValue
			// 
			this.tbValue.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.tbValue.AutoSize = false;
			this.tbValue.LargeChange = 16;
			this.tbValue.Location = new System.Drawing.Point(31, 74);
			this.tbValue.Margin = new System.Windows.Forms.Padding(0, 3, 3, 6);
			this.tbValue.Maximum = 255;
			this.tbValue.Name = "tbValue";
			this.tbValue.Size = new System.Drawing.Size(207, 32);
			this.tbValue.TabIndex = 41;
			this.tbValue.TickFrequency = 32;
			this.toolTip.SetToolTip(this.tbValue, "Value");
			this.tbValue.Scroll += new System.EventHandler(this.HandleHSVScroll);
			// 
			// lblValue
			// 
			this.lblValue.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.lblValue.AutoSize = true;
			this.lblValue.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblValue.Location = new System.Drawing.Point(244, 74);
			this.lblValue.Name = "lblValue";
			this.lblValue.Size = new System.Drawing.Size(25, 13);
			this.lblValue.TabIndex = 51;
			this.lblValue.Text = "000";
			this.lblValue.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// tbSaturation
			// 
			this.tbSaturation.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.tbSaturation.AutoSize = false;
			this.tbSaturation.LargeChange = 16;
			this.tbSaturation.Location = new System.Drawing.Point(31, 48);
			this.tbSaturation.Margin = new System.Windows.Forms.Padding(0, 3, 3, 0);
			this.tbSaturation.Maximum = 255;
			this.tbSaturation.Name = "tbSaturation";
			this.tbSaturation.Size = new System.Drawing.Size(207, 32);
			this.tbSaturation.TabIndex = 39;
			this.tbSaturation.TickFrequency = 32;
			this.toolTip.SetToolTip(this.tbSaturation, "Saturation");
			this.tbSaturation.Scroll += new System.EventHandler(this.HandleHSVScroll);
			// 
			// lblSaturation
			// 
			this.lblSaturation.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.lblSaturation.AutoSize = true;
			this.lblSaturation.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblSaturation.Location = new System.Drawing.Point(244, 48);
			this.lblSaturation.Name = "lblSaturation";
			this.lblSaturation.Size = new System.Drawing.Size(25, 13);
			this.lblSaturation.TabIndex = 50;
			this.lblSaturation.Text = "000";
			this.lblSaturation.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// tbHue
			// 
			this.tbHue.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.tbHue.AutoSize = false;
			this.tbHue.LargeChange = 16;
			this.tbHue.Location = new System.Drawing.Point(30, 22);
			this.tbHue.Margin = new System.Windows.Forms.Padding(0, 3, 3, 0);
			this.tbHue.Maximum = 255;
			this.tbHue.Name = "tbHue";
			this.tbHue.Size = new System.Drawing.Size(208, 32);
			this.tbHue.TabIndex = 36;
			this.tbHue.TickFrequency = 32;
			this.toolTip.SetToolTip(this.tbHue, "Hue");
			this.tbHue.Scroll += new System.EventHandler(this.HandleHSVScroll);
			// 
			// lblHue
			// 
			this.lblHue.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.lblHue.AutoSize = true;
			this.lblHue.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblHue.Location = new System.Drawing.Point(244, 24);
			this.lblHue.Margin = new System.Windows.Forms.Padding(3, 8, 3, 0);
			this.lblHue.Name = "lblHue";
			this.lblHue.Size = new System.Drawing.Size(25, 13);
			this.lblHue.TabIndex = 49;
			this.lblHue.Text = "000";
			this.lblHue.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// ColorChooserForm
			// 
			this.AcceptButton = this.btnOk;
			this.AccessibleRole = System.Windows.Forms.AccessibleRole.Dialog;
			this.AutoScaleBaseSize = new System.Drawing.Size(5, 13);
			this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
			this.CancelButton = this.btnCancel;
			this.ClientSize = new System.Drawing.Size(288, 447);
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
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "Choose Color";
			this.Load += new System.EventHandler(this.ColorChooserLoad);
			this.Paint += new System.Windows.Forms.PaintEventHandler(this.ColorChooserPaint);
			this.MouseDown += new System.Windows.Forms.MouseEventHandler(this.HandleMouse);
			this.MouseMove += new System.Windows.Forms.MouseEventHandler(this.HandleMouse);
			this.MouseUp += new System.Windows.Forms.MouseEventHandler(this.FormMainMouseUp);
			((System.ComponentModel.ISupportInitialize)(this.tbAlpha)).EndInit();
			this.panelAlpha.ResumeLayout(false);
			this.panelAlpha.PerformLayout();
			this.groupBoxRGB.ResumeLayout(false);
			this.groupBoxRGB.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.tbBlue)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.tbGreen)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.tbRed)).EndInit();
			this.groupBoxHSV.ResumeLayout(false);
			this.groupBoxHSV.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.tbValue)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.tbSaturation)).EndInit();
			((System.ComponentModel.ISupportInitialize)(this.tbHue)).EndInit();
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