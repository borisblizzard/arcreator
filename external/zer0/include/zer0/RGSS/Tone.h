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
			float red;
			float green;
			float blue;
			float gray;
			Tone();
			Tone(float r, float g, float b, float gr = 255.0f);
			~Tone();

			void set(float r, float g, float b, float gr = 255.0f);

			float getRed();
			void setRed(float value);
			float getGreen();
			void setGreen(float value);
			float getBlue();
			void setBlue(float value);
			float getGray();
			void setGray(float value);

		};
	
	}
}
#endif
