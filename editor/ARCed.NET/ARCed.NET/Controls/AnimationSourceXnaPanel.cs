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
	/// Control for selecting individual Animation graphics.
	/// </summary>
	[Description("Control for selecting individual Animation graphics.")]
	public partial class AnimationSourceXnaPanel : GraphicsDeviceControl
	{
		SpriteBatch _batch;
		RPG.Animation _animation;
		Texture2D _srcTexture;
		int _frames, _selectedId;
		Rectangle srcRect, destRect;

		/// <summary>
		/// Gets or sets the ID of the selected sub-image of the animation.
		/// </summary>
		[Browsable(false)]
		public int SelectedId
		{
			get { return _selectedId; }
			set 
			{
				_selectedId = value;
				Invalidate();
			}
		}

		/// <summary>
		/// Gets or sets the associated RPG.Animation for the panel.
		/// </summary>
		[Browsable(false)]
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
			_selectedId = -1;
			GraphicsDevice.Clear(Editor.Settings.ImageColorSettings.BackgroundColor);
			this.MouseDown += new System.Windows.Forms.MouseEventHandler(AnimationSourceXnaPanel_MouseDown);
		}

		void AnimationSourceXnaPanel_MouseDown(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			if (_frames > 0)
				SelectedId = e.X / (this.Width / _frames);
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			GraphicsDevice.Clear(Editor.Settings.ImageColorSettings.BackgroundColor);
			if (_srcTexture != null)
			{
				int dim = Parent.ClientSize.Height;
				this.Width = dim * _frames;
				int x, y;
				_batch.Begin();
				for (int i = 0; i < _frames; i++)
				{
					x = (i % (_srcTexture.Width / Constants.ANIMESIZE)) * Constants.ANIMESIZE;
					y = (i / (_srcTexture.Width / Constants.ANIMESIZE)) * Constants.ANIMESIZE;
					srcRect = new Rectangle(x, y, Constants.ANIMESIZE, Constants.ANIMESIZE);
					destRect = new Rectangle(i * dim, 0, dim, dim);
					_batch.Draw(_srcTexture, destRect, srcRect, Color.White);
					_batch.DrawRectangle(i * dim - 1, 0, 1, dim + 1, Color.Black, 1);
					if (SelectedId >= 0)
					{
						Rectangle rect = new Rectangle(SelectedId * dim - 1, 0, dim + 1, dim);
						_batch.DrawSelectionRect(rect, Color.White, 2);
					}
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
					_srcTexture = null;
					_frames = 0;
					this.Visible = false;
					return;
				}
				this.Visible = true;
				_frames = (image.Width / Constants.ANIMESIZE) * (image.Height / Constants.ANIMESIZE);
				_srcTexture = image.ToTexture(GraphicsDevice);
			}
		}

		#endregion

	}
}
