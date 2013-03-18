#region Using Directives

using System.ComponentModel;
using System.Windows.Forms;
using ARCed.Helpers;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using RPG;
using Color = Microsoft.Xna.Framework.Color;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// Control for selecting individual Animation graphics.
	/// </summary>
	[Description("Control for selecting individual Animation graphics.")]
	public partial class AnimationSourceXnaPanel : GraphicsDeviceControl
	{
		SpriteBatch _batch;
		Animation _animation;
		Texture2D _srcTexture;
		int _frames, _selectedId;
		Rectangle srcRect, destRect;

		/// <summary>
		/// Gets or sets the ID of the selected sub-image of the animation.
		/// </summary>
		[Browsable(false)]
		public int SelectedId
		{
			get { return this._selectedId; }
			set 
			{
				this._selectedId = value;
				Invalidate();
			}
		}

		/// <summary>
		/// Gets or sets the associated RPG.Animation for the panel.
		/// </summary>
		[Browsable(false)]
		public Animation Animation 
		{
			get { return this._animation; }
			set
			{
				if (this._animation != value)
				{
					this._animation = value;
					this.RefreshTexture();
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
			this.InitializeComponent();
		}

		#endregion

		#region Protected Methods

		/// <summary>
		/// Creates the context and prepares for drawing
		/// </summary>
		protected override void Initialize()
		{
			this._batch = new SpriteBatch(GraphicsDevice);
			this._selectedId = -1;
            // TODO: Edit this
            GraphicsDevice.Clear(TilesetXnaPanel.Settings.BackgroundColor);
			MouseDown += this.AnimationSourceXnaPanel_MouseDown;
		}

		void AnimationSourceXnaPanel_MouseDown(object sender, MouseEventArgs e)
		{
			if (this._frames > 0)
				this.SelectedId = e.X / (Width / this._frames);
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			GraphicsDevice.Clear(TilesetXnaPanel.Settings.BackgroundColor);
			if (this._srcTexture != null)
			{
				int dim = Parent.ClientSize.Height;
				Width = dim * this._frames;
				int x, y;
				this._batch.Begin();
				for (int i = 0; i < this._frames; i++)
				{
					x = (i % (this._srcTexture.Width / Constants.ANIMESIZE)) * Constants.ANIMESIZE;
					y = (i / (this._srcTexture.Width / Constants.ANIMESIZE)) * Constants.ANIMESIZE;
					this.srcRect = new Rectangle(x, y, Constants.ANIMESIZE, Constants.ANIMESIZE);
					this.destRect = new Rectangle(i * dim, 0, dim, dim);
					this._batch.Draw(this._srcTexture, this.destRect, this.srcRect, Color.White);
					this._batch.DrawRectangle(i * dim - 1, 0, 1, dim + 1, Color.Black, 1);
					if (this.SelectedId >= 0)
					{
						var rect = new Rectangle(this.SelectedId * dim - 1, 0, dim + 1, dim);
						this._batch.DrawSelectionRect(rect, Color.White, 2);
					}
				}
				this._batch.End();
			}
		}

		private void RefreshTexture()
		{
			using (var image = Cache.Animation(this._animation.animation_name, this._animation.animation_hue))
			{
				if (image == null)
				{
					this._srcTexture = null;
					this._frames = 0;
					Visible = false;
					return;
				}
				Visible = true;
				this._frames = (image.Width / Constants.ANIMESIZE) * (image.Height / Constants.ANIMESIZE);
				this._srcTexture = image.ToTexture(GraphicsDevice);
			}
		}

		#endregion

	}
}
