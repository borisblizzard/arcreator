#ifndef RGSS_VIEWPORT_H
#define RGSS_VIEWPORT_H

#include <ruby.h>

#include "Renderable.h"
#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cViewport;

	class Color;
	class Rect;
	class RenderQueue;
	class Tone;

	/// @brief Emulates RGSS's Viewport class.
	class rgssExport Viewport : public Renderable
	{
	public:
		RenderQueue* renderQueue;

		/// @brief Gets the Rect.
		/// @return The Rect.
		Rect* getRect() { return this->rect; }

		/// @brief Draws this sprite on the screen.
		void draw();
		/// @brief Disposed this viewport.
		void dispose();

		/// @brief Initializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Marks referenced values of Viewport for garbage collection.
		/// @param[in] viewport Pointer to the Viewport to mark.
		static void gc_mark(Viewport* viewport);
		/// @brief Frees allocated memory.
		/// @param[in] viewport Pointer to the Viewport to free.
		static void gc_free(Viewport* viewport);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "x, y, w, h" or "rect".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Gets a string representation of the instance.
		/// @return value The string representation of the instance.
		static VALUE rb_inspect(VALUE self);

		/// @brief Gets the color.
		/// @return The Viewport's RGSS::Color object.
		static VALUE rb_getColor(VALUE self);
		/// @brief Sets the color.
		/// @param[in] value An RGSS::Color object.
		static VALUE rb_setColor(VALUE self, VALUE value);
		/// @brief Gets the display rectangle.
		/// @return The Viewport's RGSS::Rect object.
		static VALUE rb_getRect(VALUE self);
		/// @brief Sets the display rectangle.
		/// @param[in] value An RGSS::Rect object.
		static VALUE rb_setRect(VALUE self, VALUE value);
		/// @brief Gets the tone.
		/// @return The Viewport's RGSS::Tone object.
		static VALUE rb_getTone(VALUE self);
		/// @brief Sets the tone.
		/// @param[in] value A RGSS::Tone object.
		static VALUE rb_setTone(VALUE self, VALUE value);

		/// @brief Blends a color with the Viewport for a duration.
		/// @param[in] clr The Color to blend.
		/// @param[in] duration The number of frames the color will be blended.
		void flash(Color clr, int duration);
		
	protected:
		/// @brief Color.
		Color* color;
		/// @brief Ruby object of color.
		VALUE rb_color;
		/// @brief Display rectangle.
		Rect* rect;
		/// @brief Ruby object of display rectangle.
		VALUE rb_rect;
		/// @brief Tone.
		Tone* tone;
		/// @brief Ruby object of tone.
		VALUE rb_tone;

		/// @brief Renders the actual texture.
		void _render();

	};

}
#endif
