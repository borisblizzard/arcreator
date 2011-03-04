#include <time.h>

#include <hltypes/hmap.h>
#include <hltypes/hfile.h>
#include <hltypes/hstring.h>

#include "System/Constants.h"
#include "System/Main.h"
#include "System/Utility.h"

namespace System
{
	hstr generateName(chstr prefix)
	{
		static hmap<hstr, int> counters;
		counters[prefix]++;
		return (prefix + hstr(counters[prefix]));
	}
	
	void log(chstr message)
	{
#ifdef _CONSOLE
		printf("%s\n", message.c_str());
#endif
		hfile file((System::path + "log.txt"), hfile::APPEND);
		file.writef("%s\n", message.c_str());
	}
	
	unsigned int getTime()
	{
		return (unsigned int)time(NULL);
	}
	
	hstr getVersionString()
	{
		return getVersionString(GAME_VERSION_MAJOR, GAME_VERSION_MINOR,
			GAME_VERSION_REVISION, GAME_VERSION_BUILD);
	}
	
	hstr getVersionString(int major, int minor, int revision, int build)
	{
		return hsprintf("%d.%d.%d.%d", major, minor, revision, build);
	}
	
	hstr getVersionDisplay()
	{
		return hsprintf("v%d.%d.%d", GAME_VERSION_MAJOR, GAME_VERSION_MINOR,
			GAME_VERSION_REVISION);
	}
	
}
