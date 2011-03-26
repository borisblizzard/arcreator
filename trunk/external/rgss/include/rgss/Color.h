#ifndef RGSS_COLOR_H
#define RGSS_COLOR_H

#include <ruby.h>

#include <april/Color.h>

#include "rgssExport.h"

namespace rgss
{
	static VALUE rb_cColor;

	/// @brief Emulates RGSS's Color class.
	class rgssExport Color
	{
	public:
		/// @brief Default constructor.
		Color();
		/// @brief Constructor.
		/// @param[in] r Red component.
		/// @param[in] g Green component.
		/// @param[in] b Blue component.
		/// @param[in] a Alpha component.
		/// @note Color values will be clamped between -255 and 255.
		/// @note Alpha is clamped between 0 and 255.
		Color(float r, float g, float b, float a = 0.0f);
		/// @brief Constructor.
		/// @param[in] color april::Color.
		/// @note Color values will be clamped between -255 and 255.
		/// @note Alpha is clamped between 0 and 255.
		Color(april::Color color);
		/// @todo Dummy, needs to be removed.
		~Color();

		/// @brief Red component.
		float red;
		/// @brief Green component.
		float green;
		/// @brief Blue component.
		float blue;
		/// @brief Alpha component.
		float alpha;

		/// @brief Sets the color to the specified value.
		/// @param[in] r Red component.
		/// @param[in] g Green component.
		/// @param[in] b Blue component.
		/// @param[in] a Alpha component.
		/// @note Color values will be clamped between -255 and 255.
		/// @note Alpha is clamped between 0 and 255.
		void set(float r, float g, float b, float a = 0.0f);
		/// @brief Sets the color to the specified value.
		/// @param[in] color april::Color.
		/// @note Color values will be clamped between -255 and 255.
		/// @note Alpha is clamped between 0 and 255.
		void set(april::Color color);

		/// @brief Converts this instance into april::Color.
		/// @return april::Color represenation.
		april::Color toAColor();

		/// @brief Intializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Wraps into Ruby cobject.
		/// @param[in] bitmap The bitmap to convert.
		VALUE wrap();
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Sets the color to the specified value.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "r, g, b[, a]".
		/// @note Color values will be clamped between -255 and 255.
		/// @note Alpha is clamped between 0 and 255.
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Gets a string representation of the instance.
		/// @return String representation of the instance.
		static VALUE rb_inspect(VALUE self);

		/// @brief Gets the red component.
		/// @return Red component.
		static VALUE rb_getRed(VALUE self);
		/// @brief Sets the red component.
		/// @param[in] value Red component.
		/// @note The value will be clamped between -255 and 255.
		static VALUE rb_setRed(VALUE self, VALUE value);
		/// @brief Gets the green component.
		/// @return Green component.
		static VALUE rb_getGreen(VALUE self);
		/// @brief Sets the green component.
		/// @param[in] value Green component.
		/// @note The value will be clamped between -255 and 255.
		static VALUE rb_setGreen(VALUE self, VALUE value);
		/// @brief Gets the blue component.
		/// @return Blue component.
		static VALUE rb_getBlue(VALUE self);
		/// @brief Sets the blue component.
		/// @param[in] value Blue component.
		/// @note The value will be clamped between -255 and 255.
		static VALUE rb_setBlue(VALUE self, VALUE value);
		/// @brief Gets the alpha component.
		/// @return Alpha component.
		static VALUE rb_getAlpha(VALUE self);
		/// @brief Sets the alpha component.
		/// @param[in] value Alpha component.
		/// @note The value will be clamped between 0 and 255.
		static VALUE rb_setAlpha(VALUE self, VALUE value);

		/// @brief Sets the color to the specified value.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "r, g, b[, a]".
		/// @note Color values will be clamped between -255 and 255.
		/// @note Alpha is clamped between 0 and 255.
		static VALUE rb_set(int argc, VALUE* argv, VALUE self);

	};
	
}
#endif
