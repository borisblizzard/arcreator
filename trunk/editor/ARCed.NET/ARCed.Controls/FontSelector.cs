#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Font selection control that allows selecting of TrueType fonts with size and style settings.
	/// </summary>
	public partial class FontSelector : UserControl
	{
		#region Private Field

		private bool _suppressEvents;

		#endregion

		#region Events

		public delegate void FontChangedEventHandler(object sender, EventArgs e);
		/// <summary>
		/// Fired whenever the selected font is changed
		/// </summary>
		[Category("ARCed"), Description("Fired whenever the selected font is changed.")]
		public event FontChangedEventHandler OnUserFontChanged;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the text of the groupbox
		/// </summary>
		[Category("ARCed"), Description("Defines the text of the groupbox")]
		[DefaultValue("Font")]
		public string GroupBoxText
		{
			get { return groupBoxFont.Text; }
			set { groupBoxFont.Text = value; }
		}

		/// <summary>
		/// Enables/disables the style GroupBox.
		/// </summary>
		[Category("ARCed"), Description("Defines if style can be changed by the user.")]
		[DefaultValue(true)]
		public bool StyleChangeEnabled
		{
			get { return groupBoxFont.Enabled; }
			set { groupBoxFont.Enabled = value; }
		}

		/// <summary>
		/// Enables/disables the size NumericUpDown.
		/// </summary>
		[Category("ARCed"), Description("Defines if size can be changed by the user.")]
		[DefaultValue(true)]
		public bool SizeChangeEnabled
		{
			get { return numericSize.Enabled; }
			set { numericSize.Enabled = value; }
		}

		/// <summary>
		/// Gets or sets the minimum font size the user can select.
		/// </summary>
		[Category("ARCed"), Description("Defines the minimum font size the user can select.")]
		[DefaultValue(4.0f)]
		public float MinimumFontSize
		{
			get { return (float)numericSize.Minimum; }
			set { numericSize.Minimum = (decimal)value; }
		}

		/// <summary>
		/// Gets or sets the maximum font size the user can select.
		/// </summary>
		[Category("ARCed"), Description("Defines the maximum font size the user can select.")]
		[DefaultValue(72.0f)]
		public float MaximimFontSize
		{
			get { return (float)numericSize.Maximum; }
			set { numericSize.Maximum = (decimal)value; }
		}

		/// <summary>
		/// Gets or sets the selected font for the control
		/// </summary>
		[Browsable(false)]
		[DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
		public Font UserFont 
		{
			get { return GetFont(); }
			set { SetFont(value); }
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public FontSelector()
		{
			InitializeComponent();
		}

		#endregion

		#region Private Methods

		private void SetFont(Font font)
		{
			_suppressEvents = true;
			fontComboBox.SelectedFontFamily = font.OriginalFontName;
			numericSize.Value = (decimal)font.Size;
			checkBoxBold.Checked = font.Style.HasFlag(FontStyle.Bold);
			checkBoxItalic.Checked = font.Style.HasFlag(FontStyle.Italic);
			checkBoxUnderline.Checked = font.Style.HasFlag(FontStyle.Underline);
			_suppressEvents = false;
			labelSample.Font = GetFont();
		}

		private Font GetFont()
		{
			var style = FontStyle.Regular;
			if (checkBoxBold.Checked) style |= FontStyle.Bold;
			if (checkBoxItalic.Checked) style |= FontStyle.Italic;
			if (checkBoxUnderline.Checked) style |= FontStyle.Underline;
			var size = (float)numericSize.Value;
			string fontName = fontComboBox.SelectedFontFamily;
			return FontHelper.GetFont(fontName, size, style);
		}

		private void FontSetting_Changed(object sender, EventArgs e)
		{
			if (!_suppressEvents)
				labelSample.Font = GetFont();
			if (OnUserFontChanged != null)
				OnUserFontChanged(this, e);
		}

		#endregion
	}
}
