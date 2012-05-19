#ifndef RGSS_BLENDABLE_H
#define RGSS_BLENDABLE_H

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
		/// @brief Constructor.
		Blendable();
		/// @brief Constructor.
		/// @param[in] viewport Viewport object.
		Blendable(Viewport* viewport);
		/// @brief Destructor.
		~Blendable();
		/// @brief Initializes the basic object.
		/// @param[in] rb_viewport Ruby Viewport object.
		void initialize(VALUE rb_viewport);

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
