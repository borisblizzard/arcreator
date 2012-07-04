using System;
using System.Collections.Generic;
using System.Drawing;
using System.IO;
using ARCed.Helpers;
using Microsoft.Xna.Framework.Graphics;

namespace ARCed.Database.Tilesets
{
	public static class IconCache
	{
		private const int DOWN = 0x01;
		private const int LEFT = 0x02;
		private const int RIGHT = 0x04;
		private const int UP = 0x08;
		private const int ALL = 0x01 | 0x02 | 0x04 | 0x08;
		private const int BUSH = 0x40;
		private const int COUNTER = 0x80;

		private static Dictionary<string, Texture2D> _cache =
			new Dictionary<string, Texture2D>();
		public static GraphicsDevice GraphicsDevice { get; set; }

		private static Bitmap GetBitmap(string key)
		{
			string name = String.Format("ARCed.Resources.TilesetIcons.{0}.png", key);
			using (Stream stream = SystemHelper.ARCedAssembly.GetManifestResourceStream(name))
				return new Bitmap(stream);
		}

		private static Texture2D CacheTexture(string key)
		{
			if (_cache.ContainsKey(key))
				return _cache[key];
			_cache[key] = GetBitmap(key).ToTexture(GraphicsDevice);
			return _cache[key];
		}

		public static Texture2D Passage(int passage)
		{
			passage &= ~BUSH;
			passage &= ~COUNTER;
			string key = (passage == 0) ? "PassageCircle" : "PassageX";
			return CacheTexture(key);
		}

		public static Texture2D Priority(int priority)
		{
			string key = String.Format("Priority{0}", priority);
			return CacheTexture(key);
		}

		public static Texture2D Counter(int passage)
		{
			string key = ((passage & COUNTER) == COUNTER) ? "Counter" : "Priority0";
			return CacheTexture(key);
		}

		public static Texture2D Bush(int passage)
		{
			string key = ((passage & BUSH) == BUSH) ? "Bush" : "Priority0";
			return CacheTexture(key);
		}

		public static Texture2D Terrain(int terrain)
		{
			string key = String.Format("Terrain{0}", terrain);
			return CacheTexture(key);
		}

		public static Texture2D Passage4Dir(int passage)
		{
			passage &= ~BUSH;
			passage &= ~COUNTER;
			string key = String.Format("Passage{0}", passage);
			if (_cache.ContainsKey(key))
				return _cache[key];
			if (passage == 0)
				return CacheTexture("PassageAll");
			if ((passage & ALL) == ALL)
				return CacheTexture("PassageNone");
			{
				Bitmap b = GetBitmap("PassageNone");
				using (Graphics g = Graphics.FromImage(b))
				{
					if ((passage & DOWN) != DOWN)
						g.DrawImage(GetBitmap("PassageDown"), PointF.Empty);
					if ((passage & LEFT) != LEFT)
						g.DrawImage(GetBitmap("PassageLeft"), PointF.Empty);
					if ((passage & RIGHT) != RIGHT)
						g.DrawImage(GetBitmap("PassageRight"), PointF.Empty);
					if ((passage & UP) != UP)
						g.DrawImage(GetBitmap("PassageUp"), PointF.Empty);
				}
				_cache[key] = b.ToTexture(GraphicsDevice);
				return _cache[key];
			}
		}
	}
}
