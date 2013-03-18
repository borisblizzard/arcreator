#region Using Directives

using System;
using System.Text;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for the AutoCompleteAccepted event
    /// </summary>
    public class AutoCompleteAcceptedEventArgs : EventArgs
    {
        #region Fields

        private readonly string _text;
        private readonly int _wordStartPosition;
        private bool _cancel;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Gets/Sets if the autocomplete action should be cancelled
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
        ///     Text of the selected autocomplete entry selected
        /// </summary>
        public string Text
        {
            get { return this._text; }
        }


        /// <summary>
        ///     Returns the _start position of the current word in the document.
        /// </summary>
        /// <remarks>
        ///     This controls how many characters of the selected autocomplete entry
        ///     is actually inserted into the document
        /// </remarks>
        public int WordStartPosition
        {
            get
            {
                return this._wordStartPosition;
            }
        }

        #endregion Properties


        #region Constructors

        #pragma warning disable 612, 618
        internal AutoCompleteAcceptedEventArgs(SCNotification eventSource, Encoding encoding)
        {
            this._wordStartPosition = (int)eventSource.lParam;
            this._text = Utilities.IntPtrToString(encoding, eventSource.text);
        }
        #pragma warning restore 612, 618

        /// <summary>
        ///     Initializes a new instance of the AutoCompleteAcceptedEventArgs class.
        /// </summary>
        /// <param name="text">Text of the selected autocomplete entry selected</param>
        public AutoCompleteAcceptedEventArgs(string text)
        {
            this._text = text;
        }

        #endregion Constructors
    }
}
