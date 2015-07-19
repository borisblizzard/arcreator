using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ARCed.Database
{
    public partial class ChangeMaximumForm : Form
    {
        public bool Confirm;
        public int Value;

        public ChangeMaximumForm(int currentSize,int y)
        {
            InitializeComponent();
            numericNewMax.Value = currentSize;
            this.Location = new Point(60, y - 35);
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void buttonOK_Click(object sender, EventArgs e)
        {
            Confirm = true;
            Value = (int)numericNewMax.Value;
            this.Close();
        }

        private void buttonCancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
