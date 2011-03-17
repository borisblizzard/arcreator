#include <ruby.h>

#include <hltypes/util.h>

#include "RGSS/Color.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Color::createRubyInterface()
		{
			rb_cColor = rb_define_class("Color", rb_cObject);
			rb_define_alloc_func(rb_cColor, &Color::rb_new);
			// initialize
			rb_define_method(rb_cColor, "initialize", RUBY_METHOD_FUNC(&Color::initialize), -1);
			// getters and setters
			rb_define_method(rb_cColor, "red", RUBY_METHOD_FUNC(&Color::getRed), 0);
			rb_define_method(rb_cColor, "red=", RUBY_METHOD_FUNC(&Color::setRed), 1);
			rb_define_method(rb_cColor, "green", RUBY_METHOD_FUNC(&Color::getGreen), 0);
			rb_define_method(rb_cColor, "green=", RUBY_METHOD_FUNC(&Color::setGreen), 1);
			rb_define_method(rb_cColor, "blue", RUBY_METHOD_FUNC(&Color::getBlue), 0);
			rb_define_method(rb_cColor, "blue=", RUBY_METHOD_FUNC(&Color::setBlue), 1);
			rb_define_method(rb_cColor, "alpha", RUBY_METHOD_FUNC(&Color::getAlpha), 0);
			rb_define_method(rb_cColor, "alpha=", RUBY_METHOD_FUNC(&Color::setAlpha), 1);
			// all other methods
			rb_define_method(rb_cColor, "set", RUBY_METHOD_FUNC(&Color::set), -1);
			rb_define_method(rb_cColor, "inspect", RUBY_METHOD_FUNC(&Color::inspect), 0);
			// static methods
		}

		VALUE Color::rb_new(VALUE classe)
		{
			Color* color;
			return Data_Make_Struct(classe, Color, NULL, NULL, color);
		}

		VALUE Color::initialize(int argc, VALUE* argv, VALUE self)
		{
			return Color::set(argc, argv, self);
		}

		VALUE Color::getRed(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			return rb_float_new(color->red);
		}

		VALUE Color::setRed(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Color, color);
			color->red = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
			return self;
		}

		VALUE Color::getGreen(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			return rb_float_new(color->green);
		}

		VALUE Color::setGreen(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Color, color);
			color->green = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
			return self;
		}

		VALUE Color::getBlue(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			return rb_float_new(color->blue);
		}

		VALUE Color::setBlue(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Color, color);
			color->blue = hclamp((float)NUM2DBL(value), -255.0f, 255.0f);
			return self;
		}

		VALUE Color::getAlpha(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			return rb_float_new(color->alpha);
		}

		VALUE Color::setAlpha(VALUE self, VALUE value)
		{
			RB_VAR2CPP(Color, color);
			color->alpha = hclamp((float)NUM2DBL(value), 0.0f, 255.0f);
			return self;
		}

		VALUE Color::set(int argc, VALUE* argv, VALUE self)
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

		VALUE Color::inspect(VALUE self)
		{
			RB_VAR2CPP(Color, color);
			hstr result = hsprintf("(%.1f,%.1f,%.1f,%.1f)", color->red, color->green, color->blue, color->alpha);
			return rb_str_new2(result.c_str());
		}

	}
}
