#ifndef RGSS_H
#define RGSS_H

#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "rgssExport.h"

namespace april
{
	class PixelShader;
}

namespace rgss
{
	rgssFnExport void init(hmap<hstr, hstr> parameters);
	rgssFnExport void destroy();
	rgssFnExport void setLogFunction(void (*fnptr)(chstr));
	rgssFnExport void log(chstr message, chstr prefix = "[rgss] ");
	rgssFnExport bool isDebugMode();
	rgssFnExport void setDebugMode(bool value);
	rgssFnExport void setPixelShader(april::PixelShader* value);

	extern hmap<hstr, hstr> parameters;

}

#endif
