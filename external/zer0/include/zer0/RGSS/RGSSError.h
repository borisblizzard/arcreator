#ifndef ZER0_RGSS_RGSS_ERROR_H
#define ZER0_RGSS_RGSS_ERROR_H

#include <ruby.h>

#include <hltypes/exception.h>
#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		static VALUE rb_cRGSSError;

		class zer0Export RGSSError : public hltypes::exception
		{
		public:
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Wraps this instance into a Ruby cobject.
			/// @return Ruby object.
			VALUE wrap();
			/// @brief Ruby allocation of an instance.
			static VALUE rb_new(VALUE classe);
			/// @brief Sets the bitmap dimensions
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);

			/// @brief Gets the exception from the parent class.
			/// @return Exception of the parent.
			static VALUE rb_getException(VALUE self);
			/// @brief Gets the message associated with this exception.
			/// @return String message.
			static VALUE rb_getMessage(VALUE self);
			/// @brief Gets the formatted string tracing the exception.
			/// @return String trace information.
			static VALUE rb_getBacktrace(VALUE self);
			/// @brief Gets the exception formatted as a string.
			/// @return The string representation of the exception.
			static VALUE rb_getString(VALUE self);
			/// @brief Sets the backtrace information for the exception.
			/// @param[in] ???????
			static VALUE rb_setBacktrace(VALUE self, VALUE value);

		protected:
			/// @brief The exception of the parent class.
			exception rbException;
			/// @brief The formatted string used to trace the exception.
			hstr backtrace;
			/// @brief The string used to describe the exception.
			hstr message;
		};
	
	}
}
#endif
