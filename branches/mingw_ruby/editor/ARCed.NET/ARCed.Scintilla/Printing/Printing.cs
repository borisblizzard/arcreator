#region Using Directives

using System.ComponentModel;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class Printing : TopLevelHelper
    {
        #region Fields

        private PrintDocument _printDocument;

        #endregion Fields


        #region Methods

        public bool Print()
        {
            return this.Print(true);
        }


        public bool Print(bool showPrintDialog)
        {
            if (showPrintDialog)
            {
                var pd = new PrintDialog
                {
                    Document = this._printDocument,
                    UseEXDialog = true,
                    AllowCurrentPage = true,
                    AllowSelection = true,
                    AllowSomePages = true,
                    PrinterSettings = this.PageSettings.PrinterSettings
                };

                if (pd.ShowDialog(Scintilla) == DialogResult.OK)
                {
                    this._printDocument.PrinterSettings = pd.PrinterSettings;
                    this._printDocument.Print();
                    return true;
                }

                return false;
            }

            this._printDocument.Print();
            return true;
        }


        public DialogResult PrintPreview()
        {
            var ppd = new PrintPreviewDialog
            {
                WindowState = FormWindowState.Maximized,
                Document = this._printDocument
            };

            return ppd.ShowDialog();
        }


        public DialogResult PrintPreview(IWin32Window owner)
        {
            var ppd = new PrintPreviewDialog
            {
                WindowState = FormWindowState.Maximized
            };

            if (owner is Form)
                ppd.Icon = ((Form)owner).Icon;

            ppd.Document = this._printDocument;
            return ppd.ShowDialog(owner);
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializePageSettings() || this.ShouldSerializePrintDocument();
        }


        private bool ShouldSerializePageSettings()
        {
            return this.PageSettings.ShouldSerialize();
        }


        private bool ShouldSerializePrintDocument()
        {
            return this._printDocument.ShouldSerialize();
        }


        public DialogResult ShowPageSetupDialog()
        {
            var psd = new PageSetupDialog
            {
                PageSettings = this.PageSettings,
                PrinterSettings = this.PageSettings.PrinterSettings
            };
            return psd.ShowDialog();
        }


        public DialogResult ShowPageSetupDialog(IWin32Window owner)
        {
            var psd = new PageSetupDialog
            {
                AllowPrinter = true,
                PageSettings = this.PageSettings,
                PrinterSettings = this.PageSettings.PrinterSettings
            };

            return psd.ShowDialog(owner);
        }

        #endregion Methods


        #region Properties

        [Browsable(true), DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public PageSettings PageSettings
        {
            get
            {
                return this._printDocument.DefaultPageSettings as PageSettings;
            }
            set
            {
                this._printDocument.DefaultPageSettings = value;
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public PrintDocument PrintDocument
        {
            get
            {
                return this._printDocument;
            }
            set
            {
                this._printDocument = value;
            }
        }

        #endregion Properties


        #region Constructors

        internal Printing(Scintilla scintilla) : base(scintilla)
        {
            this._printDocument = new PrintDocument(scintilla);
        }

        #endregion Constructors
    }
}
