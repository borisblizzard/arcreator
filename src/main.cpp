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
	arc::setupSystemPath("ExampleGameName");
	bool result = zer0::init(800, 600, false, "Advanced RPG Creator", &arc::log);
	if (!result)
	{
		return 1;
	}
	zer0::destroy();
	return 0;
}
