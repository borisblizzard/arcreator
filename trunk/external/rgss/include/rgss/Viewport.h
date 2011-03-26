#ifndef RGSS_VIEWPORT_H
#define RGSS_VIEWPORT_H

#include <ruby.h>

#include "Color.h"
#include "Rect.h"
#include "Tone.h"
#include "rgssExport.h"

namespace rgss
{
	static VALUE rb_cViewport;

	class rgssExport Viewport
	{
	public:
		/// @brief Intializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();

		Viewport();
		Viewport(int x, int y, int width, int height);
		Viewport(Rect rect);
		~Viewport();

		Color color;
		Rect rect;
		Tone tone;
		bool visible;
		int ox;
		int oy;
		int z;

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
#endif
