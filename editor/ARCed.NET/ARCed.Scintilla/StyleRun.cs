﻿#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla
{
	/// <summary>
	///     Defines a run of styled text in a <see cref="Scintilla" /> control
	/// </summary>
	public struct StyleRun
	{
		#region Fields

		/// <summary>
		///     Represents a new instance of the <see cref="StyleRun" /> struct with member data left uninitialized.
		/// </summary>
		public static readonly StyleRun Empty = new StyleRun();

		private int _length;
		private int _style;

		#endregion Fields


		#region Properties

		/// <summary>
		///     Gets or sets length of this <see cref="StyleRun" />.
		/// </summary>
		/// <returns>An <see cref="int" /> representing the length of this <see cref="StyleRun" />.</returns>
		public int Length
		{
			get
			{
				return this._length;
			}
			set
			{
				this._length = value;
			}
		}


		/// <summary>
		///     Gets or sets the style index of this <see cref="StyleRun" />.
		/// </summary>
		/// <returns>An <see cref="int" /> representing the zero-based style index of this <see cref="StyleRun" />.</returns>
		public int Style
		{
			get
			{
				return this._style;
			}
			set
			{
				this._style = value;
			}
		}

		#endregion Properties


		#region Constructors

		/// <summary>
		///     Initializes a new instance of the <see cref="StyleRun" /> struct.
		/// </summary>
		/// <param name="length">The length of the run.</param>
		/// <param name="style">The zero-based index of the style that the run represents.</param>
		public StyleRun(int length, int style)
		{
			this._length = length;
			this._style = style;
		}

		#endregion Constructors
	}
}
