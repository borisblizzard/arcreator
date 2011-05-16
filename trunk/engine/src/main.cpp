#ifdef _WIN32
#include <windows.h>
#endif

#include <zer0/zer0.h>

#include "Utility.h"

#if !defined(_CONSOLE) && defined(_WIN32)
int CALLBACK WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
#else
int main(int argc, char** argv)
#endif
{
	//TODO - add reading of configuration data from INI
	arc::setupSystemPath("ExampleGameName");
	bool initialized = zer0::init(640, 480, false, "Advanced RPG Creator", arc::path, &arc::log);
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
