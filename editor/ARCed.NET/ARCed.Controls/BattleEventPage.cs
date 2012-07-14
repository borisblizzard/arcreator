using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;

using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ARCed.Controls
{
	public partial class BattleEventPage : UserControl
	{
		[Browsable(false)]
		public EventTextBox Editor { get { return eventTextBox; } }

		private RPG.Troop.Page _page;

		/// <summary>
		/// Gets or sets the instance of the RPG.Troop.Page this control represents.
		/// </summary>
		[Browsable(false)]
		public RPG.Troop.Page EventPage 
		{
			get { return _page; }
			set { SetPage(value); }
		}

		public BattleEventPage()
		{
			InitializeComponent();
			_page = new RPG.Troop.Page();
			comboBoxSpan.SelectedIndex = 0;
		}

		public void SetPage(RPG.Troop.Page page)
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
