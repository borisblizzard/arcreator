#include <ruby.h>

#include <hltypes/util.h>

#include "RGSS/Color.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Color::set(float r, float g, float b, float a)
		{
			this->red = hclamp(r, -255.0f, 255.0f);
			this->green = hclamp(g, -255.0f, 255.0f);
			this->blue = hclamp(b, -255.0f, 255.0f);
			this->alpha = hclamp(a, 0.0f, 255.0f);
		}

		void Color::createRubyInterface()
		{
			rb_cColor = rb_define_class("Color", rb_cObject);
			rb_define_alloc_func(rb_cColor, &Color::rb_new);
			// initialize
			rb_define_method(rb_cColor, "initialize", RUBY_METHOD_FUNC(&Color::rb_initialize), -1);
			rb_define_method(rb_cColor, "inspect", RUBY_METHOD_FUNC(&Color::rb_inspect), 0);
			// getters and setters
			rb_define_method(rb_cColor, "red", RUBY_METHOD_FUNC(&Color::rb_getRed), 0);
			rb_define_method(rb_cColor, "red=", RUBY_METHOD_FUNC(&Color::rb_setRed), 1);
			rb_define_method(rb_cColor, "green", RUBY_METHOD_FUNC(&Color::rb_getGreen), 0);
			rb_define_method(rb_cColor, "green=", RUBY_METHOD_FUNC(&Color::rb_setGreen), 1);
			rb_define_method(rb_cColor, "blue", RUBY_METHOD_FUNC(&Color::rb_getBlue), 0);
			rb_define_method(rb_cColor, "blue=", RUBY_METHOD_FUNC(&Color::rb_setBlue), 1);
			rb_define_method(rb_cColor, "alpha", RUBY_METHOD_FUNC(&Color::rb_getAlpha), 0);
			rb_define_method(rb_cColor, "alpha=", RUBY_METHOD_FUNC(&Color::rb_setAlpha), 1);
			// all other methods
			rb_define_method(rb_cColor, "set", RUBY_METHOD_FUNC(&Color::rb_set), -1);
			// static methods
		}

		VALUE Color::rb_new(VALUE classe)
		{
			Color* color;
			return Data_Make_Struct(classe, Color, NULL, NULL, color);
		}

		VALUE Color::rb_initialize(int argc, VALUE* argv, VALUE self)
		{
			return Color::rb_set(argc, argv, self);
		}

		VALUE Color::rb_inspect(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			hstr result = hsprintf("(%.1f,%.1f,%.1f,%.1f)", color->red, color->green, color->blue, color->alpha);
			return rb_str_new2(result.c_str());
		}

		VALUE Color::rb_getRed(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			return rb_float_new(color->red);
		}

		VALUE Color::rb_setRed(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Color, color);
			color->red = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
			return self;
		}

		VALUE Color::rb_getGreen(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			return rb_float_new(color->green);
		}

		VALUE Color::rb_setGreen(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Color, color);
			color->green = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
			return self;
		}

		VALUE Color::rb_getBlue(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			return rb_float_new(color->blue);
		}

		VALUE Color::rb_setBlue(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Color, color);
			color->blue = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
			return self;
		}

		VALUE Color::rb_getAlpha(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			return rb_float_new(color->alpha);
		}

		VALUE Color::rb_setAlpha(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Color, color);
			color->alpha = hclamp((float)NUM2DBL(value), 0.0f, 255.0f);
			return self;
		}

		VALUE Color::rb_set(int argc, VALUE* argv, VALUE self)
		{
			VALUE r, g, b, a;
			// "31" means 3 mandatory arguments, 1 optional argument
			rb_scan_args(argc, argv, "31", &r, &g, &b, &a);
			RB_VAR2CPP(Color, color);
			color->red = hclamp((float)NUM2DBL(r), -255.0f, 255.0f);
			color->green = hclamp((float)NUM2DBL(g), -255.0f, 255.0f);
			color->blue = hclamp((float)NUM2DBL(b), -255.0f, 255.0f);
			color->alpha = (NIL_P(a) ? 255.0f : hclamp((float)NUM2DBL(a), 0.0f, 255.0f));
			return self;
		}

	}
}
