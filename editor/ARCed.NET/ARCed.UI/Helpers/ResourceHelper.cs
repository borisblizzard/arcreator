#region Using Directives

using System.Resources;

#endregion

namespace ARCed.UI
{
	internal static class ResourceHelper
	{
        private static ResourceManager _resourceManager;

        private static ResourceManager ResourceManager
        {
            get
            {
                if (_resourceManager == null)
                    _resourceManager = new ResourceManager("ARCed.UI.Strings", typeof(ResourceHelper).Assembly);
                return _resourceManager;
            }

        }

		public static string GetString(string name)
		{
			return ResourceManager.GetString(name);
		}
	}
}
