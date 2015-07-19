using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using RPG;
using ARCed.Controls;
using System.Reflection;


namespace ARCed.Database
{
    public partial class ChangeMaximumForm : Form
    {
        public bool Confirm;

        /// <summary>
        /// Creates a new Form
        /// </summary>
        /// <param name="currentSize">Current size of the list to set</param>
        /// <param name="y"></param>
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
            this.Close();
        }

        private void buttonCancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        /// <summary>
        /// Changes the maximum number of elements of a database panel
        /// </summary>
        /// <typeparam name="T">Type of the object</typeparam>
        /// <param name="Data">Dynamic List 'Data' that there's in every panel</param>
        /// <param name="dataObjectList">DatabaseObjectListBox control</param>
        public void ChangeMaximum <T>(List<dynamic> Data, DatabaseObjectListBox dataObjectList) where T : new()
        {
            int prevSize = dataObjectList.Items.Count;
            int size = (int)numericNewMax.Value;

            if (size == prevSize) return;

            if (size > prevSize)
            {
                for (int i = 0; i < size - prevSize; i++)
                {
                    T s = new T();
                    s.GetType().GetProperty("id").SetValue(s, (int)(prevSize + i + 1), null);
                    Data.Add(s);
                    dataObjectList.Items.Add(s.ToString());
                }
            }
            else
            {
                while (prevSize != size)
                {
                    dataObjectList.Items.RemoveAt(prevSize - 1);
                    Data.RemoveAt(prevSize);
                    prevSize--;
                }
                if (dataObjectList.SelectedIndex == -1)
                {
                    dataObjectList.SelectedIndex = size - 1;
                }
            }
            this.Dispose();
        }

    }
}
