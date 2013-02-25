#ifndef REACTOR_ARC_ERROR_H
#define REACTOR_ARC_ERROR_H

#include <ruby.h>

#include "reactorExport.h"

namespace reactor
{
	extern VALUE rb_eARC_Error;

	class reactorExport ARC_Error
	{
	public:
		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();

	};
	
}
#endif
