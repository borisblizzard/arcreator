#region Using Directives

using System;
using System.Collections;

#endregion


namespace ARCed.Scintilla
{
	public class LineCollection : TopLevelHelper, ICollection
	{
		#region Methods

		public void CopyTo(Array array, int index)
		{
			if (array == null)
				throw new ArgumentNullException("array");

			if (index < 0)
				throw new ArgumentOutOfRangeException("index");

			if (index >= array.Length)
				throw new ArgumentException("index is equal to or greater than the _length of array.");

			int count = this.Count;
			if (count > array.Length - index)
				throw new ArgumentException("The number of elements in the source ICollection is greater than the available space from number to the _end of the destination array.");

			for (int i = index; i < count; i++)
				array.SetValue(this[i], i);
		}


		public Line FromPosition(int position)
		{
			return this[NativeScintilla.LineFromPosition(position)];
		}


		public Line FromVisibleLineNumber(int displayLine)
		{
			return new Line(Scintilla, NativeScintilla.DocLineFromVisible(displayLine));
		}


		public IEnumerator GetEnumerator()
		{
			return new LinesEnumerator(this);
		}


		public Line GetMaxLineWithState()
		{
			int line = NativeScintilla.GetMaxLineState();
			if (line < 0)
				return null;

			return this[line];
		}


		public void Hide(int startLine, int endLine)
		{
			NativeScintilla.HideLines(startLine, endLine);
		}


		public void Join(int startLine, int endLine)
		{
			NativeScintilla.SetTargetStart(startLine);
			NativeScintilla.SetTargetEnd(endLine);
			Scintilla.DirectMessage(NativeMethods.SCI_LINESJOIN, IntPtr.Zero, IntPtr.Zero);
		}


		private void Show(int startLine, int endLine)
		{
			NativeScintilla.ShowLines(startLine, endLine);
		}

		#endregion Methods


		#region Properties

		public int Count
		{
			get
			{
				return Scintilla.DirectMessage(NativeMethods.SCI_GETLINECOUNT, IntPtr.Zero, IntPtr.Zero).ToInt32();
			}
		}


		public Line Current
		{
			get
			{
				return this[Scintilla.Caret.LineNumber];
			}
		}


		public Line FirstVisible
		{
			get
			{
				return this[NativeScintilla.GetFirstVisibleLine()];
			}
		}


		public bool IsSynchronized
		{
			get { return false; }
		}


		public object SyncRoot
		{
			get { throw new Exception("The method or operation is not implemented."); }
		}


		public Line this[int index]
		{
			get
			{
				return new Line(Scintilla, index);
			}
		}


		public int VisibleCount
		{
			get
			{
				return NativeScintilla.LinesOnScreen();
			}
		}


		public Line[] VisibleLines
		{
			get
			{
				// [workitem:21678] 2009-10-14 Chris Rickard
				// This whole thing was fubard. mjpa fixed part of it but another issue arose
				// that VisibleCount returns how many *possible* lines are visible, not 
				// taking into account that there may not be that many lines defined in 
				// the document.
				int min = NativeScintilla.GetFirstVisibleLine();
				int max = min + this.VisibleCount + 1;
				if (max > this.Count)
					max = this.Count;

				var ret = new Line[max - min];

				for (int i = min; i < max; i++)
					ret[i - min] = this.FromVisibleLineNumber(i);

				return ret;
			}
		}

		#endregion Properties


		#region Constructors

		protected internal LineCollection(Scintilla scintilla) : base(scintilla) { }

		#endregion Constructors


		#region Types

		private class LinesEnumerator : IEnumerator
		{
			#region Fields

			private readonly int _count;
			private int _index = -1;
			private readonly LineCollection _lines;

			#endregion Fields


			#region Methods

			public bool MoveNext()
			{
				if (++this._index >= this._count)
					return false;

				return true;
			}


			public void Reset()
			{
				this._index = -1;
			}

			#endregion Methods


			#region Properties

			public object Current
			{
				get { return this._lines[this._index]; }
			}

			#endregion Properties


			#region Constructors

			public LinesEnumerator(LineCollection lines)
			{
				this._lines = lines;
				this._count = lines.Count;
			}

			#endregion Constructors
		}

		#endregion Types
	}
}
