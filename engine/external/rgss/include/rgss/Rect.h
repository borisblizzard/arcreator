#ifndef RGSS_RECT_H
#define RGSS_RECT_H

#include <ruby.h>

#include <gtypes/Rectangle.h>

#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cRect;

	/// @brief Emulates RGSS's Rect class.
	class rgssExport Rect
	{
	public:
		/// @brief X coordinate.
		int x;
		/// @brief Y coordinate.
		int y;
		/// @brief Width.
		int width;
		/// @brief Height.
		int height;

		/// @brief Sets the rect to the specified value.
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @param[in] width The width.
		/// @param[in] height The height.
		void set(int x, int y, int width, int height);

		/// @brief Converts this instance into gtypes::Rectangle.
		/// @return gtypes::Rectangle representation.
		grect toGRect();

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Constructor.
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @param[in] width The width.
		/// @param[in] height The height.
		static VALUE rb_initialize(VALUE self, VALUE x, VALUE y, VALUE width, VALUE height);
		/// @brief Used for clone and dup.
		/// @param[in] original The original.
		static VALUE rb_initialize_copy(VALUE self, VALUE original);
		/// @brief Gets a string representation of the instance.
		/// @return value String representation of the instance.
		static VALUE rb_inspect(VALUE self);
		/// @brief Creates a C++ version of this class.
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @param[in] width The width.
		/// @param[in] height The height.
		static VALUE create(VALUE x, VALUE y, VALUE width, VALUE height);

		/// @brief Gets the x coordinate.
		/// @return value The X coordinate.
		static VALUE rb_getX(VALUE self);
		/// @brief Sets the x coordinate.
		/// @param[in] value The X coordinate.
		static VALUE rb_setX(VALUE self, VALUE value);
		/// @brief Gets the y coordinate.
		/// @return The Y coordinate.
		static VALUE rb_getY(VALUE self);
		/// @brief Sets the y coordinate.
		/// @param[in] value The Y coordinate.
		static VALUE rb_setY(VALUE self, VALUE value);
		/// @brief Gets the width.
		/// @return value The width.
		static VALUE rb_getWidth(VALUE self);
		/// @brief Sets the width.
		/// @param[in] value The width.
		static VALUE rb_setWidth(VALUE self, VALUE value);
		/// @brief Gets the height.
		/// @return value The height.
		static VALUE rb_getHeight(VALUE self);
		/// @brief Sets the height.
		/// @param[in] value The height.
		static VALUE rb_setHeight(VALUE self, VALUE value);

		/// @brief Sets the Rect to the specified value.
		/// @param[in] x The X coordinate.
		/// @param[in] y The Y coordinate.
		/// @param[in] width The width.
		/// @param[in] height The height.
		static VALUE rb_set(VALUE self, VALUE x, VALUE y, VALUE width, VALUE height);
		/// @brief Resets the Rect.
		static VALUE rb_empty(VALUE self);

		/// @brief Returns a byte string containing data needed to reconstruct the Rect object.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Only one argument d, it defaults to 0 and is used for object depth.
		/// @return value The byte string.
		static VALUE rb_dump(int argc, VALUE* argv, VALUE self);

		/// @brief Returns a Rect object constructed from a byte string.
		/// @param[in] value The byte string from which to load the object.
		static VALUE rb_load(VALUE self, VALUE value);

	};
	
}
#endif
