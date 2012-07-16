#region Using Directives

using System;
using System.Globalization;
using System.Threading;
using System.Windows.Forms;

#endregion

namespace ARCed.Dialogs
{
    /// <summary>
    /// 
    /// </summary>
    public partial class LocalizationDialog : Form
    {
        /// <summary>
        /// Gets or sets the index of the selected language;
        /// </summary>
        public int LanguageIndex
        {
            get { return comboBoxLanguage.SelectedIndex; }
            set { comboBoxLanguage.SelectedIndex = value; }
        }

        /// <summary>
        /// Dialog for specifying ARCed.NET localization.
        /// </summary>
        public LocalizationDialog()
        {
            InitializeComponent();
        }

        private void ButtonOkClick(object sender, EventArgs e)
        {
            CultureInfo info;
            switch (comboBoxLanguage.SelectedIndex)
            {
                case 1: info = new CultureInfo("es-ES"); break;
                case 2: info = new CultureInfo("de-DE"); break;
                case 3: info = new CultureInfo("fr-FR"); break;
                default: info = new CultureInfo("en-US"); break;
            }
            Thread.CurrentThread.CurrentUICulture = info;
            this.DialogResult = DialogResult.OK;
            this.Close();
        }
    }
}
