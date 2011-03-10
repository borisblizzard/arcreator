#ifndef ZER0_TONE_H
#define ZER0_TONE_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Tone
		{
		public:
			Tone();
			Tone(float r, float g, float b, float gr = 255.0f);
			~Tone();

			float getRed() { return this->red; }
			float getGreen() { return this->green; }
			float getBlue() { return this->blue; }
			float getGray() { return this->gray; }

			void setRed(float value);
			void setGreen(float value);
			void setBlue(float value);
			void setGray(float value);

			void set(float r, float g, float b, float gr = 255.0f);

		protected:
			float red;
			float green;
			float blue;
			float gray;

		};
	
	}
}
#endif
