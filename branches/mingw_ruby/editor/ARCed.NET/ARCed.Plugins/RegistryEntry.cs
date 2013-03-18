#region Using Directives

using System;
using ARCed.UI;

#endregion

namespace ARCed.Plugins
{
    /// <summary>
    /// Represents an entry in the plugin registry.
    /// </summary>
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
// ReSharper disable SuspiciousTypeConversion.Global
        public DockContent Content { get { return (DockContent)this.Window; } }
// ReSharper restore SuspiciousTypeConversion.Global

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
			this.Plugin = plugin;
			this.Host = plugin.Host;
			this.ClassType = type;
			this.Name = name;
			this.ClassName = className;
			this.Description = "";
		}

		/// <summary>
		/// Gets the associated window for the entry
		/// </summary>
		public IPluginClient Window
		{
			get
			{
                var dockContent = (DockContent)this._instance;
			    if (dockContent != null && (this._instance == null || dockContent.IsDisposed))
					this._instance = (IPluginClient)Activator.CreateInstance(this.ClassType);
				return this._instance;
			}
		}

		/// <summary>
		/// Displays the contents in the host's default dock panel
		/// </summary>
		public void Show()
		{
			this.Window.Show(this.Host.DockPanel);
		}

		/// <summary>
		/// Displays the contents in the given panel
		/// </summary>
		/// <param name="panel">The parent panel to dock the content in</param>
		public void Show(DockPanel panel)
		{
			this.Window.Show(panel);
		}

	}
}