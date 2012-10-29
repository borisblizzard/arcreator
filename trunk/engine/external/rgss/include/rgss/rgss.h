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
	extern hstr logTag;

	rgssFnExport void init(hmap<hstr, hstr> parameters);
	rgssFnExport void destroy();
	rgssFnExport bool isDebugMode();
	rgssFnExport void setDebugMode(bool value);
	rgssFnExport void setPixelShader(april::PixelShader* value);

	extern hmap<hstr, hstr> parameters;

}

#endif
