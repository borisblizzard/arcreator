#ifndef RGSS_APPLICATION_EXIT_EXCEPTION_H
#define RGSS_APPLICATION_EXIT_EXCEPTION_H

#include <hltypes/exception.h>

#include "rgssExport.h"

namespace rgss
{
	class rgssExport ApplicationExitException : public hltypes::exception
	{
	public:
		ApplicationExitException();

	};

}

#endif
