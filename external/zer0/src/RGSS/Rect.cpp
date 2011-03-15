#include <ruby.h>

#include "RGSS/Rect.h"

namespace zer0
{
	namespace RGSS
	{
		VALUE rb_cRect;

		void Rect::createRubyInterface()
		{
		}

		Rect::Rect()
		{
			this->set(0, 0, 0, 0);
		}

		Rect::Rect(int x, int y, int width, int height)
		{
			this->set(x, y, width, height);
		}

		Rect::~Rect()
		{
		}

		void Rect::set(int x, int y, int width, int height)
		{
			this->x = x;
			this->y = y;
			this->width = width;
			this->height = height;
		}

		void Rect::empty()
		{
			this->set(0, 0, 0, 0);
		}

	}
}