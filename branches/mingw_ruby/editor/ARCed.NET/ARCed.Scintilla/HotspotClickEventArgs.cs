#region Using Directives

using System;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for the <see cref="Scintilla.HotspotClick" />, <see cref="Scintilla.HotspotDoubleClick" />, and
    ///     <see cref="Scintilla.HotspotReleaseClick" /> events.
    /// </summary>
    public class HotspotClickEventArgs : EventArgs
    {
        #region Fields

        private readonly int _position;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Gets the byte offset in the document of the character that was clicked.
        /// </summary>
        /// <returns>An <see cref="Int32" /> representing the byte offset in the document of the character that was clicked.</returns>
        public int Position
        {
            get
            {
                return this._position;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the <see cref="HotspotClickEventArgs" /> class.
        /// </summary>
        /// <param name="position">The byte offset in the document of the character that was clicked.</param>
        public HotspotClickEventArgs(int position)
        {
            this._position = position;
        }

        #endregion Constructors
    }
}
