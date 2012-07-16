#region Using Directives

using ARCed.UI;

#endregion

namespace ARCed.Plugins
{
    /// <summary>
    /// Interface for host applications to inherit from.
    /// </summary>
	public interface IPluginHost
	{
        /// <summary>
        /// Gets the <see cref="DockPanel"/> instance of the host form.
        /// </summary>
		DockPanel DockPanel { get; }
	}
}
