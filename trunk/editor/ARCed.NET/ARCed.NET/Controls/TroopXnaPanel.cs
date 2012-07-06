using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using ARCed.Helpers;
using Microsoft.Xna.Framework.Graphics;
using Vector2 = Microsoft.Xna.Framework.Vector2;
using XnaColor = Microsoft.Xna.Framework.Color;
using XnaRect = Microsoft.Xna.Framework.Rectangle;

namespace ARCed.Controls
{
	/// <summary>
	/// Class representing a sprite in the Editor's Troop panel
	/// </summary>
	public class EnemySprite : IComparable, IDisposable
	{
		#region Private Fields

		private bool _selected;
		private Image _image;
		private Pen pen = new Pen(Color.White, 2);
		private RPG.Troop.Member _member;

		#endregion

		#region Events

		public delegate void SelectionChangedHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised when the sprite selection changes.
		/// </summary>
		public event SelectionChangedHandler OnSelectionChanged;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets or sets the GraphicsDevice associated with the sprite
		/// </summary>
		public GraphicsDevice GraphicsDevice { get; set; }
		/// <summary>
		/// Gets or sets the sprites associated image
		/// </summary>
		public Image Image 
		{ 
			get { return _image; }
			set { _image = value; }
		}
		/// <summary>
		/// Gets the sprites texture
		/// </summary>
		public Texture2D Texture { get { return Image.ToTexture(GraphicsDevice); } }
		/// <summary>
		/// Gets a vector that represents the sprites location
		/// </summary>
		public Microsoft.Xna.Framework.Vector2 Vector
		{
			get { return new Microsoft.Xna.Framework.Vector2(X, Y); } 
		}
		/// <summary>
		/// Gets or sets the X-coordinate of the sprite
		/// </summary>
		public int X 
		{
			get { return _member.x - (Width / 2); }
			set { _member.x = value + (Width / 2); }
		}
		/// <summary>
		/// Gets or sets the Y-coordinate of the sprite
		/// </summary>
		public int Y 
		{
			get { return _member.y - Height; }
			set { _member.y = value + Height; }
		}
		/// <summary>
		/// Gets or sets the selected flag of the sprite
		/// </summary>
		public bool Selected 
		{
			get { return _selected; }
			set
			{
				_selected = value;
				if (OnSelectionChanged != null)
					OnSelectionChanged(this, new EventArgs());
			}
		}
		/// <summary>
		/// Gets or sets the moving flag of the sprite
		/// </summary>
		public bool Moving { get; set; }
		/// <summary>
		/// Gets the width of the sprite
		/// </summary>
		public int Width { get { return Image.Width; } }
		/// <summary>
		/// Gets the height of the sprite
		/// </summary>
		public int Height { get { return Image.Height; } }
		/// <summary>
		/// Gets the rectangle of the sprite
		/// </summary>
		public XnaRect Rectangle 
		{ 
			get { return new XnaRect(X, Y, Image.Width, Image.Height); } 
		}
		/// <summary>
		/// Gets or sets the immortal status of the RPG.Troop.Member
		/// </summary>
		public bool Immortal 
		{ 
			get { return _member.immortal; } 
			set { _member.immortal = value; } 
		}
		/// <summary>
		/// Gets or sets the hidden status of the RPG.Troop.Member
		/// </summary>
		public bool Hidden 
		{ 
			get { return _member.hidden; } 
			set {_member.hidden = value; } 
		}
		/// <summary>
		/// Gets the ID of the enemy the sprite represents
		/// </summary>
		public int EnemyId 
		{ 
			get { return _member.enemy_id; }  
		}
		/// <summary>
		/// Gets or sets the RPG.Troop.Member the sprite represents
		/// </summary>
		public RPG.Troop.Member TroopMember
		{
			get { return _member; }
			set { _member = value; }
		}
		/// <summary>
		/// Gets the disposed status of the sprite
		/// </summary>
		public bool IsDisposed { get; private set; }

		#endregion

