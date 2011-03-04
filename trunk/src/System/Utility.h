#ifndef SYSTEM_UTILITY_H
#define SYSTEM_UTILITY_H

#include <hltypes/harray.h>
#include <hltypes/hstring.h>

namespace System
{
	void log(chstr message);
	hstr generateName(chstr prefix);
	unsigned int getTime();
	
	hstr getVersionString();
	hstr getVersionString(int major, int minor, int revision, int build);
	hstr getVersionDisplay();
	
}

#endif