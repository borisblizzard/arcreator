#include <ruby.h>

#include <april/RenderSystem.h>
#include <april/Texture.h>
#include <hltypes/exception.h>

#include "RGSS/Bitmap.h"
#include "RGSS/Color.h"
#include "RGSS/Font.h"
#include "RGSS/Rect.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		/****************************************************************************************
		 * Pure C++ code
		 ****************************************************************************************/

		int Bitmap::getWidth()
		{
			return this->texture->getWidth();
		}

		int Bitmap::getHeight()
		{
			return this->texture->getHeight();
		}

		/****************************************************************************************
		 * Ruby Interfacing, Creation, Destruction, Systematics
		 ****************************************************************************************/

		void Bitmap::createRubyInterface()
		{
			rb_cBitmap = rb_define_class("Bitmap", rb_cObject);
			rb_define_alloc_func(rb_cBitmap, &Bitmap::rb_new);
			// initialize
			rb_define_method(rb_cBitmap, "initialize", RUBY_METHOD_FUNC(&Bitmap::rb_initialize), -1);
			// getters and setters
			rb_define_method(rb_cBitmap, "width", RUBY_METHOD_FUNC(&Bitmap::rb_getWidth), 0);
			rb_define_method(rb_cBitmap, "height", RUBY_METHOD_FUNC(&Bitmap::rb_getHeight), 0);
			// not implemented yet
			rb_define_method(rb_cBitmap, "font", RUBY_METHOD_FUNC(&Bitmap::rb_getFont), 0);
			rb_define_method(rb_cBitmap, "font=", RUBY_METHOD_FUNC(&Bitmap::rb_setFont), 1);
			rb_define_method(rb_cBitmap, "rect", RUBY_METHOD_FUNC(&Bitmap::rb_getRect), 0);
			// methods
			rb_define_method(rb_cBitmap, "get_pixel", RUBY_METHOD_FUNC(&Bitmap::rb_getPixel), 2); 
			// not implemented yet
			rb_define_method(rb_cBitmap, "set_pixel", RUBY_METHOD_FUNC(&Bitmap::rb_setPixel), 3); 
			rb_define_method(rb_cBitmap, "blt", RUBY_METHOD_FUNC(&Bitmap::rb_blt), -1); 
			rb_define_method(rb_cBitmap, "clear", RUBY_METHOD_FUNC(&Bitmap::rb_clear), 0); 
			rb_define_method(rb_cBitmap, "dispose", RUBY_METHOD_FUNC(&Bitmap::rb_dispose), 0); 
			rb_define_method(rb_cBitmap, "disposed?", RUBY_METHOD_FUNC(&Bitmap::rb_isDisposed), 0); 
			rb_define_method(rb_cBitmap, "draw_text", RUBY_METHOD_FUNC(&Bitmap::rb_drawText), -1); 
			rb_define_method(rb_cBitmap, "fill_rect", RUBY_METHOD_FUNC(&Bitmap::rb_fillRect), -1); 
			rb_define_method(rb_cBitmap, "hue_change", RUBY_METHOD_FUNC(&Bitmap::rb_changeHue), 1); 
			rb_define_method(rb_cBitmap, "stretch_blt", RUBY_METHOD_FUNC(&Bitmap::rb_stretchBlt), 4); 
			rb_define_method(rb_cBitmap, "text_size", RUBY_METHOD_FUNC(&Bitmap::rb_textSize), 1); 
		}
	
		VALUE Bitmap::wrap()
		{
			Bitmap* bitmap = this;
			return Data_Wrap_Struct(rb_cBitmap, NULL, NULL, bitmap);
		}

		void Bitmap::gc_free(Bitmap* bitmap)
		{
			if (bitmap->texture != NULL)
			{
				delete bitmap->texture;
				bitmap->texture = NULL;
			}
		}

		VALUE Bitmap::rb_new(VALUE classe) 
		{
			Bitmap* bitmap;
			return Data_Make_Struct(classe, Bitmap, NULL, Bitmap::gc_free, bitmap);
		}

		VALUE Bitmap::rb_initialize(int argc, VALUE* argv, VALUE self) 
		{
			RB_SELF2CPP(Bitmap, bitmap);
			VALUE arg1, arg2;
			// "11" means 1 mandatory argument, 1 optional argument
			rb_scan_args(argc, argv, "11", &arg1, &arg2);
			if (NIL_P(arg2))
			{
				hstr filename = april::rendersys->findTextureFile(StringValuePtr(arg1));
				bitmap->texture = april::rendersys->loadTexture(filename);
			}
			else
			{
				bitmap->texture = april::rendersys->createEmptyTexture(NUM2INT(arg1), NUM2INT(arg2));
			}
			return self;
		}

		/****************************************************************************************
		 * Ruby Getters/Setters
		 ****************************************************************************************/

		VALUE Bitmap::rb_getWidth(VALUE self)
		{
			RB_SELF2CPP(Bitmap, bitmap);
			return INT2FIX(bitmap->getWidth());
		}

		VALUE Bitmap::rb_getHeight(VALUE self)
		{
			RB_SELF2CPP(Bitmap, bitmap);
			return INT2FIX(bitmap->getHeight());
		}

		/****************************************************************************************
		 * Ruby Methods
		 ****************************************************************************************/

		VALUE Bitmap::rb_getPixel(VALUE self, VALUE x, VALUE y)
		{
			RB_SELF2CPP(Bitmap, bitmap);
			april::Color aColor = bitmap->texture->getPixel(NUM2INT(x), NUM2INT(y));
			VALUE result = Color::rb_new(rb_cColor);
			RB_VAR2CPP(result, Color, color);
			color->set(aColor);
			return result;
		}

		/// @todo This is problematic because after the change, this texture has to be uploaded to the graphic card again.
		/// @todo It might be a good idea to put together an update batch that updates the texture on drawing only.
		VALUE Bitmap::rb_setPixel(VALUE self, VALUE x, VALUE y, VALUE color)
		{
			RB_SELF2CPP(Bitmap, bitmap);
			RB_VAR2CPP(color, Color, cColor);
			april::Color aColor((int)cColor->red, (int)cColor->green, (int)cColor->blue, (int)cColor->alpha);
			//bitmap->texture->setPixel(NUM2INT(x), NUM2INT(y), aColor);
			return Qnil;
		}

		/****************************************************************************************
		 * TODO
		 ****************************************************************************************/




		VALUE Bitmap::rb_dispose(VALUE self) 
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

		VALUE Bitmap::rb_blt(VALUE self, VALUE x, VALUE y, VALUE src_bitmap, VALUE src_rect, VALUE opacity)
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

		VALUE Bitmap::rb_changeHue(VALUE self, VALUE hue)
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
