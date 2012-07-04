using System;
using System.Collections.Generic;
using System.IO;
using System.Drawing;
using ARCed.Data;
using System.Drawing.Imaging;

namespace ARCed.Helpers
{
	static class Cache
	{
		#region Fields
		/// <summary>
		/// The internal dictionary that contains all the cached images
		/// </summary>
		private static Dictionary<string, Image> _cache = new Dictionary<string, Image>();
		/// <summary>
		/// The cached _image of the currently loaded tileset graphic
		/// </summary>
		private static string currentTilesetName;
		/// <summary>
		/// The frames of the currently loaded tileset graphic
		/// </summary>
		private static Image currentTilesetBitmap;
		/// <summary>
		/// The index to reference for building autotile graphics
		/// </summary>
		private static readonly int[][] AUTOINDEX = new int[][] { 
			new[] { 27,28,33,34 },   new[] { 5,28,33,34 },   new[] { 27,6,33,34 },  
			new[] { 5,6,33,34 },     new[] { 27,28,33,12 },  new[] { 5,28,33,12 },  
			new[] { 27,6,33,12 },    new[] { 5,6,33,12 },    new[] { 27,28,11,34 },  
			new[] { 5,28,11,34 },    new[] { 27,6,11,34 },   new[] { 5,6,11,34 },
			new[] { 27,28,11,12 },   new[] { 5,28,11,12 },   new[] { 27,6,11,12 },  
			new[] { 5,6,11,12 },     new[] { 25,26,31,32 },  new[] { 25,6,31,32 },  
			new[] { 25,26,31,12 },   new[] { 25,6,31,12 },   new[] { 15,16,21,22 },  
			new[] { 15,16,21,12 },   new[] { 15,16,11,22 },  new[] { 15,16,11,12 },
			new[] { 29,30,35,36 },   new[] { 29,30,11,36 },  new[] { 5,30,35,36 },  
			new[] { 5,30,11,36 },    new[] { 39,40,45,46 },  new[] { 5,40,45,46 },  
			new[] { 39,6,45,46 },    new[] { 5,6,45,46 },    new[] { 25,30,31,36 },  
			new[] { 15,16,45,46 },   new[] { 13,14,19,20 },  new[] { 13,14,19,12 },
			new[] { 17,18,23,24 },   new[] { 17,18,11,24 },  new[] { 41,42,47,48 }, 
			new[] { 5,42,47,48 },    new[] { 37,38,43,44 },  new[] { 37,6,43,44 },  
			new[] { 13,18,19,24 },   new[] { 13,14,43,44 },  new[] { 37,42,43,48 },  
			new[] { 17,18,47,48 },   new[] { 13,18,43,48 },  new[] { 13,18,43,48 }
		};
		#endregion

		const string BASE_DIRECTORY = @"C:\Program Files (x86)\Common Files\Enterbrain\RGSS\Standard\Graphics";

		/// <summary>
		/// Loads a filename as a Image from the specified folder, or recalls
		/// a cached image, and returns it.
		/// </summary>
		/// <param frames="type">Detailed type specifying where the image will be searched</param>
		/// <param frames="filename">FullPath of the image, omitting extension</param>
		/// <returns>Cached image</returns>
		public static Image LoadBitmap(string folder, string filename)
		{
			string path = ResourceHelper.GetFullPath(folder, filename);
			if (String.IsNullOrEmpty(path))
				return new Bitmap(32, 32);
			if (_cache.ContainsKey(path))
				return _cache[path];
			try
			{
				_cache[path] = Image.FromFile(path);
				return _cache[path];
			}
			catch { return new Bitmap(32, 32); }
		}

		/// <summary>
		/// Rotates the hue and alters the opacity of an image. Using this
		/// method is more efficient than performing the actions seperately.
		/// </summary>
		/// <param frames="_image">Image to change</param>
		/// <param frames="hue">Degree of hue displacement (0..360)</param>
		/// <param frames="opacity">Opacity change to apply (0..255)</param>
		/// <remarks>Values out of range will be automatically corrected</remarks>
		public static void ChangeHueOpacity(Image image, int hue, int opacity)
		{
			using (Image newImage = new Bitmap(image))
			{
				using (Graphics g = Graphics.FromImage(image))
				{
					ImageAttributes imageAttr = new ImageAttributes();
					QColorMatrix qm = new QColorMatrix();
					qm.RotateHue(hue % 360);
					qm.ScaleOpacity(opacity.Clamp(0, 255) / 255.0f);
					imageAttr.SetColorMatrix(qm.ToColorMatrix());
					Rectangle destRect = new Rectangle(new Point(), image.Size);
					g.Clear(Color.Transparent);
					g.DrawImage(newImage, destRect, 0, 0, image.Width, image.Height,
						GraphicsUnit.Pixel, imageAttr);
				}
			}
		}

