#region Using Directives

using System.Collections.Generic;

#endregion


namespace ARCed.Scintilla.Configuration
{
	public class LexerPropertiesConfig : Dictionary<string, string>
	{
		#region Fields

		private bool? _inherit;

		#endregion Fields


		#region Properties

		public bool? Inherit
		{
			get
			{
				return this._inherit;
			}
			set
			{
				this._inherit = value;
			}
		}

		#endregion Properties
	}
}
