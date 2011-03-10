#ifndef ZER0_RGSS_RGSS_ERROR_H
#define ZER0_RGSS_RGSS_ERROR_H

#include <hltypes/exception.h>
#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export RGSSError : public hltypes::exception
		{
		public:
			RGSSError(chstr message);

		};
	
	}
}
#endif
