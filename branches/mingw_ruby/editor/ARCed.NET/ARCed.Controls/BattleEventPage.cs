#region Using Directives

using System;
using System.ComponentModel;
using System.Windows.Forms;
using RPG;

#endregion

namespace ARCed.Controls
{
	public partial class BattleEventPage : UserControl
	{
		[Browsable(false)]
		public EventTextBox Editor { get { return this.eventTextBox; } }

		private Troop.Page _page;

		/// <summary>
		/// Gets or sets the instance of the RPG.Troop.Page this control represents.
		/// </summary>
		[Browsable(false)]
		public Troop.Page EventPage 
		{
			get { return this._page; }
			set { this.SetPage(value); }
		}

		public BattleEventPage()
		{
			this.InitializeComponent();
			this._page = new Troop.Page();
			this.comboBoxSpan.SelectedIndex = 0;
		}

		public void SetPage(Troop.Page page)
		{
			this._page = page;
			this.eventTextBox.Parse(page.list);
		}

		private void comboBoxSpan_SelectedIndexChanged(object sender, EventArgs e)
		{
			this._page.span = this.comboBoxSpan.SelectedIndex;
		}
	}
}
