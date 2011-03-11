#ifndef ZER0_RGSS_VIEWPORT_H
#define ZER0_RGSS_VIEWPORT_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class Color;

		class zer0Export Viewport
		{
			Viewport();
			~Viewport();
		private:
			Color color;
		};

	}
}
#endif
