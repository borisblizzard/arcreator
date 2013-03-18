#region Using Directives

using System;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Properties;
using ARCed.UI;

#endregion

namespace ARCed.Forms
{
	/// <summary>
	/// Values for the calculator display mode
	/// </summary>
	public enum CalculatorMode
	{
		/// <summary>
		/// Basic display mode with advanced functions hidden
		/// </summary>
		Basic,
		/// <summary>
		/// Scientific display mode with trigonometry functions, logarithms, etc.
		/// </summary>
		Full
	}

    public partial class CalculatorForm : DockContent
	{
		#region Constants
		/// <summary>
		/// PI / 180
		/// </summary>
		const double RADIAN = Math.PI / 180;
		#endregion

		#region Fields

		private double number1, number2, result;
        private string function;
        private bool inputstatus;

		#endregion

		#region Properties

		/// <summary>
		/// Gets the text from the calculator textbox and returns it as a double
		/// </summary>
		private double InputValue { get { return Convert.ToDouble(this.textBox.Text); } }

		/// <summary>
		/// Gets the current display mode of the calculator
		/// </summary>
		public CalculatorMode Mode
		{
			get { return this.groupBoxScientific.IsCollapsed ? CalculatorMode.Basic : CalculatorMode.Full; } 
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public CalculatorForm() 
		{
			this.InitializeComponent();
			this.number1 = this.number2 = 0.0;
			this.textBox.ReadOnly = true;
			this.textBox.RightToLeft = RightToLeft.Yes;
			this.textBox.Text = "0";
			this.radioDegree.Checked = true;
			Icon = Icon.FromHandle(Resources.Calculator.GetHicon());
			this.checkBoxTopMost.DataBindings.Add("Checked", this,
				"Topmost", false, DataSourceUpdateMode.OnPropertyChanged);
		}

		#endregion

		#region Basic Functions

		private void buttonNumber_Click(object sender, EventArgs e)
		{
			if (!this.inputstatus || this.textBox.Text == "0")
			{
				this.textBox.Text = (sender as Button).Text;
				this.inputstatus = true;
			}
			else
				this.textBox.Text += (sender as Button).Text;
		}

        private void buttonEquals_Click(object sender, EventArgs e)
        {
            this.CalculateFunction();
            this.inputstatus = false;
        }

        private void buttonSquared_Click(object sender, EventArgs e)
        {
			double num = this.InputValue;
			this.textBox.Text = Convert.ToString(num * num);
            this.inputstatus = false;
        }

        private void buttonCubed_Click(object sender, EventArgs e)
        {
			double num = this.InputValue;
            this.textBox.Text = Convert.ToString(num * num * num);
            this.inputstatus = false;
        }

        private void buttonSquareRoot_Click(object sender, EventArgs e)
        {
            this.textBox.Text = Convert.ToString(Math.Sqrt(this.InputValue));
            this.inputstatus = false;
        }

        private void buttonPi_Click(object sender, EventArgs e)
        {
            this.textBox.Text = Convert.ToString(Math.PI);
        }

		private void buttonBackspace_Click(object sender, EventArgs e)
		{
			int n = this.textBox.Text.Length;
			if (n == 1)
				this.textBox.Text = "0";
			else if (n > 0)
				this.textBox.Text = this.textBox.Text.Substring(0, n - 1);
		}

		private void buttonOperator_Click(object sender, EventArgs e)
		{
			this.textBox.Text = (this.InputValue * -1).ToString();
			this.inputstatus = false;
		}

		#endregion

		#region Trig Functions

		private void buttonSine_Click(object sender, EventArgs e)
        {
			this.number1 = this.InputValue;
			if (this.radioDegree.Checked) this.number1 *= RADIAN;
			this.textBox.Text = Convert.ToString(Math.Sin(this.number1));
			this.inputstatus = false;
        }

        private void buttonCosine_Click(object sender, EventArgs e)
        {
			this.number1 = this.InputValue;
			if (this.radioDegree.Checked) this.number1 *= RADIAN;
			this.textBox.Text = Convert.ToString(Math.Cos(this.number1));
			this.inputstatus = false;
        }

        private void buttonTangent_Click(object sender, EventArgs e)
        {
			this.number1 = this.InputValue;
			if (this.radioDegree.Checked) this.number1 *= RADIAN;
			this.textBox.Text = Convert.ToString(Math.Tan(this.number1));
			this.inputstatus = false;
        }

		private void buttonInverseSine_Click(object sender, EventArgs e)
		{
			this.number1 = this.InputValue;
			if (this.radioDegree.Checked) this.number1 *= RADIAN;
			this.textBox.Text = Convert.ToString(Math.Asin(this.number1));
			this.inputstatus = false;
		}

		private void buttonInverseCosine_Click(object sender, EventArgs e)
		{
			this.number1 = this.InputValue;
			if (this.radioDegree.Checked) this.number1 *= RADIAN;
			this.textBox.Text = Convert.ToString(Math.Acos(this.number1));
			this.inputstatus = false;
		}

		private void buttonInverseTangent_Click(object sender, EventArgs e)
		{
			this.number1 = this.InputValue;
			if (this.radioDegree.Checked) this.number1 *= RADIAN;
			this.textBox.Text = Convert.ToString(Math.Atan(this.number1));
			this.inputstatus = false;
		}

		#endregion

		#region Scientific Functions

		private void button1DividedBy_Click(object sender, EventArgs e)
        {
			this.textBox.Text = Convert.ToString(1.0 / this.InputValue);
			this.inputstatus = false;
        }

        private void buttonFactor_Click(object sender, EventArgs e)
        {
            int num = 1;
            for (int i = 1; i <= Convert.ToInt32(this.InputValue); i++)
                num = num * i;
            this.textBox.Text = Convert.ToString(num);
            this.inputstatus = false;
        }

        private void buttonLog10_Click(object sender, EventArgs e)
        {
            this.textBox.Text = Convert.ToString(Math.Log10(this.InputValue));
            this.inputstatus=false;
        }

        private void buttonNaturalLog_Click(object sender, EventArgs e)
        {
            this.textBox.Text = Convert.ToString(Math.Log(this.InputValue));
            this.inputstatus = false;
        }

		#endregion

		#region Clipboard Functions

		private void buttonCopy_Click(object sender, EventArgs e)
        {
			Clipboard.SetText(this.textBox.Text);
        }

		private void buttonPaste_Click(object sender, EventArgs e)
		{
			if (Clipboard.ContainsText())
			{
				try { this.textBox.Text = Clipboard.GetText(); }
				catch { Console.WriteLine("TEXT"); }
			}
		}

		#endregion

		#region Misc. Functions

		private void buttonClear_Click(object sender, EventArgs e)
		{
			this.textBox.Enabled = true;
			this.textBox.Text = "0";
		}

		private void groupBoxScientific_CollapseBoxClickedEvent(object sender)
		{
			int y = this.groupBoxScientific.FullHeight - this.groupBoxScientific.CollapsedHeight;
			if (this.groupBoxScientific.IsCollapsed) y *= -1;
			this.panelBasic.Location =
				new Point(this.panelBasic.Location.X, this.panelBasic.Location.Y + y);
		}

		private void SetFunction(object sender, EventArgs e)
		{
			this.number1 = this.InputValue;
			this.textBox.Text = "";
			this.function = (sender as Button).Text;
		}

		private void CalculateFunction()
		{
			double var1, var2, var3;
			this.number2 = this.InputValue;
			switch (this.function)
			{
				case "+":
					this.result = this.number1 + this.number2;
					break;
				case "-":
					this.result = this.number1 - this.number2;
					break;
				case "*":
					this.result = this.number1 * this.number2;
					break;
				case "/":
					if (this.number2 == 0)
					{
						this.textBox.Text = "ERROR";
						return;
					}
					this.result = this.number1 / this.number2;
					break;
				case "x^y":
					this.result = Math.Pow(this.number1, this.number2);
					break;
				case "%":
					this.result = this.number1 % this.number2;
					break;
				case "nPr":
					var1 = Factorial((int)this.number1);
					var2 = Factorial((int)(this.number1 - this.number2));
					this.result = var1 / var2;
					break;
				case "nCr":
					var1 = Factorial((int)this.number1);
					var2 = Factorial((int)(this.number1 - this.number2));
					var3 = Factorial((int)this.number2);
					this.result = var1 / (var3 * var2);
					break;
			}
			this.textBox.Text = Convert.ToString(this.result);
		}

		private static int Factorial(int x)
		{
			int i = 1;
			for (int s = 1; s <= x; s++)
				i = i * s;
			return i;
		}

		#endregion
	}
} 