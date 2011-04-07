#ifndef RGSS_SOURCE_RENDERER_H
#define RGSS_SOURCE_RENDERER_H

#include <ruby.h>

#include "Renderable.h"
#include "rgssExport.h"

namespace rgss
{
	class Bitmap;
	class Viewport;

	/// @brief Provides commonly used rendering functionality using an existing bitmap source.
	class rgssExport SourceRenderer : public Renderable
	{
	public:
		/// @brief Initializes the basic Renderable object.
		void initializeSourceRenderer(VALUE rb_viewport = Qnil);

		/// @brief Marks referenced values of sourceRenderer for garbage collection.
		/// @param[in] sourceRenderer SourceRenderer to mark.
		static void gc_mark(SourceRenderer* sourceRenderer);
		/// @brief Frees allocated memory.
		/// @param[in] sourceRenderer SourceRenderer to free.
		static void gc_free(SourceRenderer* sourceRenderer);

		/// @brief Gets the opacity.
		/// @return The opacity.
		static VALUE rb_getOpacity(VALUE self);
		/// @brief Sets the opacity.
		/// @param[in] value Opacity.
		static VALUE rb_setOpacity(VALUE self, VALUE value);
		/// @brief Gets the bitmap.
		/// @return Bitmap.
		static VALUE rb_getBitmap(VALUE self);
		/// @brief Sets the bitmap.
		/// @param[in] value Bitmap.
		static VALUE rb_setBitmap(VALUE self, VALUE value);
		/// @brief Gets the viewport.
		/// @return Viewport.
		static VALUE rb_getViewport(VALUE self);
		/// @brief Sets the viewport.
		/// @param[in] value Viewport.
		static VALUE rb_setViewport(VALUE self, VALUE value);

	protected:
		/// @brief Opacity of the SourceRenderer.
		int opacity;
		/// @brief Bitmap drawing reference.
		Bitmap* bitmap;
		/// @brief Ruby object of bitmap drawing reference.
		VALUE rb_bitmap;
		/// @brief Viewport.
		Viewport* viewport;
		/// @brief Ruby object of viewport.
		VALUE rb_viewport;

	};

}
#endif
