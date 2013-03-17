#ifdef _WIN32
#include <windows.h>
#endif

#include <hltypes/hfile.h>
#include <hltypes/hstring.h>
#include <reactor/reactor.h>

#if !defined(_CONSOLE) && defined(_WIN32)
int CALLBACK WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
#else
int main(int argc, char** argv)
#endif
{
	bool initialized = reactor::init();
	if (!initialized)
	{
		return 1;
	}
	harray<hstr> args;
#if !defined(_CONSOLE) && defined(_WIN32)
	int argc = 0;
	wchar_t** argv = CommandLineToArgvW(GetCommandLineW(), &argc);
	for_iter (i, 0, argc)
	{
		args += hstr::from_unicode(argv[i]);
	}
	LocalFree(argv);
#else
	for_iter (i, 0, argc)
	{
		args += hstr(argv[i]);
	}
#endif
	int result = reactor::enterMainLoop(args);
	reactor::destroy();
	return result;
}
