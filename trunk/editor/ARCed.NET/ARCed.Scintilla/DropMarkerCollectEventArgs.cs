#region Using Directives

using System.ComponentModel;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for a DropMarkerCollect event
    /// </summary>
    public class DropMarkerCollectEventArgs : CancelEventArgs
    {
        #region Fields

        private readonly DropMarker _dropMarker;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Returns the DropMarker that was collected
        /// </summary>
        public DropMarker DropMarker
        {
            get
            {
                return this._dropMarker;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the DropMarkerCollectEventArgs class.
        /// </summary>
        public DropMarkerCollectEventArgs(DropMarker dropMarker)
        {
            this._dropMarker = dropMarker;
        }

        #endregion Constructors
    } 
}