		#region Construction

		/// <summary>
		/// Create EnemySprite instance from an RPG.Enemy instance
		/// </summary>
		/// <param name="enemy">RPG.Enemy instance to create from</param>
		public EnemySprite(RPG.Enemy enemy) 
		{
			Image = Cache.Battler(enemy.battler_name, enemy.battler_hue);
			_member = new RPG.Troop.Member();
			_member.enemy_id = enemy.id;
			_selected = false;
			Moving = false;
		}

		/// <summary>
		/// Create EnemySprite instance from an RPG.Troop.Member instance
		/// </summary>
		/// <param name="member">RPG.Troop.Member instance to create from</param>
		public EnemySprite(RPG.Troop.Member member)
		{
			RPG.Enemy enemy = Project.Data.Enemies[member.enemy_id];
			Image = Cache.Battler(enemy.battler_name, enemy.battler_hue);
			_member = member;
			_selected = false;
			Moving = false;
		}

		/// <summary>
		/// Create EnemySprite instance from the ID of an RPG.Enemy 
		/// </summary>
		/// <param name="enemy">ID of an RPG.Enemy to create from</param>
		public EnemySprite(int enemyId)
		{
			RPG.Enemy enemy = Project.Data.Enemies[enemyId];
			Image = Cache.Battler(enemy.battler_name, enemy.battler_hue);
			_member = new RPG.Troop.Member();
			_selected = false;
			Moving = false;
		}

