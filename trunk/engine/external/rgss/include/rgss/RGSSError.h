#ifndef RGSS_RGSS_ERROR_H
#define RGSS_RGSS_ERROR_H

#include <ruby.h>

#include "rgssExport.h"
#include "RubyObject.h"

namespace rgss
{
	extern VALUE rb_eRGSSError;

	/// @brief Emulates RGSS's RGSSError class.
	class rgssExport RGSSError : public RubyObject
	{
	public:
		/// @brief Constructor.
		RGSSError();
		/// @brief Destructor.
		~RGSSError();

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);

		/// @brief Mimics a dumping method to prevent dumping of this class.
		static VALUE rb_arcDump(VALUE self);

	};
	
}
#endif
