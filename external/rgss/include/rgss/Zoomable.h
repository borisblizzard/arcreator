#ifndef RGSS_ZOOMABLE_H
#define RGSS_ZOOMABLE_H

#include <ruby.h>

#include "BlendType.h"
#include "SourceRenderer.h"
#include "rgssExport.h"

namespace rgss
{
	/// @brief Provides commonly used rendering functionality using an existing bitmap source.
	class rgssExport Zoomable : public SourceRenderer
	{
	public:
		/// @brief Initializes the basic Zoomable object.
		/// @param[in] rb_viewport Ruby Viewport object.
		void initializeZoomable(VALUE rb_viewport);

		/// @brief Marks referenced values of zoomable for garbage collection.
		/// @param[in] zoomable Zoomable to mark.
		static void gc_mark(Zoomable* zoomable);
		/// @brief Frees allocated memory.
		/// @param[in] zoomable Zoomable to free.
		static void gc_free(Zoomable* zoomable);

		/// @brief Gets the X zoom.
		/// @return value The X zoom.
		static VALUE rb_getZoomX(VALUE self);
		/// @brief Sets the X zoom.
		/// @param[in] value The X zoom.
		static VALUE rb_setZoomX(VALUE self, VALUE value);
		/// @brief Gets the Y zoom.
		/// @return value The Y zoom.
		static VALUE rb_getZoomY(VALUE self);
		/// @brief Sets the Y zoom.
		/// @param[in] value The Y zoom.
		static VALUE rb_setZoomY(VALUE self, VALUE value);
		/// @brief Gets the blend type.
		/// @return value The blend type.
		static VALUE rb_getBlendType(VALUE self);
		/// @brief Sets the blend type.
		/// @param[in] value The blend type.
		static VALUE rb_setBlendType(VALUE self, VALUE value);

	protected:
		/// @brief X zoom.
		float zoomX;
		/// @brief Y zoom.
		float zoomY;
		/// @brief Blend type.
		BlendType blendType;

	};

}
#endif
