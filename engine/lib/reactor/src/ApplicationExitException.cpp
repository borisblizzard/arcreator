#include <hltypes/hstring.h>

#include "ApplicationExitException.h"

namespace reactor
{
	ApplicationExitException::ApplicationExitException() :
		hexception("Application has existed", __FILE__, __LINE__)
	{
	}

	ApplicationExitException::~ApplicationExitException()
	{
	}

}
