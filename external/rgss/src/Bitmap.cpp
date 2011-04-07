#include <ruby.h>

#include <april/ImageSource.h>
#include <april/RenderSystem.h>
#include <april/Texture.h>
#include <hltypes/exception.h>
#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Color.h"
#include "Font.h"
#include "Rect.h"
#include "RGSSError.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/
	
	VALUE rb_cBitmap;

	int Bitmap::getWidth()
	{
		return this->imageSource->w;
	}

	int Bitmap::getHeight()
	{
		return this->imageSource->h;
	}

	void Bitmap::updateTexture()
	{
		if (this->textureNeedsUpdate)
		{
			this->textureNeedsUpdate = false;
			if (this->texture != NULL)
			{
				delete this->texture;
			}
			this->texture = april::rendersys->createTextureFromMemory(
				this->imageSource->data, this->imageSource->w, this->imageSource->h);
		}
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/
	
	void Bitmap::init()
	{
	}

	void Bitmap::createRubyInterface()
	{
		rb_cBitmap = rb_define_class("Bitmap", rb_cObject);
		rb_define_alloc_func(rb_cBitmap, &Bitmap::rb_new);
		// initialize
		rb_define_method(rb_cBitmap, "initialize", RUBY_METHOD_FUNC(&Bitmap::rb_initialize), -1);
		rb_define_method(rb_cBitmap, "initialize_copy", RUBY_METHOD_FUNC(&Bitmap::rb_initialize_copy), 1);
		// getters and setters
		rb_define_method(rb_cBitmap, "width", RUBY_METHOD_FUNC(&Bitmap::rb_getWidth), 0);
		rb_define_method(rb_cBitmap, "height", RUBY_METHOD_FUNC(&Bitmap::rb_getHeight), 0);
		// not implemented yet
		rb_define_method(rb_cBitmap, "font", RUBY_METHOD_FUNC(&Bitmap::rb_getFont), 0);
		rb_define_method(rb_cBitmap, "font=", RUBY_METHOD_FUNC(&Bitmap::rb_setFont), 1);
		rb_define_method(rb_cBitmap, "rect", RUBY_METHOD_FUNC(&Bitmap::rb_getRect), 0);
		// methods
		rb_define_method(rb_cBitmap, "get_pixel", RUBY_METHOD_FUNC(&Bitmap::rb_getPixel), 2);
		rb_define_method(rb_cBitmap, "set_pixel", RUBY_METHOD_FUNC(&Bitmap::rb_setPixel), 3);
		rb_define_method(rb_cBitmap, "fill_rect", RUBY_METHOD_FUNC(&Bitmap::rb_fillRect), -1); 
		rb_define_method(rb_cBitmap, "blt", RUBY_METHOD_FUNC(&Bitmap::rb_blt), -1); 
		// not implemented yet
			
		rb_define_method(rb_cBitmap, "clear", RUBY_METHOD_FUNC(&Bitmap::rb_clear), 0); 
		rb_define_method(rb_cBitmap, "dispose", RUBY_METHOD_FUNC(&Bitmap::rb_dispose), 0); 
		rb_define_method(rb_cBitmap, "disposed?", RUBY_METHOD_FUNC(&Bitmap::rb_isDisposed), 0); 
		rb_define_method(rb_cBitmap, "draw_text", RUBY_METHOD_FUNC(&Bitmap::rb_drawText), -1); 
		rb_define_method(rb_cBitmap, "hue_change", RUBY_METHOD_FUNC(&Bitmap::rb_changeHue), 1); 
		rb_define_method(rb_cBitmap, "stretch_blt", RUBY_METHOD_FUNC(&Bitmap::rb_stretchBlt), 4); 
		rb_define_method(rb_cBitmap, "text_size", RUBY_METHOD_FUNC(&Bitmap::rb_textSize), 1); 
	}
	
	void Bitmap::gc_mark(Bitmap* bitmap)
	{
		if (!NIL_P(bitmap->rb_font))
		{
			rb_gc_mark(bitmap->rb_font);
		}
	}

	void Bitmap::gc_free(Bitmap* bitmap)
	{
		if (bitmap->imageSource != NULL)
		{
			delete bitmap->imageSource;
			bitmap->imageSource = NULL;
		}
		if (bitmap->texture != NULL)
		{
			delete bitmap->texture;
			bitmap->texture = NULL;
		}
	}

	VALUE Bitmap::rb_new(VALUE classe) 
	{
		Bitmap* bitmap;
		VALUE result = Data_Make_Struct(classe, Bitmap, Bitmap::gc_mark, Bitmap::gc_free, bitmap);
		bitmap->disposed = true;
		return result;
	}

	VALUE Bitmap::rb_initialize(int argc, VALUE* argv, VALUE self) 
	{
		RB_SELF2CPP(Bitmap, bitmap);
		bitmap->disposed = false;
		VALUE arg1, arg2;
		rb_scan_args(argc, argv, "11", &arg1, &arg2);
		if (NIL_P(arg2))
		{
			hstr filename = april::rendersys->findTextureFile(StringValuePtr(arg1));
			bitmap->imageSource = april::loadImage(filename);
		}
		else
		{
			int w = NUM2INT(arg1);
			int h = NUM2INT(arg2);
			if (w < 1 || h < 1)
			{
				rb_raise(rb_eRGSSError, "failed to create bitmap");
			}
			bitmap->imageSource = april::createEmptyImage(w, h);
		}
		Bitmap::rb_setFont(self, Font::create(0, NULL));
		bitmap->textureNeedsUpdate = true;
		return self;
	}

	VALUE Bitmap::rb_initialize_copy(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_VAR2CPP(original, Bitmap, other);
		bitmap->imageSource = april::createEmptyImage(other->imageSource->w, other->imageSource->h);
		bitmap->imageSource->copyImage(other->imageSource);
		bitmap->textureNeedsUpdate = true;
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

	VALUE Bitmap::rb_getFont(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		return bitmap->rb_font;
	}

	VALUE Bitmap::rb_setFont(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Bitmap, bitmap, Font, font);
		return self;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Bitmap::rb_getPixel(VALUE self, VALUE x, VALUE y)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		april::Color color = bitmap->imageSource->getPixel(NUM2INT(x), NUM2INT(y));
		VALUE argv[4] = {INT2FIX(color.r), INT2FIX(color.g), INT2FIX(color.b), INT2FIX(color.a)};
		return Color::create(4, argv);
	}

	VALUE Bitmap::rb_setPixel(VALUE self, VALUE x, VALUE y, VALUE color)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_VAR2CPP(color, Color, cColor);
		bitmap->imageSource->setPixel(NUM2INT(x), NUM2INT(y), cColor->toAColor());
		bitmap->textureNeedsUpdate = true;
		return Qnil;
	}

	VALUE Bitmap::rb_fillRect(int argc, VALUE* argv, VALUE self)
	{
		if (argc != 2 && argc != 5)
		{
			hstr message = hsprintf("wrong number of arguments (%d for 2 or 5)", argc);
			rb_raise(rb_eArgError, message.c_str());
		}
		RB_SELF2CPP(Bitmap, bitmap);
		int x, y, w, h;
		VALUE arg1, arg2, arg3, arg4, color;
		rb_scan_args(argc, argv, "23", &arg1, &arg2, &arg3, &arg4, &color);
		if (NIL_P(arg3) && NIL_P(arg4) && NIL_P(color))
		{
			color = arg2;
			RB_VAR2CPP(arg1, Rect, rect);
			x = rect->x;
			y = rect->y;
			w = rect->width;
			h = rect->height;
		}
		else
		{
			x = NUM2INT(arg1);
			y = NUM2INT(arg2);
			w = NUM2INT(arg3);
			h = NUM2INT(arg4);
		}
		RB_VAR2CPP(color, Color, cColor);
		bitmap->imageSource->setPixels(x, y, w, h, cColor->toAColor());
		bitmap->textureNeedsUpdate = true;
		return self;
	}

	VALUE Bitmap::rb_blt(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		VALUE arg1, arg2, arg3, arg4, arg5;
		rb_scan_args(argc, argv, "41", &arg1, &arg2, &arg3, &arg4, &arg5);
		int x = NUM2INT(arg1);
		int y = NUM2INT(arg2);
		RB_VAR2CPP(arg3, Bitmap, source);
		RB_VAR2CPP(arg4, Rect, rect);
		if (NIL_P(arg5))
		{
			bitmap->imageSource->blit(x, y, source->imageSource, rect->x, rect->y, rect->width, rect->height);
		}
		else
		{
			bitmap->imageSource->blit(x, y, source->imageSource, rect->x, rect->y, rect->width, rect->height,
				(unsigned char)NUM2INT(arg5));
		}
		bitmap->textureNeedsUpdate = true;
		return self;
	}

	/****************************************************************************************
	 * TODO
	 ****************************************************************************************/




	VALUE Bitmap::rb_dispose(VALUE self) 
	{
		return self;
	}

	VALUE Bitmap::rb_getRect(VALUE self)
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
