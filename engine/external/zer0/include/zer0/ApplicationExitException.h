#ifndef ZER0_APPLICATION_EXIT_EXCEPTION_H
#define ZER0_APPLICATION_EXIT_EXCEPTION_H

#include <hltypes/exception.h>

#include "zer0Export.h"

namespace zer0
{
	class zer0Export ApplicationExitException : public hltypes::exception
	{
	public:
		ApplicationExitException();

	};

}

#endif
