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
		public EventTextBox Editor { get { return eventTextBox; } }

		private Troop.Page _page;

		/// <summary>
		/// Gets or sets the instance of the RPG.Troop.Page this control represents.
		/// </summary>
		[Browsable(false)]
		public Troop.Page EventPage 
		{
			get { return _page; }
			set { SetPage(value); }
		}

		public BattleEventPage()
		{
			InitializeComponent();
			_page = new Troop.Page();
			comboBoxSpan.SelectedIndex = 0;
		}

		public void SetPage(Troop.Page page)
		{
			_page = page;
			eventTextBox.Parse(page.list);
		}

		private void comboBoxSpan_SelectedIndexChanged(object sender, EventArgs e)
		{
			_page.span = comboBoxSpan.SelectedIndex;
		}
	}
}
