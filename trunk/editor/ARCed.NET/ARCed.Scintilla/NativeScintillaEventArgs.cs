#region Using Directives

using System;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides data for native Scintilla Events
    /// </summary>
    /// <remarks>
    ///     All events fired from the INativeScintilla Interface uses
    ///     NativeScintillaEventArgs. Msg is a copy
    ///     of the Notification Message sent to Scintilla's Parent WndProc
    ///     and SCNotification is the SCNotification Struct pointed to by 
    ///     Msg's lParam. 
    /// </remarks>
    [Obsolete("This type will not be public in future versions.")]
    public class NativeScintillaEventArgs : EventArgs
    {
        #region Fields

        private readonly Message _msg;
        private readonly SCNotification _notification;

        #endregion Fields


        #region Properties

        /// <summary>
        ///     Notification Message sent from the native Scintilla
        /// </summary>
        public Message Msg
        {
            get
            {
                return this._msg;
            }
        }


        /// <summary>
        ///     SCNotification structure sent from Scintilla that contains the event data
        /// </summary>
        public SCNotification SCNotification
        {
            get
            {
                return this._notification;
            }
        }

        #endregion Properties


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the NativeScintillaEventArgs class.
        /// </summary>
        /// <param name="msg">Notification Message sent from the native Scintilla</param>
        /// <param name="notification">SCNotification structure sent from Scintilla that contains the event data</param>
        public NativeScintillaEventArgs(Message msg, SCNotification notification)
        {
            this._msg = msg;
            this._notification = notification;
        }

        #endregion Constructors
    }
}
