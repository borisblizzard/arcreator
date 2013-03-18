#region Using Directives

using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    public class GoTo : TopLevelHelper
    {
        #region Methods

        public void Line(int number)
        {
            NativeScintilla.GotoLine(number);
        }


        public void Position(int pos)
        {
            NativeScintilla.GotoPos(pos);
        }


        public void ShowGoToDialog()
        {
            var gd = new GoToDialog
            {
                CurrentLineNumber = Scintilla.Lines.Current.Number,
                MaximumLineNumber = Scintilla.Lines.Count,
                Scintilla = Scintilla
            };

            if (gd.ShowDialog() == DialogResult.OK)
                this.Line(gd.GotoLineNumber);

            Scintilla.Focus();
        }

        #endregion Methods


        #region Constructors

        internal GoTo(Scintilla scintilla) : base(scintilla) {}

        #endregion Constructors
    }
}
