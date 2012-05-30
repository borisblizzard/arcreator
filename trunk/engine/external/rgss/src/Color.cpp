#include <ruby.h>

#include <april/Color.h>
#include <hltypes/hltypesUtil.h>

#include "CodeSnippets.h"
#include "Color.h"

namespace rgss
{
	VALUE rb_cColor;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	Color::Color() : RubyObject()
	{
		this->set(0.0f, 0.0f, 0.0f, 0.0f);
	}
	
	Color::Color(float r, float g, float b, float a) : RubyObject()
	{
		this->set(r, g, b, a);
	}
	
	Color::~Color()
	{
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Color::set(float r, float g, float b, float a)
	{
		this->red = hclamp(r, 0.0f, 255.0f);
		this->green = hclamp(g, 0.0f, 255.0f);
		this->blue = hclamp(b, 0.0f, 255.0f);
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

	void Color::destroy()
	{
	}

	void Color::createRubyInterface()
	{
		rb_cColor = rb_define_class("Color", rb_cObject);
		rb_define_alloc_func(rb_cColor, &Color::rb_new);
		// initialize
		rb_define_method(rb_cColor, "initialize", RUBY_METHOD_FUNC(&Color::rb_initialize), -1);
		rb_define_method(rb_cColor, "initialize_copy", RUBY_METHOD_FUNC(&Color::rb_initialize_copy), 1);
		rb_define_method(rb_cColor, "inspect", RUBY_METHOD_FUNC(&Color::rb_inspect), 0);
		rb_define_method(rb_cColor, "_dump", RUBY_METHOD_FUNC(&Color::rb_dump), -1);
		rb_define_singleton_method(rb_cColor, "_load", RUBY_METHOD_FUNC(&Color::rb_load), 1);
		rb_define_method(rb_cColor, "_arc_dump", RUBY_METHOD_FUNC(&Color::rb_arcDump), 0);
		rb_define_singleton_method(rb_cColor, "_arc_load", RUBY_METHOD_FUNC(&Color::rb_arcLoad), 1);
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
		return RB_OBJECT_NEW(classe, Color, color, &Color::gc_mark, &Color::gc_free);
	}

	VALUE Color::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Color, color);
		Color::rb_set(argc, argv, self);
		return self;
	}

	VALUE Color::rb_initialize_copy(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Color, color);
		RB_VAR2CPP(original, Color, other);
		color->red = other->red;
		color->green = other->green;
		color->blue = other->blue;
		color->alpha = other->alpha;
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
		color->red = hclamp((float)NUM2DBL(value), 0.0f, 255.0f);
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
		color->green = hclamp((float)NUM2DBL(value), 0.0f, 255.0f);
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
		color->blue = hclamp((float)NUM2DBL(value), 0.0f, 255.0f);
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
		color->red = hclamp((float)NUM2DBL(r), 0.0f, 255.0f);
		color->green = hclamp((float)NUM2DBL(g), 0.0f, 255.0f);
		color->blue = hclamp((float)NUM2DBL(b), 0.0f, 255.0f);
		color->alpha = (NIL_P(a) ? 255.0f : hclamp((float)NUM2DBL(a), 0.0f, 255.0f));
		return Qnil;
	}

	/****************************************************************************************
	 * Serialization
	 ****************************************************************************************/

	VALUE Color::rb_dump(int argc, VALUE* argv, VALUE self)
	{
		VALUE d;
		rb_scan_args(argc, argv, "01", &d);
		if (NIL_P(d))
		{
			d = INT2FIX(-1);
		}
		RB_SELF2CPP(Color, color);
		VALUE arr = rb_ary_new3(4, rb_float_new(color->red), rb_float_new(color->green),
			rb_float_new(color->blue), rb_float_new(color->alpha));
		VALUE byte_string = rb_f_ary_pack(arr, "d4");
		return byte_string;
	}

	VALUE Color::rb_load(VALUE self, VALUE value)
	{
		VALUE arr = rb_f_str_unpack(value, "d4");
		VALUE c_arr[4];
		c_arr[0] = rb_ary_shift(arr);
		c_arr[1] = rb_ary_shift(arr);
		c_arr[2] = rb_ary_shift(arr);
		c_arr[3] = rb_ary_shift(arr);
		return Color::create(4, c_arr);
	}

	VALUE Color::rb_arcDump(VALUE self)
	{
		RB_SELF2CPP(Color, color);
		VALUE arr = rb_ary_new3(4, rb_float_new(color->red), rb_float_new(color->green),
			rb_float_new(color->blue), rb_float_new(color->alpha));
		VALUE byte_string = rb_f_ary_pack(arr, "eeee");
		return byte_string;
	}

	VALUE Color::rb_arcLoad(VALUE self, VALUE value)
	{
		VALUE arr = rb_f_str_unpack(value, "eeee");
		VALUE c_arr[4];
		c_arr[0] = rb_ary_shift(arr);
		c_arr[1] = rb_ary_shift(arr);
		c_arr[2] = rb_ary_shift(arr);
		c_arr[3] = rb_ary_shift(arr);
		return Color::create(4, c_arr);
	}

}
