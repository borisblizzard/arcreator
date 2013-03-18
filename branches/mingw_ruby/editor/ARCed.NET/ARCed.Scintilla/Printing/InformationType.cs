﻿#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Type of data to display at one of the positions in a Page Information section
    /// </summary>
    public enum InformationType
    {
        /// <summary>
        ///     Nothing is displayed at the position
        /// </summary>
        Nothing,

        /// <summary>
        ///     The page number is displayed in the format "Page #"
        /// </summary>
        PageNumber,

        /// <summary>
        ///     The document name is displayed
        /// </summary>
        DocumentName
    }
}
