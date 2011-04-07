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

		/// @brief Intializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Marks referenced values of plane for garbage collection.
		/// @param[in] plane Plane to mark.
		static void gc_mark(Plane* sprite);
		/// @brief Frees allocated memory.
		/// @param[in] plane Plane to free.
		static void gc_free(Plane* plane);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[viewport]".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
			
		/// @brief Gets the plane's blend type
		static VALUE rb_getBlendType(VALUE self);
		/// @brief Sets the plan's blend type
		/// @param[in] value The blend type to set
		static VALUE rb_setBlendType(VALUE self, VALUE value);
		/// @brief Gets the plan's color
		static VALUE rb_getColor(VALUE self);
		/// @brief Sets the plan;s color
		/// @param[in] value the RGSS::Color object to set
		static VALUE rb_setColor(VALUE self, VALUE value);
		/// @brief gets the Tone of the plane
		static VALUE rb_getTone(VALUE self);
		/// @brief sets the tone of the plane
		/// @param[in] value the RGSS::Tone object to set
		static VALUE rb_setTone(VALUE self, VALUE value);
		/// @brief gets the plane's  zoom on the x-axis
		static VALUE rb_getZoomX(VALUE self);
		/// @brief Sets the plane's zoom on the x-axis
		/// param[in] Zoom value. 1.0 denotes actual pixel size
		static VALUE rb_setZoomX(VALUE self, VALUE value);
		/// @brief gets the plane's zoom on the y-axis
		static VALUE rb_getZoomY(VALUE self);
		/// @brief Sets the sprite zoom on the y-axis
		/// param[in] Zoom value. 1.0 denotes actual pixel size
		static VALUE rb_setZoomY(VALUE self, VALUE value);

	protected:
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
