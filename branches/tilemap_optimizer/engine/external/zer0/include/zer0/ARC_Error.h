#ifndef ZER0_ARC_ERROR_H
#define ZER0_ARC_ERROR_H

#include <ruby.h>

#include "zer0Export.h"

namespace zer0
{
	extern VALUE rb_eARC_Error;

	class zer0Export ARC_Error
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
