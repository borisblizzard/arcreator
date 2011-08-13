#ifndef ARC_CONSTANTS_H
#define ARC_CONSTANTS_H

#define VERSION_MAJOR (1)
#define VERSION_MINOR (0)
#define VERSION_REVISION (0)
#define VERSION_BUILD (285)

#define cstr(s) #s
#define cstr2(s) cstr(s)
#define VERSION_STRING cstr2(VERSION_MAJOR) "." cstr2(VERSION_MINOR) "." cstr2(VERSION_REVISION) "." cstr2(VERSION_BUILD) "\0"
#define VERSION_STRING_SHORT "v" cstr2(VERSION_MAJOR) "." cstr2(VERSION_MINOR) "." cstr2(VERSION_REVISION) "\0"

#define VER_VERSION VERSION_MAJOR,VERSION_MINOR,VERSION_REVISION,VERSION_BUILD
#define VER_VERSION_STR VERSION_STRING
#define VER_COMPANYNAME_STR "Chaos Project"
#define VER_FILEDESCRIPTION_STR "ARC Executable"
#define VER_LEGALCOPYRIGHT_STR "© Chaos Project"
#define VER_PRODUCTNAME_STR "Advanced RPG Creator Executable"

#define CFG_TITLE "Title"
#define CFG_RESOLUTION "Resolution"
#define CFG_FULLSCREEN "Fullscreen"

#endif
