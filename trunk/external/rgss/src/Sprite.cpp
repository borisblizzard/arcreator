#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

#include "Bitmap.h"
#include "Color.h"
#include "Graphics.h"
#include "Rect.h"
#include "Sprite.h"
#include "Tone.h"
#include "Viewport.h"
#include "CodeSnippets.h"

namespace rgss
{
	/****************************************************************************************
		* Pure C++ code
		****************************************************************************************/

	void Sprite::draw()
	{
		if (this->bitmap != NULL)
		{
			this->bitmap->updateTexture();
			april::rendersys->setTexture(this->bitmap->getTexture());
			april::rendersys->drawTexturedQuad(
				grect(this->x, this->y, this->bitmap->getWidth(), this->bitmap->getHeight()), grect(0, 0, 1, 1));
		}
	}

	/****************************************************************************************
		* Ruby Interfacing, Creation, Destruction, Systematics
		****************************************************************************************/

	void Sprite::createRubyInterface()
	{
		rb_cSprite = rb_define_class("Sprite", rb_cObject);
		rb_define_alloc_func(rb_cSprite, &Sprite::rb_new);
		// initialize
		rb_define_method(rb_cSprite, "initialize", RUBY_METHOD_FUNC(&Sprite::rb_initialize), -1);
		rb_define_method(rb_cSprite, "dispose", RUBY_METHOD_FUNC(&Sprite::rb_dispose), 0);
		// getters and setters
		rb_define_method(rb_cSprite, "x", RUBY_METHOD_FUNC(&Sprite::rb_getX), 0);
		rb_define_method(rb_cSprite, "x=", RUBY_METHOD_FUNC(&Sprite::rb_setX), 1);
		rb_define_method(rb_cSprite, "y", RUBY_METHOD_FUNC(&Sprite::rb_getY), 0);
		rb_define_method(rb_cSprite, "y=", RUBY_METHOD_FUNC(&Sprite::rb_setY), 1);
		rb_define_method(rb_cSprite, "z", RUBY_METHOD_FUNC(&Sprite::rb_getZ), 0);
		rb_define_method(rb_cSprite, "z=", RUBY_METHOD_FUNC(&Sprite::rb_setZ), 1);
		rb_define_method(rb_cSprite, "bitmap", RUBY_METHOD_FUNC(&Sprite::rb_getBitmap), 0);
		rb_define_method(rb_cSprite, "bitmap=", RUBY_METHOD_FUNC(&Sprite::rb_setBitmap), 1);
		rb_define_method(rb_cSprite, "disposed?", RUBY_METHOD_FUNC(&Sprite::rb_isDisposed), 0);
		// methods
	}

	VALUE Sprite::wrap()
	{
		Sprite* sprite = this;
		return Data_Wrap_Struct(rb_cSprite, NULL, NULL, sprite);
	}

	void Sprite::gc_mark(Sprite* sprite)
	{
		if (!NIL_P(sprite->rb_bitmap))
		{
			rb_gc_mark(sprite->rb_bitmap);
		}
	}

	void Sprite::gc_free(Sprite* sprite)
	{
		sprite->rb_bitmap = Qnil;
		sprite->bitmap = NULL;
		sprite->disposed = true;
		Graphics::removeSprite(sprite);
	}

	VALUE Sprite::rb_new(VALUE classe)
	{
		Sprite* sprite;
		return Data_Make_Struct(rb_cSprite, Sprite, Sprite::gc_mark, Sprite::gc_free, sprite);
	}

	VALUE Sprite::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		Graphics::addSprite(sprite);
		return self;
	}

	VALUE Sprite::rb_dispose(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		if (!sprite->disposed)
		{
			sprite->disposed = true;
			Graphics::removeSprite(sprite);
		}
		return Qnil;
	}

	/****************************************************************************************
		* Ruby Getters/Setters
		****************************************************************************************/

	VALUE Sprite::rb_getX(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		return INT2NUM(sprite->x);
	}

	VALUE Sprite::rb_setX(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		sprite->x = NUM2INT(value);
		return value;
	}

	VALUE Sprite::rb_getY(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		return INT2NUM(sprite->y);
	}

	VALUE Sprite::rb_setY(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		sprite->y = NUM2INT(value);
		return value;
	}

	VALUE Sprite::rb_getZ(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		return INT2NUM(sprite->z);
	}

	VALUE Sprite::rb_setZ(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		int z = NUM2INT(value);
		if (sprite->z != z)
		{
			sprite->z = z;
			Graphics::updateSprite(sprite);
		}
		return value;
	}

	VALUE Sprite::rb_getBitmap(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		return sprite->rb_bitmap;
	}

	VALUE Sprite::rb_setBitmap(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		sprite->rb_bitmap = value;
		if (!NIL_P(value))
		{
			RB_VAR2CPP(value, Bitmap, bitmap);
			sprite->bitmap = bitmap;
		}
		else
		{
			sprite->bitmap = NULL;
		}
		return value;
	}

	VALUE Sprite::rb_isDisposed(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		return (sprite->disposed ? Qtrue : Qfalse);
	}

	/****************************************************************************************
		* Ruby Methods
		****************************************************************************************/

	/****************************************************************************************
		* TODO
		****************************************************************************************/





	VALUE Sprite::flash(VALUE self, VALUE color, VALUE duration)
	{
		/// @todo implement
		return Qnil;
	}

	VALUE Sprite::setAngle(VALUE self, VALUE value)
	{
		value = rb_int_new(NUM2INT(value) % 360);
		rb_iv_set(rb_cSprite, "@angle", value);
		return value;
	}

	VALUE Sprite::setOpacity(VALUE self, VALUE value)
	{
		value = rb_float_new(hclamp(NUM2DBL(value), 0.0, 255.0));
		rb_iv_set(rb_cSprite, "@opacity", value);
		return value;
	}

	VALUE Sprite::setZoomX(VALUE self, VALUE value)
	{
		value = rb_float_new(hclamp(NUM2DBL(value), 0.1, NUM2DBL(value)));
		rb_iv_set(rb_cSprite, "@zoom_x", value);
		return value;
	}

	VALUE Sprite::setZoomY(VALUE self, VALUE value)
	{
		value = rb_float_new(hclamp(NUM2DBL(value), 0.1, NUM2DBL(value)));
		rb_iv_set(rb_cSprite, "@zoom_y", value);
		return value;
	}

	VALUE Sprite::update(VALUE self)
	{
		/// @todo implement
		return Qnil;
	}

}
