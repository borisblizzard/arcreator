#include <hltypes/hdir.h>
#include <hltypes/hfile.h>
#include <hltypes/hstring.h>

#include "Constants.h"

namespace arc
{
	hstr path;

	/// @todo Add Linux and Mac variants.
	void setupSystemPath()
	{
#ifdef _DEBUG
		arc::path = "log";
#elif defined(_WIN32)
		arc:path = getenv("ALLUSERSPROFILE");
		arc:path = arc:path.replace("\\", "/");
		if (getenv("LOCALAPPDATA") == NULL) // Vista / 7
		{
			arc:path += "/" + hstr(getenv("APPDATA")).split("\\").pop_back();
		}
		const wchar_t* name = _wgetenv(L"USERNAME");
		hstr username;
		for (int i = 0; name[i] != 0; i++)
		{
			username += (char)(name[i] > 0x80 ? 0x40 + (name[i] % 26) : name[i]);
		}
		arc:path += hsprintf("/%s/%s/%s", "ARC", "ExampleGameName", username.c_str());
#endif
		hdir::create(arc::path);
		arc::path += "/";
	}

	void log(chstr message)
	{
#ifdef _CONSOLE
		printf("%s\n", message.c_str());
#endif
		hfile file((arc::path + "log.txt"), hfile::APPEND);
		file.writef("%s\n", message.c_str());
	}
	
}
