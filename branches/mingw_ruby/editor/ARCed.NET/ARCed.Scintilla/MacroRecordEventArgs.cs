#region Using Directives

using System;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for the MacroRecorded event
    /// </summary>
    public class MacroRecordEventArgs : EventArgs
    {
        #region Fields

        private readonly Message _recordedMessage;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Returns the recorded window message that can be sent back to the native Scintilla window
        /// </summary>
        public Message RecordedMessage
        {
            get
            {
                return this._recordedMessage;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the MacroRecordEventArgs class.
        /// </summary>
        /// <param name="recordedMessage">the recorded window message that can be sent back to the native Scintilla window</param>
        public MacroRecordEventArgs(Message recordedMessage)
        {
            this._recordedMessage = recordedMessage;
        }

        #pragma warning disable 612, 618
        /// <summary>
        ///     Initializes a new instance of the MacroRecordEventArgs class.
        /// </summary>
        /// <param name="ea">NativeScintillaEventArgs object containing the message data</param>
        public MacroRecordEventArgs(NativeScintillaEventArgs ea)
        {
            this._recordedMessage = ea.Msg;
            this._recordedMessage.LParam = ea.SCNotification.lParam;
            this._recordedMessage.WParam = ea.SCNotification.wParam;
        }
        #pragma warning restore 612, 618
        
        #endregion Constructors
    } 
}
