#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

#include "RGSS/Bitmap.h"
#include "RGSS/Color.h"
#include "RGSS/Graphics.h"
#include "RGSS/Rect.h"
#include "RGSS/Sprite.h"
#include "RGSS/Tone.h"
#include "RGSS/Viewport.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Sprite::draw()
		{
			april::Color color(hrand(255), hrand(255), hrand(255));
			april::rendersys->drawColoredQuad(grect((float)this->x, (float)this->y, 80.0f, 80.0f), color);
		}

		void Sprite::createRubyInterface()
		{
			rb_cSprite = rb_define_class("Sprite", rb_cObject);
			rb_define_alloc_func(rb_cSprite, &Sprite::rb_new);
			// initialize
			rb_define_method(rb_cSprite, "initialize", RUBY_METHOD_FUNC(&Sprite::rb_initialize), -1);
			// getters and setters
			rb_define_method(rb_cSprite, "x", RUBY_METHOD_FUNC(&Sprite::rb_getX), 0);
			rb_define_method(rb_cSprite, "x=", RUBY_METHOD_FUNC(&Sprite::rb_setX), 1);
			rb_define_method(rb_cSprite, "y", RUBY_METHOD_FUNC(&Sprite::rb_getY), 0);
			rb_define_method(rb_cSprite, "y=", RUBY_METHOD_FUNC(&Sprite::rb_setY), 1);
			rb_define_method(rb_cSprite, "z", RUBY_METHOD_FUNC(&Sprite::rb_getZ), 0);
			rb_define_method(rb_cSprite, "z=", RUBY_METHOD_FUNC(&Sprite::rb_setZ), 1);

			/*
			rb_define_attr(rb_cSprite, "angle", 1, 1);
			rb_define_attr(rb_cSprite, "bitmap", 1, 0);
			rb_define_attr(rb_cSprite, "blend_type", 1, 1);
			rb_define_attr(rb_cSprite, "bush_depth", 1, 1);
			rb_define_attr(rb_cSprite, "color", 1, 1);
			rb_define_attr(rb_cSprite, "mirror", 1, 1);
			rb_define_attr(rb_cSprite, "opacity", 1, 0);
			rb_define_attr(rb_cSprite, "ox", 1, 1);
			rb_define_attr(rb_cSprite, "oy", 1, 1);
			rb_define_attr(rb_cSprite, "src_rect", 1, 1);
			rb_define_attr(rb_cSprite, "tone", 1, 1);
			rb_define_attr(rb_cSprite, "viewport", 1, 0);
			rb_define_attr(rb_cSprite, "visible", 1, 1);
			rb_define_attr(rb_cSprite, "zoom_x", 1, 0);
			rb_define_attr(rb_cSprite, "zoom_y", 1, 0);
			rb_define_method(rb_cSprite, "bitmap=", RUBY_METHOD_FUNC(&Sprite::setBitmap), 1);
			rb_define_method(rb_cSprite, "dispose", RUBY_METHOD_FUNC(&Sprite::rb_dispose), 0);
			rb_define_method(rb_cSprite, "disposed?", RUBY_METHOD_FUNC(&Sprite::isDisposed), 0);
			rb_define_method(rb_cSprite, "flash", RUBY_METHOD_FUNC(&Sprite::flash), 2);
			rb_define_method(rb_cSprite, "opacity=", RUBY_METHOD_FUNC(&Sprite::setOpacity), 1);
			rb_define_method(rb_cSprite, "update", RUBY_METHOD_FUNC(&Sprite::update), 0);
			rb_define_method(rb_cSprite, "zoom_x=", RUBY_METHOD_FUNC(&Sprite::setZoomX), 1);
			rb_define_method(rb_cSprite, "zoom_y=", RUBY_METHOD_FUNC(&Sprite::setZoomY), 1);
			*/
		}

		void Sprite::gc_mark(Sprite* sprite)
		{
			//rb_gc_mark(sprite->getBitmap())
		}

		VALUE Sprite::rb_new(VALUE classe)
		{
			Sprite* sprite;
			//return Data_Make_Struct(classe, Sprite, gc_mark, NULL, sprite);
			return Data_Make_Struct(classe, Sprite, NULL, NULL, sprite);
		}

		VALUE Sprite::rb_initialize(int argc, VALUE* argv, VALUE self)
		{
			RB_VAR2CPP(Sprite, sprite);
			Graphics::addSprite(sprite);
			return self;
		}

		VALUE Sprite::rb_dispose(VALUE self)
		{
			RB_VAR2CPP(Sprite, sprite);
			Graphics::removeSprite(sprite);
			/// @todo implement
			return Qnil;
		}

		VALUE Sprite::rb_getX(VALUE self)
		{
			RB_VAR2CPP(Sprite, sprite);
			return rb_float_new(sprite->x);
		}

		VALUE Sprite::rb_setX(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Sprite, sprite);
			sprite->x = NUM2INT(value);
			return self;
		}

		VALUE Sprite::rb_getY(VALUE self)
		{
			RB_VAR2CPP(Sprite, sprite);
			return rb_float_new(sprite->y);
		}

		VALUE Sprite::rb_setY(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Sprite, sprite);
			sprite->y = NUM2INT(value);
			return self;
		}

		VALUE Sprite::rb_getZ(VALUE self)
		{
			RB_VAR2CPP(Sprite, sprite);
			return rb_float_new(sprite->z);
		}

		VALUE Sprite::rb_setZ(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Sprite, sprite);
			int z = NUM2INT(value);
			if (sprite->z != z)
			{
				sprite->z = z;
				Graphics::updateSprite(sprite);
			}
			return self;
		}

		VALUE Sprite::flash(VALUE self, VALUE color, VALUE duration)
		{
			/// @todo implement
			return Qnil;
		}

		VALUE Sprite::isDisposed(VALUE self)
		{
			/// @todo needs to return bool, not Qnil after implementing
			return Qnil;
		}

		VALUE Sprite::setAngle(VALUE self, VALUE value)
		{
			value = rb_int_new(NUM2INT(value) % 360);
			rb_iv_set(rb_cSprite, "@angle", value);
			return value;
		}

		VALUE Sprite::setBitmap(VALUE self, VALUE* value)
		{
			/// @todo add exception
			rb_iv_set(rb_cSprite, "@bitmap", *value);
			return *value;
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
}
