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
// 4 : error getting exe path
int main(int argc, char** argv)
{
    char *exepath, *pypath, *pypath_sep, *exepathdirname;
    wchar_t **wargv, *wfileName, *wexepath, *wpypath;
    int i, size, PATHLENMAX;
    int status;
#if defined(__APPLE__)
    uint32_t exepathsize;
#endif
#if defined(__linux__)
    ssize_t linkreadlen;
#endif

    // in truth we can never know what the true max path length is on windows 
    //it is the only OS that actualy limits it
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
    exepath = (char *)calloc(PATHLENMAX, sizeof(char));
    if (!exepath) {
        status = 2;
        goto cleanup1;
    }
#if defined(_WIN32) || defined(__APPLE__) || defined(__linux__)

#if defined(_WIN32)
    GetModuleFileName(NULL, exepath, PATHLENMAX);
    PathRemoveFileSpec(exepath);
    exepathdirname = exepath;
#elif defined(__APPLE__)
    exepathsize = PATHLENMAX;
    if (_NSGetExecutablePath(exepath, exepathsize) != 0) {
        status = 4;
        goto cleanup2;
    }
    exepathdirname = dirname(exepath);
#elif defined(__linux__)
    linkreadlen = readlink("/proc/self/exe", exepath, PATHLENMAX);
    if (linkreadlen != -1) {
        exepath[linkreadlen] = '\0';
    }
    else {
        status = 4;
        goto cleanup2;
    }
    exepathdirname = dirname(exepath);
#endif 

    size = strlen(exepathdirname);
    wexepath = (wchar_t *)calloc((size + 1), sizeof(wchar_t));
    if (!wexepath) {
        status = 2;
        goto cleanup2;
    }
    status = mbstowcs(wexepath, exepathdirname, size + 1);
    if (status < 0) {
        status = 3;
        goto cleanup3;
    } 
#else
    wexepath = L".";
#endif 

    wprintf(L"[LOADER] Exe Path:  %ls\n", wexepath);

    //Py_SetPythonHome(wexepath);

    pypath_sep = (char *)calloc(2, sizeof(char) );
    if (!pypath_sep) {
        status = 2;
        goto cleanup3;
    }
#if defined(_WIN32)
    strcpy(pypath_sep, ";");
#else
    strcpy(pypath_sep, ":");
#endif

    pypath = (char *)calloc((PATHLENMAX * 5 + 5), sizeof(char));
    if (!pypath) {
        status = 2;
        goto cleanup4;
    }
    
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
    wpypath = (wchar_t *)calloc((size + 1), sizeof(wchar_t));
    if (!wpypath) {
        status = 2;
        goto cleanup5;
    }
    status = mbstowcs(wpypath, pypath, size + 1);
    if (status < 0) {
        status = 3;
        goto cleanup6;
    }


    wargv = (wchar_t **)calloc(argc, sizeof(wchar_t*));
    if (!wargv) {
        status = 2;
        goto cleanup6;
    }
    for (i = 0; i < argc; i++) {
        size = strlen(argv[i]);
        wargv[i] = (wchar_t *)calloc((size + 1), sizeof(wchar_t));
        if (!wargv[i]) {
            status = 2;
            goto cleanup7;
        }
        status = mbstowcs(wargv[i], argv[i], size + 1);
        if (status < 0) {
            status = 3;
            goto cleanup7;
        }
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
cleanup7:
    for (i = 0; i < argc; i++) {
        if (wargv[i] != NULL) {
            free(wargv[i]);
        }
    }
    free(wargv);
cleanup6:
    free(wpypath);
cleanup5:
    free(pypath);
cleanup4:
    free(pypath_sep);
cleanup3:
    free(exepath); 
cleanup2:
    free(wexepath);
cleanup1:
    return status;
}
