#include "RGSS/Rect.h"

namespace zer0
{
	namespace RGSS
	{
		Rect::Rect()
		{
			this->set(0, 0, 0, 0);
		}
		void Rect::empty()
		{
			this->set(0, 0, 0, 0);
		}

		int Rect::getX()
		{
			return this->x;
		}
		int Rect::getY()
		{
			return this->y;
		}
		int getWidth()
		{
			// This causes an error. Says it cannot be used in non-static member function. Why?
			// How is different from the x and y? Confusion with the parent?
			//return this->width;
		}
		int getHeight()
		{
			// This too.
			//return this->height; 
		}

		void Rect::setX(int value)
		{
			this->x = value;
		}
		void Rect::setY(int value)
		{
			this->x = value;
		}
		void Rect::setWidth(int value)
		{
			this->width = value;
		}
		void Rect::setHeight(int value)
		{
			this->height = value;
		}

		void Rect::set(int vx, int vy, int vw, int vh)
		{
			this->x = vx;
			this->y = vy;
			this->width = vw;
			this->height = vh;
		}

		Rect::~Rect()
		{
			// ????
		}
	}
}