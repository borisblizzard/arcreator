#region Using Directives

using System;
using System.Runtime.InteropServices;

#endregion


namespace ARCed.Scintilla
{
	/// <summary>
	///     A range within the editor. Start and End are both Positions.
	/// </summary>
	public class Range : ScintillaHelperBase, IComparable
	{
		#region Fields

		private int _end;
		private int _start;

		#endregion Fields


		#region Methods

		public void ClearIndicator(int indicator)
		{
			NativeScintilla.SetIndicatorCurrent(indicator);
			NativeScintilla.IndicatorClearRange(this._start, this.Length);
		}


		public void ClearIndicator(Indicator indicator)
		{
			NativeScintilla.SetIndicatorCurrent(indicator.Number);
			NativeScintilla.IndicatorClearRange(this._start, this.Length);
		}


		/// <summary>
		///     Collapses all folds
		/// </summary>
		public void CollapseAllFolds()
		{
			for (int i = this.startingLine; i < this.endingLine; i++)
			{
				int maxSubOrd = NativeScintilla.GetLastChild(i, -1);
				NativeScintilla.SetFoldExpanded(i, false);
				NativeScintilla.HideLines(i + 1, maxSubOrd);
			}
		}


		public void Colorize()
		{
			NativeScintilla.Colourise(this._start, this._end);
		}


		public int CompareTo(object otherObj)
		{
			var other = otherObj as Range;

			if (other == null)
				return 1;

			if (other._start < this._start)
				return 1;
			else if (other._start > this._start)
				return -1;

			//	Starts must equal, lets try ends
			if (other._end < this._end)
				return 1;
			else if (other._end > this._end)
				return -1;

			//	Start and End equal. Comparitavely the same
			return 0;
		}


		public void Copy()
		{
			this.Copy(CopyFormat.Text);
		}


		public void Copy(CopyFormat format)
		{
			if (format == CopyFormat.Text)
			{
				Scintilla.Clipboard.Copy(this._start, this._end);
			}
			else if (format == CopyFormat.Rtf)
			{
				throw new NotImplementedException("Someday...");
			}
			else
			{

			}
		}


		public override bool Equals(object obj)
		{
			var r = obj as Range;
			if (r == null)
				return false;

			return r._start == this._start && r._end == this._end;
		}


		/// <summary>
		///     Expands all folds
		/// </summary>
		public void ExpandAllFolds()
		{
			for (int i = this.startingLine; i < this.endingLine; i++)
			{
				NativeScintilla.SetFoldExpanded(i, true);
				NativeScintilla.ShowLines(i + 1, i + 1);
			}
		}


		public override int GetHashCode()
		{
			return base.GetHashCode();
		}


		public void GotoEnd()
		{
			NativeScintilla.GotoPos(this._end);
		}


		public void GotoStart()
		{
			NativeScintilla.GotoPos(this._start);
		}


		public void HideLines()
		{
			NativeScintilla.HideLines(this.startingLine, this.endingLine);
		}


		public bool IntersectsWith(Range otherRange)
		{
			return otherRange.PositionInRange(this._start) | otherRange.PositionInRange(this._end) | this.PositionInRange(otherRange.Start) | this.PositionInRange(otherRange.End);
		}


		public bool PositionInRange(int position)
		{
			return position >= this._start && position <= this._end;
		}


		public void Select()
		{
			NativeScintilla.SetSel(this._start, this._end);
		}


		// Chris Rickard 7/10/2007
		// Woo hoo! Modern Indicator support. We won't even
		// mess with legacy indicators as they'll be removed
		// from Scintilla Someday
		public void SetIndicator(int indicator)
		{
			NativeScintilla.SetIndicatorCurrent(indicator);
			NativeScintilla.IndicatorFillRange(this._start, this.Length);
		}


		// Now the Scintilla documentation is a little unclear to me,
		// but it seems as though the whole indicator value doesn't 
		// really do anything yet, but may in the future.
		public void SetIndicator(int indicator, int value)
		{
			NativeScintilla.SetIndicatorValue(value);
			NativeScintilla.SetIndicatorCurrent(indicator);
			NativeScintilla.IndicatorFillRange(this._start, this.Length);
		}


		public void SetStyle(string styleName)
		{
			this.SetStyle(Scintilla.Lexing.StyleNameMap[styleName]);
		}


		public void SetStyle(int style)
		{
			SetStyle(0xff, style);
		}


		public void SetStyle(byte styleMask, string styleName)
		{
			this.SetStyle(styleMask, Scintilla.Lexing.StyleNameMap[styleName]);
		}


