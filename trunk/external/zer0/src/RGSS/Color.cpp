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
