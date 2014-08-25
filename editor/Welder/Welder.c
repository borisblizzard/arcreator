#include <Python.h>
#include <locale.h>
#ifdef MS_WINDOWS
#include <windows.h>
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// disable filename globbing on Windows
#if defined(_WIN32)
int _CRT_glob = 0;
#endif




int main(int argc, char** argv)
{
    wchar_t **wargv, *wfileName;
    int i, size;
    int status;

    // hide the console window on windows
#if defined(_WIN32)
    ShowWindow( GetConsoleWindow(), SW_HIDE );
#endif

    /*
    Set Flags
     */
    Py_NoSiteFlag = 1;
    Py_FrozenFlag = 1;
    Py_IgnoreEnvironmentFlag = 1;

    setlocale(LC_CTYPE, "");
    Py_SetPythonHome(L".");

    wargv = (wchar_t **)PyMem_Malloc(sizeof(wchar_t*) * argc);
    if (!wargv)
        return 2;
    for (i = 0; i < argc; i++) {
        size = strlen(argv[i]);
        wargv[i] = (wchar_t *)PyMem_Malloc(sizeof(wchar_t) * (size + 1));
        if (!wargv[i])
            return 2;
        status = mbstowcs(wargv[i], argv[i], size + 1);
        if (status < 0)
            return 3;
    }

    Py_SetProgramName(wargv[0]);
    wfileName = Py_GetProgramFullPath();

    //call SetPath after SetProgramName becasue otherwise the new name is ignored
#if defined(_WIN32)
    Py_SetPath(L".;./python.zip;./lib");
#else
    Py_SetPath(L".:./python.zip:./lib");
#endif

    wprintf(L"[LOADER] Search Path:  %ls\n", Py_GetPath());
    wprintf(L"[LOADER] Filename:     %ls\n", wfileName);

    Py_Initialize();
    //Py_InitializeEx(0);
    
    PySys_SetArgv(argc, wargv);

    status = PyRun_SimpleString(
        "import sys\n"
        "try:\n"
        "    print(\"System Path:\", sys.path)\n"
        "    print(\"Running main code now:\")\n"
        "    import main\n"
        "except:\n"
        "    print(\"[LOADER] Unexpected error:\", repr(sys.exc_info()[0]))\n"
        "    raise\n"
    );

    if (status < 0) {
        printf("[LOADER] %s\n", "There was an unknown error");
    }
    
    Py_Finalize();
    return status;
}
