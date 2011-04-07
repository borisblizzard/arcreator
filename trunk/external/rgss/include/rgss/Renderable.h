#ifndef RGSS_RENDERABLE_H
#define RGSS_RENDERABLE_H

#include <ruby.h>

#include "rgssExport.h"

#define TYPE_VIEWPORT 0
#define TYPE_SPRITE 1
#define TYPE_PLANE 2
#define TYPE_WINDOW 3
#define TYPE_TILEMAP 4

namespace rgss
{
	/// @brief Provides commonly used rendering functionality.
	class rgssExport Renderable
	{
	public:
		/// @brief Initializes the basic Renderable object.
		void initializeRenderable();

		/// @brief Gets the Z coordinate.
		/// @return The Z coordinate.
		int getZ() { return this->z; }
		/// @brief Sets the Z coordinate.
		/// @param[in] value The Z coordinate.
		void setZ(int value) { this->z = value; }

		/// @brief Draws this sprite on the screen.
		void draw();

		/// @brief Marks referenced values of renderable for garbage collection.
		/// @param[in] renderable Renderable to mark.
		static void gc_mark(Renderable* renderable);
		/// @brief Frees allocated memory.
		/// @param[in] renderable Renderable to free.
		static void gc_free(Renderable* renderable);

		/// @brief Gets the visibility.
		/// @return The visibility.
		static VALUE rb_getVisible(VALUE self);
		/// @brief Sets the visibility.
		/// @param[in] value Visibility.
		static VALUE rb_setVisible(VALUE self, VALUE value);
		/// @brief Gets the Z coordinate.
		/// @return The Z coordinate.
		static VALUE rb_getZ(VALUE self);
		/// @brief Sets the Z coordinate.
		/// @param[in] value Z coordinate.
		static VALUE rb_setZ(VALUE self, VALUE value);
		/// @brief Gets the offset X coordinate.
		/// @return Offset X coordinate.
		static VALUE rb_getOX(VALUE self);
		/// @brief Sets the offset X coordinate.
		/// @param[in] value Offset X coordinate.
		static VALUE rb_setOX(VALUE self, VALUE value);
		/// @brief Gets the offset Y coordinate.
		/// @return Offset Y coordinate.
		static VALUE rb_getOY(VALUE self);
		/// @brief Sets the offset Y coordinate.
		/// @param[in] value Offset Y coordinate.
		static VALUE rb_setOY(VALUE self, VALUE value);
		/// @brief Checks whether this renderable is disposed.
		/// @return True if renderable is disposed.
		static VALUE rb_isDisposed(VALUE self);

	protected:
		/// @brief Disposed flag.
		bool disposed;
		/// @brief Visible flag.
		bool visible;
		/// @brief Z coordinate.
		int z;
		/// @brief Offset X coordinate.
		int ox;
		/// @brief Offset Y coordinate.
		int oy;
		/// @brief Used for determining which renderable subclass it actually is.
		/// @note This is a necessity because objects created through Ruby don't have a virtual function pointer table.
		unsigned int type;

	};

}
#endif
