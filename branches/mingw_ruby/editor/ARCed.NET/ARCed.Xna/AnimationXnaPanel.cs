#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using RPG;
using Color = Microsoft.Xna.Framework.Color;
using Rectangle = Microsoft.Xna.Framework.Rectangle;

#endregion

namespace ARCed.Controls
{
	public class FrameSprite : IDisposable
	{
		Rectangle _rect = Rectangle.Empty;
		Texture2D _texture;

		public bool IsDisposed { get; private set; }
		public Animation.Frame Frame { get; set; }

		public int Index { get; set; }

		public Texture2D Texture 
		{
			get { return this._texture; }
			set
			{
				this._texture = value;
				this._rect.Width = value.Width;
				this._rect.Height = value.Height;
			}
		}

		public Rectangle Rectangle { get { return this._rect; } }

		public int Width { get { return this._rect.Width; } }
		public int Height { get { return this._rect.Height; } }

		public int X 
		{ 
			get { return this._rect.X; }
			set { this._rect.X = value; }
		}

		public int Y
		{
			get { return this._rect.Y; }
			set { this._rect.Y = value; }
		}

		public FrameSprite(Texture2D texture, int x, int y)
		{
			this.Texture = texture;
			this._rect.X = x;
			this._rect.Y = y;
		}

		#region IDisposable Members

		/// <summary>
		/// Releases all resources used by the EnemySprite
		/// </summary>
		public void Dispose()
		{
			this.Dispose(true);
			GC.SuppressFinalize(this);
			this.IsDisposed = true;
		}

		protected virtual void Dispose(bool disposing)
		{
			if (disposing)
			{
				if (this._texture != null)
					this._texture.Dispose();
			}
		}

		~FrameSprite()
		{
			this.Dispose(false);
		}

		#endregion
	}



	/// <summary>
	/// Control for configuring Troop layouts
	/// </summary>
	public partial class AnimationXnaPanel : GraphicsDeviceControl
	{
		SpriteBatch _batch;
		Animation _animation;
		Texture2D _texture;
		Font _font;

		private static Rectangle VIEWPORT;
		private List<FrameSprite> _sprites;

		public List<FrameSprite> Sprites 
		{
			get { return this._sprites; }
			set { this._sprites = value; }
		}

		public Animation Animation 
		{
			get { return this._animation; }
			set
			{
				if (this._animation != value)
				{
					this._animation = value;
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
			this.InitializeComponent();
		}

		#endregion

		#region Protected Methods

		/// <summary>
		/// Creates the context and prepares for drawing
		/// </summary>
		protected override void Initialize()
		{
			this._sprites = new List<FrameSprite>();
			this._font = new Font("Courier New", 8.25f, FontStyle.Regular);
			this._batch = new SpriteBatch(GraphicsDevice);
			GraphicsDevice.Clear(Color.Black);
			VIEWPORT = new Rectangle(0, 0, 320, 160);
			Disposed += this.AnimationXnaPanel_Disposed;
		}

		void AnimationXnaPanel_Disposed(object sender, EventArgs e)
		{
			foreach (FrameSprite sprite in this._sprites)
				sprite.Dispose();
			this._font.Dispose();
			this._batch.Dispose();
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			GraphicsDevice.Clear(Color.Black);

			this._batch.Begin();
			this.DrawBackground();


			Rectangle destRect;
			Rectangle srcRect;
			foreach (FrameSprite sprite in this._sprites)
			{
				srcRect = new Rectangle(0, 0, sprite.Width, sprite.Height);
				destRect = new Rectangle(sprite.X / 2, sprite.Y / 2, sprite.Width / 2, sprite.Height / 2);
				this._batch.Draw(sprite.Texture, destRect, srcRect, Color.White);
				this._batch.DrawRectangle(destRect, Color.Blue, 2);
				this._batch.FillTriangle(
					new Vector2(destRect.X, destRect.Y),
					new Vector2(destRect.X + 16, destRect.Y),
					new Vector2(destRect.X, destRect.Y + 16),
					Color.Blue);
				this._batch.DrawString(sprite.Index.ToString(), this._font, Color.Black, 
					new Rectangle(destRect.X, destRect.Y - 2, 16, 16));
			}
			this._batch.End();	
		}

		public void DrawBackground()
		{
			VIEWPORT.X = (Width - 320) / 2;
			VIEWPORT.Y = (Height - 160) / 2;
			this._batch.DrawRectangle(VIEWPORT, Color.DarkGreen, 1);
			this._batch.DrawRectangle(VIEWPORT.X, VIEWPORT.Y + 80, 320, 1, Color.DarkGreen, 1);
			this._batch.DrawRectangle(VIEWPORT.X + 160, VIEWPORT.Y, 1, 160, Color.DarkGreen, 1);
		}

		#endregion

	}
}
