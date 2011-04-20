#ifndef RGSS_PLANE_H
#define RGSS_PLANE_H

#include <ruby.h>

#include "Color.h"
#include "Rect.h"
#include "SourceRenderer.h"
#include "Tone.h"
#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cPlane;

	class rgssExport Plane : public SourceRenderer
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
			
		/// @brief Gets the plane's blend type
		/// @return Returns the Plane's blend type.
		static VALUE rb_getBlendType(VALUE self);
		/// @brief Sets the Plane's blend type
		/// @param[in] value The blend type to set.
		static VALUE rb_setBlendType(VALUE self, VALUE value);
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
		/// @brief Gets the plane's  zoom on the x-axis.
		/// @return Returns the zoom value on the x-axis.
		static VALUE rb_getZoomX(VALUE self);
		/// @brief Sets the Plane's zoom on the x-axis.
		/// param[in] value Zoom value. 1.0 denotes actual pixel size
		static VALUE rb_setZoomX(VALUE self, VALUE value);
		/// @brief Gets the Plane's zoom on the y-axis
		/// @return Returns the zoom value on the y-axis.
		static VALUE rb_getZoomY(VALUE self);
		/// @brief Sets the sprite zoom on the y-axis
		/// param[in] value Zoom value. 1.0 denotes actual pixel size
		static VALUE rb_setZoomY(VALUE self, VALUE value);

	protected:
		/// @brief Gets the render area rectangle.
		/// @return The render area rectangle.
		Rect _getRenderRect();
		/// @brief Renders the actual texture.
		void _render();

		/// @brief Blend type used for the plane
		short blend_type;
		/// @brief Color blended with plane
		Color color;
		/// @brief The plane's color tone
		Tone tone;
		/// @brief The plane's X-axis zoom level
		float zoomX;
		/// @brief The plane's Y-axis zoom level
		float zoomY;

	};

}
#endif
