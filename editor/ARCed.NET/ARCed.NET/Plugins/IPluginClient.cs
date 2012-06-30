using ARCed.UI;

namespace ARCed.Plugins
{
	public interface IPluginClient
	{
		void Show();
		void Show(DockPanel panel);
	}
}
