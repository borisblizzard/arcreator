#ifndef ZER0_RGSS_VIEWPORT_H
#define ZER0_RGSS_VIEWPORT_H

#include <ruby.h>

#include "RGSS/Color.h"
#include "RGSS/Rect.h"
#include "RGSS/Tone.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		static VALUE rb_cViewport;

		class zer0Export Viewport
		{
		public:
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();

			Viewport();
			~Viewport();
			Color color;
			Rect rect;
			Tone tone;
			bool visible;
			int ox;
			int oy;
			int z;

			Viewport(int x, int y, int width, int height);
			Viewport(Rect rect);

			void setColor(float r, float g, float b, float a = 255.0f);
			void setTone(float r, float g, float b, float gr = 255.0f);
			void setRect(int x, int y, int width, int height);
			void flash(Color clr, int duration);
			void setOX(int value);
			void setOY(int value);
			void setZ(int value);
			void setVisible(bool value);

		};

	}
}
#endif
