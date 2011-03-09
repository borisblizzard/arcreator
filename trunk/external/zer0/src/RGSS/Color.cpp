#include <hltypes/util.h>

#include "RGSS/Color.h"

namespace zer0
{
	namespace RGSS
	{
		Color::Color()
		{
			this->set(255.0f, 255.0f, 255.0f);
		}

		void Color::setRed(float value)
		{
			value = hclamp<float>(value, -255, 255);
			this->red = value;
		}
		void Color::setGreen(float value)
		{
			value = hclamp<float>(value, -255, 255);
			this->green = value;
		}
		void Color::setBlue(float value)
		{
			value = hclamp<float>(value, -255, 255);
			this->blue = value;
		}

		float Color::getRed()
		{
			return this->red;
		}
		float Color::getGreen()
		{
			return this->green;
		}
		float Color::getBlue()
		{
			return this->blue;
		}

		Color::Color(float r, float g, float b, float a)
		{
			this->set(r, g, b, a);
		}

		Color::~Color()
		{
		}

		void Color::set(float r, float g, float b, float a)
		{
			this->red = hclamp(r, -255.0f, 255.0f);
			this->green = hclamp(g, -255.0f, 255.0f);
			this->blue = hclamp(b, -255.0f, 255.0f);
			this->alpha = hclamp(a, -255.0f, 255.0f);
		}

	}
}
