#include <hltypes/util.h>

#include "RGSS/Tone.h"

namespace zer0
{
	namespace RGSS
	{
		Tone::Tone()
		{
			this->set(255.0f, 255.0f, 255.0f, 255.0f);
		}
		Tone::Tone(float r, float g, float b, float gr = 255.0f)
		{
			this->set(r, g, b, gr);
		}
		Tone::~Tone()
		{

		}

		void Tone::setRed(float value)
		{
			this->red =  hclamp<float>(value, -255, 255);
		}
		void Tone::setGreen(float value)
		{
			this->green = hclamp<float>(value, -255, 255);
		}
		void Tone::setBlue(float value)
		{
			this->blue = hclamp<float>(value, -255, 255);;
		}
		void Tone::setGray(float value)
		{
			this->gray = hclamp<float>(value, -255, 255);;
		}

		float Tone::getRed()
		{
			return this->red;
		}
		float Tone::getGreen()
		{
			return this->green;
		}
		float Tone::getBlue()
		{
			return this->blue;
		}
		float Tone::getGray()
		{
			return this->gray;
		}

		void Tone::set(float r, float g, float b, float gr = 255.0f)
		{
			this->red = hclamp(r, -255.0f, 255.0f);
			this->green = hclamp(g, -255.0f, 255.0f);
			this->blue = hclamp(b, -255.0f, 255.0f);
			this->gray = hclamp(gr, -255.0f, 255.0f);
		}
	}
}
