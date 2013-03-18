#region Using Directives

using ARCed.UI;

#endregion

namespace ARCed.Plugins
{
    /// <summary>
    /// Interface for plugin forms to inherit.
    /// </summary>
	public interface IPluginClient
	{
        /// <summary>
        /// Shows the control.
        /// </summary>
		void Show();

        /// <summary>
        /// Shows the control using the specified <see cref="ARCed.UI.DockPanel"/> parent.
        /// </summary>
        /// <param name="panel">Parent dock panel to dock form in.</param>
		void Show(DockPanel panel);
	}
}
