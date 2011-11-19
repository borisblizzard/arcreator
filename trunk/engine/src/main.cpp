#ifdef _WIN32
#include <windows.h>
#endif

#ifdef _DEBUG
#include <hltypes/hfile.h>
#endif
#include <hltypes/hstring.h>
#include <zer0/zer0.h>

void log(chstr path, chstr message)
{
#ifdef _DEBUG
#ifdef _CONSOLE
	printf("%s\n", message.c_str());
#endif
	hfile file((path + "log.txt"), hfile::APPEND);
	file.writef("%s\n", message.c_str());
#endif
}

#if !defined(_CONSOLE) && defined(_WIN32)
int CALLBACK WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
#else
int main(int argc, char** argv)
#endif
{
	bool initialized = zer0::init(&log);
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
