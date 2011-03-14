#include <ruby.h>

#include <hltypes/util.h>

#include "zer0.h"
#include "RGSS/Color.h"

namespace zer0
{
	namespace RGSS
	{
		VALUE Color::initialize(int argc, VALUE *argv, VALUE self)
		{
			return Color::set(argc, argv, self);
		}
		/*
		VALUE Color::initialize(VALUE self, VALUE r, VALUE g, VALUE b, VALUE a)
		{
			Color::set(self, r, g, b, a);
			return self;
		}*/

		/*

		Color::Color()
		{
			this->set(255.0f, 255.0f, 255.0f);
		}

		Color::Color(float r, float g, float b, float a)
		{
			this->set(r, g, b, a);
		}

		Color::~Color()
		{
		}

		VALUE getRed(VALUE self)
		{
			return rb_float_new(this->red);
		}

		VALUE Color::setRed(VALUE self, VALUE value)
		{
			this->red = hclamp(value, -255.0f, 255.0f);
		}

		VALUE getGreen(VALUE self)
		{
			return this->red;
		}

		VALUE Color::setGreen(VALUE self, VALUE value)
		{
			this->green = hclamp(value, -255.0f, 255.0f);
		}

		VALUE getBlue(VALUE self)
		{
			return this->blue;
		}

		VALUE Color::setBlue(VALUE self, VALUE value)
		{
			this->blue = hclamp(value, -255.0f, 255.0f);
		}

		VALUE getAlpha(VALUE self)
		{
			return this->alpha;
		}

		VALUE Color::setAlpha(VALUE self, VALUE value)
		{
			this->alpha = hclamp(value, -255.0f, 255.0f);
		}
		*/

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

		void Color::createRubyInterface()
		{
			VALUE rb_cColor = rb_define_class("Color", rb_cObject);
			rb_define_attr(rb_cColor, "red", 1, 0);
			rb_define_attr(rb_cColor, "green", 1, 0);
			rb_define_attr(rb_cColor, "blue", 1, 0);
			rb_define_attr(rb_cColor, "alpha", 1, 0);
			rb_define_method(rb_cColor, "initialize", RUBY_METHOD_FUNC(&Color::initialize), -1);
			rb_define_method(rb_cColor, "set", RUBY_METHOD_FUNC(&Color::set), -1);
		}

	}
}
