#include <ruby.h>

#include <hltypes/util.h>

#include "RGSS/Rect.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Rect::set(float x, float y, float width, float height)
		{
			this->x = x;
			this->y = y;
			this->width = width;
			this->height = height;
		}

		void Rect::createRubyInterface()
		{
			rb_cRect = rb_define_class("Rect", rb_cObject);
			rb_define_alloc_func(rb_cRect, &Rect::rb_new);
			// initialize
			rb_define_method(rb_cRect, "initialize", RUBY_METHOD_FUNC(&Rect::rb_initialize), -1);
			rb_define_method(rb_cRect, "inspect", RUBY_METHOD_FUNC(&Rect::rb_inspect), 0);
			// getters and setters
			rb_define_method(rb_cRect, "x", RUBY_METHOD_FUNC(&Rect::rb_getX), 0);
			rb_define_method(rb_cRect, "x=", RUBY_METHOD_FUNC(&Rect::rb_setX), 1);
			rb_define_method(rb_cRect, "y", RUBY_METHOD_FUNC(&Rect::rb_getY), 0);
			rb_define_method(rb_cRect, "y=", RUBY_METHOD_FUNC(&Rect::rb_setY), 1);
			rb_define_method(rb_cRect, "width", RUBY_METHOD_FUNC(&Rect::rb_getWidth), 0);
			rb_define_method(rb_cRect, "width=", RUBY_METHOD_FUNC(&Rect::rb_setWidth), 1);
			rb_define_method(rb_cRect, "height", RUBY_METHOD_FUNC(&Rect::rb_getHeight), 0);
			rb_define_method(rb_cRect, "height=", RUBY_METHOD_FUNC(&Rect::rb_setHeight), 1);
			// all other methods
			rb_define_method(rb_cRect, "set", RUBY_METHOD_FUNC(&Rect::rb_set), -1);
			// static methods
		}

		VALUE Rect::wrap()
		{
			Rect* rect = this;
			return Data_Wrap_Struct(rb_cRect, NULL, NULL, rect);
		}

		VALUE Rect::rb_new(VALUE classe)
		{
			Rect* rect;
			return Data_Make_Struct(classe, Rect, NULL, NULL, rect);
		}

		VALUE Rect::rb_initialize(int argc, VALUE* argv, VALUE self)
		{
			return Rect::rb_set(argc, argv, self);
		}

		VALUE Rect::rb_inspect(VALUE self)
		{
			RB_SELF2CPP(Rect, rect);
			hstr result = hsprintf("(%.1f,%.1f,%.1f,%.1f)", rect->x, rect->y, rect->width, rect->height);
			return rb_str_new2(result.c_str());
		}

		VALUE Rect::rb_getX(VALUE self)
		{
			RB_SELF2CPP(Rect, rect);
			return rb_float_new(rect->x);
		}

		VALUE Rect::rb_setX(VALUE self, VALUE value)
		{
			RB_SELF2CPP(Rect, rect);
			rect->x = (float)NUM2DBL(value);
			return self;
		}

		VALUE Rect::rb_getY(VALUE self)
		{
			RB_SELF2CPP(Rect, rect);
			return rb_float_new(rect->y);
		}

		VALUE Rect::rb_setY(VALUE self, VALUE value)
		{
			RB_SELF2CPP(Rect, rect);
			rect->y = (float)NUM2DBL(value);
			return self;
		}

		VALUE Rect::rb_getWidth(VALUE self)
		{
			RB_SELF2CPP(Rect, rect);
			return rb_float_new(rect->width);
		}

		VALUE Rect::rb_setWidth(VALUE self, VALUE value)
		{
			RB_SELF2CPP(Rect, rect);
			rect->width = (float)NUM2DBL(value);
			return self;
		}

		VALUE Rect::rb_getHeight(VALUE self)
		{
			RB_SELF2CPP(Rect, rect);
			return rb_float_new(rect->height);
		}

		VALUE Rect::rb_setHeight(VALUE self, VALUE value)
		{
			RB_SELF2CPP(Rect, rect);
			rect->height = (float)NUM2DBL(value);
			return self;
		}

		VALUE Rect::rb_set(int argc, VALUE* argv, VALUE self)
		{
			VALUE x, y, width, height;
			// "31" means 3 mandatory arguments, 1 optional argument
			rb_scan_args(argc, argv, "4", &x, &y, &width, &height);
			RB_SELF2CPP(Rect, rect);
			rect->x = (float)NUM2DBL(x);
			rect->y = (float)NUM2DBL(y);
			rect->width = (float)NUM2DBL(width);
			rect->height = (float)NUM2DBL(height);
			return self;
		}

	}
}
