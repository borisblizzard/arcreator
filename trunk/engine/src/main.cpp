#ifdef _WIN32
#include <windows.h>
#endif

#include <hltypes/hfile.h>
#include <hltypes/hmap.h>
#include <hltypes/hstring.h>
#include <zer0/zer0.h>

#include "Constants.h"
#include "Utility.h"

#if !defined(_CONSOLE) && defined(_WIN32)
int CALLBACK WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
#else
int main(int argc, char** argv)
#endif
{
	hmap<hstr, hstr> parameters = arc::readCfgFile("arc.cfg");
	arc::setupSystemPath(parameters[CFG_TITLE]);
	harray<int> resolution = parameters[CFG_RESOLUTION].split("x").cast<int>();
	bool fullscreen = (bool)parameters[CFG_FULLSCREEN];
	bool initialized = zer0::init(resolution[0], resolution[1], fullscreen, parameters[CFG_TITLE], arc::path, &arc::log);
	if (!initialized)
	{
		return 1;
	}
#if !defined(_CONSOLE) && defined(_WIN32)
	int result = zer0::enterMainLoop(0, NULL); // needs to be changed
#else
	int result = zer0::enterMainLoop(argc, argv);
#endif
	zer0::destroy();
	return result;
}
