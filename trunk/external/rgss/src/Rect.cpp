#include <ruby.h>

#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Rect.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cRect;

	void Rect::set(int x, int y, int width, int height)
	{
		this->x = x;
		this->y = y;
		this->width = width;
		this->height = height;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Rect::init()
	{
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
		rb_define_method(rb_cRect, "_dump", RUBY_METHOD_FUNC(&Rect::rb_dump), -1);
		rb_define_singleton_method(rb_cRect, "_load", RUBY_METHOD_FUNC(&Rect::rb_load), 1);
		// static methods
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
		hstr result = hsprintf("(%d,%d,%d,%d)", rect->x, rect->y, rect->width, rect->height);
		return rb_str_new2(result.c_str());
	}

	VALUE Rect::create(VALUE x, VALUE y, VALUE width, VALUE height)
	{
		VALUE object = Rect::rb_new(rb_cRect);
		object = Rect::rb_initialize(object, x, y, width, height);
		return object;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

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

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Rect::rb_set(VALUE self, VALUE x, VALUE y, VALUE width, VALUE height)
	{
		RB_SELF2CPP(Rect, rect);
		rect->x = NUM2INT(x);
		rect->y = NUM2INT(y);
		rect->width = NUM2INT(width);
		rect->height = NUM2INT(height);
		return Qnil;
	}

	VALUE Rect::rb_dump(int argc, VALUE* argv, VALUE self)
	{
		VALUE d;
		rb_scan_args(argc, argv, "01", &d);
		if (NIL_P(d))
		{
			d = INT2FIX(0);
		}
		RB_SELF2CPP(Rect, rect);
		// create array
		VALUE arr = rb_ary_new();
		// populate array
		rb_ary_push(arr, INT2FIX(rect->x));
		rb_ary_push(arr, INT2FIX(rect->y));
		rb_ary_push(arr, INT2FIX(rect->width));
		rb_ary_push(arr, INT2FIX(rect->height));
		// get the method id
		ID pack_id = rb_intern("pack");
		// create the ruby pack format string 
		VALUE format_str = rb_str_new2("l4");
		// call the pack method
		VALUE byte_string = rb_funcall(arr, pack_id, 1, format_str);
		return byte_string;

	}

	VALUE Rect::rb_load(VALUE self, VALUE value)
	{
		// get the method id
		ID unpack_id = rb_intern("unpack");
		// create the ruby pack format string 
		VALUE format_str = rb_str_new2("l4");
		// call the unpack function
		VALUE arr = rb_funcall(value, unpack_id, 1, format_str);
		VALUE x = rb_ary_shift(arr);
		VALUE y = rb_ary_shift(arr);
		VALUE width = rb_ary_shift(arr);
		VALUE height = rb_ary_shift(arr);
		return Rect::create(x, y, width, height);
	}

}
