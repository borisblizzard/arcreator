namespace ARCed.Forms
{
    partial class CalculatorForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
			this.components = new System.ComponentModel.Container();
			this.buttonZero = new System.Windows.Forms.Button();
			this.buttonDecimal = new System.Windows.Forms.Button();
			this.buttonAddition = new System.Windows.Forms.Button();
			this.buttonPi = new System.Windows.Forms.Button();
			this.buttonEquals = new System.Windows.Forms.Button();
			this.buttonOne = new System.Windows.Forms.Button();
			this.buttonTwo = new System.Windows.Forms.Button();
			this.buttonThree = new System.Windows.Forms.Button();
			this.buttonSubtract = new System.Windows.Forms.Button();
			this.buttonMultiply = new System.Windows.Forms.Button();
			this.buttonFour = new System.Windows.Forms.Button();
			this.buttonFive = new System.Windows.Forms.Button();
			this.buttonSix = new System.Windows.Forms.Button();
			this.buttonAC = new System.Windows.Forms.Button();
			this.textBox = new System.Windows.Forms.TextBox();
			this.buttonDivide = new System.Windows.Forms.Button();
			this.buttonSeven = new System.Windows.Forms.Button();
			this.buttonEight = new System.Windows.Forms.Button();
			this.buttonNone = new System.Windows.Forms.Button();
			this.buttonSquared = new System.Windows.Forms.Button();
			this.buttonCubed = new System.Windows.Forms.Button();
			this.buttonSquareRoot = new System.Windows.Forms.Button();
			this.buttonExponent = new System.Windows.Forms.Button();
			this.buttonPaste = new System.Windows.Forms.Button();
			this.buttonSine = new System.Windows.Forms.Button();
			this.buttonCosine = new System.Windows.Forms.Button();
			this.buttonTangent = new System.Windows.Forms.Button();
			this.buttonRoute = new System.Windows.Forms.Button();
			this.buttonFactor = new System.Windows.Forms.Button();
			this.buttonLog = new System.Windows.Forms.Button();
			this.buttonInX = new System.Windows.Forms.Button();
			this.buttonBackspace = new System.Windows.Forms.Button();
			this.radioDegree = new System.Windows.Forms.RadioButton();
			this.radioRadian = new System.Windows.Forms.RadioButton();
			this.buttonPercent = new System.Windows.Forms.Button();
			this.buttonOperator = new System.Windows.Forms.Button();
			this.buttonInverseCosine = new System.Windows.Forms.Button();
			this.buttonInverseSine = new System.Windows.Forms.Button();
			this.buttonInverseTangent = new System.Windows.Forms.Button();
			this.buttonPermutation = new System.Windows.Forms.Button();
			this.buttonCombination = new System.Windows.Forms.Button();
			this.buttonCopy = new System.Windows.Forms.Button();
			this.groupBoxScientific = new ARCed.Controls.CollapsibleGroupBox();
			this.panelBasic = new System.Windows.Forms.Panel();
			this.checkBoxTopMost = new System.Windows.Forms.CheckBox();
			this.toolTip = new System.Windows.Forms.ToolTip(this.components);
			this.groupBoxScientific.SuspendLayout();
			this.panelBasic.SuspendLayout();
			this.SuspendLayout();
			// 
			// buttonZero
			// 
			this.buttonZero.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonZero.Location = new System.Drawing.Point(52, 119);
			this.buttonZero.Name = "buttonZero";
			this.buttonZero.Size = new System.Drawing.Size(40, 23);
			this.buttonZero.TabIndex = 0;
			this.buttonZero.Text = "0";
			this.buttonZero.UseVisualStyleBackColor = true;
			this.buttonZero.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonDecimal
			// 
			this.buttonDecimal.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonDecimal.Location = new System.Drawing.Point(98, 119);
			this.buttonDecimal.Name = "buttonDecimal";
			this.buttonDecimal.Size = new System.Drawing.Size(40, 23);
			this.buttonDecimal.TabIndex = 1;
			this.buttonDecimal.Text = ".";
			this.toolTip.SetToolTip(this.buttonDecimal, "Decimal");
			this.buttonDecimal.UseVisualStyleBackColor = true;
			this.buttonDecimal.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonAddition
			// 
			this.buttonAddition.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonAddition.Location = new System.Drawing.Point(188, 119);
			this.buttonAddition.Name = "buttonAddition";
			this.buttonAddition.Size = new System.Drawing.Size(40, 23);
			this.buttonAddition.TabIndex = 2;
			this.buttonAddition.Text = "+";
			this.toolTip.SetToolTip(this.buttonAddition, "Addition");
			this.buttonAddition.UseVisualStyleBackColor = true;
			this.buttonAddition.Click += new System.EventHandler(this.SetFunction);
			// 
			// buttonPi
			// 
			this.buttonPi.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonPi.Location = new System.Drawing.Point(142, 3);
			this.buttonPi.Name = "buttonPi";
			this.buttonPi.Size = new System.Drawing.Size(40, 23);
			this.buttonPi.TabIndex = 3;
			this.buttonPi.Text = "Pi";
			this.toolTip.SetToolTip(this.buttonPi, "Pi");
			this.buttonPi.UseVisualStyleBackColor = true;
			this.buttonPi.Click += new System.EventHandler(this.buttonPi_Click);
			// 
			// buttonEquals
			// 
			this.buttonEquals.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonEquals.Location = new System.Drawing.Point(142, 119);
			this.buttonEquals.Name = "buttonEquals";
			this.buttonEquals.Size = new System.Drawing.Size(40, 23);
			this.buttonEquals.TabIndex = 4;
			this.buttonEquals.Text = "=";
			this.toolTip.SetToolTip(this.buttonEquals, "Calculate");
			this.buttonEquals.UseVisualStyleBackColor = true;
			this.buttonEquals.Click += new System.EventHandler(this.buttonEquals_Click);
			// 
			// buttonOne
			// 
			this.buttonOne.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonOne.Location = new System.Drawing.Point(52, 90);
			this.buttonOne.Name = "buttonOne";
			this.buttonOne.Size = new System.Drawing.Size(40, 23);
			this.buttonOne.TabIndex = 5;
			this.buttonOne.Text = "1";
			this.buttonOne.UseVisualStyleBackColor = true;
			this.buttonOne.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonTwo
			// 
			this.buttonTwo.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonTwo.Location = new System.Drawing.Point(98, 90);
			this.buttonTwo.Name = "buttonTwo";
			this.buttonTwo.Size = new System.Drawing.Size(40, 23);
			this.buttonTwo.TabIndex = 6;
			this.buttonTwo.Text = "2";
			this.buttonTwo.UseVisualStyleBackColor = true;
			this.buttonTwo.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonThree
			// 
			this.buttonThree.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonThree.Location = new System.Drawing.Point(142, 90);
			this.buttonThree.Name = "buttonThree";
			this.buttonThree.Size = new System.Drawing.Size(40, 23);
			this.buttonThree.TabIndex = 7;
			this.buttonThree.Text = "3";
			this.buttonThree.UseVisualStyleBackColor = true;
			this.buttonThree.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonSubtract
			// 
			this.buttonSubtract.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonSubtract.Location = new System.Drawing.Point(188, 90);
			this.buttonSubtract.Name = "buttonSubtract";
			this.buttonSubtract.Size = new System.Drawing.Size(40, 23);
			this.buttonSubtract.TabIndex = 8;
			this.buttonSubtract.Text = "-";
			this.toolTip.SetToolTip(this.buttonSubtract, "Subtraction");
			this.buttonSubtract.UseVisualStyleBackColor = true;
			this.buttonSubtract.Click += new System.EventHandler(this.SetFunction);
			// 
			// buttonMultiply
			// 
			this.buttonMultiply.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonMultiply.Location = new System.Drawing.Point(188, 61);
			this.buttonMultiply.Name = "buttonMultiply";
			this.buttonMultiply.Size = new System.Drawing.Size(40, 23);
			this.buttonMultiply.TabIndex = 9;
			this.buttonMultiply.Text = "*";
			this.toolTip.SetToolTip(this.buttonMultiply, "Multiplication");
			this.buttonMultiply.UseVisualStyleBackColor = true;
			this.buttonMultiply.Click += new System.EventHandler(this.SetFunction);
			// 
			// buttonFour
			// 
			this.buttonFour.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonFour.Location = new System.Drawing.Point(52, 61);
			this.buttonFour.Name = "buttonFour";
			this.buttonFour.Size = new System.Drawing.Size(40, 23);
			this.buttonFour.TabIndex = 10;
			this.buttonFour.Text = "4";
			this.buttonFour.UseVisualStyleBackColor = true;
			this.buttonFour.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonFive
			// 
			this.buttonFive.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonFive.Location = new System.Drawing.Point(98, 61);
			this.buttonFive.Name = "buttonFive";
			this.buttonFive.Size = new System.Drawing.Size(40, 23);
			this.buttonFive.TabIndex = 11;
			this.buttonFive.Text = "5";
			this.buttonFive.UseVisualStyleBackColor = true;
			this.buttonFive.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonSix
			// 
			this.buttonSix.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonSix.Location = new System.Drawing.Point(142, 61);
			this.buttonSix.Name = "buttonSix";
			this.buttonSix.Size = new System.Drawing.Size(40, 23);
			this.buttonSix.TabIndex = 12;
			this.buttonSix.Text = "6";
			this.buttonSix.UseVisualStyleBackColor = true;
			this.buttonSix.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonAC
			// 
			this.buttonAC.BackColor = System.Drawing.SystemColors.Control;
			this.buttonAC.FlatAppearance.BorderColor = System.Drawing.SystemColors.Control;
			this.buttonAC.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonAC.Image = global::ARCed.Properties.Resources.Delete;
			this.buttonAC.Location = new System.Drawing.Point(4, 32);
			this.buttonAC.Name = "buttonAC";
			this.buttonAC.Size = new System.Drawing.Size(40, 23);
			this.buttonAC.TabIndex = 13;
			this.toolTip.SetToolTip(this.buttonAC, "Clear all");
			this.buttonAC.UseVisualStyleBackColor = true;
			this.buttonAC.Click += new System.EventHandler(this.buttonClear_Click);
			// 
			// textBox
			// 
			this.textBox.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBox.BackColor = System.Drawing.SystemColors.Window;
			this.textBox.Font = new System.Drawing.Font("Consolas", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.textBox.ForeColor = System.Drawing.Color.Black;
			this.textBox.Location = new System.Drawing.Point(14, 12);
			this.textBox.MaxLength = 20;
			this.textBox.Name = "textBox";
			this.textBox.ShortcutsEnabled = false;
			this.textBox.Size = new System.Drawing.Size(236, 30);
			this.textBox.TabIndex = 14;
			this.textBox.TabStop = false;
			// 
			// buttonDivide
			// 
			this.buttonDivide.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonDivide.Location = new System.Drawing.Point(188, 32);
			this.buttonDivide.Name = "buttonDivide";
			this.buttonDivide.Size = new System.Drawing.Size(40, 23);
			this.buttonDivide.TabIndex = 16;
			this.buttonDivide.Text = "/";
			this.toolTip.SetToolTip(this.buttonDivide, "Division");
			this.buttonDivide.UseVisualStyleBackColor = true;
			this.buttonDivide.Click += new System.EventHandler(this.SetFunction);
			// 
			// buttonSeven
			// 
			this.buttonSeven.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonSeven.Location = new System.Drawing.Point(52, 32);
			this.buttonSeven.Name = "buttonSeven";
			this.buttonSeven.Size = new System.Drawing.Size(40, 23);
			this.buttonSeven.TabIndex = 17;
			this.buttonSeven.Text = "7";
			this.buttonSeven.UseVisualStyleBackColor = true;
			this.buttonSeven.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonEight
			// 
			this.buttonEight.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonEight.Location = new System.Drawing.Point(98, 32);
			this.buttonEight.Name = "buttonEight";
			this.buttonEight.Size = new System.Drawing.Size(40, 23);
			this.buttonEight.TabIndex = 18;
			this.buttonEight.Text = "8";
			this.buttonEight.UseVisualStyleBackColor = true;
			this.buttonEight.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonNone
			// 
			this.buttonNone.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonNone.Location = new System.Drawing.Point(142, 32);
			this.buttonNone.Name = "buttonNone";
			this.buttonNone.Size = new System.Drawing.Size(40, 23);
			this.buttonNone.TabIndex = 19;
			this.buttonNone.Text = "9";
			this.buttonNone.UseVisualStyleBackColor = true;
			this.buttonNone.Click += new System.EventHandler(this.buttonNumber_Click);
			// 
			// buttonSquared
			// 
			this.buttonSquared.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonSquared.Location = new System.Drawing.Point(6, 19);
			this.buttonSquared.Name = "buttonSquared";
			this.buttonSquared.Size = new System.Drawing.Size(40, 23);
			this.buttonSquared.TabIndex = 20;
			this.buttonSquared.Text = "x^2";
			this.toolTip.SetToolTip(this.buttonSquared, "Squared");
			this.buttonSquared.UseVisualStyleBackColor = true;
			this.buttonSquared.Click += new System.EventHandler(this.buttonSquared_Click);
			// 
			// buttonCubed
			// 
			this.buttonCubed.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonCubed.Location = new System.Drawing.Point(52, 19);
			this.buttonCubed.Name = "buttonCubed";
			this.buttonCubed.Size = new System.Drawing.Size(40, 23);
			this.buttonCubed.TabIndex = 21;
			this.buttonCubed.Text = "x^3";
			this.toolTip.SetToolTip(this.buttonCubed, "Cubed");
			this.buttonCubed.UseVisualStyleBackColor = true;
			this.buttonCubed.Click += new System.EventHandler(this.buttonCubed_Click);
			// 
			// buttonSquareRoot
			// 
			this.buttonSquareRoot.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonSquareRoot.Location = new System.Drawing.Point(98, 3);
			this.buttonSquareRoot.Name = "buttonSquareRoot";
			this.buttonSquareRoot.Size = new System.Drawing.Size(40, 23);
			this.buttonSquareRoot.TabIndex = 22;
			this.buttonSquareRoot.Text = "sqrt";
			this.toolTip.SetToolTip(this.buttonSquareRoot, "Square Root");
			this.buttonSquareRoot.UseVisualStyleBackColor = true;
			this.buttonSquareRoot.Click += new System.EventHandler(this.buttonSquareRoot_Click);
			// 
			// buttonExponent
			// 
			this.buttonExponent.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonExponent.Location = new System.Drawing.Point(98, 19);
			this.buttonExponent.Name = "buttonExponent";
			this.buttonExponent.Size = new System.Drawing.Size(40, 23);
			this.buttonExponent.TabIndex = 23;
			this.buttonExponent.Text = "x^y";
			this.toolTip.SetToolTip(this.buttonExponent, "Exponent");
			this.buttonExponent.UseVisualStyleBackColor = true;
			this.buttonExponent.Click += new System.EventHandler(this.SetFunction);
			// 
			// buttonPaste
			// 
			this.buttonPaste.BackColor = System.Drawing.SystemColors.Control;
			this.buttonPaste.FlatAppearance.BorderColor = System.Drawing.SystemColors.Control;
			this.buttonPaste.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonPaste.Image = global::ARCed.Properties.Resources.Paste;
			this.buttonPaste.Location = new System.Drawing.Point(6, 119);
			this.buttonPaste.Name = "buttonPaste";
			this.buttonPaste.Size = new System.Drawing.Size(40, 23);
			this.buttonPaste.TabIndex = 24;
			this.toolTip.SetToolTip(this.buttonPaste, "Paste number from clipboard");
			this.buttonPaste.UseVisualStyleBackColor = true;
			this.buttonPaste.Click += new System.EventHandler(this.buttonPaste_Click);
			// 
			// buttonSine
			// 
			this.buttonSine.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonSine.Location = new System.Drawing.Point(6, 48);
			this.buttonSine.Name = "buttonSine";
			this.buttonSine.Size = new System.Drawing.Size(40, 23);
			this.buttonSine.TabIndex = 25;
			this.buttonSine.Text = "sin";
			this.toolTip.SetToolTip(this.buttonSine, "Sine");
			this.buttonSine.UseVisualStyleBackColor = true;
			this.buttonSine.Click += new System.EventHandler(this.buttonSine_Click);
			// 
			// buttonCosine
			// 
			this.buttonCosine.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonCosine.Location = new System.Drawing.Point(52, 48);
			this.buttonCosine.Name = "buttonCosine";
			this.buttonCosine.Size = new System.Drawing.Size(40, 23);
			this.buttonCosine.TabIndex = 26;
			this.buttonCosine.Text = "cos";
			this.toolTip.SetToolTip(this.buttonCosine, "Cosine");
			this.buttonCosine.UseVisualStyleBackColor = true;
			this.buttonCosine.Click += new System.EventHandler(this.buttonCosine_Click);
			// 
			// buttonTangent
			// 
			this.buttonTangent.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonTangent.Location = new System.Drawing.Point(98, 48);
			this.buttonTangent.Name = "buttonTangent";
			this.buttonTangent.Size = new System.Drawing.Size(40, 23);
			this.buttonTangent.TabIndex = 27;
			this.buttonTangent.Text = "tan";
			this.toolTip.SetToolTip(this.buttonTangent, "Tangent");
			this.buttonTangent.UseVisualStyleBackColor = true;
			this.buttonTangent.Click += new System.EventHandler(this.buttonTangent_Click);
			// 
			// buttonRoute
			// 
			this.buttonRoute.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonRoute.Location = new System.Drawing.Point(144, 48);
			this.buttonRoute.Name = "buttonRoute";
			this.buttonRoute.Size = new System.Drawing.Size(40, 23);
			this.buttonRoute.TabIndex = 28;
			this.buttonRoute.Text = "1/x";
			this.toolTip.SetToolTip(this.buttonRoute, "1 divided by");
			this.buttonRoute.UseVisualStyleBackColor = true;
			this.buttonRoute.Click += new System.EventHandler(this.button1DividedBy_Click);
			// 
			// buttonFactor
			// 
			this.buttonFactor.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonFactor.Location = new System.Drawing.Point(190, 48);
			this.buttonFactor.Name = "buttonFactor";
			this.buttonFactor.Size = new System.Drawing.Size(40, 23);
			this.buttonFactor.TabIndex = 29;
			this.buttonFactor.Text = "n!";
			this.toolTip.SetToolTip(this.buttonFactor, "Factorial");
			this.buttonFactor.UseVisualStyleBackColor = true;
			this.buttonFactor.Click += new System.EventHandler(this.buttonFactor_Click);
			// 
			// buttonLog
			// 
			this.buttonLog.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonLog.Location = new System.Drawing.Point(144, 19);
			this.buttonLog.Name = "buttonLog";
			this.buttonLog.Size = new System.Drawing.Size(40, 23);
			this.buttonLog.TabIndex = 30;
			this.buttonLog.Text = "log x";
			this.toolTip.SetToolTip(this.buttonLog, "Base 10 logarithm");
			this.buttonLog.UseVisualStyleBackColor = true;
			this.buttonLog.Click += new System.EventHandler(this.buttonLog10_Click);
			// 
			// buttonInX
			// 
			this.buttonInX.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonInX.Location = new System.Drawing.Point(190, 19);
			this.buttonInX.Name = "buttonInX";
			this.buttonInX.Size = new System.Drawing.Size(40, 23);
			this.buttonInX.TabIndex = 31;
			this.buttonInX.Text = "ln x";
			this.toolTip.SetToolTip(this.buttonInX, "Natural logarithm");
			this.buttonInX.UseVisualStyleBackColor = true;
			this.buttonInX.Click += new System.EventHandler(this.buttonNaturalLog_Click);
			// 
			// buttonBackspace
			// 
			this.buttonBackspace.BackColor = System.Drawing.SystemColors.Control;
			this.buttonBackspace.FlatAppearance.BorderColor = System.Drawing.SystemColors.Control;
			this.buttonBackspace.FlatAppearance.MouseOverBackColor = System.Drawing.Color.Orange;
			this.buttonBackspace.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonBackspace.Location = new System.Drawing.Point(6, 3);
			this.buttonBackspace.Name = "buttonBackspace";
			this.buttonBackspace.Size = new System.Drawing.Size(40, 23);
			this.buttonBackspace.TabIndex = 32;
			this.buttonBackspace.Text = "Back";
			this.toolTip.SetToolTip(this.buttonBackspace, "Backspace");
			this.buttonBackspace.UseVisualStyleBackColor = true;
			this.buttonBackspace.Click += new System.EventHandler(this.buttonBackspace_Click);
			// 
			// radioDegree
			// 
			this.radioDegree.AutoSize = true;
			this.radioDegree.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.radioDegree.Location = new System.Drawing.Point(71, 106);
			this.radioDegree.Name = "radioDegree";
			this.radioDegree.Size = new System.Drawing.Size(60, 17);
			this.radioDegree.TabIndex = 33;
			this.radioDegree.TabStop = true;
			this.radioDegree.Text = "Degree";
			this.toolTip.SetToolTip(this.radioDegree, "Display value in degrees");
			this.radioDegree.UseVisualStyleBackColor = true;
			// 
			// radioRadian
			// 
			this.radioRadian.AutoSize = true;
			this.radioRadian.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.radioRadian.Location = new System.Drawing.Point(6, 106);
			this.radioRadian.Name = "radioRadian";
			this.radioRadian.Size = new System.Drawing.Size(59, 17);
			this.radioRadian.TabIndex = 35;
			this.radioRadian.TabStop = true;
			this.radioRadian.Text = "Radian";
			this.toolTip.SetToolTip(this.radioRadian, "Display value in radians");
			this.radioRadian.UseVisualStyleBackColor = true;
			// 
			// buttonPercent
			// 
			this.buttonPercent.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonPercent.Location = new System.Drawing.Point(188, 3);
			this.buttonPercent.Name = "buttonPercent";
			this.buttonPercent.Size = new System.Drawing.Size(40, 23);
			this.buttonPercent.TabIndex = 37;
			this.buttonPercent.Text = "%";
			this.toolTip.SetToolTip(this.buttonPercent, "Modulo");
			this.buttonPercent.UseVisualStyleBackColor = true;
			this.buttonPercent.Click += new System.EventHandler(this.SetFunction);
			// 
			// buttonOperator
			// 
			this.buttonOperator.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonOperator.Location = new System.Drawing.Point(50, 3);
			this.buttonOperator.Name = "buttonOperator";
			this.buttonOperator.Size = new System.Drawing.Size(40, 23);
			this.buttonOperator.TabIndex = 38;
			this.buttonOperator.Text = "+/-";
			this.toolTip.SetToolTip(this.buttonOperator, "Operator");
			this.buttonOperator.UseVisualStyleBackColor = true;
			this.buttonOperator.Click += new System.EventHandler(this.buttonOperator_Click);
			// 
			// buttonInverseCosine
			// 
			this.buttonInverseCosine.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonInverseCosine.Location = new System.Drawing.Point(52, 77);
			this.buttonInverseCosine.Name = "buttonInverseCosine";
			this.buttonInverseCosine.Size = new System.Drawing.Size(40, 23);
			this.buttonInverseCosine.TabIndex = 39;
			this.buttonInverseCosine.Text = "cos-1";
			this.toolTip.SetToolTip(this.buttonInverseCosine, "Inverse cosine");
			this.buttonInverseCosine.UseVisualStyleBackColor = true;
			this.buttonInverseCosine.Click += new System.EventHandler(this.buttonInverseCosine_Click);
			// 
			// buttonInverseSine
			// 
			this.buttonInverseSine.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonInverseSine.Location = new System.Drawing.Point(6, 77);
			this.buttonInverseSine.Name = "buttonInverseSine";
			this.buttonInverseSine.Size = new System.Drawing.Size(40, 23);
			this.buttonInverseSine.TabIndex = 40;
			this.buttonInverseSine.Text = "sin-1";
			this.toolTip.SetToolTip(this.buttonInverseSine, "Inverse sine");
			this.buttonInverseSine.UseVisualStyleBackColor = true;
			this.buttonInverseSine.Click += new System.EventHandler(this.buttonInverseSine_Click);
			// 
			// buttonInverseTangent
			// 
			this.buttonInverseTangent.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonInverseTangent.Location = new System.Drawing.Point(98, 77);
			this.buttonInverseTangent.Name = "buttonInverseTangent";
			this.buttonInverseTangent.Size = new System.Drawing.Size(40, 23);
			this.buttonInverseTangent.TabIndex = 41;
			this.buttonInverseTangent.Text = "tan-1";
			this.toolTip.SetToolTip(this.buttonInverseTangent, "Inverse tangent");
			this.buttonInverseTangent.UseVisualStyleBackColor = true;
			this.buttonInverseTangent.Click += new System.EventHandler(this.buttonInverseTangent_Click);
			// 
			// buttonPermutation
			// 
			this.buttonPermutation.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonPermutation.Location = new System.Drawing.Point(144, 77);
			this.buttonPermutation.Name = "buttonPermutation";
			this.buttonPermutation.Size = new System.Drawing.Size(40, 23);
			this.buttonPermutation.TabIndex = 42;
			this.buttonPermutation.Text = "nPr";
			this.toolTip.SetToolTip(this.buttonPermutation, "Permutation");
			this.buttonPermutation.UseVisualStyleBackColor = true;
			this.buttonPermutation.Click += new System.EventHandler(this.SetFunction);
			// 
			// buttonCombination
			// 
			this.buttonCombination.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonCombination.Location = new System.Drawing.Point(190, 77);
			this.buttonCombination.Name = "buttonCombination";
			this.buttonCombination.Size = new System.Drawing.Size(40, 23);
			this.buttonCombination.TabIndex = 43;
			this.buttonCombination.Text = "nCr";
			this.toolTip.SetToolTip(this.buttonCombination, "Combination");
			this.buttonCombination.UseVisualStyleBackColor = true;
			this.buttonCombination.Click += new System.EventHandler(this.SetFunction);
			// 
			// buttonCopy
			// 
			this.buttonCopy.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.buttonCopy.Image = global::ARCed.Properties.Resources.Copy;
			this.buttonCopy.Location = new System.Drawing.Point(6, 90);
			this.buttonCopy.Name = "buttonCopy";
			this.buttonCopy.Size = new System.Drawing.Size(40, 23);
			this.buttonCopy.TabIndex = 45;
			this.toolTip.SetToolTip(this.buttonCopy, "Copy number to clipboard");
			this.buttonCopy.UseVisualStyleBackColor = true;
			this.buttonCopy.Click += new System.EventHandler(this.buttonCopy_Click);
			// 
			// groupBoxScientific
			// 
			this.groupBoxScientific.Controls.Add(this.buttonFactor);
			this.groupBoxScientific.Controls.Add(this.buttonSquared);
			this.groupBoxScientific.Controls.Add(this.buttonCombination);
			this.groupBoxScientific.Controls.Add(this.radioDegree);
			this.groupBoxScientific.Controls.Add(this.radioRadian);
			this.groupBoxScientific.Controls.Add(this.buttonCubed);
			this.groupBoxScientific.Controls.Add(this.buttonPermutation);
			this.groupBoxScientific.Controls.Add(this.buttonExponent);
			this.groupBoxScientific.Controls.Add(this.buttonInverseTangent);
			this.groupBoxScientific.Controls.Add(this.buttonSine);
			this.groupBoxScientific.Controls.Add(this.buttonInverseSine);
			this.groupBoxScientific.Controls.Add(this.buttonCosine);
			this.groupBoxScientific.Controls.Add(this.buttonInverseCosine);
			this.groupBoxScientific.Controls.Add(this.buttonTangent);
			this.groupBoxScientific.Controls.Add(this.buttonRoute);
			this.groupBoxScientific.Controls.Add(this.buttonLog);
			this.groupBoxScientific.Controls.Add(this.buttonInX);
			this.groupBoxScientific.Location = new System.Drawing.Point(12, 44);
			this.groupBoxScientific.Name = "groupBoxScientific";
			this.groupBoxScientific.Size = new System.Drawing.Size(238, 132);
			this.groupBoxScientific.TabIndex = 46;
			this.groupBoxScientific.TabStop = false;
			this.groupBoxScientific.Text = "Scientific Functions";
			this.groupBoxScientific.CollapseBoxClickedEvent += new ARCed.Controls.CollapsibleGroupBox.CollapseBoxClickedEventHandler(this.groupBoxScientific_CollapseBoxClickedEvent);
			// 
			// panelBasic
			// 
			this.panelBasic.Controls.Add(this.checkBoxTopMost);
			this.panelBasic.Controls.Add(this.buttonBackspace);
			this.panelBasic.Controls.Add(this.buttonZero);
			this.panelBasic.Controls.Add(this.buttonCopy);
			this.panelBasic.Controls.Add(this.buttonDecimal);
			this.panelBasic.Controls.Add(this.buttonOperator);
			this.panelBasic.Controls.Add(this.buttonAddition);
			this.panelBasic.Controls.Add(this.buttonPercent);
			this.panelBasic.Controls.Add(this.buttonPi);
			this.panelBasic.Controls.Add(this.buttonEquals);
			this.panelBasic.Controls.Add(this.buttonPaste);
			this.panelBasic.Controls.Add(this.buttonOne);
			this.panelBasic.Controls.Add(this.buttonSquareRoot);
			this.panelBasic.Controls.Add(this.buttonTwo);
			this.panelBasic.Controls.Add(this.buttonNone);
			this.panelBasic.Controls.Add(this.buttonThree);
			this.panelBasic.Controls.Add(this.buttonEight);
			this.panelBasic.Controls.Add(this.buttonSubtract);
			this.panelBasic.Controls.Add(this.buttonSeven);
			this.panelBasic.Controls.Add(this.buttonMultiply);
			this.panelBasic.Controls.Add(this.buttonDivide);
			this.panelBasic.Controls.Add(this.buttonFour);
			this.panelBasic.Controls.Add(this.buttonFive);
			this.panelBasic.Controls.Add(this.buttonAC);
			this.panelBasic.Controls.Add(this.buttonSix);
			this.panelBasic.Location = new System.Drawing.Point(14, 182);
			this.panelBasic.Name = "panelBasic";
			this.panelBasic.Size = new System.Drawing.Size(236, 148);
			this.panelBasic.TabIndex = 47;
			// 
			// checkBoxTopMost
			// 
			this.checkBoxTopMost.Appearance = System.Windows.Forms.Appearance.Button;
			this.checkBoxTopMost.BackgroundImage = global::ARCed.Properties.Resources.Pin;
			this.checkBoxTopMost.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
			this.checkBoxTopMost.Location = new System.Drawing.Point(6, 61);
			this.checkBoxTopMost.Name = "checkBoxTopMost";
			this.checkBoxTopMost.Size = new System.Drawing.Size(40, 23);
			this.checkBoxTopMost.TabIndex = 46;
			this.checkBoxTopMost.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			this.toolTip.SetToolTip(this.checkBoxTopMost, "Toggle always on top");
			this.checkBoxTopMost.UseVisualStyleBackColor = true;
			// 
			// CalculatorForm
			// 
			this.AllowEndUserDocking = false;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.AutoSize = true;
			this.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
			this.BackColor = System.Drawing.SystemColors.Control;
			this.ClientSize = new System.Drawing.Size(258, 339);
			this.Controls.Add(this.panelBasic);
			this.Controls.Add(this.groupBoxScientific);
			this.Controls.Add(this.textBox);
			this.DockAreas = ARCed.UI.DockAreas.Float;
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedToolWindow;
			this.Name = "CalculatorForm";
			this.ShowHint = ARCed.UI.DockState.Float;
			this.ShowInTaskbar = false;
			this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "Calculator";
			this.groupBoxScientific.ResumeLayout(false);
			this.groupBoxScientific.PerformLayout();
			this.panelBasic.ResumeLayout(false);
			this.ResumeLayout(false);
			this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button buttonZero;
        private System.Windows.Forms.Button buttonDecimal;
        private System.Windows.Forms.Button buttonAddition;
        private System.Windows.Forms.Button buttonPi;
        private System.Windows.Forms.Button buttonEquals;
        private System.Windows.Forms.Button buttonOne;
        private System.Windows.Forms.Button buttonTwo;
        private System.Windows.Forms.Button buttonThree;
        private System.Windows.Forms.Button buttonSubtract;
        private System.Windows.Forms.Button buttonMultiply;
        private System.Windows.Forms.Button buttonFour;
        private System.Windows.Forms.Button buttonFive;
        private System.Windows.Forms.Button buttonSix;
        private System.Windows.Forms.Button buttonAC;
		private System.Windows.Forms.TextBox textBox;
        private System.Windows.Forms.Button buttonDivide;
        private System.Windows.Forms.Button buttonSeven;
        private System.Windows.Forms.Button buttonEight;
        private System.Windows.Forms.Button buttonNone;
        private System.Windows.Forms.Button buttonSquared;
        private System.Windows.Forms.Button buttonCubed;
        private System.Windows.Forms.Button buttonSquareRoot;
        private System.Windows.Forms.Button buttonExponent;
        private System.Windows.Forms.Button buttonPaste;
        private System.Windows.Forms.Button buttonSine;
        private System.Windows.Forms.Button buttonCosine;
        private System.Windows.Forms.Button buttonTangent;
        private System.Windows.Forms.Button buttonRoute;
        private System.Windows.Forms.Button buttonFactor;
        private System.Windows.Forms.Button buttonLog;
        private System.Windows.Forms.Button buttonInX;
        private System.Windows.Forms.Button buttonBackspace;
        private System.Windows.Forms.RadioButton radioDegree;
        private System.Windows.Forms.RadioButton radioRadian;
        private System.Windows.Forms.Button buttonPercent;
        private System.Windows.Forms.Button buttonOperator;
        private System.Windows.Forms.Button buttonInverseCosine;
        private System.Windows.Forms.Button buttonInverseSine;
        private System.Windows.Forms.Button buttonInverseTangent;
        private System.Windows.Forms.Button buttonPermutation;
		private System.Windows.Forms.Button buttonCombination;
		private System.Windows.Forms.Button buttonCopy;
		private ARCed.Controls.CollapsibleGroupBox groupBoxScientific;
		private System.Windows.Forms.Panel panelBasic;
		private System.Windows.Forms.ToolTip toolTip;
		private System.Windows.Forms.CheckBox checkBoxTopMost;
    }
}

