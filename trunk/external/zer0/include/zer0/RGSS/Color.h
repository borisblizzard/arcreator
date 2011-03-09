#ifndef ZER0_COLOR_H
#define ZER0_COLOR_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Color
		{
		public:
			float red;
			float green;
			float blue;
			float alpha;

			// constructors/destructors
			Color();
			Color(float r, float g, float b, float a = 255.0f);
			~Color();

			void set(float r, float g, float b, float a = 255.0f);

			float getRed();
			void setRed(float value);
			float getGreen();
			void setGreen(float value);
			float getBlue();
			void setBlue(float value);
			float getAlpha();
			void setAlpha(float value);

		};
	
	}
}
#endif
