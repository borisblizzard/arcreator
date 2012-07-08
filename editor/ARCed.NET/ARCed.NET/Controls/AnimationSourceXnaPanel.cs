using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;
using ARCed.Helpers;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework;

namespace ARCed.Controls
{

	/// <summary>
	/// Control for configuring Troop layouts
	/// </summary>
	public partial class AnimationSourceXnaPanel : GraphicsDeviceControl
	{
		SpriteBatch _batch;
		RPG.Animation _animation;
		Texture2D _texture;
		int _frames;

		public RPG.Animation Animation 
		{
			get { return _animation; }
			set
			{
				if (_animation != value)
				{
					_animation = value;
					RefreshTexture();
					Invalidate();
				}
			}
		}

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public AnimationSourceXnaPanel()
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
			_batch = new SpriteBatch(GraphicsDevice);
			GraphicsDevice.Clear(Color.DarkGray);
			//this.SizeChanged += new EventHandler(AnimationSourceXnaPanel_SizeChanged);
		}

		void AnimationSourceXnaPanel_SizeChanged(object sender, EventArgs e)
		{

			if (_texture != null)
			{
				int width = this.Height * _frames;
				if (this.Width != width)
				{
					this.SuspendLayout();
					this.Width = width;
					this.ResumeLayout(true);
					(this.Parent as System.Windows.Forms.Panel).Refresh();
				}
			}
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			GraphicsDevice.Clear(Color.White);
			if (_texture != null)
			{
				this.Width = this.Height * _frames;
				int dim = this.Height;
				Rectangle srcRect;
				Rectangle destRect;
				int x, y;
				_batch.Begin();
				for (int i = 0; i < _frames; i++)
				{
					x = (i * Constants.ANIMATIONSIZE) % _texture.Width;
					y = (i * Constants.ANIMATIONSIZE) / _texture.Height;
					srcRect = new Rectangle(x, y, Constants.ANIMATIONSIZE, Constants.ANIMATIONSIZE);
					destRect = new Rectangle(i * dim, 0, dim, dim);
					_batch.Draw(_texture, destRect, srcRect, Color.White);
					_batch.DrawRectangle(i * dim - 1, 0, 1, dim, Color.Black, 1);
				}
				_batch.End();
			}
		}

		private void RefreshTexture()
		{
			using (var image = Cache.Animation(_animation.animation_name, _animation.animation_hue))
			{
				if (image == null)
				{
					_texture = null;
					return;
				}
				_frames = (image.Width / Constants.ANIMATIONSIZE) + (image.Height / Constants.ANIMATIONSIZE);
				this.Width = (this.Height * _frames);
				_texture = image.ToTexture(GraphicsDevice);
			}
		}

		#endregion

	}
}
