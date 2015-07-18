﻿#region Using Directives

using System;
using System.Collections.Generic;

#endregion


namespace ARCed.Scintilla.Configuration
{
	public class ResolvedStyleList : Dictionary<int, StyleConfig>
	{
		#region Methods

		public StyleConfig FindByName(string name)
		{

			foreach (StyleConfig item in Values)
			{
				if (item.Name.Equals(name, StringComparison.OrdinalIgnoreCase))
					return item;
			}

			return null;
		}

		#endregion Methods


		#region Constructors

		#endregion Constructors
	}
}
