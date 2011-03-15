#include <ruby.h>

#include <hltypes/util.h>

#include "RGSS/Color.h"

namespace zer0
{
	namespace RGSS
	{
		VALUE rb_cColor;

		void Color::createRubyInterface()
		{
			VALUE rb_cColor = rb_define_class("Color", rb_cObject);
			rb_define_attr(rb_cColor, "red", 1, 0);
			rb_define_attr(rb_cColor, "green", 1, 0);
			rb_define_attr(rb_cColor, "blue", 1, 0);
			rb_define_attr(rb_cColor, "alpha", 1, 0);
			rb_define_method(rb_cColor, "initialize", RUBY_METHOD_FUNC(&Color::initialize), -1);
			rb_define_method(rb_cColor, "red=", RUBY_METHOD_FUNC(&Color::setRed), 1);
			rb_define_method(rb_cColor, "green=", RUBY_METHOD_FUNC(&Color::setGreen), 1);
			rb_define_method(rb_cColor, "blue=", RUBY_METHOD_FUNC(&Color::setBlue), 1);
			rb_define_method(rb_cColor, "alpha=", RUBY_METHOD_FUNC(&Color::setAlpha), 1);
			rb_define_method(rb_cColor, "set", RUBY_METHOD_FUNC(&Color::set), -1);
		}

		VALUE Color::initialize(int argc, VALUE *argv, VALUE self)
		{
			if (argc < 3 || argc > 4)
			{
				//rb_raise(ArgumentError);
			}
			return Color::set(argc, argv, self);
		}

		VALUE Color::setRed(VALUE self, VALUE value)
		{
			value = rb_float_new(hclamp(NUM2DBL(value), -255.0, 255.0));
			rb_iv_set(self, "@red", value);
			return value;
		}

		VALUE Color::setGreen(VALUE self, VALUE value)
		{
			value = rb_float_new(hclamp(NUM2DBL(value), -255.0, 255.0));
			rb_iv_set(self, "@green", value);
			return value;
		}

		VALUE Color::setBlue(VALUE self, VALUE value)
		{
			value = rb_float_new(hclamp(NUM2DBL(value), -255.0, 255.0));
			rb_iv_set(self, "@blue", value);
			return value;
		}

		VALUE Color::setAlpha(VALUE self, VALUE value)
		{
			value = rb_float_new(hclamp(NUM2DBL(value), -255.0, 255.0));
			rb_iv_set(self, "@alpha", value);
			return value;
		}

		VALUE Color::set(int argc, VALUE *argv, VALUE self)
		{
			if (argc < 3 || argc > 4)
			{
				//rb_raise(ArgumentError);
			}
			rb_iv_set(self, "@red", rb_float_new(hclamp(NUM2DBL(argv[0]), -255.0, 255.0)));
			rb_iv_set(self, "@green", rb_float_new(hclamp(NUM2DBL(argv[1]), -255.0, 255.0)));
			rb_iv_set(self, "@blue", rb_float_new(hclamp(NUM2DBL(argv[2]), -255.0, 255.0)));
			rb_iv_set(self, "@alpha", rb_float_new(argc == 4 ? hclamp(NUM2DBL(argv[3]), -255.0, 255.0) : 255.0));
			return self;
		}

	}
}
