using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;

using Bitmap = System.Drawing.Bitmap;

namespace ARCed
{
	public static class XnaExtensions
	{
		/// <summary>
		/// Draws and fills a triangle using the given points and color.
		/// </summary>
		/// <param name="batch">SpriteBatch to draw triangle</param>
		/// <param name="p1">First point</param>
		/// <param name="p2">Second point</param>
		/// <param name="p3">Third point</param>
		/// <param name="color">Color to fill triangle</param>
		public static void FillTriangle(this SpriteBatch batch, Vector2 p1, Vector2 p2, 
			Vector2 p3, Color color)
		{
			Vector2 tp;
			if (p2.Y > p1.Y) { tp = p1; p1 = p2; p2 = tp; }
			if (p3.Y > p1.Y) { tp = p1; p1 = p3; p3 = tp; }
			if (p3.Y > p2.Y) { tp = p2; p2 = p3; p3 = tp; }
			int steps13 = (int)(p1.Y - p3.Y);
			int steps12 = (int)(p1.Y - p2.Y);
			int steps23 = (int)(p2.Y - p3.Y);
			float sx13 = (float)(p1.X - p3.X) / (float)steps13;
			float sx12 = (float)(p1.X - p2.X) / (float)steps12;
			float sx23 = (float)(p2.X - p3.X) / (float)steps23;
			float x13 = p1.X;
			float x12 = p1.X;
			float dx = 1;
			for (int i = 0; i < steps12; i++)
			{
				x13 -= sx13;
				x12 -= sx12;
				dx = x13 - x12;
				if (dx > 0)
					batch.FillRectangle((int)x12, (int)p1.Y - i, (int)Math.Abs(dx), 1, color);
				else
					batch.FillRectangle((int)x13, (int)p1.Y - i, (int)Math.Abs(dx), 1, color);
			}
			float x23 = p2.X;
			for (int i = 0; i < steps23; i++)
			{
				x13 -= sx13;
				x23 -= sx23;
				dx = x13 - x23;
				if (dx > 0)
					batch.FillRectangle((int)x23, (int)p2.Y - i, (int)Math.Abs(dx), 1, color);
				else
					batch.FillRectangle((int)x13, (int)p2.Y - i, (int)Math.Abs(dx), 1, color);
			}
		}

		/// <summary>
		/// Draws the specified string using the given font and location.
		/// </summary>
		/// <param name="batch">SpriteBatch to draw the string</param>
		/// <param name="text">Text to draw</param>
		/// <param name="font">Font to draw text with.</param>
		/// <param name="color">Color of the text.</param>
		/// <param name="rect">Rectangle where text will be drawn.</param>
		/// <remarks>Without the use of a ContentPipeline, it is necessary to use GDI+ to 
		/// draw the font onto a bitmap and transfer it to a texture.</remarks>
		public static void DrawString(this SpriteBatch batch, string text, 
			System.Drawing.Font font, Color color, Rectangle rect)
		{
			using (Bitmap bmp = new Bitmap(rect.Width, rect.Height))
			{
				using (var g = System.Drawing.Graphics.FromImage(bmp))
				{
					g.DrawString(text, font, System.Drawing.Brushes.White,
						new System.Drawing.PointF(0, 0));
					batch.Draw(bmp.ToTexture(batch.GraphicsDevice), rect, color);
				}
			}
		}

		/// <summary>
		/// Draws a bordered selection rectangle around the given rectangle.
		/// </summary>
		/// <param name="batch">SpriteBatch to draw the rectangle.</param>
		/// <param name="rect">Rectangle to draw</param>
		/// <param name="color">Color of the rectangle border</param>
		/// <param name="thickness">Thickness, in pixels, of the inner selection rectangle</param>
		public static void DrawSelectionRect(this SpriteBatch batch, Rectangle rect, Color color, int thickness = 1)
		{
			DrawRectangle(batch, rect, Color.Black, thickness + 2);
			DrawRectangle(batch, new Rectangle(rect.X + 1, rect.Y + 1,
				rect.Width - 2, rect.Height - 2), color, thickness);
		}

		/// <summary>
		/// Draws a rectangle with given location, size, color, and border width.
		/// </summary>
		/// <param name="batch">SpriteBatch to draw the rectangle.</param>
		/// <param name="x">Coordinate of the rectangle on the x-axis</param>
		/// <param name="y">Coordinate of the rectangle on the y-axis</param>
		/// <param name="width">Width of the rectangle in pixels</param>
		/// <param name="height">Height of the rectangle in pixels</param>
		/// <param name="color">Color of the rectangle border</param>
		/// <param name="border">Width of the border in pixels</param>
		public static void DrawRectangle(this SpriteBatch batch, int x, int y, 
			int width, int height, Color color, int border = 1)
		{
			Rectangle rect = new Rectangle(x, y, width, height);
			DrawRectangle(batch, rect, color, border);
		}

