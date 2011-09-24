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

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
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
		/// @brief Used for clone and dup.
		/// @param[in] original The original.
		static VALUE rb_initialize_copy(VALUE self, VALUE original);
		/// @brief Gets a string representation of the instance.
		/// @return value The string representation of the instance.
		static VALUE rb_inspect(VALUE self);

		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "r, g, b[, gr]".
		/// @note Color values will be clamped between -255 and 255.
		/// @note Gray is clamped between 0 and 255.
		static VALUE create(int argc, VALUE* argv);

		/// @brief Gets the red component.
		/// @return value The red component.
		static VALUE rb_getRed(VALUE self);
		/// @brief Sets the red component.
		/// @param[in] value The red component.
		/// @note The value will be clamped between -255 and 255.
		static VALUE rb_setRed(VALUE self, VALUE value);
		/// @brief Gets the green component.
		/// @return value The green component.
		static VALUE rb_getGreen(VALUE self);
		/// @brief Sets the green component.
		/// @param[in] value Green component.
		/// @note The value will be clamped between -255 and 255.
		static VALUE rb_setGreen(VALUE self, VALUE value);
		/// @brief Gets the blue component.
		/// @return value The blue component.
		static VALUE rb_getBlue(VALUE self);
		/// @brief Sets the blue component.
		/// @param[in] value The blue component.
		/// @note The value will be clamped between -255 and 255.
		static VALUE rb_setBlue(VALUE self, VALUE value);
		/// @brief Gets the gray component.
		/// @return value The gray component.
		static VALUE rb_getGray(VALUE self);
		/// @brief Sets the gray component.
		/// @param[in] value The gray component.
		/// @note The value will be clamped between 0 and 255.
		static VALUE rb_setGray(VALUE self, VALUE value);

		/// @brief Sets the color to the specified value.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "r, g, b[, gr]".
		/// @note Tone values will be clamped between -255 and 255.
		/// @note Gray is clamped between 0 and 255.
		static VALUE rb_set(int argc, VALUE* argv, VALUE self);

		/// @brief Returns a byte stream containing serialization data for Marshal.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[depth = -1]".
		/// @return Data byte stream.
		static VALUE rb_dump(int argc, VALUE* argv, VALUE self);
		/// @brief Returns an RGSS::Tone object constructed from a serialized Marshal byte stream.
		/// @param[in] stream The byte stream from which to load the object.
		static VALUE rb_load(VALUE self, VALUE stream);

		/// @brief Returns a byte stream containing serialization data.
		/// @return Data byte stream.
		static VALUE rb_arcDump(VALUE self);
		/// @brief Returns an RGSS::Tone object constructed from a serialized byte stream.
		/// @param[in] stream The byte stream from which to load the object.
		static VALUE rb_arcLoad(VALUE self, VALUE stream);

	};
	
}
#endif
