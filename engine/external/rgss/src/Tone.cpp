#include <ruby.h>

#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Tone.h"

namespace rgss
{
	VALUE rb_cTone;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Tone::set(float r, float g, float b, float a)
	{
		this->red = hclamp(r, -255.0f, 255.0f);
		this->green = hclamp(g, -255.0f, 255.0f);
		this->blue = hclamp(b, -255.0f, 255.0f);
		this->gray = hclamp(a, 0.0f, 255.0f);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Tone::init()
	{
	}

	void Tone::destroy()
	{
	}

	void Tone::createRubyInterface()
	{
		rb_cTone = rb_define_class("Tone", rb_cObject);
		rb_define_alloc_func(rb_cTone, &Tone::rb_new);
		// initialize
		rb_define_method(rb_cTone, "initialize", RUBY_METHOD_FUNC(&Tone::rb_initialize), -1);
		rb_define_method(rb_cTone, "initialize_copy", RUBY_METHOD_FUNC(&Tone::rb_initialize_copy), 1);
		rb_define_method(rb_cTone, "inspect", RUBY_METHOD_FUNC(&Tone::rb_inspect), 0);
		rb_define_method(rb_cTone, "_dump", RUBY_METHOD_FUNC(&Tone::rb_dump), -1);
		rb_define_singleton_method(rb_cTone, "_load", RUBY_METHOD_FUNC(&Tone::rb_load), 1);
		rb_define_method(rb_cTone, "_arc_dump", RUBY_METHOD_FUNC(&Tone::rb_arcDump), 0);
		rb_define_singleton_method(rb_cTone, "_arc_load", RUBY_METHOD_FUNC(&Tone::rb_arcLoad), 1);
		// getters and setters
		rb_define_method(rb_cTone, "red", RUBY_METHOD_FUNC(&Tone::rb_getRed), 0);
		rb_define_method(rb_cTone, "red=", RUBY_METHOD_FUNC(&Tone::rb_setRed), 1);
		rb_define_method(rb_cTone, "green", RUBY_METHOD_FUNC(&Tone::rb_getGreen), 0);
		rb_define_method(rb_cTone, "green=", RUBY_METHOD_FUNC(&Tone::rb_setGreen), 1);
		rb_define_method(rb_cTone, "blue", RUBY_METHOD_FUNC(&Tone::rb_getBlue), 0);
		rb_define_method(rb_cTone, "blue=", RUBY_METHOD_FUNC(&Tone::rb_setBlue), 1);
		rb_define_method(rb_cTone, "gray", RUBY_METHOD_FUNC(&Tone::rb_getGray), 0);
		rb_define_method(rb_cTone, "gray=", RUBY_METHOD_FUNC(&Tone::rb_setGray), 1);
		// all other methods
		rb_define_method(rb_cTone, "set", RUBY_METHOD_FUNC(&Tone::rb_set), -1);
	}

	VALUE Tone::rb_new(VALUE classe)
	{
		Tone* color;
		return Data_Make_Struct(classe, Tone, NULL, NULL, color);
	}

	VALUE Tone::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		VALUE r, g, b, a;
		rb_scan_args(argc, argv, "31", &r, &g, &b, &a);
		Tone::rb_set(argc, argv, self);
		return self;
	}

