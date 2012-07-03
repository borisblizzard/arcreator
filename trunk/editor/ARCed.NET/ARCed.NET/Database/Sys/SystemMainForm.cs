using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ARCed.Controls;

namespace ARCed.Database.Sys
{
	public partial class SystemMainForm : DatabaseWindow
	{

		#region Protected Properties

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return null; } }

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the data associated with this panel.
		/// </summary>
		public new RPG.System Data { get { return Project.Data.System; } }

		#endregion

		public SystemMainForm()
		{
			InitializeComponent();
		}

		/// <summary>
		/// Refreshes objects by type flag
		/// </summary>
		/// <param name="type">Flag for type of object to refresh</param>
		public override void NotifyRefresh(RefreshType type)
		{
			if (type.HasFlag(RefreshType.Actors))
			{

			}
		}

		public override void RefreshCurrentObject()
		{
			suppressEvents = true;

			suppressEvents = false;
		}
	}
}