		/// <summary>
		/// Rotates the hue of an image
		/// </summary>
		/// <param frames="_image">Image to change</param>
		/// <param frames="hue">Degree of hue displacement (0..360)</param>
		/// <remarks>Values out of range will be automatically corrected</remarks>
		public static void RotateHue(Image image, int hue)
		{
			using (Image newImage = new Bitmap(image))
			{
				using (Graphics g = Graphics.FromImage(image))
				{
					ImageAttributes imageAttr = new ImageAttributes();
					QColorMatrix qm = new QColorMatrix();
					qm.RotateHue(hue % 360);
					imageAttr.SetColorMatrix(qm.ToColorMatrix());
					Rectangle destRect = new Rectangle(new Point(), image.Size);
					g.Clear(Color.Transparent);
					g.DrawImage(newImage, destRect, 0, 0, image.Width, image.Height,
						GraphicsUnit.Pixel, imageAttr);
				}
			}
		}

		/// <summary>
		/// Changes the opacity of an image. 
		/// </summary>
		/// <param frames="_image">Image to change</param>
		/// <param frames="opacity">Opacity change to apply (0..255)</param>
		/// <remarks>Values out of range will be automatically corrected</remarks>
		public static void ChangeOpacity(Image image, int opacity)
		{
			using (Image newImage = new Bitmap(image))
			{
				using (Graphics g = Graphics.FromImage(image))
				{
					ImageAttributes imageAttr = new ImageAttributes();
					QColorMatrix qm = new QColorMatrix();
					qm.ScaleOpacity(opacity.Clamp(0, 255) / 255.0f);
					imageAttr.SetColorMatrix(qm.ToColorMatrix());
					Rectangle destRect = new Rectangle(new Point(), image.Size);
					g.Clear(Color.Transparent);
					g.DrawImage(newImage, destRect, 0, 0, image.Width, image.Height,
						GraphicsUnit.Pixel, imageAttr);
				}
			}
		}

		/// <summary>
		/// Loads/recalls a cached image autotile file and returns it
		/// </summary>
		/// <param frames="filename">Full path of the autotile graphic</param>
		/// <param frames="hue">Hue rotation to apply to graphic, with 360 degrees of displacment</param>
		/// <param frames="opacity">Opacity of the returned _image</param>
		/// <returns>Cached image with effects applied</returns>
		public static Image Autotile(string filename, int hue = 0, int opacity = 255)
		{
			using (Image image = new Bitmap(LoadBitmap(@"Graphics\Autotiles", filename)))
			{
				if (hue != 0)
					RotateHue(image, hue);
				if (opacity != 255)
					ChangeOpacity(image, opacity);
				GC.Collect(GC.GetGeneration(image), GCCollectionMode.Forced);
				return new Bitmap(image);
			}
		}

		/// <summary>
		/// Loads/recalls a cached image icon file and returns it
		/// </summary>
		/// <param frames="filename">Full path of the icon graphic</param>
		/// <param frames="hue">Hue rotation to apply to graphic, with 360 degrees of displacment</param>
		/// <param frames="opacity">Opacity of the returned _image</param>
		/// <returns>Cached image with effects applied</returns>
		public static Image Icon(string filename, int hue = 0, int opacity = 255)
		{
			using (Image image = new Bitmap(LoadBitmap(@"Graphics\Icons", filename)))
			{
				if (hue != 0)
					RotateHue(image, hue);
				if (opacity != 255)
					ChangeOpacity(image, opacity);
				GC.Collect(GC.GetGeneration(image), GCCollectionMode.Forced);
				return new Bitmap(image);
			}
		}

		/// <summary>
		/// Loads/recalls a cached character file and returns it
		/// </summary>
		/// <param frames="filename">Full path of the character graphic</param>
		/// <param frames="hue">Hue rotation to apply to graphic, with 360 degrees of displacment</param>
		/// <param frames="opacity">Opacity of the returned _image</param>
		/// <returns>Cached image with effects applied</returns>
		public static Image Character(string filename, int hue = 0, int opacity = 255)
		{
			using (Image image = new Bitmap(LoadBitmap(@"Graphics\Characters", filename)))
			{
				if (hue != 0)
					RotateHue(image, hue);
				if (opacity != 255)
					ChangeOpacity(image, opacity);
				GC.Collect(GC.GetGeneration(image), GCCollectionMode.Forced);
				return new Bitmap(image);
			}
		}

