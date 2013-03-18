#region Using Directives

using System;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for the CallTipClick event
    /// </summary>
    public class CallTipClickEventArgs : EventArgs
    {
        #region Fields

        private readonly CallTipArrow _callTipArrow;
        private readonly int _currentIndex;
        private int _newIndex;
        private readonly OverloadList _overloadList;
        private bool _cancel;
        private int _highlightStart;
        private int _highlightEnd;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Returns the CallTipArrow that was clicked
        /// </summary>
        public CallTipArrow CallTipArrow
        {
            get
            {
                return this._callTipArrow;
            }
        }


        /// <summary>
        ///     Gets/Sets if the CallTip should be hidden
        /// </summary>
        public bool Cancel
        {
            get
            {
                return this._cancel;
            }
            set
            {
                this._cancel = value;
            }
        }


        /// <summary>
        ///     Gets the current index of the CallTip's overload list
        /// </summary>
        public int CurrentIndex
        {
            get
            {
                return this._currentIndex;
            }
        }


        /// <summary>
        ///     Gets/Sets the _end position of the CallTip's highlighted portion of text
        /// </summary>
        public int HighlightEnd
        {
            get
            {
                return this._highlightEnd;
            }
            set
            {
                this._highlightEnd = value;
            }
        }


        /// <summary>
        ///     Gets/Sets the _start position of the CallTip's highlighted portion of text
        /// </summary>
        public int HighlightStart
        {
            get
            {
                return this._highlightStart;
            }
            set
            {
                this._highlightStart = value;
            }
        }


        /// <summary>
        ///     Gets/Sets the new index of the CallTip's overload list
        /// </summary>
        public int NewIndex
        {
            get
            {
                return this._newIndex;
            }
            set
            {
                this._newIndex = value;
            }
        }


        /// <summary>
        ///     Returns the OverLoad list of the CallTip
        /// </summary>
        public OverloadList OverloadList
        {
            get
            {
                return this._overloadList;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the CallTipClickEventArgs class.
        /// </summary>
        /// <param name="callTipArrow">CallTipArrow clicked</param>
        /// <param name="currentIndex">Current posision of the overload list</param>
        /// <param name="newIndex">New position of the overload list</param>
        /// <param name="overloadList">List of overloads to be cycled in the calltip</param>
        /// <param name="highlightStart">Start position of the highlighted text</param>
        /// <param name="highlightEnd">End position of the highlighted text</param>
        public CallTipClickEventArgs(CallTipArrow callTipArrow, int currentIndex, int newIndex, OverloadList overloadList, int highlightStart, int highlightEnd)
        {
            this._callTipArrow = callTipArrow;
            this._currentIndex = currentIndex;
            this._newIndex = newIndex;
            this._overloadList = overloadList;
            this._highlightStart = highlightStart;
            this._highlightEnd = highlightEnd;
        }

        #endregion Constructors
    }
}
