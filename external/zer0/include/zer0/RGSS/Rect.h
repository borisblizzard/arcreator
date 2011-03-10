#ifndef ZER0_RGSS_RECT_H
#define ZER0_RGSS_RECT_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Rect
		{
		public:
			int x;
			int y;
			int width;
			int height;

			Rect();
			Rect(int x, int y, int width, int height);
			~Rect();

			void set(int x, int y, int width, int height);
			void empty();

		protected:
		};
	}
}
#endif
