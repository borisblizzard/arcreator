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
		extern VALUE rb_cRGSSError;

		class zer0Export RGSSError : public hltypes::exception
		{
		public:
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();

			RGSSError(chstr message);

		};
	
	}
}
#endif
