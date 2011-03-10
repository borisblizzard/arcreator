#ifndef ZER0_H
#define ZER0_H

#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	zer0FnExport bool init(int width, int height, bool fullscreen, chstr name, chstr path, void (*logFunction)(chstr));
	zer0FnExport bool destroy();
	zer0FnExport void setLogFunction(void (*fnptr)(chstr));
	zer0FnExport void log(chstr message, chstr prefix = "[zer0] ");
	zer0FnExport int enterMainLoop(int argc, char** argv);

}

#endif
