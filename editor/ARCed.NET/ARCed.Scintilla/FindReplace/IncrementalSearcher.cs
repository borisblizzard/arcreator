#region Using Directives

using System;
using System.Drawing;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    public partial class IncrementalSearcher : UserControl
    {
        #region Fields

        private Scintilla _scintilla;
        private readonly bool _toolItem;

        #endregion Fields


        #region Methods

        private void brnPrevious_Click(object sender, EventArgs e)
        {
            this.findPrevious();
        }


        private void btnClearHighlights_Click(object sender, EventArgs e)
        {
            if (this.Scintilla == null) 
                return;
            this.Scintilla.FindReplace.ClearAllHighlights();
        }


        private void btnHighlightAll_Click(object sender, EventArgs e)
        {
            if (this.txtFind.Text == string.Empty)
                return;
            if (this.Scintilla == null)
                return;
            this.Scintilla.FindReplace.HighlightAll(this.Scintilla.FindReplace.FindAll(this.txtFind.Text));
        }


        private void btnNext_Click(object sender, EventArgs e)
        {
            this.findNext();
        }


        private void findNext()
        {
            if (this.txtFind.Text == string.Empty)
                return;
            if (this.Scintilla == null)
                return;

            Range r = this.Scintilla.FindReplace.FindNext(this.txtFind.Text, true, this.Scintilla.FindReplace.Window.GetSearchFlags());
            if (r != null)
                r.Select();

            this.moveFormAwayFromSelection();
        }


        private void findPrevious()
        {
            if (this.txtFind.Text == string.Empty)
                return;
            if (this.Scintilla == null)
                return;

            Range r = this.Scintilla.FindReplace.FindPrevious(this.txtFind.Text, true, this.Scintilla.FindReplace.Window.GetSearchFlags());
            if (r != null)
                r.Select();

            this.moveFormAwayFromSelection();
        }


        public void moveFormAwayFromSelection()
        {
            if (!Visible || this.Scintilla == null)
                return;

            int pos = this.Scintilla.Caret.Position;
            int x = this.Scintilla.PointXFromPosition(pos);
            int y = this.Scintilla.PointYFromPosition(pos);

            var cursorPoint = new Point(x, y);

            var r = new Rectangle(Location, Size);
            if (r.Contains(cursorPoint))
            {
                Point newLocation;
                if (cursorPoint.Y < (Screen.PrimaryScreen.Bounds.Height / 2))
                {
                    // Top half of the screen
                    newLocation = new Point(Location.X, cursorPoint.Y + this.Scintilla.Lines.Current.Height * 2);
                        
                }
                else
                {
                    // FixedY half of the screen
                    newLocation = new Point(Location.X, cursorPoint.Y - Height - (this.Scintilla.Lines.Current.Height * 2));
                }
                
                Location = newLocation;
            }
        }


        protected override void OnCreateControl()
        {
            base.OnCreateControl();
            this.moveFormAwayFromSelection();
            this.txtFind.Focus();
        }


        protected override void OnLeave(EventArgs e)
        {
            base.OnLostFocus(e);
            if(!this._toolItem)
            Hide();
        }


        protected override void OnVisibleChanged(EventArgs e)
        {
            base.OnVisibleChanged(e);

            this.txtFind.Text = string.Empty;
            this.txtFind.BackColor = SystemColors.Window;

            this.moveFormAwayFromSelection();

            if (Visible)
                this.txtFind.Focus();
            else if(this.Scintilla!=null)
                this.Scintilla.Focus();
        }


        private void txtFind_KeyDown(object sender, KeyEventArgs e)
        {
            switch (e.KeyCode)
            {
                case Keys.Enter:
                case Keys.Down:
                    this.findNext();
                    e.Handled = true;
                    break;
                case Keys.Up:
                    this.findPrevious();
                    e.Handled = true;
                    break;
                case Keys.Escape:
                    if(!this._toolItem)
                    Hide();
                    break;
            }
        }


        private void txtFind_TextChanged(object sender, EventArgs e)
        {
            this.txtFind.BackColor = SystemColors.Window;
            if (this.txtFind.Text == string.Empty)
                return;
            if (this.Scintilla == null)
                return;

            int pos = Math.Min(this.Scintilla.Caret.Position, this.Scintilla.Caret.Anchor);
            Range r = this.Scintilla.FindReplace.Find(pos, this.Scintilla.TextLength, this.txtFind.Text, this.Scintilla.FindReplace.Window.GetSearchFlags());
            if (r == null)
                r = this.Scintilla.FindReplace.Find(0, pos, this.txtFind.Text, this.Scintilla.FindReplace.Window.GetSearchFlags());

            if (r != null)
                r.Select();
            else
                this.txtFind.BackColor = Color.Tomato;

            this.moveFormAwayFromSelection();
        }

        #endregion Methods


        #region Properties

        public Scintilla Scintilla
        {
            get
            {
                return this._scintilla;
            }
            set
            {
                this._scintilla = value;
            }
        }

        #endregion Properties


        #region Constructors

        public IncrementalSearcher()
        {
            this.InitializeComponent();
        }


        public IncrementalSearcher(bool toolItem)
        {
            this.InitializeComponent();
            this._toolItem = toolItem;
            if (toolItem)
                BackColor = Color.Transparent;
        }

        #endregion Constructors
    }
}
