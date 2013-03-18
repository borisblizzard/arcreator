using System;
using System.Collections.Generic;
using System.ComponentModel;
using ARCed.Helpers;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using SysRect = System.Drawing.Rectangle;
using Bitmap = System.Drawing.Bitmap;
using Graphics = System.Drawing.Graphics;
using Size = System.Drawing.Size;

namespace ARCed.Controls
{

	public partial class MapEditorXnaPanel : GraphicsDeviceControl
	{
		#region Private Fields

		private Point _originPoint, _endPoint;

		private bool _selectionEnabled, _selectionActive, _mouseDown;

		private RPG.Map _map;
		private RPG.MapInfo _mapInfo;
		private static Color _backColor;
		private SpriteBatch _batch;
		private Texture2D _srcTexture;
		private Texture2D[][] _autotiles;
		private RPG.Tileset _tileset;

		private static readonly Dictionary<string, Texture2D[]> _autotileCache =
			new Dictionary<string, Texture2D[]>();
		private static readonly int[][] _autoindex = new[] { 
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

		#region Public Properties

		/// <summary>
		/// Gets the rectangle of the selector
		/// </summary>
		[Browsable(false)]
		public Rectangle SelectionRectangle
		{
			get
			{
				int sx = Math.Min(_originPoint.X, _endPoint.X).RoundFloor(Constants.TILESIZE);
				int ex = Math.Max(_originPoint.X, _endPoint.X).RoundCeil(Constants.TILESIZE);
				int sy = Math.Min(_originPoint.Y, _endPoint.Y).RoundFloor(Constants.TILESIZE);
				int ey = Math.Max(_originPoint.Y, _endPoint.Y).RoundCeil(Constants.TILESIZE);
				return new Rectangle(Math.Max(0, sx), Math.Max(0, sy),
					ex - sx + 1, ey - sy + 1);
			}
		}

		/// <summary>
		/// Gets or sets the ability to select regions on the control.
		/// </summary>
		[Browsable(false)]
		public bool SelectionEnabled
		{
			get { return _selectionEnabled; }
			set { _selectionEnabled = value; Invalidate(); }
		}

		/// <summary>
		/// Gets the width of the map in pixels. 
		/// Based off the number of tiles and size of the tiles.
		/// </summary>
		[Browsable(false)]
		public int MapPixelWidth
		{
			get { return _map.width * Constants.TILESIZE; }
		}

		/// <summary>
		/// Gets the height of the map in pixels. 
		/// Based off the number of tiles and size of the tiles.
		/// </summary>
		[Browsable(false)]
		public int MapPixelHeight
		{
			get { return _map.height * Constants.TILESIZE; }
		}

		/// <summary>
		/// Gets the map rectangle in pixels. 
		/// Based off the number of tiles and size of the tiles.
		/// </summary>
		[Browsable(false)]
		public Rectangle MapRect
		{
			get { return new Rectangle(0, 0, MapPixelWidth, MapPixelHeight);}
		}

		/// <summary>
		/// Gets or sets the associates <see cref="RPG.Map"/> object of the panel.
		/// </summary>
		[Browsable(false)]
		public RPG.Map Map
		{
			get { return _map; }
			set { this.LoadNewMap(value); }
		}

		/// <summary>
		/// Gets or sets the associates <see cref="RPG.MapInfo"/> object of the panel.
		/// </summary>
		[Browsable(false)]
		public RPG.MapInfo MapInfo
		{
			get { return _mapInfo; }
			set 
			{ 
				_mapInfo = value;
				Invalidate();
			}
		}

		#endregion

		#region Constructor

		/// <summary>
		/// Creates and returns a new instance of a <see cref="MapEditorXnaPanel"/>.
		/// </summary>
		public MapEditorXnaPanel()
		{
			_selectionEnabled = true;
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
			_autotiles = new Texture2D[Constants.AUTOTILES + 1][];
			_backColor = Color.Black;
			Disposed += MapEditorXnaPanelDisposed;
			MouseDown += this.MapEditorXnaPanelMouseDown;
			MouseMove += this.MapEditorXnaPanelMouseMove;
			MouseUp += this.MapEditorXnaPanelMouseUp;
			ResetPoints();
		}

		/// <summary>
		/// Creates an internal texture used for blit operations from the autotile graphic.
		/// </summary>
		/// <param name="filename">Filename of the autotile graphic</param>
		/// <returns>A 48 element array of <see cref="Texture2D"/> objects.</returns>
		public Texture2D[] CreateAutotile(string filename)
		{
			const int w = Constants.TILESIZE;
			const int hw = Constants.TILESIZE / 2;
			var data = new Texture2D[48];
			var autotile = Cache.Autotile(filename);
			if (autotile == null)
				return data;
			int x, y, num, index, sx, sy;
			SysRect destRect, srcRect;
			for (var frame = 0; frame < (autotile.Width / 96); frame++)
			{
				using (var template = new Bitmap(256, 192))
				{
					for (var lvl = 0; lvl < 6; lvl++)
					{
						for (var j = 0; j < 8; j++)
						{
							using (var g = Graphics.FromImage(template))
							{
								foreach (var number in _autoindex[8 * lvl + j])
								{
									num = number - 1;
									x = 16 * (num % 6);
									y = 16 * (num / 6);
									srcRect = new SysRect(x + (frame * 96), y, hw, hw);
									destRect = new SysRect(w * j + x % w, w * lvl + y % w, hw, hw); 
									g.DrawImage(autotile, destRect, srcRect, System.Drawing.GraphicsUnit.Pixel);
								}
							}
							index = 8 * lvl + j;
							using (var b = new Bitmap(w, w))
							{
								sx = w * (index % 8);
								sy = w * (index / 8);
								srcRect = new SysRect(sx, sy, w, w);
								using (var g = Graphics.FromImage(b))
									g.DrawImage(template, new SysRect(0, 0, w, w), srcRect, System.Drawing.GraphicsUnit.Pixel);
								data[index] = b.ToTexture(GraphicsDevice);
							}
						}
					}
				}
			}
			return data;
		}

		/// <summary>
		/// Performs painting of the control
		/// </summary>
		protected override void Draw()
		{
			GraphicsDevice.Clear(_backColor);
			const float mod = Constants.MAP_LAYERS + Constants.PRIORITIES;
			if (_map == null) return;
			_batch.Begin(SpriteSortMode.FrontToBack, BlendState.AlphaBlend);
			int tileId;
			float depth;
			Rectangle srcRect, destRect;
			for (int z = 0; z < Constants.MAP_LAYERS; z++)
			{
				for (int y = 0; y < _map.height; y++)
				{
					for (int x = 0; x < _map.width; x++)
					{
						tileId = _map.data[x, y, z];
						depth = (_tileset.priorities[tileId] + z) / mod;
						destRect = new Rectangle
						{
							X = x * Constants.TILESIZE,
							Y = y * Constants.TILESIZE,
							Width = Constants.TILESIZE,
							Height = Constants.TILESIZE
						};
						if (tileId >= Constants.AUTO_IDS)
						{
							srcRect = new Rectangle
							{
								X = ((tileId - Constants.AUTO_IDS) % 8) * Constants.TILESIZE,
								Y = ((tileId - Constants.AUTO_IDS) / 8) * Constants.TILESIZE,
								Width = Constants.TILESIZE,
								Height = Constants.TILESIZE
							};
							_batch.Draw(_srcTexture, destRect, srcRect, Color.White, 0.0f, Vector2.Zero,
								SpriteEffects.None, depth);
						}
						else
						{
							int index = tileId / 48;
							if (index == 0) continue;
							Texture2D src = _autotiles[index][tileId % 48];
							if (src != null)
								_batch.Draw(src, destRect, src.Bounds, Color.White, 0.0f, Vector2.Zero,
								SpriteEffects.None, depth);
						}
					}
				}
			}
			_batch.End();
			if (SelectionEnabled && _originPoint != _endPoint)
			{
				_batch.Begin(SpriteSortMode.Immediate, BlendState.AlphaBlend);
				_batch.DrawSelectionRect(SelectionRectangle, Color.White, 2);
				_batch.End();
			}
		}

		#endregion

		private void ResetPoints()
		{
			_originPoint = _endPoint = new Point(-1, -1);
		}

		#region Mouse Events

		private void MapEditorXnaPanelMouseUp(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			_mouseDown = false;
			_selectionActive = false;
		}

		private void MapEditorXnaPanelMouseDown(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			_mouseDown = true;
			ResetPoints();
			if (SelectionEnabled)
			{
				_originPoint.X = _endPoint.X = e.X;
				_originPoint.Y = _endPoint.Y = e.Y;
				_selectionActive = true;
				Invalidate();
			}
			/*
			else if (!this.SelectionEnabled)
				this.ChangeData(e);
			else if (this.SelectionRectangle.Contains(e.X, e.Y))
			{
				foreach (int id in this.SelectedTileIds)
				{
					Vector2 vector = this.GetTileVector(id);
					this.ChangeData(new MouseEventArgs(e.Button, 1,
						(int)vector.X + (e.X % Constants.TILESIZE),
						(int)vector.Y + (e.Y % Constants.TILESIZE),
						0));
				}
			}
			 */
		}

		private void MapEditorXnaPanelMouseMove(object sender, System.Windows.Forms.MouseEventArgs e)
		{
			if (_map != null)
			{
				int x = e.X.Clamp(0, Width);
				int y = e.Y.Clamp(0, Height);
				if (SelectionEnabled && _mouseDown && _selectionActive)
				{
					_endPoint.X = x;
					_endPoint.Y = y;
				}
				Invalidate();
			}
		}

		#endregion

		private void MapEditorXnaPanelDisposed(object sender, System.EventArgs e)
		{
			if (!_batch.IsDisposed) _batch.Dispose();
			if (!_srcTexture.IsDisposed) _srcTexture.Dispose();
		}

		private void LoadNewMap(RPG.Map map)
		{
			_map = map;
			if (map == null)
			{
				Invalidate();
				return;
			}
			_tileset = Project.Data.Tilesets[_map.tileset_id];
			Size = new Size(MapPixelWidth, MapPixelHeight);
			_srcTexture = Cache.Tileset(_tileset.tileset_name).ToTexture(GraphicsDevice);
			_autotiles[0] = null;
			for (int i = 1; i <= _tileset.autotile_names.Count; i++)
			{
				string name = _tileset.autotile_names[i - 1];
				if (!_autotileCache.ContainsKey(name))
					_autotileCache[name] = CreateAutotile(name);
				_autotiles[i] = _autotileCache[name];
			}
			Invalidate();
		}

	}
}
