#ifndef ZER0_RECT_H
#define ZER0_RECT_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Rect
		{
		public:
			Rect();
			Rect(int x, int y, int width, int height);
			~Rect();

			int getX() { return this->x; }
			void setX(int value) { this->x = value; }
			int getY() { return this->y; }
			void setY(int value) { this->x = value; }
			int getWidth() { return this->width; }
			void setWidth(int value) { this->width = value; }
			int getHeight() { return this->height; }
			void setHeight(int value) { this->height = value; }

			void set(int x, int y, int width, int height);
			void empty();

		protected:
			int x;
			int y;
			int width;
			int height;

		};
	}
}
#endif
