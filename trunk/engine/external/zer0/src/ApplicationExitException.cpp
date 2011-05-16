#include <hltypes/hstring.h>

#include "ApplicationExitException.h"

namespace zer0
{
	ApplicationExitException::ApplicationExitException() :
		hltypes::exception("Application has existed", __FILE__, __LINE__)
	{
	}

}
