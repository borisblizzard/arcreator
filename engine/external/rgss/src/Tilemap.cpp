#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/harray.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#include "Bitmap.h"
#include "CodeSnippets.h"
#include "Graphics.h"
#include "RGSSError.h"
#include "SystemSprite.h"
#include "Table.h"
#include "Tilemap.h"
#include "Viewport.h"

#define TILE_SIZE 32

namespace rgss
{
	VALUE rb_cTilemap;

	static int _autotiles[6][8][4] = {
		{{27, 28, 33, 34}, { 5, 28, 33, 34}, {27,  6, 33, 34}, { 5,  6, 33, 34},
		 {27, 28, 33, 12}, { 5, 28, 33, 12}, {27,  6, 33, 12}, { 5,  6, 33, 12}},
		{{27, 28, 11, 34}, { 5, 28, 11, 34}, {27,  6, 11, 34}, { 5,  6, 11, 34},
		 {27, 28, 11, 12}, { 5, 28, 11, 12}, {27,  6, 11, 12}, { 5,  6, 11, 12}},
		{{25, 26, 31, 32}, {25,  6, 31, 32}, {25, 26, 31, 12}, {25,  6, 31, 12},
		 {15, 16, 21, 22}, {15, 16, 21, 12}, {15, 16, 11, 22}, {15, 16, 11, 12}},
		{{29, 30, 35, 36}, {29, 30, 11, 36}, { 5, 30, 35, 36}, { 5, 30, 11, 36},
		 {39, 40, 45, 46}, { 5, 40, 45, 46}, {39,  6, 45, 46}, { 5,  6, 45, 46}},
		{{25, 30, 31, 36}, {15, 16, 45, 46}, {13, 14, 19, 20}, {13, 14, 19, 12},
		 {17, 18, 23, 24}, {17, 18, 11, 24}, {41, 42, 47, 48}, { 5, 42, 47, 48}},
		{{37, 38, 43, 44}, {37,  6, 43, 44}, {13, 18, 19, 24}, {13, 14, 43, 44},
		 {37, 42, 43, 48}, {17, 18, 47, 48}, {13, 18, 43, 48}, { 1,  2,  7,  8}}
	};
	
	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	Tilemap::Tilemap() : SourceRenderer()
	{
		this->typeName = "tilemap";
		this->rb_autotiles = rb_ary_new3(MAX_AUTOTILES, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil);
		this->rb_currentAutotiles = rb_ary_new3(MAX_AUTOTILES, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil);
		for_iter (i, 0, MAX_AUTOTILES)
		{
			this->generatedAutotiles[i] = NULL;
		}
		this->width = (Graphics::getWidth() + TILE_SIZE - 1) / TILE_SIZE + 1;
		this->height = (Graphics::getHeight() + TILE_SIZE - 1) / TILE_SIZE + 1;
		this->depth = 0;
		this->autotileUpdateCount = 0;
		this->rb_mapData = Qnil;
		this->mapData = NULL;
		this->rb_priorities = Qnil;
		this->priorities = NULL;
	}
	
	Tilemap::~Tilemap()
	{
		this->dispose();
		foreach (SystemSprite*, it, this->tileSprites)
		{
			delete (*it);
		}
		this->tileSprites.clear();
	}

	void Tilemap::initialize(VALUE rb_viewport)
	{
		SourceRenderer::initialize(rb_viewport);
		this->rb_autotiles = rb_ary_new3(MAX_AUTOTILES, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil);
		this->rb_currentAutotiles = rb_ary_new3(MAX_AUTOTILES, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil);
		for_iter (i, 0, MAX_AUTOTILES)
		{
			this->generatedAutotiles[i] = NULL;
		}
		this->width = (Graphics::getWidth() + TILE_SIZE - 1) / TILE_SIZE + 1;
		this->height = (Graphics::getHeight() + TILE_SIZE - 1) / TILE_SIZE + 1;
		this->depth = 0;
		this->autotileUpdateCount = 0;
		this->rb_mapData = Qnil;
		this->mapData = NULL;
		this->rb_priorities = Qnil;
		this->priorities = NULL;
	}

