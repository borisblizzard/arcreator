#ifndef RGSS_RGSS_ERROR_H
#define RGSS_RGSS_ERROR_H

#include <ruby.h>

#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_eRGSSError;

	class rgssExport RGSSError
	{
	public:
		/// @brief Initializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();

	};
	
}
#endif