		/// <summary>
		/// Draws a rectangle with given location, size, color, and border width.
		/// </summary>
		/// <param name="batch">SpriteBatch to draw the rectangle.</param>
		/// <param name="rect">Rectangle to draw.</param>
		/// <param name="border">Width of the border in pixels</param>
		public static void DrawRectangle(this SpriteBatch batch, Rectangle rect, Color color, int border = 1)
		{
			Texture2D _texture = new Texture2D(batch.GraphicsDevice, 1, 1);
			_texture.SetData(new[] { Color.White });
			batch.Draw(_texture, new Rectangle(rect.Left, rect.Top, rect.Width, border), color);
			batch.Draw(_texture, new Rectangle(rect.Left, rect.Bottom - border, rect.Width, border), color);
			batch.Draw(_texture, new Rectangle(rect.Left, rect.Top, border, rect.Height), color);
			batch.Draw(_texture, new Rectangle(rect.Right - border, rect.Top, border, rect.Height - border), color);
		}

		/// <summary>
		/// Draws and fills a rectangle with given location, size, and color.
		/// </summary>
		/// <param name="batch">SpriteBatch to draw the rectangle.</param>
		/// <param name="x">Coordinate of the rectangle on the x-axis</param>
		/// <param name="y">Coordinate of the rectangle on the y-axis</param>
		/// <param name="width">Width of the rectangle in pixels</param>
		/// <param name="height">Height of the rectangle in pixels</param>
		/// <param name="color">Color of the rectangle border</param>
		public static void FillRectangle(this SpriteBatch batch, int x, int y,
			int width, int height, Color color)
		{
			Texture2D rectangleTexture = new Texture2D(batch.GraphicsDevice, width, height);
			Color[] colors = Enumerable.Repeat(color, width * height).ToArray();
			rectangleTexture.SetData(colors);
			batch.Draw(rectangleTexture, new Vector2(x, y), Color.White);
		}

		/// <summary>
		/// Draws and fills a rectangle with given location, size, and color.
		/// </summary>
		/// <param name="batch">SpriteBatch to draw the rectangle.</param>
		/// <param name="rect">Rectangle to draw</param>
		/// <param name="color">Color of the rectangle border</param>
		public static void FillRectangle(this SpriteBatch batch, Rectangle rect, Color color)
		{
			FillRectangle(batch, rect.X, rect.Y, rect.Width, rect.Height, color);
		}

		/// <summary>
		/// Converts a <paramref name="System.Drawing.Rectangle"/> to a 
		/// <paramref name="Microsoft.Xna.Framework.Rectangle"/> and returns it.
		/// </summary>
		/// <param name="rect">Rectangle to convert</param>
		/// <returns>Converted rectangle</returns>
		public static Rectangle ToXnaRect(this System.Drawing.Rectangle rect)
		{
			return new Rectangle(rect.X, rect.Y, rect.Width, rect.Height);
		}

		/// <summary>
		/// Converts a <paramref name="Microsoft.Xna.Framework.Rectangle"/> to a 
		/// <paramref name="System.Drawing.Rectangle"/> and returns it.
		/// </summary>
		/// <param name="rect">Rectangle to convert</param>
		/// <returns>Converted rectangle</returns>
		public static System.Drawing.Rectangle ToSystemRect(this Rectangle rect)
		{
			return new System.Drawing.Rectangle(rect.X, rect.Y, rect.Width, rect.Height);
		}

		/// <summary>
		/// Converts and returns a <paramref name="System.Drawing.Color"/> to 
		/// a <paramref name="Microsoft.Xna.Framework.Color"/>.
		/// </summary>
		/// <param name="color">Color to convert.</param>
		/// <returns>Converted color</returns>
		public static Color ToXnaColor(this System.Drawing.Color color)
		{
			return new Color(color.R, color.G, color.B, color.A);
		}

		/// <summary>
		/// Converts and returns a <paramref name="Microsoft.Xna.Framework.Color"/> to 
		/// a <paramref name="System.Drawing.Color"/>.
		/// </summary>
		/// <param name="color">Color to convert.</param>
		/// <returns>Converted color</returns>
		public static System.Drawing.Color ToSystemColor(this Color color)
		{
			return System.Drawing.Color.FromArgb(color.A, color.R, color.G, color.B);
		}

		/// <summary>
		/// Converts a Texture2D to an <paramref name="System.Drawing.Image"/> and returns it.
		/// </summary>
		/// <param name="texture">Texture to convert</param>
		/// <returns>Image representation of the texture.</returns>
		public static System.Drawing.Image ToImage(this Texture2D texture)
		{
			System.Drawing.Image image = null;
			using (MemoryStream stream = new MemoryStream())
			{
				texture.SaveAsPng(stream, texture.Width, texture.Height);
				stream.Seek(0, SeekOrigin.Begin);
				image = System.Drawing.Image.FromStream(stream);
			}
			return image;
		}

		/// <summary>
		/// Converts a Image to a Texture2D and returns it.
		/// </summary>
		/// <param name="image">Image to convert</param>
		/// <param name="device">Texture graphics device</param>
		/// <returns>Texture2D representation of the image</returns>
		public static Texture2D ToTexture(this System.Drawing.Image image, GraphicsDevice device)
		{
			Texture2D texture = null;
			using (MemoryStream stream = new MemoryStream())
			{
				image.Save(stream, System.Drawing.Imaging.ImageFormat.Png);
				stream.Seek(0, SeekOrigin.Begin);
				texture = Texture2D.FromStream(device, stream);
			}
			return texture;
		}
	}
}
