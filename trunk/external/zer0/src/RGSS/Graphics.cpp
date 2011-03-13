#include <ruby.h>
#include <windows.h>
#include "RGSS/Graphics.h"

namespace zer0
{
	namespace RGSS
	{
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

		VALUE Graphics::getFrameCount()
		{
			return INT2FIX(frameCount);
		}

		void Graphics::setFrameCount(VALUE value)
		{
			printf("frame_count: %u\n", FIX2UINT(INT2FIX(frameCount)));
			frameCount = FIX2UINT(value);
			frameCount++;
			printf("frame_count: %u\n", frameCount);
		}

		void Graphics::update()
		{
			frameCount++;
			printf("test %u\n", frameCount);
		}
	}
}
