#ifndef LEGACY_H
#define LEGACY_H

#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "legacyExport.h"

namespace april
{
	class PixelShader;
}

namespace legacy
{
	extern hstr logTag;

	legacyFnExport void init(hmap<hstr, hstr> parameters);
	legacyFnExport void destroy();
	legacyFnExport bool isDebugMode();
	legacyFnExport void setDebugMode(bool value);
	legacyFnExport void setPixelShader(april::PixelShader* value);

	extern hmap<hstr, hstr> parameters;

}

#endif
