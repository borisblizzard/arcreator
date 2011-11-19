#ifndef RGSS_ZOOMABLE_H
#define RGSS_ZOOMABLE_H

#include <ruby.h>

#include "BlendType.h"
#include "SourceRenderer.h"
#include "rgssExport.h"

namespace rgss
{
	/// @brief Provides commonly used rendering functionality using an existing bitmap source.
	class rgssExport Blendable : public SourceRenderer
	{
	public:
		/// @brief Initializes the basic Blendable object.
		/// @param[in] rb_viewport Ruby Viewport object.
		void initializeBlendable(VALUE rb_viewport = Qnil);

		/// @brief Marks referenced values of blendable for garbage collection.
		/// @param[in] blendable Blendable to mark.
		static void gc_mark(Blendable* blendable);
		/// @brief Frees allocated memory.
		/// @param[in] blendable Blendable to free.
		static void gc_free(Blendable* blendable);

		/// @brief Gets the blend type.
		/// @return The blend type.
		static VALUE rb_getBlendType(VALUE self);
		/// @brief Sets the blend type.
		/// @param[in] value The blend type.
		static VALUE rb_setBlendType(VALUE self, VALUE value);

	protected:
		/// @brief Blend type.
		BlendType blendType;

	};

}
#endif
