#include <hltypes/hstring.h>

#include "ApplicationExitException.h"

namespace rgss
{
	ApplicationExitException::ApplicationExitException() :
		hltypes::exception("Application has existed", __FILE__, __LINE__)
	{
	}

	ApplicationExitException::~ApplicationExitException()
	{
	}

}