	void Tilemap::dispose()
	{
		if (!this->disposed)
		{
			this->rb_autotiles = Qnil;
			this->rb_currentAutotiles = Qnil;
			this->rb_mapData = Qnil;
			this->mapData = NULL;
			this->rb_priorities = Qnil;
			this->priorities = NULL;
			for_iter (i, 0, MAX_AUTOTILES)
			{
				if (this->generatedAutotiles[i] != NULL)
				{
					delete this->generatedAutotiles[i];
					this->generatedAutotiles[i] = NULL;
				}
			}
			foreach (SystemSprite*, it, this->tileSprites)
			{
				(*it)->dispose();
			}
		}
		SourceRenderer::dispose();
	}

	void Tilemap::mark()
	{
		SourceRenderer::mark();
		RB_GC_MARK(autotiles);
		RB_GC_MARK(currentAutotiles);
		RB_GC_MARK(mapData);
		RB_GC_MARK(priorities);
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Tilemap::update()
	{
		if (this->mapData == NULL || this->depth != this->mapData->getZSize())
		{
			foreach (SystemSprite*, it, this->tileSprites)
			{
				delete (*it);
			}
			this->tileSprites.clear();
		}
		if (this->mapData == NULL || this->disposed)
		{
			return;
		}
		if (!this->visible)
		{
			foreach (SystemSprite*, it, this->tileSprites)
			{
				(*it)->setVisible(false);
			}
			return;
		}
		this->depth = this->mapData->getZSize();
		if (this->tileSprites.size() == 0)
		{
			SystemSprite* tileSprite;
			int i;
			int j;
			int k;
			for_iterx (k, 0, this->depth)
			{
				for_iterx (j, 0, this->height)
				{
					for_iterx (i, 0, this->width)
					{
						tileSprite = new SystemSprite(this->viewport);
						tileSprite->getSrcRect()->set(0, 0, TILE_SIZE, TILE_SIZE);
						this->tileSprites += tileSprite;
					}
				}
			}
		}
		this->_updateAutotiles();
		this->_updateTileSprites();
	}

	void Tilemap::_updateAutotiles()
	{
		VALUE rb_autotile;
		Bitmap* generated;
		static VALUE argv1[2] = {INT2FIX(256), INT2FIX(192)};
		static VALUE argv2[2] = {INT2FIX(256), INT2FIX(768)};
		int position;
		int sx;
		int sy;
		int tx;
		int ty;
		bool animated;
		int x;
		int y;
		int j;
		for_iter (i, 0, MAX_AUTOTILES)
		{
			rb_autotile = rb_ary_entry(this->rb_autotiles, i);
			if (rb_autotile != rb_ary_entry(this->rb_currentAutotiles, i))
			{
				rb_ary_store(this->rb_currentAutotiles, i, rb_autotile);
				if (NIL_P(rb_autotile))
				{
					if (this->generatedAutotiles[i] != NULL)
					{
						delete this->generatedAutotiles[i];
						this->generatedAutotiles[i] = NULL;
					}
					continue;
				}
				generated = this->generatedAutotiles[i];
				animated = (NUM2INT(Bitmap::rb_getWidth(rb_autotile)) > 96);
				if (generated == NULL)
				{
					generated = new Bitmap(256, (!animated ? 192 : 768));
					this->generatedAutotiles[i] = generated;
				}
				else
				{
					generated->clear();
				}
				RB_VAR2CPP(rb_autotile, Bitmap, autotile);
				for_iterx (y, 0, 6)
				{
					for_iterx (x, 0, 8)
					{
						for_iterx (j, 0, 4)
						{
							position = _autotiles[y][x][j] - 1;
							tx = x * 32 + j % 2 * 16;
							ty = y * 32 + j / 2 * 16;
							sx = position % 6 * 16;
							sy = position / 6 * 16;
							generated->bltOver(tx, ty, autotile, sx, sy, 16, 16);
							if (animated)
							{
								generated->bltOver(tx, ty + 192, autotile, sx + 96, sy, 16, 16);
								generated->bltOver(tx, ty + 384, autotile, sx + 192, sy, 16, 16);
								generated->bltOver(tx, ty + 576, autotile, sx + 288, sy, 16, 16);
							}
						}
					}
				}
			}
		}
	}

	void Tilemap::_updateTileSprites()
	{
		SystemSprite* tileSprite;
		int i;
		int j;
		int k;
		int priority;
		int tileId;
		Bitmap* autotile;
		Rect* rect;
		for_iterx (k, 0, this->depth)
		{
			for_iterx (j, 0, this->height)
			{
				for_iterx (i, 0, this->width)
				{
					tileSprite = this->tileSprites[i + this->width * (j + this->height * k)];
					tileId = this->mapData->getCircularData(
						-this->ox / TILE_SIZE + i, -this->oy / TILE_SIZE + j, k);
					tileSprite->setX(this->ox % TILE_SIZE + i * TILE_SIZE);
					tileSprite->setY(this->oy % TILE_SIZE + j * TILE_SIZE);
					if (tileId < 48)
					{
						tileSprite->setVisible(false);
					}
					else
					{
						tileSprite->setVisible(true);
						rect = tileSprite->getSrcRect();
						if (tileId >= 384)
						{
							tileSprite->setBitmap(this->bitmap);
							rect->x = ((tileId - 384) % 8) * TILE_SIZE;
							rect->y = ((tileId - 384) / 8) * TILE_SIZE;
						}
						else
						{
							autotile = this->generatedAutotiles[(tileId / 48) - 1];
							tileSprite->setBitmap(autotile);
							rect->x = (tileId % 8) * TILE_SIZE;
							rect->y = ((tileId % 48) / 8) * TILE_SIZE;
							if (autotile->getHeight() > 192)
							{
								rect->y += this->autotileUpdateCount / 16 * 192;
							}
						}
					}
					priority = this->priorities->getData(tileId);
					if (priority > 0)
					{
						tileSprite->setZ(tileSprite->getY() + (priority + 1) * TILE_SIZE - 1);
					}
					else
					{
						tileSprite->setZ(0);
					}
				}
			}
		}
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Tilemap::init()
	{
	}

	void Tilemap::destroy()
	{
	}

	void Tilemap::createRubyInterface()
	{
		rb_cTilemap = rb_define_class("Tilemap", rb_cObject);
		rb_define_alloc_func(rb_cTilemap, &Tilemap::rb_new);
		// initialize
		rb_define_method(rb_cTilemap, "initialize", RUBY_METHOD_FUNC(&Tilemap::rb_initialize), -1);
		rb_define_method(rb_cTilemap, "initialize_clone", RUBY_METHOD_FUNC(&Tilemap::rb_initialize_clone), 1);
		rb_define_method(rb_cTilemap, "initialize_dup", RUBY_METHOD_FUNC(&Tilemap::rb_initialize_dup), 1);
		rb_define_method(rb_cTilemap, "dispose", RUBY_METHOD_FUNC(&Tilemap::rb_dispose), 0);
		rb_define_method(rb_cTilemap, "_arc_dump", RUBY_METHOD_FUNC(&Tilemap::rb_arcDump), 0);
		// getters and setters (Renderable) (except "z" and "z=")
		rb_define_method(rb_cTilemap, "visible", RUBY_METHOD_FUNC(&Tilemap::rb_getVisible), 0);
		rb_define_method(rb_cTilemap, "visible=", RUBY_METHOD_FUNC(&Tilemap::rb_setVisible), 1);
		rb_define_method(rb_cTilemap, "ox", RUBY_METHOD_FUNC(&Tilemap::rb_getOX), 0);
		rb_define_method(rb_cTilemap, "ox=", RUBY_METHOD_FUNC(&Tilemap::rb_setOX), 1);
		rb_define_method(rb_cTilemap, "oy", RUBY_METHOD_FUNC(&Tilemap::rb_getOY), 0);
		rb_define_method(rb_cTilemap, "oy=", RUBY_METHOD_FUNC(&Tilemap::rb_setOY), 1);
		rb_define_method(rb_cTilemap, "disposed?", RUBY_METHOD_FUNC(&Tilemap::rb_isDisposed), 0);
		// getters and setters (SourceRenderer) (except "opacity" and "opacity=")
		rb_define_method(rb_cTilemap, "viewport", RUBY_METHOD_FUNC(&Tilemap::rb_getViewport), 0);
		rb_define_method(rb_cTilemap, "tileset", RUBY_METHOD_FUNC(&Tilemap::rb_getBitmap), 0);
		rb_define_method(rb_cTilemap, "tileset=", RUBY_METHOD_FUNC(&Tilemap::rb_setBitmap), 1);
		// getters and setters
		rb_define_method(rb_cTilemap, "autotiles", RUBY_METHOD_FUNC(&Tilemap::rb_getAutotiles), 0);
		rb_define_method(rb_cTilemap, "map_data", RUBY_METHOD_FUNC(&Tilemap::rb_getMapData), 0);
		rb_define_method(rb_cTilemap, "map_data=", RUBY_METHOD_FUNC(&Tilemap::rb_setMapData), 1);
		rb_define_method(rb_cTilemap, "priorities", RUBY_METHOD_FUNC(&Tilemap::rb_getPriorities), 0);
		rb_define_method(rb_cTilemap, "priorities=", RUBY_METHOD_FUNC(&Tilemap::rb_setPriorities), 1);
		// methods
		rb_define_method(rb_cTilemap, "update", RUBY_METHOD_FUNC(&Tilemap::rb_update), 0);
	}

	VALUE Tilemap::rb_new(VALUE classe) 
	{
		Tilemap* tilemap;
		return RB_OBJECT_NEW(classe, Tilemap, tilemap, &Tilemap::gc_mark, &Tilemap::gc_free);
	}

	VALUE Tilemap::rb_initialize(int argc, VALUE* argv, VALUE self) 
	{
		RB_SELF2CPP(Tilemap, tilemap);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		tilemap->initialize(viewport);
		return self;
	}

	VALUE Tilemap::rb_initialize_clone(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CANT_CLONE_ERROR(tilemap);
		return self;
	}

	VALUE Tilemap::rb_initialize_dup(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CANT_DUP_ERROR(tilemap);
		return self;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Tilemap::rb_getAutotiles(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CHECK_DISPOSED(tilemap);
		return tilemap->rb_autotiles;
	}

	VALUE Tilemap::rb_getMapData(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CHECK_DISPOSED(tilemap);
		return tilemap->rb_mapData;
	}

	VALUE Tilemap::rb_setMapData(VALUE self, VALUE value)
	{
		{
			RB_SELF2CPP(Tilemap, tilemap);
			RB_CHECK_DISPOSED(tilemap);
		}
		RB_GENERATE_SETTER(Tilemap, tilemap, Table, mapData);
		return value;
	}

	VALUE Tilemap::rb_getPriorities(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CHECK_DISPOSED(tilemap);
		return tilemap->rb_priorities;
	}

	VALUE Tilemap::rb_setPriorities(VALUE self, VALUE value)
	{
		{
			RB_SELF2CPP(Tilemap, tilemap);
			RB_CHECK_DISPOSED(tilemap);
		}
		RB_GENERATE_SETTER(Tilemap, tilemap, Table, priorities);
		return value;
	}

	/****************************************************************************************
	 * Methods
	 ****************************************************************************************/

	VALUE Tilemap::rb_update(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CHECK_DISPOSED(tilemap);
		tilemap->autotileUpdateCount = (tilemap->autotileUpdateCount + 1) % 64;
		return Qnil;
	}
	
}
