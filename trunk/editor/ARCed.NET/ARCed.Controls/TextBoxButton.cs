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
			get { return this.textBox.Text; }
			set { this.textBox.Text = value; }
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public TextBoxButton()
		{
			this.InitializeComponent();
			this.button.Parent = this.textBox;
		}

		#endregion

		#region Private Methods

		private void button_Click(object sender, EventArgs e)
		{
			if (this.OnButtonClick != null)
				this.OnButtonClick(this, new EventArgs());
		}

		private void textBox_TextChanged(object sender, EventArgs e)
		{
			if (this.OnTextChanged != null)
				this.OnTextChanged(this, new EventArgs());
		}

		#endregion
	}
}
