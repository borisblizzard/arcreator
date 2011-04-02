#ifndef RGSS_RENDERABLE_H
#define RGSS_RENDERABLE_H

#include <ruby.h>

#include "rgssExport.h"

#define TYPE_VIEWPORT 0
#define TYPE_SPRITE 1
#define TYPE_PLANE 2
#define TYPE_WINDOW 3

namespace rgss
{
	/// @brief Provides commonly used rendering functionality.
	class rgssExport Renderable
	{
	public:
		/// @brief Gets the Z coordinate.
		/// @return The Z coordinate.
		int getZ() { return this->z; }
		/// @brief Sets the Z coordinate.
		/// @param[in] value The Z coordinate.
		void setZ(int value) { this->z = value; }

		/// @brief Draws this sprite on the screen.
		void draw();

		/// @brief Gets the Z coordinate.
		/// @return The Z coordinate.
		static VALUE rb_getZ(VALUE self);
		/// @brief Sets the Z coordinate.
		/// @param[in] value Z coordinate.
		static VALUE rb_setZ(VALUE self, VALUE value);

	protected:
		/// @brief Z coordinate.
		int z;
		/// @brief Used for determining which renderable subclass it actually is.
		/// @note This is a necessity because objects created through Ruby don't have a virtual function pointer table.
		unsigned int type;

	};

}
#endif
