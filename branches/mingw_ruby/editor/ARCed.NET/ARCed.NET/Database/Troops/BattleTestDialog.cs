#region Using Directives

using System;
using System.Collections.Generic;
using System.Globalization;
using System.Windows.Forms;
using ARCed.Controls;

#endregion

namespace ARCed.Database.Troops
{
    /// <summary>
    /// Dialog for getting user-defined battle test configuration.
    /// </summary>
	public partial class BattleTestDialog : Form
    {
        #region Constructor

        /// <summary>
        /// Defualt constructor
        /// </summary>
		public BattleTestDialog()
		{
			this.InitializeComponent();
			if (Project.BTActors == null)
				Project.BTActors = new List<dynamic>
				{ Project.Data.Actors[0] };
			this.numericUpDownActors.Value = Project.BTActors.Count;
		}

        #endregion

        #region Private Methods

        private void NumericUpDownActorsValueChanged(object sender, EventArgs e)
		{
			var value = (int)this.numericUpDownActors.Value;
			if (value < this.tabControlActors.TabCount)
			{
				for (int i = this.tabControlActors.TabCount - 1; i >= value; i--)
				{
					this.tabControlActors.TabPages.RemoveAt(i);
					Project.BTActors.RemoveAt(i);
				}
			}
			else
			{
				this.tabControlActors.SuspendLayout();
				for (int i = this.tabControlActors.TabCount; i < value; i++)
				{
					var page = new TabPage((i + 1).ToString(CultureInfo.InvariantCulture));
					var panel = new BattleTestActorPanel();
					page.Controls.Add(panel);
					panel.Dock = DockStyle.Fill;
					this.tabControlActors.TabPages.Add(page);
					Project.BTActors.Add(Project.Data.Actors[0]);
				}
				this.tabControlActors.ResumeLayout(true);
			}
        }

        #endregion
    }
}
