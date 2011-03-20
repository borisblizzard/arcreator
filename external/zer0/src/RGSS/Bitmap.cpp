#include <ruby.h>

#include "RGSS/Bitmap.h"
#include "RGSS/Color.h"
#include "RGSS/Font.h"
#include "RGSS/Rect.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		Bitmap::Bitmap(chstr filename) { }
		Bitmap::Bitmap(int width, int height) { }
		Bitmap::~Bitmap() { }

		void Bitmap::createRubyInterface()
		{
			rb_cBitmap = rb_define_class("Bitmap", rb_cObject);
			rb_define_alloc_func(rb_cBitmap, &Bitmap::rb_new);
			// initialize
			rb_define_method(rb_cBitmap, "initialize", RUBY_METHOD_FUNC(&Bitmap::rb_initialize), -1);
			// getters and setters
			rb_define_method(rb_cBitmap, "font", RUBY_METHOD_FUNC(&Bitmap::rb_getFont), 0);
			rb_define_method(rb_cBitmap, "font=", RUBY_METHOD_FUNC(&Bitmap::rb_setFont), 1);
			rb_define_method(rb_cBitmap, "height", RUBY_METHOD_FUNC(&Bitmap::rb_getHeight), 0);
			rb_define_method(rb_cBitmap, "rect", RUBY_METHOD_FUNC(&Bitmap::rb_getRect), 0);
			rb_define_method(rb_cBitmap, "width", RUBY_METHOD_FUNC(&Bitmap::rb_getWidth), 0);
			// methods
			rb_define_method(rb_cBitmap, "blt", RUBY_METHOD_FUNC(&Bitmap::rb_blckTran), -1); 
			rb_define_method(rb_cBitmap, "clear", RUBY_METHOD_FUNC(&Bitmap::rb_clear), 0); 
			rb_define_method(rb_cBitmap, "dispose", RUBY_METHOD_FUNC(&Bitmap::rb_dispose), 0); 
			rb_define_method(rb_cBitmap, "disposed?", RUBY_METHOD_FUNC(&Bitmap::rb_isDisposed), 0); 
			rb_define_method(rb_cBitmap, "draw_text", RUBY_METHOD_FUNC(&Bitmap::rb_drawText), -1); 
			rb_define_method(rb_cBitmap, "fill_rect", RUBY_METHOD_FUNC(&Bitmap::rb_fillRect), -1); 
			rb_define_method(rb_cBitmap, "get_pixel", RUBY_METHOD_FUNC(&Bitmap::rb_getPixel), 2); 
			rb_define_method(rb_cBitmap, "hue_change", RUBY_METHOD_FUNC(&Bitmap::rb_changeHue), 1); 
			rb_define_method(rb_cBitmap, "set_pixel", RUBY_METHOD_FUNC(&Bitmap::rb_setPixel), 3); 
			rb_define_method(rb_cBitmap, "stretch_blt", RUBY_METHOD_FUNC(&Bitmap::rb_stretchBlt), 4); 
			rb_define_method(rb_cBitmap, "text_size", RUBY_METHOD_FUNC(&Bitmap::rb_textSize), 1); 
		}
	

		/// @todo The following functions need implemented, all return self for now to allow compilation
		VALUE Bitmap::rb_new(VALUE classe) 
		{
			return classe;
		}

		VALUE Bitmap::rb_initialize(int argc, VALUE* argv, VALUE self) 
		{
			return self;
		}

		VALUE rb_inspect(VALUE self)
		{
			// not sure if this is how it will be implemented or not
			RB_VAR2CPP(Bitmap, bitmap);
			hstr result = hsprintf("Bitmap(%.1f, %.1f)", bitmap->rb_getWidth(self), bitmap->rb_getHeight(self));
			return rb_str_new2(result.c_str());
		}

		void Bitmap::gc_mark(Bitmap* bitmap) { } 

		VALUE Bitmap::rb_dispose(VALUE self) 
		{
			return self;
		}

		VALUE Bitmap::rb_getHeight(VALUE self)
		{
			return self;
		}

		VALUE Bitmap::rb_getWidth(VALUE self)
		{
			return self;
		}

		VALUE Bitmap::rb_getFont(VALUE self)
		{
			return self;
		}

		VALUE Bitmap::rb_setFont(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Bitmap::rb_getRect(VALUE self)
		{
			return self;
		}

		VALUE Bitmap::rb_blckTran(VALUE self, VALUE x, VALUE y, VALUE src_bitmap, VALUE src_rect, VALUE opacity)
		{
			return self;
		}

		VALUE Bitmap::rb_clear(VALUE self)
		{
			return self;
		}

		VALUE Bitmap::rb_isDisposed(VALUE self)
		{
			return self;
		}

		VALUE Bitmap::rb_drawText(int argc, VALUE* argv, VALUE self)
		{
			return self;
		}

		VALUE Bitmap::rb_fillRect(int argc, VALUE* argv, VALUE self)
		{
			return self;
		}

		VALUE Bitmap::rb_getPixel(VALUE self, VALUE x, VALUE y)
		{
			return self;
		}

		VALUE Bitmap::rb_changeHue(VALUE self, VALUE hue)
		{
			return self;
		}

		VALUE Bitmap::rb_setPixel(VALUE self, VALUE x, VALUE y, VALUE color)
		{
			return self;
		}

		VALUE Bitmap::rb_stretchBlt(VALUE self, VALUE dest_rect, VALUE src_bitmap, VALUE src_rect, VALUE opacity)
		{
			return self;
		}

		VALUE Bitmap::rb_textSize(VALUE self, VALUE value)
		{
			return self;
		}
	}
}
