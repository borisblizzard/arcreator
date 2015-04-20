#include <Python.h>
#include <locale.h>
#if defined(_WIN32)
#include <windows.h>
#include "Shlwapi.h"
#endif
#if defined(__APPLE__)
#include <dyld.h>
#include <libgen.h>
#include <wchar.h>
#endif
#if defined(__linux__)
#include <unistd.h>
#include <libgen.h>
#include <wchar.h>
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// disable filename globbing on Windows
#if defined(_WIN32)
int _CRT_glob = 0;
#endif

//exit codes
// 1 : ?
// 2 : malloc failure
// 3 : mbstowcs failure
// 4 : error gettign exe path
int main(int argc, char** argv)
{
    char *exepath, *exepathdirname, *pypath, *pypath_sep;
    wchar_t **wargv, *wfileName, *wexepath, *wpypath;
    int i, size, PATHLENMAX;
    int status;
#if defined(__APPLE__)
    uint32_t exepathsize;
    char *exepathdirname;
#endif
#if defined(__linux__)
    ssize_t linkreadlen;
#endif

    // in truth we can never know what the true max path length is windows is the only OS that actualy limits it
    // I'm just seting an arbatraly high value
    PATHLENMAX = 10240;
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

    //get the folder of the exe
#if defined(_WIN32)
    exepath = (char *)malloc(sizeof(char) * PATHLENMAX);
    if (!exepath)
        return 2;
    GetModuleFileName(NULL, exepath, PATHLENMAX);
    PathRemoveFileSpec(exepath);
    size = strlen(exepath);
    wexepath = (wchar_t *)malloc(sizeof(wchar_t) * (size + 1));
    if (!wexepath)
        return 2;
    status = mbstowcs(wexepath, exepath, size + 1);
    if (status < 0)
        return 3;
#elif defined(__APPLE__)
    exepath = (char *)malloc(sizeof(char) * PATHLENMAX);
    exepathsize = PATHLENMAX;
    if (_NSGetExecutablePath(exepath, exepathsize) != 0)
        return 4;
    exepathdirname = dirname(exepath);
    size = strlen(exepathdirname);
    wexepath = (wchar_t *)malloc(sizeof(wchar_t) * (size + 1));
    if (!wexepath)
        return 2;
    status = mbstowcs(wexepath, exepathdirname, size + 1);
    if (status < 0)
        return 3;
#elif defined(__linux__)
    exepath = (char *)malloc(sizeof(char) * PATHLENMAX);
    linkreadlen = readlink("/proc/self/exe", exepath, PATHLENMAX);
    if (linkreadlen != -1) {
        exepath[linkreadlen] = '\0';
    }
    else {
        return 4;
    }
    exepathdirname = dirname(exepath);
    size = strlen(exepathdirname);
    wexepath = (wchar_t *)malloc(sizeof(wchar_t) * (size + 1));
    if (!wexepath)
        return 2;
    status = mbstowcs(wexepath, exepathdirname, size + 1);
    if (status < 0)
        return 3;
#else
    wexepath = L".";
#endif 

    wprintf(L"[LOADER] Exe Path:  %ls\n", wexepath);

    //Py_SetPythonHome(wexepath);

    pypath_sep = (char *)malloc(sizeof(char) * 2);
#if defined(_WIN32)
    strcpy(pypath_sep, ";");
#else
    strcpy(pypath_sep, ":");
#endif

    pypath = (char *)malloc(sizeof(char) * (PATHLENMAX * 5 + 5));
    
    strcpy(pypath, exepath);
    strcat(pypath, pypath_sep);
    strcat(pypath, exepath);
    strcat(pypath, "/python.zip");
    strcat(pypath, pypath_sep);
    strcat(pypath, exepath);
    strcat(pypath, "/lib");
    strcat(pypath, pypath_sep);
    strcat(pypath, exepath);
    strcat(pypath, "/lib/site-packages");
    strcat(pypath, pypath_sep);
    strcat(pypath, exepath);
#if defined(_WIN32)
    strcat(pypath, "/lib/DLLs");
#elif defined(__APPLE__)
    strcat(pypath, "/lib/lib-dynload");
#elif defined(__linux__)
    strcat(pypath, "/lib/lib-dynload");
#else
    strcat(pypath, "/lib/dyn");
#endif

    // should look somthing like this now
    // "<exepath>:<exepath>/python.zip:<exepath>/lib"

    size = strlen(pypath);
    wpypath = (wchar_t *)malloc(sizeof(wchar_t)* (size + 1));
    if (!wpypath)
        return 2;
    status = mbstowcs(wpypath, pypath, size + 1);
    if (status < 0)
        return 3;


    wargv = (wchar_t **)PyMem_Malloc(sizeof(wchar_t*) * argc);
    if (!wargv)
        return 2;
    for (i = 0; i < argc; i++) {
        size = strlen(argv[i]);
        wargv[i] = (wchar_t *)PyMem_Malloc(sizeof(wchar_t)* (size + 1));
        if (!wargv[i])
            return 2;
        status = mbstowcs(wargv[i], argv[i], size + 1);
        if (status < 0)
            return 3;
    }

    Py_SetProgramName(wargv[0]);
    wfileName = Py_GetProgramFullPath();

    //call SetPath after SetProgramName becasue otherwise the new name is ignored
    Py_SetPath(wpypath);

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

    free(wexepath);
    free(exepath);
    free(pypath_sep);
    return status;
}
