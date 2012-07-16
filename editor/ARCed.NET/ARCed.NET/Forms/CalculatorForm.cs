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
		private double InputValue { get { return Convert.ToDouble(textBox.Text); } }

		/// <summary>
		/// Gets the current display mode of the calculator
		/// </summary>
		public CalculatorMode Mode
		{
			get { return groupBoxScientific.IsCollapsed ? CalculatorMode.Basic : CalculatorMode.Full; } 
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public CalculatorForm() 
		{
			InitializeComponent();
			number1 = number2 = 0.0;
			textBox.ReadOnly = true;
			textBox.RightToLeft = RightToLeft.Yes;
			textBox.Text = "0";
			radioDegree.Checked = true;
			this.Icon = Icon.FromHandle(Resources.Calculator.GetHicon());
			this.checkBoxTopMost.DataBindings.Add("Checked", this,
				"Topmost", false, DataSourceUpdateMode.OnPropertyChanged);
		}

		#endregion

		#region Basic Functions

		private void buttonNumber_Click(object sender, EventArgs e)
		{
			if (!inputstatus || textBox.Text == "0")
			{
				textBox.Text = (sender as Button).Text;
				inputstatus = true;
			}
			else
				textBox.Text += (sender as Button).Text;
		}

        private void buttonEquals_Click(object sender, EventArgs e)
        {
            CalculateFunction();
            inputstatus = false;
        }

        private void buttonSquared_Click(object sender, EventArgs e)
        {
			double num = InputValue;
			textBox.Text = Convert.ToString(num * num);
            inputstatus = false;
        }

        private void buttonCubed_Click(object sender, EventArgs e)
        {
			double num = InputValue;
            textBox.Text = Convert.ToString(num * num * num);
            inputstatus = false;
        }

        private void buttonSquareRoot_Click(object sender, EventArgs e)
        {
            textBox.Text = Convert.ToString(Math.Sqrt(InputValue));
            inputstatus = false;
        }

        private void buttonPi_Click(object sender, EventArgs e)
        {
            textBox.Text = Convert.ToString(Math.PI);
        }

		private void buttonBackspace_Click(object sender, EventArgs e)
		{
			int n = textBox.Text.Length;
			if (n == 1)
				textBox.Text = "0";
			else if (n > 0)
				textBox.Text = textBox.Text.Substring(0, n - 1);
		}

		private void buttonOperator_Click(object sender, EventArgs e)
		{
			textBox.Text = (InputValue * -1).ToString();
			inputstatus = false;
		}

		#endregion

		#region Trig Functions

		private void buttonSine_Click(object sender, EventArgs e)
        {
			number1 = InputValue;
			if (radioDegree.Checked) number1 *= RADIAN;
			textBox.Text = Convert.ToString(Math.Sin(number1));
			inputstatus = false;
        }

        private void buttonCosine_Click(object sender, EventArgs e)
        {
			number1 = InputValue;
			if (radioDegree.Checked) number1 *= RADIAN;
			textBox.Text = Convert.ToString(Math.Cos(number1));
			inputstatus = false;
        }

        private void buttonTangent_Click(object sender, EventArgs e)
        {
			number1 = InputValue;
			if (radioDegree.Checked) number1 *= RADIAN;
			textBox.Text = Convert.ToString(Math.Tan(number1));
			inputstatus = false;
        }

		private void buttonInverseSine_Click(object sender, EventArgs e)
		{
			number1 = InputValue;
			if (radioDegree.Checked) number1 *= RADIAN;
			textBox.Text = Convert.ToString(Math.Asin(number1));
			inputstatus = false;
		}

		private void buttonInverseCosine_Click(object sender, EventArgs e)
		{
			number1 = InputValue;
			if (radioDegree.Checked) number1 *= RADIAN;
			textBox.Text = Convert.ToString(Math.Acos(number1));
			inputstatus = false;
		}

		private void buttonInverseTangent_Click(object sender, EventArgs e)
		{
			number1 = InputValue;
			if (radioDegree.Checked) number1 *= RADIAN;
			textBox.Text = Convert.ToString(Math.Atan(number1));
			inputstatus = false;
		}

		#endregion

		#region Scientific Functions

		private void button1DividedBy_Click(object sender, EventArgs e)
        {
			textBox.Text = Convert.ToString(1.0 / InputValue);
			inputstatus = false;
        }

        private void buttonFactor_Click(object sender, EventArgs e)
        {
            int num = 1;
            for (int i = 1; i <= Convert.ToInt32(InputValue); i++)
                num = num * i;
            textBox.Text = Convert.ToString(num);
            inputstatus = false;
        }

        private void buttonLog10_Click(object sender, EventArgs e)
        {
            textBox.Text = Convert.ToString(Math.Log10(InputValue));
            inputstatus=false;
        }

        private void buttonNaturalLog_Click(object sender, EventArgs e)
        {
            textBox.Text = Convert.ToString(Math.Log(InputValue));
            inputstatus = false;
        }

		#endregion

		#region Clipboard Functions

		private void buttonCopy_Click(object sender, EventArgs e)
        {
			Clipboard.SetText(textBox.Text);
        }

		private void buttonPaste_Click(object sender, EventArgs e)
		{
			if (Clipboard.ContainsText())
			{
				try { textBox.Text = Clipboard.GetText(); }
				catch { Console.WriteLine("TEXT"); }
			}
		}

		#endregion

		#region Misc. Functions

		private void buttonClear_Click(object sender, EventArgs e)
		{
			textBox.Enabled = true;
			textBox.Text = "0";
		}

		private void groupBoxScientific_CollapseBoxClickedEvent(object sender)
		{
			int y = groupBoxScientific.FullHeight - groupBoxScientific.CollapsedHeight;
			if (groupBoxScientific.IsCollapsed) y *= -1;
			panelBasic.Location =
				new Point(panelBasic.Location.X, panelBasic.Location.Y + y);
		}

		private void SetFunction(object sender, EventArgs e)
		{
			number1 = InputValue;
			textBox.Text = "";
			function = (sender as Button).Text;
		}

		private void CalculateFunction()
		{
			double var1, var2, var3;
			number2 = InputValue;
			switch (function)
			{
				case "+":
					result = number1 + number2;
					break;
				case "-":
					result = number1 - number2;
					break;
				case "*":
					result = number1 * number2;
					break;
				case "/":
					if (number2 == 0)
					{
						textBox.Text = "ERROR";
						return;
					}
					result = number1 / number2;
					break;
				case "x^y":
					result = Math.Pow(number1, number2);
					break;
				case "%":
					result = number1 % number2;
					break;
				case "nPr":
					var1 = Factorial((int)number1);
					var2 = Factorial((int)(number1 - number2));
					result = var1 / var2;
					break;
				case "nCr":
					var1 = Factorial((int)number1);
					var2 = Factorial((int)(number1 - number2));
					var3 = Factorial((int)number2);
					result = var1 / (var3 * var2);
					break;
			}
			textBox.Text = Convert.ToString(result);
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