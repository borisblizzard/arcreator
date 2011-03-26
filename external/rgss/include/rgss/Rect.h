#ifndef RGSS_RECT_H
#define RGSS_RECT_H

#include <ruby.h>

#include "rgssExport.h"

namespace rgss
{
	static VALUE rb_cRect;

	/// @brief Emulates RGSS's Rect class.
	class rgssExport Rect
	{
	public:
		/// @todo Dummy for now, needs to be removed later.
		Rect() { }
		/// @todo Dummy for now, needs to be removed later.
		~Rect() { }

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

		/// @brief Intializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Wraps this instance into a Ruby cobject.
		/// @return Ruby object.
		VALUE wrap();
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Constructor.
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @param[in] width The width.
		/// @param[in] height The height.
		static VALUE rb_initialize(VALUE self, VALUE x, VALUE y, VALUE width, VALUE height);
		/// @brief Gets a string representation of the instance.
		/// @return String representation of the instance.
		static VALUE rb_inspect(VALUE self);

		/// @brief Gets the x coordinate.
		/// @return X coordinate.
		static VALUE rb_getX(VALUE self);
		/// @brief Sets the x coordinate.
		/// @param[in] value X coordinate.
		static VALUE rb_setX(VALUE self, VALUE value);
		/// @brief Gets the y coordinate.
		/// @return Y coordinate.
		static VALUE rb_getY(VALUE self);
		/// @brief Sets the y coordinate.
		/// @param[in] value Y coordinate.
		static VALUE rb_setY(VALUE self, VALUE value);
		/// @brief Gets the width.
		/// @return Width.
		static VALUE rb_getWidth(VALUE self);
		/// @brief Sets the width.
		/// @param[in] value Width.
		static VALUE rb_setWidth(VALUE self, VALUE value);
		/// @brief Gets the height.
		/// @return Height.
		static VALUE rb_getHeight(VALUE self);
		/// @brief Sets the height.
		/// @param[in] value Height.
		static VALUE rb_setHeight(VALUE self, VALUE value);

		/// @brief Sets the rect to the specified value.
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @param[in] width The width.
		/// @param[in] height The height.
		static VALUE rb_set(VALUE self, VALUE x, VALUE y, VALUE width, VALUE height);

	};
	
}
#endif
