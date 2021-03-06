﻿#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Control that provides functionality for user-defined checkbox values and markers
	/// </summary>
	public partial class MultiStateCheckbox : CheckBox
	{
		#region Private Fields

		private static readonly Font _font =
			new Font("Arial Black", 11, FontStyle.Regular, GraphicsUnit.Pixel);

		private int _stateIndex;

		#endregion

		#region Public Properties

		/// <summary>
		/// This property is not used with multi-state checkboxes.
		/// </summary>
		[Browsable(false), Obsolete("This property is not used with multi-state checkboxes.")]
		public new CheckState CheckState { get { return CheckState.Unchecked; } set { } }

		/// <summary>
		/// This property is not used with multi-state checkboxes.
		/// </summary>
		[Browsable(false), Obsolete("This property is not used with multi-state checkboxes.")]
		public new bool Checked { get { return false; } set { } }

		/// <summary>
		/// Gets or sets the letters or characters used in the checkboxes as glyphs.
		/// </summary>
		[Category("ARCed"), Description("Letters or characters used in the checkboxes as glyphs.")]
		public string[] Characters { get; set; }

		/// <summary>
		/// Gets or sets the array of colors used for painting the markers.
		/// </summary>
		[Category("ARCed"), Description("The array of colors used for painting the markers.")]
		public Color[] CharColors { get; set; }

		/// <summary>
		/// Gets or sets the index of the selected state.
		/// </summary>
		[Browsable(false)]
		public int SelectedState
		{
			get { return this._stateIndex; }
			set { this._stateIndex = value; Invalidate(); }
		}

		/// <summary>
		/// Gets the current color used to draw the item.
		/// </summary>
		[Browsable(false)]
		public Color CurrentColor
		{
			get
			{
				if (this.CharColors.Length > 0)
				{
					int colorIndex = this._stateIndex % this.CharColors.Length;
					return this.CharColors[colorIndex];
				}
				return Color.Black;
			}
		}

		/// <summary>
		/// Gets the currently selected letter/character.
		/// </summary>
		[Browsable(false)]
		public string SelectedCharacter
		{
			get { return this.Characters[this._stateIndex]; }
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Default constructor
		/// </summary>
		public MultiStateCheckbox()
		{
			this.InitializeComponent();
			AutoCheck = false;
			MouseDown += this.MultiStateCheckbox_MouseDown;
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Returns true/false if given point is within the bounds of the checkbox rectangle.
		/// </summary>
		/// <param name="point">Point to check</param>
		/// <returns>Flag if point is within bounds</returns>
		public bool IsPointInCheckBox(Point point)
		{
			return this.IsPointInCheckBox(point.X, point.Y);
		}

		/// <summary>
		/// Returns true/false if given coordinates are within the bounds of the checkbox rectangle.
		/// </summary>
		/// <param name="x">X value to check</param>
		/// <param name="y">Y value to check</param>
		/// <returns>Flag if point is within bounds</returns>
		public bool IsPointInCheckBox(int x, int y)
		{
			int left = Padding.Left;
			int top = (Height - 12) / 2;
			return (x >= left && x <= left + 12 && y >= top && y <= top + 12);
		}

		#endregion

		#region Private Methods

		void MultiStateCheckbox_MouseDown(object sender, MouseEventArgs e)
		{
			if (this.IsPointInCheckBox(e.Location))
			{
				if (e.Button.HasFlag(MouseButtons.Left))
					this._stateIndex = (this._stateIndex + 1) % this.Characters.Length;
				else if (e.Button.HasFlag(MouseButtons.Right))
				{
					this._stateIndex--;
					if (this._stateIndex < 0)
						this._stateIndex = this.Characters.Length - 1;
				}
			}
			Invalidate();
		}

		#endregion

		#region Protected Methods

		protected override void OnPaint(PaintEventArgs e)
		{
			base.OnPaint(e);
			if (this._stateIndex.IsBetween(0, this.Characters.Length - 1))
			{
				string chr = this.Characters[this._stateIndex];
				SizeF size = e.Graphics.MeasureString(chr, _font);
				float x = (12 - size.Width) / 2 + Padding.Left;
				float y = (Height - size.Height) / 2 + Padding.Top;
				var pntF = new PointF(x, y);
				using (var brush = new SolidBrush(this.CurrentColor))
					e.Graphics.DrawString(chr, _font, brush, pntF);
			}
		}

		#endregion
	}
}
