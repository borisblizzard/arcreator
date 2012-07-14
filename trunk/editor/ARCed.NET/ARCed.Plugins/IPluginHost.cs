using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using ARCed.Core;
using ARCed.UI;

namespace ARCed.Plugins
{
	public interface IPluginHost
	{
		DockPanel DockPanel { get; }
	}
}
