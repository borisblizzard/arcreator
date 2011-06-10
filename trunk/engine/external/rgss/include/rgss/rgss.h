#ifndef RGSS_H
#define RGSS_H

#include <hltypes/hstring.h>

#include "rgssExport.h"

namespace rgss
{
	rgssFnExport void init(void (*logFunction)(chstr));
	rgssFnExport void destroy();
	rgssFnExport void setLogFunction(void (*fnptr)(chstr));
	rgssFnExport void log(chstr message, chstr prefix = "[rgss] ");

}

#endif
