#include <ruby.h>

#include <hltypes/util.h>

#include "RGSS/Rect.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Rect::set(int x, int y, int width, int height)
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
			rb_define_method(rb_cRect, "initialize", RUBY_METHOD_FUNC(&Rect::rb_initialize), 4);
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
			rb_define_method(rb_cRect, "set", RUBY_METHOD_FUNC(&Rect::rb_set), 4);
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

		VALUE Rect::rb_initialize(VALUE self, VALUE x, VALUE y, VALUE width, VALUE height)
		{
			Rect::rb_set(self, x, y, width, height);
			return self;
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
			return INT2FIX(rect->x);
		}

		VALUE Rect::rb_setX(VALUE self, VALUE value)
		{
			RB_SELF2CPP(Rect, rect);
			rect->x = NUM2INT(value);
			return value;
		}

		VALUE Rect::rb_getY(VALUE self)
		{
			RB_SELF2CPP(Rect, rect);
			return INT2FIX(rect->y);
		}

		VALUE Rect::rb_setY(VALUE self, VALUE value)
		{
			RB_SELF2CPP(Rect, rect);
			rect->y = NUM2INT(value);
			return value;
		}

		VALUE Rect::rb_getWidth(VALUE self)
		{
			RB_SELF2CPP(Rect, rect);
			return INT2FIX(rect->width);
		}

		VALUE Rect::rb_setWidth(VALUE self, VALUE value)
		{
			RB_SELF2CPP(Rect, rect);
			rect->width = INT2FIX(value);
			return value;
		}

		VALUE Rect::rb_getHeight(VALUE self)
		{
			RB_SELF2CPP(Rect, rect);
			return INT2FIX(rect->height);
		}

		VALUE Rect::rb_setHeight(VALUE self, VALUE value)
		{
			RB_SELF2CPP(Rect, rect);
			rect->height = NUM2INT(value);
			return value;
		}

		VALUE Rect::rb_set(VALUE self, VALUE x, VALUE y, VALUE width, VALUE height)
		{
			RB_SELF2CPP(Rect, rect);
			rect->x = NUM2INT(x);
			rect->y = NUM2INT(y);
			rect->width = NUM2INT(width);
			rect->height = NUM2INT(height);
			return Qnil;
		}

	}
}