		/// <summary>
		/// Loads/recalls a cached battleback file and returns it
		/// </summary>
		/// <param frames="filename">Full path of the battleback graphic</param>
		/// <param frames="hue">Hue rotation to apply to graphic, with 360 degrees of displacment</param>
		/// <param frames="opacity">Opacity of the returned image</param>
		/// <returns>Cached image with effects applied</returns>
		public static Image Battleback(string filename, int hue = 0, int opacity = 255)
		{
			using (Image image = new Bitmap(LoadBitmap(@"Graphics\Battlebacks", filename)))
			{
				if (hue != 0)
					RotateHue(image, hue);
				if (opacity != 255)
					ChangeOpacity(image, opacity);
				GC.Collect(GC.GetGeneration(image), GCCollectionMode.Forced);
				return new Bitmap(image);
			}
		}

		/// <summary>
		/// Loads/recalls a cached tileset file and returns it
		/// </summary>
		/// <param frames="filename">Full path of the tileset graphic</param>
		/// <param frames="hue">Hue rotation to apply to graphic, with 360 degrees of displacment</param>
		/// <param frames="opacity">Opacity of the returned image</param>
		/// <returns>Cached image with effects applied</returns>
		public static Image Tileset(string filename, int hue = 0, int opacity = 255)
		{
			using (Image image = new Bitmap(LoadBitmap(@"Graphics\Tilesets", filename)))
			{
				if (hue != 0)
					RotateHue(image, hue);
				if (opacity != 255)
					ChangeOpacity(image, opacity);
				GC.Collect(GC.GetGeneration(image), GCCollectionMode.Forced);
				return new Bitmap(image);
			}
		}

		/// <summary>
		/// Returns a tile of a character graphic using the given pattern and direction
		/// </summary>
		/// <param frames="filename">FullPath of the character graphic</param>
		/// <param frames="pattern">Pattern of the character tile</param>
		/// <param frames="direction">Direction of the character tile</param>
		/// <param frames="hue">Hue rotation to apply to graphic, with 360 degrees of displacment</param>
		/// <param frames="opacity">Opacity of the returned _image</param>
		/// <returns>Cached _image with effects applied</returns>
		public static Image CharacterStance(string filename, int pattern, int direction, 
			int hue = 0, int opacity = 255)
		{
			Image image = Character(filename, hue, opacity);
			int cw, ch, sx, sy;
			cw = image.Width / 4;
			ch = image.Height / 4;
			sx = pattern * cw;
			sy = (direction - 2) / 2 * ch;
			Bitmap tile = new Bitmap(cw, ch);
			using (Graphics g = Graphics.FromImage(tile))
				g.DrawImage(image, new Rectangle(0, 0, cw, ch), sx, sy, cw, ch, GraphicsUnit.Pixel);
			GC.Collect(GC.GetGeneration(image), GCCollectionMode.Forced);
			return tile;
		}

		/// <summary>
		/// Loads/recalls a cached image battler file and returns it
		/// </summary>
		/// <param frames="filename">FullPath of the character graphic</param>
		/// <param frames="hue">Hue rotation to apply to graphic, with 360 degrees of displacment</param>
		/// <param frames="opacity">Opacity of the returned _image</param>
		/// <returns>Cached image with effects applied</returns>
		public static Image Battler(string filename, int hue = 0, int opacity = 255)
		{
			using (Image image = new Bitmap(LoadBitmap(@"Graphics\Battlers", filename)))
			{
				if (hue != 0)
					RotateHue(image, hue);
				if (opacity != 255)
					ChangeOpacity(image, opacity);
				GC.Collect(GC.GetGeneration(image), GCCollectionMode.Forced);
				return new Bitmap(image);
			}
		}


