using System;
using System.ComponentModel;
using System.Windows.Forms;

namespace ARCed.Controls
{
	[DefaultEvent("OnValueChanged"), DefaultProperty("Value")]
	[System.Drawing.ToolboxBitmap(typeof(NumericUpDown))]
	public partial class ParamBox : UserControl
	{

		#region Public Properties

		/// <summary>
		/// Gets the instance of the NumericUpDown on the control.
		/// </summary>
		[Browsable(false)]
		[DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
		public NumericUpDown NumberBox { get { return numericParameter; } }

		/// <summary>
		/// Gets or sets the index of the parameter the control represents.
		/// </summary>
		[Category("ARCed"), Description("Defines the index of the parameter the control represents.")]
		[DefaultValue(-1)]
		public int ParameterIndex { get; set; }

		/// <summary>
		/// Gets or sets the label of the control.
		/// </summary>
		[Category("ARCed"), Description("Defines the label of the control.")]
		public string ParameterLabel
		{
			get { return labelParameter.Text; }
			set { labelParameter.Text = value; }
		}

		/// <summary>
		/// Gets or sets the maximum value the user can select.
		/// </summary>
		[Category("ARCed"), Description("Defines the maximum value the user can select.")]
		public decimal Maximum
		{
			get { return numericParameter.Maximum; }
			set { numericParameter.Maximum = value; }
		}

		/// <summary>
		/// Gets or sets the minimum value the user can select.
		/// </summary>
		[Category("ARCed"), Description("Defines the minimum value the user can select.")]
		public decimal Minimum
		{
			get { return numericParameter.Minimum; }
			set { numericParameter.Minimum = value; }
		}

		/// <summary>
		/// Gets or sets the value of the control.
		/// </summary>
		[Category("ARCed"), Description("Defines the initial value of the control.")]
		[DefaultValue(0)]
		public decimal Value
		{
			get { return numericParameter.Value; }
			set { numericParameter.Value = value; }
		}

		/// <summary>
		/// Gets or sets the attribute name for the corresponding RPG object property.
		/// </summary>
		[Category("ARCed"), Description("Defines the attribute name for the corresponding RPG object property.")]
		[DefaultValue("")]
		public string RpgAttribute { get; set; }

		#endregion

		#region Events

		public delegate void ValueChangedEventHandler(object sender, ParameterEventArgs e);
		/// <summary>
		/// Event fired when the value of the control changes.
		/// </summary>
		[Category("ARCed"), Description("Event fired when the value of the control changes.")]
		public event ValueChangedEventHandler OnValueChanged;

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor.
		/// </summary>
		public ParamBox() { InitializeComponent(); }

		/// <summary>
		/// Constructor with arguments to set initial values;
		/// </summary>
		/// <param name="index">Parameter index of the control</param>
		/// <param name="value">Value of the control</param>
		public ParamBox(int index, decimal value)
		{
			InitializeComponent();
			ParameterIndex = index;
			Value = value;
		}

		#endregion

		#region Private Methods

		private void numericParameter_ValueChanged(object sender, EventArgs e)
		{
			if (OnValueChanged != null)
				OnValueChanged(this, new ParameterEventArgs(ParameterIndex, Value));
		}

		#endregion
	}

	/// <summary>
	/// Arguments used for changing parameters
	/// </summary>
	public class ParameterEventArgs : EventArgs 
	{
		/// <summary>
		/// The parameter index of the control.
		/// </summary>
		public int Index { get; private set; }
		/// <summary>
		/// The value of the control
		/// </summary>
		public decimal Value { get; private set; }

		/// <summary>
		/// Default constructor;
		/// </summary>
		/// <param name="index">Parameter index of the control.</param>
		/// <param name="value">Value of the control</param>
		public ParameterEventArgs(int index, decimal value)
		{
			Index = index;
			Value = value;
		}

	}
}
