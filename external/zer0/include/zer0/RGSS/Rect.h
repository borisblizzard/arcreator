#ifndef ZER0_RECT_H
#define ZER0_RECT_H

#include <gtypes/Rectangle.h>
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Rect : public grect
		{
		public:
			int x, y, width, height;

			// constructors/destructors
			Rect();
			Rect(int valueX, int valueY, int valueWidth, int valueHeight);
			~Rect();

			void set(int valueX, int valueY, int valueWidth, int valueHeight);
			void empty();

			int getX();
			int getY();
			int getWidth();
			int getHeight();

			void setX(int valueX);
			void setY(int valueY);
			void setWidth(int valueWidth);
			void setHeight(int valueHeight);
		};
	}
}
#endif
