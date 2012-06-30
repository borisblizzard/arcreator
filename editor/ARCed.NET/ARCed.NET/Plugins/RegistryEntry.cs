using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using ARCed.UI;

namespace ARCed.Plugins
{
	public class RegistryEntry : IPluginClient
	{
		/// <summary>
		/// Gets the simple name of the entry
		/// </summary>
		public string Name { get; private set; }
		/// <summary>
		/// Gets the name of the class type
		/// </summary>
		public string ClassName { get; private set; }
		/// <summary>
		/// Gets the type that will be invoked
		/// </summary>
		public Type ClassType { get; private set; }
		/// <summary>
		/// A simple description of the entry's function, used for tooltips in the editor
		/// </summary>
		public string Description { get; set; }
		/// <summary>
		/// Gets the host inherited from the plugin
		/// </summary>
		public IPluginHost Host { get; private set; }
		/// <summary>
		/// Gets the associated plugin object
		/// </summary>
		public Plugin Plugin { get; private set; }
		/// <summary>
		/// Gets the associated window as dockable content
		/// </summary>
		public DockContent Content { get { return (Window as DockContent); } }

		private IPluginClient _instance;

		/// <summary>
		/// Constructs a new RegistryEntry object
		/// </summary>
		/// <param name="plugin">The plugin the entry is from</param>
		/// <param name="type">The invokable type found in the plugin</param>
		/// <param name="name">The simple name of the entry</param>
		/// <param name="className">The full class name, including namespaces of the type</param>
		public RegistryEntry(Plugin plugin, Type type, string name, string className)
		{
			Plugin = plugin;
			Host = plugin.Host;
			ClassType = type;
			Name = name;
			ClassName = className;
			Description = "";
		}

		/// <summary>
		/// Gets the associated window for the entry
		/// </summary>
		public IPluginClient Window
		{
			get
			{
				if (_instance == null || (_instance as DockContent).IsDisposed)
					_instance = (IPluginClient)Activator.CreateInstance(ClassType);
				return _instance;
			}
		}

		/// <summary>
		/// Displays the contents in the host's default dock panel
		/// </summary>
		public void Show()
		{
			Window.Show(Host.DockPanel);
		}

		/// <summary>
		/// Displays the contents in the given panel
		/// </summary>
		/// <param name="panel">The parent panel to dock the content in</param>
		public void Show(DockPanel panel)
		{
			Window.Show(panel);
		}

	}
}