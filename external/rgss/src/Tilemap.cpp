#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/harray.h>
#include <hltypes/hstring.h>
#include <hltypes/util.h>

#include "Bitmap.h"
#include "CodeSnippets.h"
#include "Graphics.h"
#include "Sprite.h"
#include "Table.h"
#include "Tilemap.h"
#include "Viewport.h"

#define TILE_SIZE 32

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cTilemap;

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
		this->rb_mapData = Qnil;
		this->mapData = NULL;
		this->rb_priorities = Qnil;
		this->priorities = NULL;
		this->rb_flashData = Qnil;
		this->flashData = NULL;
		for_iter (i, 0, this->tileSprites->size())
		{
			Sprite::rb_dispose((*this->rb_tileSprites)[i]);
			(*this->tileSprites)[i]->setVisible(false);
		}
		delete this->rb_tileSprites;
		this->rb_tileSprites = NULL;
		delete this->tileSprites;
		this->tileSprites = NULL;
	}

	void Tilemap::_updateTileSprites()
	{
		if (NIL_P(this->rb_mapData) || NIL_P(this->rb_priorities) || NIL_P(this->rb_bitmap))
		{
			for_iter (i, 0, this->tileSprites->size())
			{
				(*this->tileSprites)[i]->setVisible(false);
				Sprite::rb_dispose((*this->rb_tileSprites)[i]);
			}
			this->rb_tileSprites->clear();
			this->tileSprites->clear();
			return;
		}
		this->depth = this->mapData->getZSize();
		Sprite* tileSprite;
		VALUE rb_tileSprite;
		if (this->tileSprites->size() == 0)
		{
			for_iter (k, 0, this->depth)
			{
				for_iter (j, 0, this->height)
				{
					for_iter (i, 0, this->width)
					{
						rb_tileSprite = Sprite::create(1, &this->rb_viewport);
						RB_VAR2CPP(rb_tileSprite, Sprite, tileSprite);
						tileSprite->getSrcRect()->set(0, 0, TILE_SIZE, TILE_SIZE);
						(*this->rb_tileSprites) += rb_tileSprite;
						(*this->tileSprites) += tileSprite;
					}
				}
			}
		}
		int tileId;
		/*
		int pattern;
		int* list;
		int position;
		VALUE bitmapArgs[2] = {INT2FIX(TILE_SIZE), INT2FIX(TILE_SIZE)};
		VALUE rb_bitmap;
		*/
		Rect* rect;
		for_iter (k, 0, this->depth)
		{
			for_iter (j, 0, this->height)
			{
				for_iter (i, 0, this->width)
				{
					tileSprite = (*this->tileSprites)[i + this->width * (j + this->height * k)];
					rb_tileSprite = (*this->rb_tileSprites)[i + this->width * (j + this->height * k)];
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
						if (tileId >= 384)
						{
							SourceRenderer::rb_setBitmap(rb_tileSprite, this->rb_bitmap);
							rect = tileSprite->getSrcRect();
							rect->x = (tileId - 384) % 8 * TILE_SIZE;
							rect->y = (tileId - 384) / 8 * TILE_SIZE;
						}
						else
						{
							tileSprite->setVisible(false);
							/*
							pattern = tileId % 48;
							list = autotiles[pattern / 8][pattern % 8];
							VALUE rb_autotile = rb_ary_entry(this->rb_autotiles, (tileId / 48) - 1);
							if (!NIL_P(rb_autotile))
							{
								rb_bitmap = Sprite::rb_getBitmap(rb_tileSprite);
								if (rb_bitmap == this->rb_bitmap)
								{
									rb_bitmap = Bitmap::create(2, bitmapArgs);
									SourceRenderer::rb_setBitmap(rb_tileSprite, rb_bitmap);
									RB_VAR2CPP(rb_autotile, Bitmap, autotile);
									RB_VAR2CPP(rb_bitmap, Bitmap, bitmap);
									for_iter (i, 0, 4)
									{
										position = list[i] - 1;
										bitmap->blt(i % 2 * 16, i / 2 + 16, autotile,
											position % 6 * 16, position / 6 * 16, 16, 16);
									}
								}
							}
							else
							{
								SourceRenderer::rb_setBitmap(rb_tileSprite, Qnil);
								tileSprite->setVisible(false);
							}
							*/
						}
					}
					tileSprite->setZ(tileSprite->getY() + (this->priorities->getData(tileId) + 1) * TILE_SIZE);
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

	void Tilemap::createRubyInterface()
	{
		rb_cTilemap = rb_define_class("Tilemap", rb_cObject);
		rb_define_alloc_func(rb_cTilemap, &Tilemap::rb_new);
		// initialize
		rb_define_method(rb_cTilemap, "initialize", RUBY_METHOD_FUNC(&Tilemap::rb_initialize), -1);
		rb_define_method(rb_cTilemap, "dispose", RUBY_METHOD_FUNC(&Tilemap::rb_dispose), 0);
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
		foreach (VALUE, it, (*tilemap->rb_tileSprites))
		{
			rb_gc_mark(*it);
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
		return result;
	}

	VALUE Tilemap::rb_initialize(int argc, VALUE* argv, VALUE self) 
	{
		RB_SELF2CPP(Tilemap, tilemap);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		tilemap->initializeSourceRenderer(viewport);
		tilemap->rb_autotiles = rb_ary_new3(7, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil, Qnil);
		tilemap->width = (Graphics::getWidth() + TILE_SIZE - 1) / TILE_SIZE + 1;
		tilemap->height = (Graphics::getHeight() + TILE_SIZE - 1) / TILE_SIZE + 1;
		tilemap->depth = 0;
		tilemap->rb_mapData = Qnil;
		tilemap->mapData = NULL;
		tilemap->rb_priorities = Qnil;
		tilemap->priorities = NULL;
		tilemap->rb_flashData = Qnil;
		tilemap->flashData = NULL;
		tilemap->rb_tileSprites = new harray<VALUE>();
		tilemap->tileSprites = new harray<Sprite*>();
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
			tilemap->_updateTileSprites();
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
			tilemap->_updateTileSprites();
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
			tilemap->_updateTileSprites();
		}
		return value;
	}

	VALUE Tilemap::rb_getAutotiles(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		return tilemap->rb_autotiles;
	}

	VALUE Tilemap::rb_getMapData(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		return tilemap->rb_mapData;
	}

	VALUE Tilemap::rb_setMapData(VALUE self, VALUE value)
	{
		VALUE rb_mapData = Tilemap::rb_getMapData(self);
		RB_GENERATE_SETTER(Tilemap, tilemap, Table, mapData);
		if (value != rb_mapData)
		{
			tilemap->_updateTileSprites();
		}
		return value;
	}

	VALUE Tilemap::rb_getPriorities(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		return tilemap->rb_priorities;
	}

	VALUE Tilemap::rb_setPriorities(VALUE self, VALUE value)
	{
		VALUE rb_priorities = Tilemap::rb_getPriorities(self);
		RB_GENERATE_SETTER(Tilemap, tilemap, Table, priorities);
		if (value != rb_priorities)
		{
			tilemap->_updateTileSprites();
		}
		return value;
	}

	VALUE Tilemap::rb_getFlashData(VALUE self)
	{
		RB_SELF2CPP(Tilemap, tilemap);
		return tilemap->rb_flashData;
	}

	VALUE Tilemap::rb_setFlashData(VALUE self, VALUE value)
	{
		VALUE rb_flashData = Tilemap::rb_getFlashData(self);
		RB_GENERATE_SETTER(Tilemap, tilemap, Table, flashData);
		if (value != rb_flashData)
		{
			tilemap->_updateTileSprites();
		}
		return value;
	}

	/****************************************************************************************
	 * TODO
	 ****************************************************************************************/

	VALUE Tilemap::rb_update(VALUE self)
	{
		return Qnil;
	}
	
}
