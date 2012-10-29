#ifdef _WIN32
#include <windows.h>
#endif

#include <hltypes/hfile.h>
#include <hltypes/hstring.h>
#include <zer0/zer0.h>

#if !defined(_CONSOLE) && defined(_WIN32)
int CALLBACK WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
#else
int main(int argc, char** argv)
#endif
{
	bool initialized = zer0::init();
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
		args += unicode_to_utf8(argv[i]);
	}
	LocalFree(argv);
#else
	for_iter (i, 0, argc)
	{
		args += hstr(argv[i]);
	}
#endif
	int result = zer0::enterMainLoop(args);
	zer0::destroy();
	return result;
}
