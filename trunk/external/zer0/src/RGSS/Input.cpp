#include <ruby.h>

#include "RGSS/Input.h"

namespace zer0
{
	namespace RGSS
	{
		VALUE rb_mInput;

		void Input::createRubyInterface()
		{
			rb_mInput = rb_define_module("Input");
			rb_define_module_function(rb_mInput, "update", RUBY_METHOD_FUNC(&Input::update), 0);
			rb_define_module_function(rb_mInput, "dir4", RUBY_METHOD_FUNC(&Input::dir4), 0);
			rb_define_module_function(rb_mInput, "dir8", RUBY_METHOD_FUNC(&Input::dir8), 0);
			rb_define_module_function(rb_mInput, "trigger?", RUBY_METHOD_FUNC(&Input::trigger), 1);
			rb_define_module_function(rb_mInput, "repeat?", RUBY_METHOD_FUNC(&Input::repeat), 1);
			rb_define_module_function(rb_mInput, "press?", RUBY_METHOD_FUNC(&Input::press), 1);
		}

		VALUE Input::update(VALUE self)
		{
			return Qnil;
		}
	
		VALUE Input::dir4(VALUE self)
		{
			return INT2NUM(0);
		}

		VALUE Input::dir8(VALUE self)
		{
			return INT2NUM(0);
		}

		VALUE Input::press(VALUE self, VALUE keycode)
		{
			return Qfalse;
		}

		VALUE Input::trigger(VALUE self, VALUE keycode)
		{
			return Qfalse;
		}

		VALUE Input::repeat(VALUE self, VALUE keycode)
		{
			return Qfalse;
		}

	}
}
