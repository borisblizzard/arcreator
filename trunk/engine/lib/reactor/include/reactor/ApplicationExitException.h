#ifndef REACTOR_APPLICATION_EXIT_EXCEPTION_H
#define REACTOR_APPLICATION_EXIT_EXCEPTION_H

#include <hltypes/exception.h>

#include "reactorExport.h"

namespace reactor
{
	class reactorExport ApplicationExitException : public hltypes::exception
	{
	public:
		ApplicationExitException();

	};

}

#endif
