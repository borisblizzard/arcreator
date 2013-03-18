#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla
{
    public class MarkerInstance : ScintillaHelperBase
    {
        #region Fields

        private readonly int _handle;
        private readonly Marker _marker;

        #endregion Fields


        #region Methods

        public void Delete()
        {
            NativeScintilla.MarkerDeleteHandle(this._handle);
        }


        public override bool Equals(object obj)
        {
            if (!IsSameHelperFamily(obj))
                return false;

            return ((MarkerInstance)obj).Handle == this.Handle;
        }


        public override int GetHashCode()
        {
            return base.GetHashCode();
        }

        #endregion Methods


        #region Properties

        public int Handle
        {
            get
            {
                return this._handle;
            }
        }


        public Line Line
        {
            get
            {
                int lineNo = NativeScintilla.MarkerLineFromHandle(this._handle);
                if (lineNo < 0)
                    return null;

                return new Line(Scintilla, lineNo);

            }
        }


        public Marker Marker
        {
            get
            {
                return this._marker;
            }
        }

        #endregion Properties


        #region Constructors

        internal MarkerInstance(Scintilla scintilla, Marker marker, int handle) : base(scintilla)
        {
            this._marker = marker;
            this._handle = handle;
        }

        #endregion Constructors
    }
}
