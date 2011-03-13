#include <ruby.h>

#include "RGSS/Graphics.h"

namespace zer0
{
	namespace RGSS
	{
		void Graphics::createRubyInterface()
		{
			VALUE classe = rb_define_module("Graphics");
			rb_define_module_function(classe, "update", &zer0::RGSS::Graphics::update, 0);
		}

	}
}