	VALUE Tone::rb_initialize_copy(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Tone, tone);
		RB_VAR2CPP(original, Tone, other);
		tone->red = other->red;
		tone->green = other->green;
		tone->blue = other->blue;
		tone->gray = other->gray;
		return self;
	}

	VALUE Tone::rb_inspect(VALUE self)
	{
		RB_SELF2CPP(Tone, color);
		hstr result = hsprintf("(%.1f,%.1f,%.1f,%.1f)", color->red, color->green, color->blue, color->gray);
		return rb_str_new2(result.c_str());
	}

	VALUE Tone::create(int argc, VALUE* argv)
	{
		VALUE object = Tone::rb_new(rb_cTone);
		object = Tone::rb_initialize(argc, argv, object);
		return object;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Tone::rb_getRed(VALUE self)
	{
		RB_SELF2CPP(Tone, color);
		return rb_float_new(color->red);
	}

	VALUE Tone::rb_setRed(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Tone, color);
		color->red = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
		return self;
	}

	VALUE Tone::rb_getGreen(VALUE self)
	{
		RB_SELF2CPP(Tone, color);
		return rb_float_new(color->green);
	}

	VALUE Tone::rb_setGreen(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Tone, color);
		color->green = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
		return self;
	}

	VALUE Tone::rb_getBlue(VALUE self)
	{
		RB_SELF2CPP(Tone, color);
		return rb_float_new(color->blue);
	}

	VALUE Tone::rb_setBlue(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Tone, color);
		color->blue = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
		return self;
	}

	VALUE Tone::rb_getGray(VALUE self)
	{
		RB_SELF2CPP(Tone, color);
		return rb_float_new(color->gray);
	}

	VALUE Tone::rb_setGray(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Tone, color);
		color->gray = hclamp((float)NUM2DBL(value), 0.0f, 255.0f);
		return self;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Tone::rb_set(int argc, VALUE* argv, VALUE self)
	{
		VALUE r, g, b, a;
		rb_scan_args(argc, argv, "31", &r, &g, &b, &a);
		RB_SELF2CPP(Tone, color);
		color->red = hclamp((float)NUM2DBL(r), -255.0f, 255.0f);
		color->green = hclamp((float)NUM2DBL(g), -255.0f, 255.0f);
		color->blue = hclamp((float)NUM2DBL(b), -255.0f, 255.0f);
		color->gray = (NIL_P(a) ? 255.0f : hclamp((float)NUM2DBL(a), 0.0f, 255.0f));
		return Qnil;
	}

	/****************************************************************************************
	 * Serialization
	 ****************************************************************************************/

	VALUE Tone::rb_dump(int argc, VALUE* argv, VALUE self)
	{
		VALUE d;
		rb_scan_args(argc, argv, "01", &d);
		if (NIL_P(d))
		{
			d = INT2FIX(-1);
		}
		RB_SELF2CPP(Tone, tone);
		VALUE arr = rb_ary_new3(4, rb_float_new(tone->red), rb_float_new(tone->green),
			rb_float_new(tone->blue), rb_float_new(tone->gray));
		VALUE byte_string = rb_funcall_1(arr, "pack", rb_str_new2("d4"));
		return byte_string;
	}

	VALUE Tone::rb_load(VALUE self, VALUE value)
	{
		VALUE arr = rb_funcall_1(value, "unpack", rb_str_new2("d4"));
		VALUE c_arr[4];
		c_arr[0] = rb_ary_shift(arr);
		c_arr[1] = rb_ary_shift(arr);
		c_arr[2] = rb_ary_shift(arr);
		c_arr[3] = rb_ary_shift(arr);
		return Tone::create(4, c_arr);
	}

	VALUE Tone::rb_arcDump(VALUE self)
	{
		RB_SELF2CPP(Tone, tone);
		VALUE arr = rb_ary_new3(4, rb_float_new(tone->red), rb_float_new(tone->green),
			rb_float_new(tone->blue), rb_float_new(tone->gray));
		VALUE byte_string = rb_funcall_1(arr, "pack", rb_str_new2("eeee"));
		return byte_string;
	}

	VALUE Tone::rb_arcLoad(VALUE self, VALUE value)
	{
		VALUE arr = rb_funcall_1(value, "unpack", rb_str_new2("eeee"));
		VALUE c_arr[4];
		c_arr[0] = rb_ary_shift(arr);
		c_arr[1] = rb_ary_shift(arr);
		c_arr[2] = rb_ary_shift(arr);
		c_arr[3] = rb_ary_shift(arr);
		return Tone::create(4, c_arr);
	}

}