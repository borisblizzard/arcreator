#include <ruby.h>

#include <april/Color.h>
#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Color.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cColor;

	void Color::set(float r, float g, float b, float a)
	{
		this->red = hclamp(r, -255.0f, 255.0f);
		this->green = hclamp(g, -255.0f, 255.0f);
		this->blue = hclamp(b, -255.0f, 255.0f);
		this->alpha = hclamp(a, 0.0f, 255.0f);
	}

	void Color::set(april::Color color)
	{
		this->red = (float)color.r;
		this->green = (float)color.g;
		this->blue = (float)color.b;
		this->alpha = (float)color.a;
	}

	april::Color Color::toAprilColor()
	{
		return april::Color((unsigned char)this->red, (unsigned char)this->green,
			(unsigned char)this->blue, (unsigned char)this->alpha);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Color::init()
	{
	}

	void Color::createRubyInterface()
	{
		rb_cColor = rb_define_class("Color", rb_cObject);
		rb_define_alloc_func(rb_cColor, &Color::rb_new);
		// initialize
		rb_define_method(rb_cColor, "initialize", RUBY_METHOD_FUNC(&Color::rb_initialize), -1);
		rb_define_method(rb_cColor, "inspect", RUBY_METHOD_FUNC(&Color::rb_inspect), 0);
		rb_define_method(rb_cColor, "_dump", RUBY_METHOD_FUNC(&Color::rb_dump), -1);
		rb_define_singleton_method(rb_cColor, "_load", RUBY_METHOD_FUNC(&Color::rb_load), 1);
		// getters and setters
		rb_define_method(rb_cColor, "red", RUBY_METHOD_FUNC(&Color::rb_getRed), 0);
		rb_define_method(rb_cColor, "red=", RUBY_METHOD_FUNC(&Color::rb_setRed), 1);
		rb_define_method(rb_cColor, "green", RUBY_METHOD_FUNC(&Color::rb_getGreen), 0);
		rb_define_method(rb_cColor, "green=", RUBY_METHOD_FUNC(&Color::rb_setGreen), 1);
		rb_define_method(rb_cColor, "blue", RUBY_METHOD_FUNC(&Color::rb_getBlue), 0);
		rb_define_method(rb_cColor, "blue=", RUBY_METHOD_FUNC(&Color::rb_setBlue), 1);
		rb_define_method(rb_cColor, "alpha", RUBY_METHOD_FUNC(&Color::rb_getAlpha), 0);
		rb_define_method(rb_cColor, "alpha=", RUBY_METHOD_FUNC(&Color::rb_setAlpha), 1);
		// methods
		rb_define_method(rb_cColor, "set", RUBY_METHOD_FUNC(&Color::rb_set), -1);
	}

	VALUE Color::rb_new(VALUE classe)
	{
		Color* color;
		return Data_Make_Struct(classe, Color, NULL, NULL, color);
	}

	VALUE Color::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		// TODO Is this needed since rb_set function checks the same values?
		VALUE r, g, b, a;
		rb_scan_args(argc, argv, "31", &r, &g, &b, &a);
		Color::rb_set(argc, argv, self);
		return self;
	}

	VALUE Color::rb_inspect(VALUE self)
	{
		RB_SELF2CPP(Color, color);
		hstr result = hsprintf("(%.1f,%.1f,%.1f,%.1f)", color->red, color->green, color->blue, color->alpha);
		return rb_str_new2(result.c_str());
	}

	VALUE Color::create(int argc, VALUE* argv)
	{
		VALUE object = Color::rb_new(rb_cColor);
		object = Color::rb_initialize(argc, argv, object);
		return object;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Color::rb_getRed(VALUE self)
	{
		RB_SELF2CPP(Color, color);
		return rb_float_new(color->red);
	}

	VALUE Color::rb_setRed(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Color, color);
		color->red = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
		return self;
	}

	VALUE Color::rb_getGreen(VALUE self)
	{
		RB_SELF2CPP(Color, color);
		return rb_float_new(color->green);
	}

	VALUE Color::rb_setGreen(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Color, color);
		color->green = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
		return self;
	}

	VALUE Color::rb_getBlue(VALUE self)
	{
		RB_SELF2CPP(Color, color);
		return rb_float_new(color->blue);
	}

	VALUE Color::rb_setBlue(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Color, color);
		color->blue = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
		return self;
	}

	VALUE Color::rb_getAlpha(VALUE self)
	{
		RB_SELF2CPP(Color, color);
		return rb_float_new(color->alpha);
	}

	VALUE Color::rb_setAlpha(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Color, color);
		color->alpha = hclamp((float)NUM2DBL(value), 0.0f, 255.0f);
		return self;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Color::rb_set(int argc, VALUE* argv, VALUE self)
	{
		VALUE r, g, b, a;
		rb_scan_args(argc, argv, "31", &r, &g, &b, &a);
		RB_SELF2CPP(Color, color);
		color->red = hclamp((float)NUM2DBL(r), -255.0f, 255.0f);
		color->green = hclamp((float)NUM2DBL(g), -255.0f, 255.0f);
		color->blue = hclamp((float)NUM2DBL(b), -255.0f, 255.0f);
		color->alpha = (NIL_P(a) ? 255.0f : hclamp((float)NUM2DBL(a), 0.0f, 255.0f));
		return Qnil;
	}

	VALUE Color::rb_dump(int argc, VALUE* argv, VALUE self)
	{
		VALUE d;
		rb_scan_args(argc, argv, "01", &d);
		if (NIL_P(d))
		{
			d = INT2FIX(0);
		}
		RB_SELF2CPP(Color, color);
		// create array
		VALUE arr = rb_ary_new();
		// populate array
		rb_ary_push(arr, rb_float_new(color->red));
		rb_ary_push(arr, rb_float_new(color->green));
		rb_ary_push(arr, rb_float_new(color->blue));
		rb_ary_push(arr, rb_float_new(color->alpha));
		// get the method id
		ID pack_id = rb_intern("pack");
		// create the ruby pack format string 
		VALUE format_str = rb_str_new2("d4");
		// call the pack method
		VALUE byte_string = rb_funcall(arr, pack_id, 1, format_str);
		return byte_string;

	}

	VALUE Color::rb_load(VALUE self, VALUE value)
	{
		// get the method id
		ID unpack_id = rb_intern("unpack");
		// create the ruby pack format string 
		VALUE format_str = rb_str_new2("d4");
		// call the unpack function
		VALUE arr = rb_funcall(value, unpack_id, 1, format_str);
		VALUE c_arr[4];
		c_arr[0] = rb_ary_shift(arr);
		c_arr[1] = rb_ary_shift(arr);
		c_arr[2] = rb_ary_shift(arr);
		c_arr[3] = rb_ary_shift(arr);
		return Color::create(4, c_arr);
	}

}
