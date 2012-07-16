#region Using Directives

using System;
using System.ComponentModel;
using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Control that combines a read-only, unselectable textbox and a button.
	/// </summary>
	[DefaultEvent("OnButtonClick"), DefaultProperty("Text")]
	public partial class TextBoxButton : UserControl
	{
		#region Events

		public delegate void ButtonClickHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised when the button is clicked on the control.
		/// </summary>
		[Category("ARCed"), Description("Event raised when the button is clicked on the control.")]
		public event ButtonClickHandler OnButtonClick;

		public delegate void TextChangeHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised when the text is changed.
		/// </summary>
		[Category("ARCed"), Description("Event raised when the text is changed.")]
		public new event TextChangeHandler OnTextChanged;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the text on the control.
		/// </summary>
		public override string Text
		{
			get { return textBox.Text; }
			set { textBox.Text = value; }
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public TextBoxButton()
		{
			InitializeComponent();
			button.Parent = textBox;
		}

		#endregion

		#region Private Methods

		private void button_Click(object sender, EventArgs e)
		{
			if (OnButtonClick != null)
				OnButtonClick(this, new EventArgs());
		}

		private void textBox_TextChanged(object sender, EventArgs e)
		{
			if (OnTextChanged != null)
				OnTextChanged(this, new EventArgs());
		}

		#endregion
	}
}
