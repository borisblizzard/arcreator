#ifndef LEGACY_LEGACY_ERROR_H
#define LEGACY_LEGACY_ERROR_H

#include <ruby.h>

#include "legacyExport.h"
#include "RubyObject.h"

namespace legacy
{
	extern VALUE rb_eRGSSError;

	/// @brief Emulates RGSS's RGSSError class.
	class legacyExport RGSSError : public RubyObject
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
