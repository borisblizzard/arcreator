#include <hltypes/hstring.h>

#include "ApplicationExitException.h"

namespace legacy
{
	ApplicationExitException::ApplicationExitException() :
		hexception("Application has exited", __FILE__, __LINE__)
	{
	}

	ApplicationExitException::~ApplicationExitException()
	{
	}

}
