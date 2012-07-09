using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using ARCed.Helpers;
using System.Linq;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework;

namespace ARCed.Controls
{
	public class FrameSprite : IDisposable
	{
		Rectangle _rect = Rectangle.Empty;
		Texture2D _texture;

		public bool IsDisposed { get; private set; }
		public RPG.Animation.Frame Frame { get; set; }

		public int Index { get; set; }

		public Texture2D Texture 
		{
			get { return _texture; }
			set
			{
				_texture = value;
				_rect.Width = value.Width;
				_rect.Height = value.Height;
			}
		}

		public Rectangle Rectangle { get { return _rect; } }

		public int Width { get { return _rect.Width; } }
		public int Height { get { return _rect.Height; } }

		public int X 
		{ 
			get { return _rect.X; }
			set { _rect.X = value; }
		}

		public int Y
		{
			get { return _rect.Y; }
			set { _rect.Y = value; }
		}

		public FrameSprite(Texture2D texture, int x, int y)
		{
			this.Texture = texture;
			_rect.X = x;
			_rect.Y = y;
		}

		#region IDisposable Members

		/// <summary>
		/// Releases all resources used by the EnemySprite
		/// </summary>
		public void Dispose()
		{
			Dispose(true);
			GC.SuppressFinalize(this);
			IsDisposed = true;
		}

		protected virtual void Dispose(bool disposing)
		{
			if (disposing)
			{
				if (_texture != null)
					_texture.Dispose();
			}
		}

		~FrameSprite()
		{
			Dispose(false);
		}

		#endregion
	}



	/// <summary>
	/// Control for configuring Troop layouts
	/// </summary>
	public partial class AnimationXnaPanel : GraphicsDeviceControl
	{
		SpriteBatch _batch;
		RPG.Animation _animation;
		Texture2D _texture;
		System.Drawing.Font _font;

		private static Rectangle VIEWPORT;
		private List<FrameSprite> _sprites;

		public List<FrameSprite> Sprites 
		{
			get { return _sprites; }
			set { _sprites = value; }
		}

		public RPG.Animation Animation 
		{
			get { return _animation; }
			set
			{
				if (_animation != value)
				{
					_animation = value;
					Invalidate();
				}
			}
		}

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public AnimationXnaPanel()
		{
			InitializeComponent();
		}

		#endregion

		#region Protected Methods

		/// <summary>
		/// Creates the context and prepares for drawing
		/// </summary>
		protected override void Initialize()
		{
			_sprites = new List<FrameSprite>();
			_font = new System.Drawing.Font("Courier New", 8.25f, System.Drawing.FontStyle.Regular);
			_batch = new SpriteBatch(GraphicsDevice);
			GraphicsDevice.Clear(Color.Black);
			VIEWPORT = new Rectangle(0, 0, 320, 160);
			GraphicsDevice.Viewport = new Viewport(VIEWPORT);
			Disposed += new EventHandler(AnimationXnaPanel_Disposed);
		}

		void AnimationXnaPanel_Disposed(object sender, EventArgs e)
		{
			foreach (FrameSprite sprite in _sprites)
				sprite.Dispose();
			_font.Dispose();
			_batch.Dispose();
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			GraphicsDevice.Clear(Color.Black);

			_batch.Begin();
			DrawBackground();


			Rectangle destRect;
			Rectangle srcRect;
			foreach (FrameSprite sprite in _sprites)
			{
				srcRect = new Rectangle(0, 0, sprite.Width, sprite.Height);
				destRect = new Rectangle(sprite.X / 2, sprite.Y / 2, sprite.Width / 2, sprite.Height / 2);
				_batch.Draw(sprite.Texture, destRect, srcRect, Color.White);
				_batch.DrawRectangle(destRect, Color.Blue, 2);
				_batch.FillTriangle(
					new Vector2(destRect.X, destRect.Y),
					new Vector2(destRect.X + 16, destRect.Y),
					new Vector2(destRect.X, destRect.Y + 16),
					Color.Blue);
				_batch.DrawString(sprite.Index.ToString(), _font, Color.Black, 
					new Rectangle(destRect.X, destRect.Y - 2, 16, 16));
			}
			_batch.End();	
		}

		public void DrawBackground()
		{
			VIEWPORT.X = (Width - 320) / 2;
			VIEWPORT.Y = (Height - 160) / 2;
			_batch.DrawRectangle(VIEWPORT, Color.DarkGreen, 1);
			_batch.DrawRectangle(VIEWPORT.X, VIEWPORT.Y + 80, 320, 1, Color.DarkGreen, 1);
			_batch.DrawRectangle(VIEWPORT.X + 160, VIEWPORT.Y, 1, 160, Color.DarkGreen, 1);
		}

		#endregion

	}
}
