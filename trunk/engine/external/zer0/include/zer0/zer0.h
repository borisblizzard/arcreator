#ifndef ZER0_H
#define ZER0_H

#include <hltypes/harray.h>
#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	zer0FnExport bool init(void (*fnptr)(chstr, chstr));
	zer0FnExport bool destroy();
	zer0FnExport void log(chstr message, chstr prefix = "[zer0] ");
	zer0FnExport int enterMainLoop(harray<hstr> args);
	zer0FnExport bool isDebugMode();
	zer0FnExport void setDebugMode(bool value);

}

#endif
