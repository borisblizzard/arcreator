#include <ruby.h>

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

	}
}
