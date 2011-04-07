#ifndef RGSS_TONE_H
#define RGSS_TONE_H

#include <ruby.h>

#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cTone;

	/// @brief Emulates RGSS's Tone class.
	class rgssExport Tone
	{
	public:
		/// @todo Dummy for now, needs to be removed later.
		Tone() { }
		/// @todo Dummy for now, needs to be removed later.
		~Tone() { }

		/// @brief Red component.
		float red;
		/// @brief Green component.
		float green;
		/// @brief Blue component.
		float blue;
		/// @brief Gray component.
		float gray;

		/// @brief Sets the tone to the specified value.
		/// @param[in] r Red component.
		/// @param[in] g Green component.
		/// @param[in] b Blue component.
		/// @param[in] gr Gray component.
		/// @note Tone values will be clamped between -255 and 255.
		/// @note Gray is clamped between 0 and 255.
		void set(float r, float g, float b, float gr = 0.0f);

		/// @brief Intializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Sets the color to the specified value.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "r, g, b[, a]".
		/// @note Tone values will be clamped between -255 and 255.
		/// @note Gray is clamped between 0 and 255.
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Gets a string representation of the instance.
		/// @return String representation of the instance.
		static VALUE rb_inspect(VALUE self);
		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "r, g, b[, gr]".
		/// @note Color values will be clamped between -255 and 255.
		/// @note Gray is clamped between 0 and 255.
		static VALUE create(int argc, VALUE* argv);

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
		/// @brief Gets the gray component.
		/// @return Gray component.
		static VALUE rb_getGray(VALUE self);
		/// @brief Sets the gray component.
		/// @param[in] value Gray component.
		/// @note The value will be clamped between 0 and 255.
		static VALUE rb_setGray(VALUE self, VALUE value);

		/// @brief Sets the color to the specified value.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "r, g, b[, gr]".
		/// @note Tone values will be clamped between -255 and 255.
		/// @note Gray is clamped between 0 and 255.
		static VALUE rb_set(int argc, VALUE* argv, VALUE self);

	};
	
}
#endif
