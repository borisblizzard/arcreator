#ifndef ZER0_RGSS_WINDOW_H
#define ZER0_RGSS_WINDOW_H

#include <ruby.h>

#include "RGSS/Rect.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		static VALUE rb_cWindow;

		class Bitmap;
		class Rect;
		class Viewport;

		class zer0Export Window
		{
		public:
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Wraps this instance into a Ruby cobject.
			/// @return Ruby object.
			VALUE wrap();
			/// @brief Ruby allocation of an instance.
			static VALUE rb_new(VALUE classe);
			/// @brief Sets the font parameters.
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
			/// @brief Disposes the object.
			static VALUE dispose(VALUE self);

			/// @brief Returns true if disposed, else false.
			static VALUE isDisposed(VALUE self);
			/// @brief Set the back opacity.
			/// @param[in] value Alpha component.
			/// @note The value will be clamped between -255 and 255.
			static VALUE setBackOpacity(VALUE self, VALUE value);
			/// @brief Set the bitmap to use for the window's contents.
			/// @param[in] value Bitmap used as contents.
			static VALUE setContents(VALUE self, VALUE* value);
			/// @brief Set the window contents' opacity.
			/// @param[in] value Alpha component
			/// @note The value will be clamped between -255 and 255.
			static VALUE setContentsOpacity(VALUE self, VALUE value);
			/// @brief Set the window overall opacity.
			/// @param[in] value Alpha component
			/// @note The value will be clamped between -255 and 255.
			static VALUE setOpacity(VALUE self, VALUE value);
			/// @brief Sets the source bitmap of the windowskin.
			/// @param[in] value Bitmap component.
			static VALUE setWindowskin(VALUE self, VALUE* value);
			/// @brief Calls the update method.
			static VALUE update(VALUE self);
		};
	}
}
#endif