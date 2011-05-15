#ifndef ARC_UTILITY_H
#define ARC_UTILITY_H

#include <hltypes/hstring.h>

namespace arc
{
	void setupSystemPath(chstr gameName);
	void log(chstr message);

	extern hstr path;
	
}

#endif