		#endregion

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
				if (_image != null)
					_image.Dispose();
				if (pen != null)
					pen.Dispose();
			}
		}

		~EnemySprite()
		{
			Dispose(false);
		}

		#endregion

		#region IComparable Members

		/// <summary>
		/// Compares two EnemySprite objects.
		/// </summary>
		/// <param name="other">EnemySprite object to compare</param>
		/// <returns>Indication of their relative values</returns>
		/// <exception cref="ArgumentException">Thrown when object to compare is not a EnemySprite</exception>
		public int CompareTo(object other)
		{
			EnemySprite sprite;
			if (other is EnemySprite)
				sprite = other as EnemySprite;
			else
				throw new ArgumentException("Object is not of type \"EnemySprite\"");
			return this.Rectangle.Bottom.CompareTo(sprite.Rectangle.Bottom);
		}

		/// <summary>
		/// Compares two instances of EnemySprite objects and returns 
		/// an indication of their relative values.
		/// </summary>
		/// <param name="obj1">First EnemySprite object to compare.</param>
		/// <param name="obj2">Second EnemySprite object to compare.</param>
		/// <returns>Indication of relative values</returns>
		public static int Compare(object obj1, object obj2)
		{
			return new EnemySpriteComparer().Compare(obj1, obj2);
		}

		private class EnemySpriteComparer : IComparer<object>
		{
			public int Compare(object obj1, object obj2)
			{
				EnemySprite sprite1, sprite2;
				if (obj1 is EnemySprite)
					sprite1 = obj1 as EnemySprite;
				else
					throw new ArgumentException("Object is not of type \"EnemySprite\"");
				if (obj2 is EnemySprite)
					sprite2 = obj2 as EnemySprite;
				else
					throw new ArgumentException("Object is not of type \"EnemySprite\"");
				return sprite1.CompareTo(sprite2);
			}
		}

		#endregion
	}

	/// <summary>
	/// Control for configuring Troop layouts
	/// </summary>
	public partial class TroopXnaPanel : GraphicsDeviceControl
	{
		#region Private Fields

		private static XnaColor _hiddenColor;
		Texture2D _background;
		SpriteBatch _batch;
		List<EnemySprite> _sprites;
		bool _mouseDown;
		int _lastX, _lastY, _moveX, _moveY;

		#endregion

		#region Events

		public delegate void OnSelectHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised whenever the selected status of a sprite is changed.
		/// </summary>
		[Category("ARCed"), Description("Raised whenever the selected status of a sprite is changed.")]
		public event OnSelectHandler OnSelectionChanged;

		public delegate void TroopChangedHandler(object sender, EventArgs e);
		/// <summary>
		/// Event raised whenever the troop is modified.
		/// </summary>
		[Category("ARCed"), Description("Raised whenever the troop is modified.")]
		public event TroopChangedHandler OnTroopChanged;

		#endregion

		#region Public Properties

		/// <summary>
		/// Gets the collection of sprites on the control
		/// </summary>
		[Browsable(false)]
		public List<EnemySprite> Sprites { get { return _sprites; } }

		/// <summary>
		/// Gets the selected sprite or null if one are selected
		/// </summary>
		[Browsable(false)]
		public EnemySprite SelectedSprite 
		{
			get 
			{
				return _sprites.Find(delegate(EnemySprite s) { return s.Selected; });
			}
		}

		#endregion

		#region Construction

		/// <summary>
		/// Default constructor
		/// </summary>
		public TroopXnaPanel()
		{
			InitializeComponent();
			Disposed += new EventHandler(TroopXnaPanel_Disposed);
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Aligns all sprites in an even row on the panel
		/// </summary>
		public void AutoAlign()
		{
			if (_sprites.Count == 0)
				return;
			int width = 0;
			foreach (EnemySprite sprite in _sprites)
				width += sprite.Width;
			int left = Math.Max((_background.Width - width) / 2, 0);
			int max = _background.Width / _sprites.Count;
			for (int i = 0; i < _sprites.Count; i++)
			{
				_sprites[i].X = left;
				left += Math.Min(_sprites[i].Width, max);
				_sprites[i].Y = 300 - _sprites[i].Height;
			}

			Invalidate();
		}

		/// <summary>
		/// Adds a sprite to the collection for drawing from an RPG.Troop.Member instance
		/// </summary>
		/// <param name="member">RPG.Troop.Member instance to add sprite from</param>
		public void AddSprite(RPG.Troop.Member member)
		{
			AddSprite(new EnemySprite(member));
		}

		/// <summary>
		/// Adds a sprite to the collection for drawing
		/// </summary>
		/// <param name="sprite">Sprite to add</param>
		public void AddSprite(EnemySprite sprite)
		{
			if (sprite.GraphicsDevice == null)
				sprite.GraphicsDevice = GraphicsDevice;
			sprite.OnSelectionChanged += new EnemySprite.SelectionChangedHandler(sprite_OnSelectionChanged);
			if (sprite.X < 0 && sprite.Y < 0)
			{
				sprite.X = (_background.Width - sprite.Width) / 2;
				sprite.Y = (_background.Height - sprite.Height) / 2;
			}
			_sprites.Add(sprite);
			Invalidate();
			if (OnTroopChanged != null)
				OnTroopChanged(this, new EventArgs());
		}

		/// <summary>
		/// Disposes and removes the selected sprites
		/// </summary>
		public void RemoveSelected()
		{
			var selected = _sprites.FindAll(delegate(EnemySprite s) { return s.Selected; });
			foreach (EnemySprite sprite in selected)
			{
				sprite.Selected = false;
				sprite.Dispose();
			}
			_sprites.RemoveAll(delegate(EnemySprite s) { return s.IsDisposed; });
			Invalidate();
			if (OnTroopChanged != null)
				OnTroopChanged(this, new EventArgs());
		}

		/// <summary>
		/// Disposed and removes the specified sprite
		/// </summary>
		/// <param name="sprite">EnemySprite to remove</param>
		public void RemoveSprite(EnemySprite sprite)
		{
			_sprites.Remove(sprite);
			sprite.Dispose();
			Invalidate();
			if (OnTroopChanged != null)
				OnTroopChanged(this, new EventArgs());
		}

		/// <summary>
		/// Sets the background image to use for the control
		/// </summary>
		/// <param name="image">Image file</param>
		public void SetBackground(Image image)
		{
			_background = image.ToTexture(GraphicsDevice);
			this.Size = image.Size;
			Invalidate();
		}

		/// <summary>
		/// Sets the filepath to the background image to use for the control
		/// </summary>
		/// <param name="path">Path to the image file.</param>
		public void SetBackground(string path)
		{
			using (Stream str = File.OpenRead(path))
				_background = Texture2D.FromStream(GraphicsDevice, str);
			this.Size = new System.Drawing.Size(_background.Width, _background.Height);
			Invalidate();
		}

		/// <summary>
		/// Disposes and removes all sprites from the control. 
		/// </summary>
		public void RemoveAll()
		{
			foreach (EnemySprite sprite in _sprites)
				sprite.Dispose();
			_sprites.Clear();
			Invalidate();
		}

		#endregion

		#region Protected Methods

		/// <summary>
		/// Creates the context and prepares for drawing
		/// </summary>
		protected override void Initialize()
		{
			_sprites = new List<EnemySprite>();
			_batch = new SpriteBatch(GraphicsDevice);
			GraphicsDevice.Clear(XnaColor.Gray);
			_hiddenColor = new XnaColor(80, 80, 80, 60);
			this.MouseDown += new System.Windows.Forms.MouseEventHandler(TroopXnaPanel_MouseDown);
			this.MouseUp += new System.Windows.Forms.MouseEventHandler(TroopXnaPanel_MouseUp);
			this.MouseMove += new System.Windows.Forms.MouseEventHandler(TroopXnaPanel_MouseMove);
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			if (_background != null)
			{
				GraphicsDevice.Clear(XnaColor.Gray);
				_batch.Begin();
				_batch.Draw(_background, new Vector2(0, 0), XnaColor.White);
				_sprites.Sort();
				foreach (EnemySprite sprite in _sprites)
				{
					_batch.Draw(sprite.Texture, sprite.Vector, 
						sprite.Hidden ? _hiddenColor : XnaColor.White);
					if (sprite.Selected)
						_batch.DrawRectangle(sprite.Rectangle, XnaColor.White, 2);
				}
				_batch.End();
			}
		}

		#endregion

		#region Private Methods

		private void sprite_OnSelectionChanged(object sender, EventArgs e)
		{
			if (OnSelectionChanged != null)
				OnSelectionChanged(sender, e);
		}

		private void TroopXnaPanel_Disposed(object sender, EventArgs e)
		{
			foreach (EnemySprite sprite in _sprites)
			{
				if (sprite != null)
					sprite.Dispose();
			}
		}

		private void TroopXnaPanel_MouseMove(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			if (_mouseDown)
			{
				_moveX = e.X - _lastX;
				_moveY = e.Y - _lastY;
				_lastX = e.X;
				_lastY = e.Y;
				foreach (EnemySprite sprite in _sprites)
				{	
					if (sprite.Selected)
					{
						sprite.Moving = true;
						sprite.X += _moveX;
						sprite.Y += _moveY;
						sprite.X = sprite.X.Clamp(-sprite.Width + 16, _background.Width - 16);
						sprite.Y = sprite.Y.Clamp(-sprite.Height + 16, _background.Height - 16);
					}
				}
				Invalidate();
			}
		}

		private void TroopXnaPanel_MouseUp(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			_mouseDown = false;
			foreach (EnemySprite sprite in _sprites)
			{
				if (sprite.Moving)
				{
					sprite.Moving = false;
					sprite.Selected = true;
					if (OnTroopChanged != null)
						OnTroopChanged(this, new EventArgs());
				}
			}
			Invalidate();
		}

		private void TroopXnaPanel_MouseDown(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			_mouseDown = true;
			_lastX = e.X;
			_lastY = e.Y;
			bool found = false;
			_sprites.Reverse();
			foreach (EnemySprite sprite in _sprites)
			{
				if (sprite.Rectangle.Contains(e.X, e.Y) && !found)
					sprite.Selected = found = true;
				else
					sprite.Selected = false;
			}
			Invalidate();
		}

		#endregion
	}
}
