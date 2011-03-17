#include <ruby.h>

#include <hltypes/util.h>

#include "RGSS/Sprite.h"
#include "RGSS/Color.h"
#include "RGSS/Rect.h"
#include "RGSS/Tone.h"
#include "RGSS/Viewport.h"
#include "RGSS/Bitmap.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Sprite::createRubyInterface()
		{
			rb_cSprite = rb_define_class("Sprite", rb_cObject);
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
			rb_define_attr(rb_cSprite, "x", 1, 1);
			rb_define_attr(rb_cSprite, "y", 1, 1);
			rb_define_attr(rb_cSprite, "z", 1, 1);
			rb_define_attr(rb_cSprite, "zoom_x", 1, 0);
			rb_define_attr(rb_cSprite, "zoom_y", 1, 0);
			rb_define_method(rb_cSprite, "initialize", RUBY_METHOD_FUNC(&Sprite::initialize), -1);
			rb_define_method(rb_cSprite, "bitmap=", RUBY_METHOD_FUNC(&Sprite::setBitmap), 1);
			rb_define_method(rb_cSprite, "dispose", RUBY_METHOD_FUNC(&Sprite::dispose), 0);
			rb_define_method(rb_cSprite, "disposed?", RUBY_METHOD_FUNC(&Sprite::isDisposed), 0);
			rb_define_method(rb_cSprite, "flash", RUBY_METHOD_FUNC(&Sprite::flash), 2);
			rb_define_method(rb_cSprite, "opacity=", RUBY_METHOD_FUNC(&Sprite::setOpacity), 1);
			rb_define_method(rb_cSprite, "update", RUBY_METHOD_FUNC(&Sprite::update), 0);
			rb_define_method(rb_cSprite, "zoom_x=", RUBY_METHOD_FUNC(&Sprite::setZoomX), 1);
			rb_define_method(rb_cSprite, "zoom_y=", RUBY_METHOD_FUNC(&Sprite::setZoomY), 1);
		}

		VALUE Sprite::dispose(VALUE self)
		{
			/// @todo implement
			return Qnil;
		}

		VALUE Sprite::flash(VALUE self, VALUE color, VALUE duration)
		{
			/// @todo implement
			return Qnil;
		}

		VALUE Sprite::initialize(int argc, VALUE *argv, VALUE self)
		{
			if (argc == 1)
				rb_iv_set(rb_cSprite, "@viewport", argv[0]);
			return self;
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
