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
	public partial class AnimationXnaPanel : GraphicsDeviceControl
	{
		SpriteBatch _batch;
		RPG.Animation _animation;
		Texture2D _texture;

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
			_batch = new SpriteBatch(GraphicsDevice);
			GraphicsDevice.Clear(Color.Black);
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			GraphicsDevice.Clear(Color.Black);
			if (_texture != null)
			{

			}
		}

		#endregion

	}
}
