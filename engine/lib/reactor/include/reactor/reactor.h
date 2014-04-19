#ifndef REACTOR_H
#define REACTOR_H

#include <hltypes/harray.h>
#include <hltypes/hstring.h>

#include "reactorExport.h"

namespace reactor
{
	extern hstr logTag;

	reactorFnExport bool init();
	reactorFnExport bool destroy();
	reactorFnExport int enterMainLoop(harray<hstr> args);
	reactorFnExport bool isDebugMode();
	reactorFnExport void setDebugMode(bool value);

}

#endif