		/*

		public static Image Fog(string filename, int hue, int opacity, float zoom)
		{
			string key = String.Format("Fog\\{0}, {1}, {2}", filename, hue, opacity);
			if (!_cache.ContainsKey(key))
			{
				using (Image fog = Bitmap.FromFile(Util.GetLocation(filename, "Fogs")))
				{
					ImageAttributes imageAttr = new ImageAttributes();
					QColorMatrix qm = new QColorMatrix();
					if (hue != 0)
						qm.RotateHue((float)hue);
					if (opacity != 255)
						qm.ScaleOpacity(opacity / 255.0f);
					imageAttr.SetColorMatrix(qm.ToColorMatrix());
					_cache[key] = new Bitmap(fog.Width, fog.Height);
					Rectangle destRect = new Rectangle(0, 0, fog.Width, fog.Height);
					using (Graphics g = Graphics.FromImage(_cache[key]))
						g.DrawImage(fog, destRect, 0, 0, _cache[key].Width,
							_cache[key].Height, GraphicsUnit.Pixel, imageAttr);
				}
			}
			return _cache[key];
		}

		public static Image Tile(string filename, int tileId)
		{
			return Tile(filename, tileId, 255);
		}

		/// <summary>
		/// Retrieves the tile with ID of the specified tileset
		/// </summary>
		/// <param frames="filename">The filename of the tileset</param>
		/// <param frames="tileId">The ID of the tile</param>
		/// <returns>A 32x32 image</returns>
		public static Image Tile(string filename, int tileId, int opacity)
		{
			string key = String.Format("Tile\\{0}, {1}, {2}", filename, tileId, opacity);
			if (!_cache.ContainsKey(key))
			{
				if (filename != currentTilesetName)
					LoadTilesetSource(filename);
				_cache[key] = new Bitmap(32, 32);
				int srcX = (tileId - 384) % 8 * 32;
				int srcY = (tileId - 384) / 8 * 32;
				Rectangle srcRect = new Rectangle(srcX, srcY, 32, 32);
				Rectangle destRect = new Rectangle(0, 0, 32, 32);
				using (Graphics g = Graphics.FromImage(_cache[key]))
					g.DrawImage(currentTilesetBitmap, destRect, srcRect, GraphicsUnit.Pixel);
				if (opacity != 255)
				{
					Bitmap opaqueBitmap = new Bitmap(_cache[key].Width, _cache[key].Height);
					ImageAttributes imageAttr = new ImageAttributes();
					QColorMatrix qm = new QColorMatrix();
					qm.ScaleOpacity(opacity / 255.0f);
					imageAttr.SetColorMatrix(qm.ToColorMatrix());
					using (Graphics g = Graphics.FromImage(opaqueBitmap))
						g.DrawImage(_cache[key], destRect, 0, 0, _cache[key].Width,
							_cache[key].Height, GraphicsUnit.Pixel, imageAttr);
					_cache[key] = opaqueBitmap;
				}
			}
			return _cache[key];
		}

		/// <summary>
		/// Sets the source for the tileset and loads the image into memory
		/// </summary>
		/// <param frames="filename">The filename of the tileset</param>
		private static void LoadTilesetSource(string filename)
		{
			currentTilesetName = filename;
			currentTilesetBitmap = Image.FromFile(Util.GetLocation(filename, "Tilesets"));
		}

		/// <summary>
		/// Retrieves the tile with ID of the specified tileset
		/// </summary>
		/// <param frames="filename">The filename of the autotile</param>
		/// <param frames="index">The index of the autotile</param>
		/// <param frames="frame">The frame (animated only, else 0)</param>
		/// <returns>A 32x32 image</returns>
		public static Image Autotile(string filename, int index, int frame)
		{
			string key = String.Format("Autotile\\{0}, {1}, {2}", filename, index % 48, frame);
			if (!_cache.ContainsKey(key))
				LoadAutotile(filename);
			return _cache[key];
		}

		/// <summary>
		/// Loads the basic autotile image and formats it into 48 separate tiles
		/// </summary>
		/// <param frames="filename">The filename of the autotile</param>
		public static void LoadAutotile(string filename)
		{
			Image autotile = Bitmap.FromFile(Util.GetLocation(filename, "Autotiles"));
			int x, y, num, index, sx, sy;
			Rectangle destRect, srcRect;
			for (int frame = 0; frame < (autotile.Width / 96); frame++)
			{
				using (Image template = new Bitmap(256, 192))
				{
					for (int lvl = 0; lvl < 6; lvl++)
					{
						for (int j = 0; j < 8; j++)
						{
							using (Graphics g = Graphics.FromImage(template))
							{
								foreach (int number in AUTOINDEX[8 * lvl + j])
								{
									num = number - 1;
									x = 16 * (num % 6);
									y = 16 * (num / 6);
									srcRect = new Rectangle(x + (frame * 96), y, 16, 16);
									destRect = new Rectangle(32 * j + x % 32, 32 * lvl + y % 32, 16, 16); // 16, 16?
									g.DrawImage(autotile, destRect, srcRect, GraphicsUnit.Pixel);
								}
							}
							index = 8 * lvl + j;
							string key = String.Format("Autotile\\{0}, {1}, {2}", filename, index, frame);
							_cache[key] = new Bitmap(32, 32);
							sx = 32 * (index % 8);
							sy = 32 * (index / 8);
							srcRect = new Rectangle(sx, sy, 32, 32);
							using (Graphics g = Graphics.FromImage(_cache[key]))
								g.DrawImage(template, new Rectangle(0, 0, 32, 32), srcRect, GraphicsUnit.Pixel);
						}
					}
				}
			}
		}

		/// <summary>
		/// Disposes all cached images and clears all keys and values of the dictionary
		/// </summary>
		public static void Clear()
		{
			try
			{
				foreach (Image image in _cache.Values)
					image.Dispose();
				currentTilesetBitmap.Dispose();
			}
			catch { }
			_cache.Clear();
			GC.Collect();
		}
		*/
	}
}