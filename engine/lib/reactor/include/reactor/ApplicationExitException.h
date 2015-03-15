#ifndef REACTOR_APPLICATION_EXIT_EXCEPTION_H
#define REACTOR_APPLICATION_EXIT_EXCEPTION_H

#include <hltypes/hexception.h>

#include "reactorExport.h"

namespace reactor
{
	class reactorExport ApplicationExitException : public hexception
	{
	public:
		ApplicationExitException();
		~ApplicationExitException();

	};

}

#endif
