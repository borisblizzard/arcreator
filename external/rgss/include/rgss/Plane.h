#ifndef RGSS_PLANE_H
#define RGSS_PLANE_H

#include <ruby.h>

#include "Color.h"
#include "Rect.h"
#include "Tone.h"
#include "rgssExport.h"

namespace rgss
{
	static VALUE rb_cPlane;

	class Bitmap;
	class Viewport;

	class rgssExport Plane
	{
	public:
		/// @todo Dummy for now, needs to be removed later.
		Plane() { }
		/// @todo Dummy for now, needs to be removed later.
		~Plane() { }

		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Wraps this instance into a Ruby cobject.
		/// @return Ruby object.
		VALUE wrap();
		/// @brief Frees the memory.
		static void gc_free(Plane* plane);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Sets the bitmap dimensions
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Argument is "[viewport]".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Gets a string representation of the instance.
		/// @return String representation of the instance.
		static VALUE rb_inspect(VALUE self);
			
			
		/// @brief Gets the plane's bitmap
		static VALUE rb_getBitmap(VALUE self);
		/// @brief Sets the plane's bitmap
		/// @param[in] value Bitmap object to set
		static VALUE rb_setBitmap(VALUE self, VALUE value);
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
		/// @brief Gets the alpha value of plane
		static VALUE rb_getOpacity(VALUE self);
		/// @brief Sets the alpha value of plane
		/// param[in] value Integer value of sprite opacity
		static VALUE rb_setOpacity(VALUE self, VALUE value);
		/// @brief Gets the plane's ox value
		static VALUE rb_getOX(VALUE self);
		/// @brief Sets the plane's OX value
		/// @param[in] value the OX value to set
		static VALUE rb_setOX(VALUE self, VALUE value);
		/// @brief Gets the plane's OY value
		static VALUE rb_getOY(VALUE self);
		/// @brief Sets the plane's OY value
		/// @param[in] value the OY value to set
		static VALUE rb_setOY(VALUE self, VALUE value);
		/// @brief gets the Tone of the plane
		static VALUE rb_getTone(VALUE self);
		/// @brief sets the tone of the plane
		/// @param[in] value the RGSS::Tone object to set
		static VALUE rb_setTone(VALUE self, VALUE value);
		/// @brief Returns the viewport specified when initialized
		static VALUE rb_getViewport(VALUE self);
		/// @brief gets the plane's visible value
		static VALUE rb_getVisible(VALUE self);
		/// @brief set the plan's visible value
		/// @param[in] the new visible value
		static VALUE rb_setVisible(VALUE self, VALUE value);
		/// @brief gets the z value of the plane
		static VALUE rb_getZ(VALUE self);
		/// @brief stes the z value of the plane
		/// @param[in] value the z value to set
		static VALUE rb_setZ(VALUE self, VALUE value);
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

		/// @brief Frees the sprite
		static VALUE rb_dispose(VALUE self);
		/// @brief Boolean value if sprite has been disposed
		static VALUE rb_isDisposed(VALUE self);

	private:
		/// @brief The plane's bitmap
		Bitmap* bitmap;
		/// @brief Blend type used for the plane
		short blend_type;
		/// @brief Color blended with plane
		Color color;
		/// @brief The alpha value of the plane
		float opacity;
		/// @brief The X-coordinate of the plane's starting point
		int ox;
		/// @brief The Y-coordinate of the plane's starting point
		int oy;
		/// @brief The plane's color tone
		Tone tone;
		/// @brief The plane's visibility.
		bool visible;
		/// @brief The plane's Z-coordinate
		float z;
		/// @brief The plane's X-axis zoom level
		float zoomX;
		/// @brief The plane's Y-axis zoom level
		float zoomY;
		/// @brief Private value to store the viewport
		Viewport* viewport;

	};

}
#endif
