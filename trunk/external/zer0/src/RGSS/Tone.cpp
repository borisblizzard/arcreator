#include <ruby.h>

#include <hltypes/util.h>

#include "RGSS/Tone.h"

namespace zer0
{
	namespace RGSS
	{
		VALUE rb_cTone;

		void Tone::createRubyInterface()
		{
		}

		Tone::Tone()
		{
			this->set(255.0f, 255.0f, 255.0f);
		}

		Tone::Tone(float r, float g, float b, float gr)
		{
			this->set(r, g, b, gr);
		}

		Tone::~Tone()
		{

		}

		void Tone::setRed(float value)
		{
			this->red = hclamp(value, -255.0f, 255.0f);
		}

		void Tone::setGreen(float value)
		{
			this->green = hclamp(value, -255.0f, 255.0f);
		}

		void Tone::setBlue(float value)
		{
			this->blue = hclamp(value, -255.0f, 255.0f);
		}

		void Tone::setGray(float value)
		{
			this->gray = hclamp(value, -255.0f, 255.0f);
		}

		void Tone::set(float r, float g, float b, float gr)
		{
			this->red = hclamp(r, -255.0f, 255.0f);
			this->green = hclamp(g, -255.0f, 255.0f);
			this->blue = hclamp(b, -255.0f, 255.0f);
			this->gray = hclamp(gr, -255.0f, 255.0f);
		}
	}
}
