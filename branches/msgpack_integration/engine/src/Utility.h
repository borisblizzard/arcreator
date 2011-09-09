#ifndef ARC_UTILITY_H
#define ARC_UTILITY_H

#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

namespace arc
{
	void setupSystemPath(chstr gameName);
	void log(chstr message);
	hmap<hstr, hstr> readCfgFile(chstr filename);

	extern hstr path;
	
}

#endif