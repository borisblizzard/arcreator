#include <ruby.h>
#include <windows.h>
#include "RGSS/Graphics.h"

namespace zer0
{
	namespace RGSS
	{
		void Graphics::createRubyInterface()
		{
			VALUE classe = rb_define_module("Graphics");
			rb_define_module_function(classe, "update", RUBY_METHOD_FUNC(zer0::RGSS::Graphics::update), 0);
			rb_define_module_function(classe, "frame_count", RUBY_METHOD_FUNC(zer0::RGSS::Graphics::getFrameCount), 0);
			rb_define_module_function(classe, "frame_count=", RUBY_METHOD_FUNC(zer0::RGSS::Graphics::setFrameCount), 1);
		}

		unsigned int Graphics::frameCount = 0;

		void Graphics::frameReset()
		{
		}

		void Graphics::freeze()
		{
		}

		void Graphics::transition(int duration = 8, hstr filename = "", int vague = 40)
		{
		}

		VALUE Graphics::getFrameCount(VALUE self)
		{
			return INT2NUM(frameCount);
		}

		VALUE Graphics::setFrameCount(VALUE self, VALUE value)
		{
			frameCount = NUM2UINT(value);
			return Qnil;
		}

		VALUE Graphics::update(VALUE self)
		{
			frameCount++;
			return Qnil;
		}
	}
}
