#ifndef RGSS_PLANE_H
#define RGSS_PLANE_H

#include <ruby.h>

#include "Color.h"
#include "Rect.h"
#include "Tone.h"
#include "Zoomable.h"
#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cPlane;

	class rgssExport Plane : public Zoomable
	{
	public:
		/// @brief Draws this sprite on the screen.
		void draw();

		/// @brief Initializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Marks referenced values of Plane for garbage collection.
		/// @param[in] plane Pointer to the Plane to mark.
		static void gc_mark(Plane* plane);
		/// @brief Frees allocated memory.
		/// @param[in] plane Pointer to the Plane to free.
		static void gc_free(Plane* plane);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[viewport]".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
			
		/// @brief Gets the plan's color
		/// @return value Returns the Plane's RGSS::Color object.
		static VALUE rb_getColor(VALUE self);
		/// @brief Sets the Plane's color
		/// @param[in] value the RGSS::Color object to set
		static VALUE rb_setColor(VALUE self, VALUE value);
		/// @brief Gets the Tone of the plane.
		/// @return Returns the Plane's RGSS::Tone object.
		static VALUE rb_getTone(VALUE self);
		/// @brief Sets the tone of the Plane.
		/// @param[in] value The RGSS::Tone object to set.
		static VALUE rb_setTone(VALUE self, VALUE value);

	protected:
		/// @brief Gets the render area rectangle.
		/// @return The render area rectangle.
		Rect _getRenderRect();
		/// @brief Renders the actual texture.
		void _render();

		/// @brief Color blended with plane
		Color color;
		/// @brief The plane's color tone
		Tone tone;

	};

}
#endif
