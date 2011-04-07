#include <ruby.h>

#include "CodeSnippets.h"
#include "Tilemap.h"
#include "Bitmap.h"
#include "Table.h"
#include "Viewport.h"

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
		// getters and setters
		rb_define_method(rb_cTilemap, "autotiles", RUBY_METHOD_FUNC(&Tilemap::rb_getAutotiles), 0);
		rb_define_method(rb_cTilemap, "autotiles=", RUBY_METHOD_FUNC(&Tilemap::rb_setAutotiles), 1);
		rb_define_method(rb_cTilemap, "map_data", RUBY_METHOD_FUNC(&Tilemap::rb_getMapData), 0);
		rb_define_method(rb_cTilemap, "map_data=", RUBY_METHOD_FUNC(&Tilemap::rb_setMapData), 1);
		rb_define_method(rb_cTilemap, "ox", RUBY_METHOD_FUNC(&Tilemap::rb_getOx), 0);
		rb_define_method(rb_cTilemap, "ox=", RUBY_METHOD_FUNC(&Tilemap::rb_setOx), 1);
		rb_define_method(rb_cTilemap, "oy", RUBY_METHOD_FUNC(&Tilemap::rb_getOy), 0);
		rb_define_method(rb_cTilemap, "oy=", RUBY_METHOD_FUNC(&Tilemap::rb_setOy), 1);
		rb_define_method(rb_cTilemap, "priorities", RUBY_METHOD_FUNC(&Tilemap::rb_getPriorities), 0);
		rb_define_method(rb_cTilemap, "priorities=", RUBY_METHOD_FUNC(&Tilemap::rb_setPriorities), 1);
		rb_define_method(rb_cTilemap, "flash_data", RUBY_METHOD_FUNC(&Tilemap::rb_getFlashData), 0);
		rb_define_method(rb_cTilemap, "flash_data=", RUBY_METHOD_FUNC(&Tilemap::rb_setFlashData), 1);
		rb_define_method(rb_cTilemap, "tileset", RUBY_METHOD_FUNC(&Tilemap::rb_getTileset), 0);
		rb_define_method(rb_cTilemap, "tileset=", RUBY_METHOD_FUNC(&Tilemap::rb_setTileset), 1);
		rb_define_method(rb_cTilemap, "viewport", RUBY_METHOD_FUNC(&Tilemap::rb_getViewport), 0);
		rb_define_method(rb_cTilemap, "visible", RUBY_METHOD_FUNC(&Tilemap::rb_getVisible), 0);
		rb_define_method(rb_cTilemap, "visible=", RUBY_METHOD_FUNC(&Tilemap::rb_setVisible), 1);
		// methods
		rb_define_method(rb_cTilemap, "update", RUBY_METHOD_FUNC(&Tilemap::rb_update), 0);
		rb_define_method(rb_cTilemap, "dispose", RUBY_METHOD_FUNC(&Tilemap::rb_dispose), 0);
		rb_define_method(rb_cTilemap, "disposed?", RUBY_METHOD_FUNC(&Tilemap::rb_isDisposed), 0);
	}

	void Tilemap::gc_mark(Tilemap* tilemap)
	{
	}

	VALUE Tilemap::rb_new(VALUE classe) 
	{
		return classe;
	}

	VALUE Tilemap::rb_initialize(int argc, VALUE* argv, VALUE self) 
	{
		return self;
	}

	VALUE Tilemap::rb_dispose(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_getAutotiles(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_setAutotiles(VALUE self, VALUE* value)
	{
		return self;
	}

	VALUE Tilemap::rb_getMapData(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_setMapData(VALUE self, VALUE* value)
	{
		return self;
	}

	VALUE Tilemap::rb_getOx(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_setOx(VALUE self, VALUE value)
	{
		return self;
	}

	VALUE Tilemap::rb_getOy(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_setOy(VALUE self, VALUE value)
	{
		return self;
	}

	VALUE Tilemap::rb_getPriorities(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_setPriorities(VALUE self, VALUE* value)
	{
		return self;
	}

	VALUE Tilemap::rb_getFlashData(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_setFlashData(VALUE self, VALUE* value)
	{
		return self;
	}

	VALUE Tilemap::rb_getTileset(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_setTileset(VALUE self, VALUE* value)
	{
		return self;
	}

	VALUE Tilemap::rb_getVisible(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_setVisible(VALUE self, VALUE value)
	{
		return self;
	}

	VALUE Tilemap::rb_getViewport(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_isDisposed(VALUE self)
	{
		return self;
	}

	VALUE Tilemap::rb_update(VALUE self)
	{
		return self;
	}
	/*

	Tilemap::Tilemap() : map_data(20, 15, 3), priorities(20, 15, 3)
	{
	}

	Tilemap::Tilemap(Viewport* value) : map_data(20, 15, 3), priorities(20, 15, 3)
	{
	}
	
	Tilemap::~Tilemap()
	{
	}

	*/
	
}
