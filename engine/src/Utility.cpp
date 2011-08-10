#include <hltypes/harray.h>
#include <hltypes/hdir.h>
#include <hltypes/hfile.h>
#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "Constants.h"

namespace arc
{
	hstr path;

	/// @todo Add Linux and Mac variants.
	void setupSystemPath(chstr gameName)
	{
#ifdef _DEBUG
		arc::path = "log";
#elif defined(_WIN32)
		arc::path = getenv("ALLUSERSPROFILE");
		arc::path = arc::path.replace("\\", "/");
		if (getenv("LOCALAPPDATA") == NULL) // Vista / 7
		{
			arc::path += "/" + hstr(getenv("APPDATA")).split("\\").pop_back();
		}
		const wchar_t* name = _wgetenv(L"USERNAME");
		hstr username;
		for (int i = 0; name[i] != 0; i++)
		{
			username += (char)(name[i] > 0x80 ? 0x40 + (name[i] % 26) : name[i]);
		}
		arc::path += hsprintf("/%s/%s/%s", "ARC", gameName.c_str(), username.c_str());
#endif
		hdir::create(arc::path);
		arc::path += "/";
		hfile::create_new(arc::path + "log.txt");
	}

	void log(chstr message)
	{
#ifdef _CONSOLE
		printf("%s\n", message.c_str());
#endif
		hfile file((arc::path + "log.txt"), hfile::APPEND);
		file.writef("%s\n", message.c_str());
	}

	hmap<hstr, hstr> readCfgFile(chstr filename)
	{
		hmap<hstr, hstr> result;
		result[CFG_TITLE] = "Example Game";
		result[CFG_RESOLUTION] = "640x480";
		result[CFG_FULLSCREEN] = "false";
		if (hfile::exists(filename))
		{
			hfile f(filename);
			harray<hstr> lines = f.read_lines();
			harray<hstr> data;
			foreach (hstr, it, lines)
			{
				data = (*it).split(":", 1);
				if (data.size() == 2)
				{
					result[data[0]] = data[1];
				}
			}
			if (result[CFG_RESOLUTION].split("x").size() != 2)
			{
				result[CFG_RESOLUTION] = "640x480";
			}
		}
		return result;
	}
	
}
