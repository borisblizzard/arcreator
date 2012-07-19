#region Using Directives

using System.Drawing;

#endregion


namespace ARCed.Scintilla
{
    public class SnippetLinkEnd : ManagedRange
    {
        #region Methods

        public override void Change(int newStart, int newEnd)
        {
            this.Invalidate();

            //	This actually changes Start and End
            base.Change(newStart, newEnd);
        }


        public override void Dispose()
        {
            if (!IsDisposed)
            {
                this.Invalidate();
                base.Dispose();
            }
        }


        public void Invalidate()
        {
            if(Scintilla != null && Start > 0)
            {
                INativeScintilla _ns = Scintilla;
                int x = _ns.PointXFromPosition(Start);
                int y = _ns.PointYFromPosition(Start) + _ns.TextHeight(0) - 2;

                //	Invalidate the old Marker Location so that we don't get "Ghosts"
                Scintilla.Invalidate(new Rectangle(x-2, y, 5, 5));
            }
        }


        protected internal override void Paint(Graphics g)
        {
            base.Paint(g);

            if (IsDisposed)
                return;

            INativeScintilla _ns = Scintilla;

            int x = _ns.PointXFromPosition(Start);
            int y = _ns.PointYFromPosition(Start) + _ns.TextHeight(0) - 2;

            //	Draw a red Triangle with a dark red border at the marker position
            g.FillPolygon(Brushes.Lime, new[] { new Point(x-2, y+4), new Point(x, y), new Point(x+2, y+4) });
            g.DrawPolygon(Pens.Green, new[] { new Point(x-2, y+4), new Point(x, y), new Point(x+2, y+4) });
        }

        #endregion Methods


        #region Properties

        // Drop Markers are points, not a spanned range.
        public override bool IsPoint
        {
            get
            {
                return true;
            }
        }

        #endregion Properties


        #region Constructors

        internal SnippetLinkEnd(int start, Scintilla scintilla) : base(start, start, scintilla)
        {
        }

        #endregion Constructors
    }
}
