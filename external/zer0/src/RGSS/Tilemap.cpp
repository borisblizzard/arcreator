#include <ruby.h>

#include "RGSS/Tilemap.h"
#include "RGSS/Bitmap.h"
#include "RGSS/Table.h"
#include "RGSS/Viewport.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Tilemap::createRubyInterface()
		{
			rb_cTilemap = rb_define_class("Tilemap", rb_cObject);
			rb_define_alloc_func(rb_cTilemap, &Tilemap::rb_new);
			// initialize
			rb_define_method(rb_cTilemap, "initialize", RUBY_METHOD_FUNC(&Tilemap::rb_initialize), -1);
			rb_define_method(rb_cTilemap, "inspect", RUBY_METHOD_FUNC(&Tilemap::rb_inspect), 0);
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

		VALUE Tilemap::wrap()
		{
			Tilemap* tilemap = this;
			return Data_Wrap_Struct(rb_cTilemap, NULL, NULL, tilemap);
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

		VALUE Tilemap::rb_inspect(VALUE self)
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
}