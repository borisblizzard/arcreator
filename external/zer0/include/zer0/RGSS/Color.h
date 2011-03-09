#ifndef ZER0_COLOR_H
#define ZER0_COLOR_H

#include <hltypes/util.h>
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Color : public april::Color
		{
		public:
			float red;
			float green;
			float blue;
			float alpha;

			// Init Methods
			Color();
			Color(float r, float g, float b, float a = 255);

			// Set methods
			void setRed(float value);
			void setGreen(float value);
			void setBlue(float value);
			void setAlpha(float value);

			// Get methods
			float getRed();
			float getGreen();
			float getBlue();
			float getAlpha();

		};
	
	}
}
#endif
