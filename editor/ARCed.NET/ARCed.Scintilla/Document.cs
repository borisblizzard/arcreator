#region Using Directives

using System;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Provides an abstraction over Scintilla's Document Pointer
    /// </summary>
    public class Document : ScintillaHelperBase
    {
        #region Fields

        private IntPtr _handle;

        #endregion Fields


        #region Methods

        /// <summary>
        ///     Increases the document's reference count
        /// </summary>
        /// <remarks>No, you aren't looking at COM, move along.</remarks>
        public void AddRef()
        {
            NativeScintilla.AddRefDocument(this._handle);
        }


        /// <summary>
        ///     Overridden. 
        /// </summary>
        /// <param name="obj">Another Document Object</param>
        /// <returns>True if both Documents have the same Handle</returns>
        public override bool Equals(object obj)
        {
            var d = obj as Document;

            if (this._handle == IntPtr.Zero)
                return false;

            return this._handle.Equals(d._handle);
        }


        /// <summary>
        ///     Overridden
        /// </summary>
        /// <returns>Document Pointer's hashcode</returns>
        public override int GetHashCode()
        {
            return this._handle.GetHashCode();
        }


        /// <summary>
        ///     Decreases the document's reference count
        /// </summary>
        /// <remarks>
        ///     When the document's reference count reaches 0 Scintilla will destroy the document
        /// </remarks>
        public void Release()
        {
            NativeScintilla.ReleaseDocument(this._handle);
        }

        #endregion Methods


        #region Properties

        /// <summary>
        /// Scintilla's internal document pointer.
        /// </summary>
        public IntPtr Handle
        {
            get
            {
                return this._handle;
            }
            set
            {
                this._handle = value;
            }
        }

        #endregion Properties


        #region Constructors

        internal Document(Scintilla scintilla, IntPtr handle) : base(scintilla) 
        {
            this._handle = handle;
        }

        #endregion Constructors
    }
}
