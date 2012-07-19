#region Using Directives

using System;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provices data for the TextModified event
    /// </summary>
    /// <remarks>
    ///     TextModifiedEventHandler is used as an abstracted subset of the
    ///     SCN_MODIFIED notification message. It's used whenever the SCNotification's
    ///     modificationType flags are SC_MOD_INSERTTEXT ,SC_MOD_DELETETEXT, 
    ///     SC_MOD_BEFOREINSERT and SC_MOD_BEFORE_DELETE. They all use a 
    ///     TextModifiedEventArgs which corresponds to a subset of the 
    ///     SCNotification struct having to do with these modification types.
    /// </remarks>
    public class TextModifiedEventArgs : ModifiedEventArgs
    {
        #region Constants

        private const string STRING_FORMAT = "ModificationTypeFlags\t:{0}\r\nPosition\t\t\t:{1}\r\nLength\t\t\t\t:{2}\r\nLinesAddedCount\t\t:{3}\r\nText\t\t\t\t:{4}\r\nIsUserChange\t\t\t:{5}\r\nMarkerChangeLine\t\t:{6}";

        #endregion Constants


        #region Fields

        private readonly bool _isUserChange;
        private readonly int _length;
        private readonly int _linesAddedCount;
        private readonly int _markerChangedLine;
        private readonly int _position;
        private readonly string _text;

        #endregion Fields


        #region Methods

        /// <summary>
        ///     Overridden.
        /// </summary>
        public override string ToString()
        {
            return string.Format(STRING_FORMAT, ModificationType, this._position, this._length, this._linesAddedCount, this._text, this._isUserChange, this._markerChangedLine) + Environment.NewLine + UndoRedoFlags.ToString();
        }

        #endregion Methods


        #region Properties

        /// <summary>
        ///     Returns true if the change was a direct result of user interaction
        /// </summary>
        public bool IsUserChange
        {
            get
            {
                return this._isUserChange;
            }
        }


        /// <summary>
        ///     Returns the length of the change occured.
        /// </summary>
        public int Length
        {
            get
            {
                return this._length;
            }
        }


        /// <summary>
        ///     Returns the # of lines added or removed as a result of the change
        /// </summary>
        public int LinesAddedCount
        {
            get
            {
                return this._linesAddedCount;
            }
        }


        /// <summary>
        ///     Returns the line # of where the marker change occured (if applicable)
        /// </summary>
        public int MarkerChangedLine
        {
            get
            {
                return this._markerChangedLine;
            }
        }


        /// <summary>
        ///     Returns the document position where the change occured
        /// </summary>
        public int Position
        {
            get
            {
                return this._position;
            }
        }


        /// <summary>
        ///     The affected text of the change
        /// </summary>
        public string Text
        {
            get
            {
                return this._text;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        /// Initializes a new instance of the TextModifiedEventArgs class.
        /// </summary>
        /// <param name="modificationType">Specifies the modification type</param>
        /// <param name="isUserChange">true if the change was a direct result of user interaction</param>
        /// <param name="markerChangedLine"> the line # of where the marker change occured (if applicable)</param>
        /// <param name="position">document position where the change occured</param>
        /// <param name="length">_length of the change occured</param>
        /// <param name="linesAddedCount">the # of lines added or removed as a result of the change</param>
        /// <param name="text">affected text of the change</param>
        public TextModifiedEventArgs(int modificationType, bool isUserChange, int markerChangedLine, int position, int length, int linesAddedCount, string text) : base(modificationType)
        {
            this._isUserChange = isUserChange;
            this._markerChangedLine = markerChangedLine;
            this._position = position;
            this._length = length;
            this._linesAddedCount = linesAddedCount;
            this._text = text;
        }

        #endregion Constructors
    }
}
