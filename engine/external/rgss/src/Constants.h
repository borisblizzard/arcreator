#ifndef RGSS_CONSTANTS_H
#define RGSS_CONSTANTS_H

#define VERSION_MAJOR (0)
#define VERSION_MINOR (9)
#define VERSION_REVISION (1)
#define VERSION_BUILD (289)

#define cstr(s) #s
#define cstr2(s) cstr(s)
#define VERSION_STRING cstr2(VERSION_MAJOR) "." cstr2(VERSION_MINOR) "." cstr2(VERSION_REVISION) "." cstr2(VERSION_BUILD) "\0"
#define VERSION_STRING_SHORT "v" cstr2(VERSION_MAJOR) "." cstr2(VERSION_MINOR) "." cstr2(VERSION_REVISION) "\0"

#define VER_VERSION VERSION_MAJOR,VERSION_MINOR,VERSION_REVISION,VERSION_BUILD
#define VER_VERSION_STR VERSION_STRING
#define VER_COMPANYNAME_STR "Chaos Project"
#define VER_FILEDESCRIPTION_STR "Zer0 Division Engine RGSS"
#define VER_LEGALCOPYRIGHT_STR "© Chaos Project"
#define VER_PRODUCTNAME_STR "Zer0 Division Engine Ruby Game Scripting System"

// numeric system constants
#define TEXTURE_UNLOAD_TIME (5.0f)
#define E_TOLERANCE (0.01f)

#endif
