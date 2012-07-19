#region Using Directives

using System;
using System.Drawing;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    public partial class SnippetChooser : UserControl
    {
        #region Fields

        private Scintilla _scintilla;
        private string _snippetList = string.Empty;

        #endregion Fields


        #region Methods

        protected override void OnCreateControl()
        {
            this.SetPosition();
            base.OnCreateControl();
            
            this.txtSnippet.Focus();
            this.txtSnippet.AutoComplete.Show(0, this._snippetList);
        }


        protected override void OnLeave(EventArgs e)
        {
            base.OnLostFocus(e);

            Hide();
        }


        protected override void OnVisibleChanged(EventArgs e)
        {
            base.OnVisibleChanged(e);

            this.txtSnippet.Text = string.Empty;
            this.SetPosition();

            if (Visible)
            {
                this.txtSnippet.Focus();
                this.txtSnippet.AutoComplete.Show(0, this._snippetList);
            }
            else
                this.Scintilla.Focus();
        }


        public void SetPosition()
        {
            if (!Visible)
                return;
            
            int pos = this.Scintilla.Caret.Position;
            int x = this.Scintilla.PointXFromPosition(pos);
            int y = this.Scintilla.PointYFromPosition(pos);

            Location = new Point(x, y);
        }


        private void SnippetChooser_Load(object sender, EventArgs e)
        {
            //	This Scintilla has a very limited command set. Its necessary becuase
            //	Scintilla's AutoComplete system is very sensitive when it comes to
            //	dismissing the window, almost anything will do it and there's really
            //	no practical way to prevent it.
            this.txtSnippet.Commands.RemoveAllBindings();

            this.txtSnippet.Commands.AddBinding(Keys.Delete, Keys.None, BindableCommand.Clear);
            this.txtSnippet.Commands.AddBinding(Keys.Back, Keys.None, BindableCommand.DeleteBack);
            this.txtSnippet.Commands.AddBinding('Z', Keys.Control, BindableCommand.Undo);
            this.txtSnippet.Commands.AddBinding('Y', Keys.Control, BindableCommand.Redo);
            this.txtSnippet.Commands.AddBinding('X', Keys.Control, BindableCommand.Cut);
            this.txtSnippet.Commands.AddBinding('C', Keys.Control, BindableCommand.Copy);
            this.txtSnippet.Commands.AddBinding('V', Keys.Control, BindableCommand.Paste);
            this.txtSnippet.Commands.AddBinding('A', Keys.Control, BindableCommand.SelectAll);

            this.txtSnippet.Commands.AddBinding(Keys.Down, Keys.None, BindableCommand.LineDown);
            this.txtSnippet.Commands.AddBinding(Keys.Up, Keys.None, BindableCommand.LineUp);

        }


        private void txtSnippet_AutoCompleteAccepted(object sender, AutoCompleteAcceptedEventArgs e)
        {
            string shortcut = this.txtSnippet.AutoComplete.SelectedText;
            Hide();
            this.Scintilla.Snippets.InsertSnippet(shortcut);
        }

        #pragma warning disable 612, 618
        private void TextSnippetDocumentChange(object sender, NativeScintillaEventArgs e)
        {
            ////	If for any reason the window DOES manage to hide itself
            ////	we merely reshow it.
            if (!this.txtSnippet.AutoComplete.IsActive && Visible)
            {
                int pos = this.Scintilla.Caret.Position;
                this.Scintilla.Caret.Goto(0);
                this.txtSnippet.AutoComplete.Show(0, this._snippetList);
                this.Scintilla.Caret.Goto(pos);
            }
        }
        #pragma warning restore 612, 618

        private void txtSnippet_KeyDown(object sender, KeyEventArgs e)
        {
            //	The built in Scintilla Command Bindings for left and right
            //	will automatically dismiss the AutoComplete Window, which
            //	we don't want. So instead we have to fake our own left and
            //	right functions
            switch (e.KeyCode)
            {
                case Keys.Right:
                    this.txtSnippet.Caret.Goto(this.txtSnippet.Caret.Position + 1);
                    break;
                case Keys.Left:
                    this.txtSnippet.Caret.Goto(this.txtSnippet.Caret.Position - 1);
                    break;
                case Keys.Enter:
                case Keys.Tab:
                    if (this.txtSnippet.AutoComplete.SelectedIndex >= 0)
                        this.txtSnippet.AutoComplete.Accept();
                    break;
                case Keys.Escape:
                    Hide();
                    break;
            }
        }

        #endregion Methods


        #region Properties

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


        public string SnippetList
        {
            get
            {
                return this._snippetList;
            }
            set
            {
                this._snippetList = value;
            }
        }

        #endregion Properties


        #region Constructors

        public SnippetChooser()
        {
            this.InitializeComponent();
        }

        #endregion Constructors
    }
}
