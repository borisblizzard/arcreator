#include <ruby.h>
#include <windows.h>
#include "RGSS/Graphics.h"

namespace zer0
{
	namespace RGSS
	{
		
		void Graphics::frameReset()
		{
		}

		void Graphics::freeze()
		{
		}

		void Graphics::transition(int duration = 8, hstr filename = "", int vague = 40)
		{
		}

		VALUE Graphics::update(...)
		{
			printf("test\n");
			return Qnil;
		}
	}
}
