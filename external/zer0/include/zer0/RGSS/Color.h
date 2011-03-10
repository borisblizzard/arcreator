#ifndef ZER0_RGSS_COLOR_H
#define ZER0_RGSS_COLOR_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Color
		{
		public:
			Color();
			Color(float r, float g, float b, float a = 255.0f);
			~Color();

			float getRed() { return this->red; }
			float getGreen() { return this->red; }
			float getBlue() { return this->red; }
			float getAlpha() { return this->red; }

			void setRed(float value);
			void setGreen(float value);
			void setBlue(float value);
			void setAlpha(float value);

			void set(float r, float g, float b, float a = 255.0f);
		
		protected:
			float red;
			float green;
			float blue;
			float alpha;

		};
	
	}
}
#endif