		public void SetStyle(byte styleMask, int style)
		{
			NativeScintilla.StartStyling(this._start, styleMask);
			NativeScintilla.SetStyling(this.Length, style);
		}


		public void ShowLines()
		{
			NativeScintilla.ShowLines(this.startingLine, this.endingLine);
		}


		/// <summary>
		///     Removes trailing spaces from each line
		/// </summary>
		public void StripTrailingSpaces()
		{
			NativeScintilla.BeginUndoAction();

			for (int line = this.startingLine; line < this.endingLine; line++)
			{
				int lineStart = NativeScintilla.PositionFromLine(line);
				int lineEnd = NativeScintilla.GetLineEndPosition(line);
				int i = lineEnd - 1;
				char ch = NativeScintilla.GetCharAt(i);
				while ((i >= lineStart) && ((ch == ' ') || (ch == '\t')))
				{
					i--;
					ch = NativeScintilla.GetCharAt(i);
				}
				if (i == lineStart - 1)
				{
					ch = NativeScintilla.GetCharAt(i + 1);
					while (i < lineEnd && ch == '\t')
					{
						i++;
						ch = NativeScintilla.GetCharAt(i + 1);
					}
				}
				if (i < (lineEnd - 1))
				{
					NativeScintilla.SetTargetStart(i + 1);
					NativeScintilla.SetTargetEnd(lineEnd);
					NativeScintilla.ReplaceTarget(0, string.Empty);
				}
			}
			NativeScintilla.EndUndoAction();
		}


		public override string ToString()
		{

			return "{Start=" + this._start + ", End=" + this._end + ", Length=" + this.Length + "}";
		}

		#endregion Methods


		#region Properties

		public bool Collapsed
		{
			get { return this._start == this._end; }
		}


		public virtual int End
		{
			get
			{
				return this._end;
			}
			set
			{
				this._end = value;
			}
		}


		private int endingLine
		{
			get
			{
				return NativeScintilla.LineFromPosition(this._end);
			}
		}


		public Line EndingLine
		{
			get
			{
				return new Line(Scintilla, this.endingLine);
			}
		}


		public bool IsMultiLine
		{
			get
			{
				return !this.StartingLine.Equals(this.EndingLine);
			}
		}


		public int Length
		{
			get
			{
				return this._end - this._start;
			}
		}


		public virtual int Start
		{
			get
			{
				return this._start;
			}
			set
			{
				this._start = value;
			}
		}


		private int startingLine
		{
			get
			{
				return NativeScintilla.LineFromPosition(this._start);
			}
		}


		public Line StartingLine
		{
			get
			{
				return new Line(Scintilla, this.startingLine);
			}
		}


		public byte[] StyledText
		{
			get
			{
				if (this.Start < 0 || this.End < 0 || Scintilla == null)
					return new byte[0];

				int bufferLength = (this.Length * 2) + 2;
				var rng = new TextRange
				{
					lpstrText = Marshal.AllocHGlobal(bufferLength),
					chrg =
					{
						cpMin = this._start,
						cpMax = this._end
					}
				};

				NativeScintilla.GetStyledText(ref rng);

				var ret = new byte[bufferLength];
				Marshal.Copy(rng.lpstrText, ret, 0, bufferLength);

				Marshal.FreeHGlobal(rng.lpstrText);
				return ret;
			}
		}


		public string Text
		{
			get
			{
				if (this.Start < 0 || this.End < 0 || Scintilla == null)
					return String.Empty;

				var rng = new TextRange();
				try
				{
					rng.lpstrText = Marshal.AllocHGlobal(this.Length + 1);
					rng.chrg.cpMin = this._start;
					rng.chrg.cpMax = this._end;

					int len = NativeScintilla.GetTextRange(ref rng);
					string ret = Utilities.IntPtrToString(Scintilla.Encoding, rng.lpstrText, len);
					return ret ?? String.Empty;
				}
				finally
				{
					Marshal.FreeHGlobal(rng.lpstrText);
				}
			}
			set
			{
				NativeScintilla.SetTargetStart(this._start);
				NativeScintilla.SetTargetEnd(this._end);
				NativeScintilla.ReplaceTarget(-1, value);
			}
		}

		#endregion Properties


		#region Constructors

		protected internal Range() : base(null) { }


		public Range(int start, int end, Scintilla scintilla)
			: base(scintilla)
		{
			if (start < end)
			{
				this._start = start;
				this._end = end;
			}
			else
			{
				this._start = end;
				this._end = start;
			}
		}

		#endregion Constructors
	}
}
