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
#include "Table.h"
#include "TileSprite.h"
#include "Tilemap.h"
#include "Viewport.h"

#define TILE_SIZE 32

namespace rgss
{
	VALUE rb_cTilemap;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	int autotiles[6][8][4] = {
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
	
	void Tilemap::dispose()
	{
		this->rb_autotiles = Qnil;
		this->rb_currentAutotiles = Qnil;
		this->rb_mapData = Qnil;
		this->mapData = NULL;
		this->rb_priorities = Qnil;
		this->priorities = NULL;
		this->rb_flashData = Qnil;
		this->flashData = NULL;
		for_iter (i, 0, MAX_AUTOTILES)
		{
			if (this->generatedAutotiles[i] != NULL)
			{
				delete this->generatedAutotiles[i];
				this->generatedAutotiles[i] = NULL;
			}
		}
		for_iter (i, 0, this->tileSprites->size())
		{
			delete (*this->tileSprites)[i];
		}
		delete this->tileSprites;
		this->tileSprites = NULL;
	}

	void Tilemap::update()
	{
		if (this->needsUpdate)
		{
			this->needsUpdate = false;
			this->_updateTileSprites();
		}
	}

	void Tilemap::_updateAutotiles()
	{
		VALUE rb_autotile;
		Bitmap* generated;
		VALUE argv1[2] = {INT2FIX(256), INT2FIX(192)};
		VALUE argv2[2] = {INT2FIX(256), INT2FIX(768)};
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
							position = autotiles[y][x][j] - 1;
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
		if (NIL_P(this->rb_mapData) || NIL_P(this->rb_priorities) || NIL_P(this->rb_bitmap))
		{
			for_iter (i, 0, this->tileSprites->size())
			{
				delete (*this->tileSprites)[i];
			}
			this->tileSprites->clear();
			return;
		}
		this->_updateAutotiles();
		this->depth = this->mapData->getZSize();
		TileSprite* tileSprite;
		int i;
		int j;
		int k;
		if (this->tileSprites->size() == 0)
		{
			for_iterx (k, 0, this->depth)
			{
				for_iterx (j, 0, this->height)
				{
					for_iterx (i, 0, this->width)
					{
						tileSprite = new TileSprite(this->viewport);
						tileSprite->getSrcRect()->set(0, 0, TILE_SIZE, TILE_SIZE);
						(*this->tileSprites) += tileSprite;
					}
				}
			}
		}
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
					tileSprite = (*this->tileSprites)[i + this->width * (j + this->height * k)];
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
		rb_define_method(rb_cTilemap, "flash_data", RUBY_METHOD_FUNC(&Tilemap::rb_getFlashData), 0);
		rb_define_method(rb_cTilemap, "flash_data=", RUBY_METHOD_FUNC(&Tilemap::rb_setFlashData), 1);
		// methods
		rb_define_method(rb_cTilemap, "update", RUBY_METHOD_FUNC(&Tilemap::rb_update), 0);
	}

	void Tilemap::gc_mark(Tilemap* tilemap)
	{
		rb_gc_mark(tilemap->rb_autotiles);
		rb_gc_mark(tilemap->rb_currentAutotiles);
		if (!NIL_P(tilemap->rb_mapData))
		{
			rb_gc_mark(tilemap->rb_mapData);
		}
		if (!NIL_P(tilemap->rb_priorities))
		{
			rb_gc_mark(tilemap->rb_priorities);
		}
		if (!NIL_P(tilemap->rb_flashData))
		{
			rb_gc_mark(tilemap->rb_flashData);
		}
		SourceRenderer::gc_mark(tilemap);
	}

	void Tilemap::gc_free(Tilemap* tilemap)
	{
		SourceRenderer::gc_free(tilemap);
	}

	VALUE Tilemap::rb_new(VALUE classe) 
	{
		Tilemap* tilemap;
		VALUE result = Data_Make_Struct(classe, Tilemap, Tilemap::gc_mark, Tilemap::gc_free, tilemap);
		tilemap->disposed = true;
		tilemap->type = TYPE_TILEMAP;
		tilemap->typeName = "tilemap";
		return result;
	}

	VALUE Tilemap::rb_initialize(int argc, VALUE* argv, VALUE self) 
	{
		RB_SELF2CPP(Tilemap, tilemap);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		tilemap->initializeSourceRenderer(viewport);
		tilemap->rb_autotiles = rb_ary_new3(MAX_AUTOTILES, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil);
		tilemap->rb_currentAutotiles = rb_ary_new3(MAX_AUTOTILES, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil);
		for_iter (i, 0, MAX_AUTOTILES)
		{
			tilemap->generatedAutotiles[i] = NULL;
		}
		tilemap->width = (Graphics::getWidth() + TILE_SIZE - 1) / TILE_SIZE + 1;
		tilemap->height = (Graphics::getHeight() + TILE_SIZE - 1) / TILE_SIZE + 1;
		tilemap->depth = 0;
		tilemap->autotileUpdateCount = 0;
		tilemap->needsUpdate = true;
		tilemap->rb_mapData = Qnil;
		tilemap->mapData = NULL;
		tilemap->rb_priorities = Qnil;
		tilemap->priorities = NULL;
		tilemap->rb_flashData = Qnil;
		tilemap->flashData = NULL;
		tilemap->tileSprites = new harray<TileSprite*>();
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

	VALUE Tilemap::rb_setOX(VALUE self, VALUE value)
	{
		VALUE rb_ox = Tilemap::rb_getOX(self);
		SourceRenderer::rb_setOX(self, value);
		if (value != rb_ox)
		{
			RB_SELF2CPP(Tilemap, tilemap);
			tilemap->needsUpdate = true;
		}
		return value;
	}

	VALUE Tilemap::rb_setOY(VALUE self, VALUE value)
	{
		VALUE rb_oy = Tilemap::rb_getOY(self);
		SourceRenderer::rb_setOY(self, value);
		if (value != rb_oy)
		{
			RB_SELF2CPP(Tilemap, tilemap);
			tilemap->needsUpdate = true;
		}
		return value;
	}

	VALUE Tilemap::rb_setVisible(VALUE self, VALUE value)
	{
		VALUE rb_visible = Tilemap::rb_getVisible(self);
		SourceRenderer::rb_setVisible(self, value);
		if (value != rb_visible)
		{
			RB_SELF2CPP(Tilemap, tilemap);
			tilemap->needsUpdate = true;
		}
		return value;
	}

	VALUE Tilemap::rb_getAutotiles(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CHECK_DISPOSED_2(tilemap);
		tilemap->needsUpdate = true;
		return tilemap->rb_autotiles;
	}

	VALUE Tilemap::rb_getMapData(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CHECK_DISPOSED_2(tilemap);
		tilemap->needsUpdate = true;
		return tilemap->rb_mapData;
	}

	VALUE Tilemap::rb_setMapData(VALUE self, VALUE value)
	{
		VALUE rb_mapData = Tilemap::rb_getMapData(self);
		RB_GENERATE_SETTER(Tilemap, tilemap, Table, mapData);
		RB_CHECK_DISPOSED_2(tilemap);
		if (value != rb_mapData)
		{
			tilemap->needsUpdate = true;
		}
		return value;
	}

	VALUE Tilemap::rb_getPriorities(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CHECK_DISPOSED_2(tilemap);
		tilemap->needsUpdate = true;
		return tilemap->rb_priorities;
	}

	VALUE Tilemap::rb_setPriorities(VALUE self, VALUE value)
	{
		VALUE rb_priorities = Tilemap::rb_getPriorities(self);
		RB_GENERATE_SETTER(Tilemap, tilemap, Table, priorities);
		RB_CHECK_DISPOSED_2(tilemap);
		if (value != rb_priorities)
		{
			tilemap->needsUpdate = true;
		}
		return value;
	}

	VALUE Tilemap::rb_getFlashData(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CHECK_DISPOSED_2(tilemap);
		return tilemap->rb_flashData;
	}

	VALUE Tilemap::rb_setFlashData(VALUE self, VALUE value)
	{
		VALUE rb_flashData = Tilemap::rb_getFlashData(self);
		RB_GENERATE_SETTER(Tilemap, tilemap, Table, flashData);
		RB_CHECK_DISPOSED_2(tilemap);
		if (value != rb_flashData)
		{
			tilemap->needsUpdate = true;
		}
		return value;
	}

	/****************************************************************************************
	 * Methods
	 ****************************************************************************************/

	VALUE Tilemap::rb_update(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		RB_CHECK_DISPOSED_2(tilemap);
		tilemap->autotileUpdateCount = (tilemap->autotileUpdateCount + 1) % 64;
		if (tilemap->autotileUpdateCount == 0)
		{
			tilemap->needsUpdate = true;
		}
		return Qnil;
	}
	
}
