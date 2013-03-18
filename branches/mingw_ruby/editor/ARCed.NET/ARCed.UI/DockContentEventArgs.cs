#region Using Directives

using System;

#endregion

namespace ARCed.UI
{
	public class DockContentEventArgs : EventArgs
	{
        private readonly IDockContent _mContent;

		public DockContentEventArgs(IDockContent content)
		{
			this._mContent = content;
		}

		public IDockContent Content
		{
			get	{	return this._mContent;	}
		}
	}
}
