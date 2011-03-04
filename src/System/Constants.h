#ifndef SYSTEM_CONSTANTS_H
#define SYSTEM_CONSTANTS_H

// iterator macros
#define foreach_xml(name, container) for (xml_node* name = container->iter_children(); name; name = name->next())
#define for_iter(name, min, max) for (int name = min; name < max; name++)

#define GAME_VERSION_MAJOR (1)
#define GAME_VERSION_MINOR (0)
#define GAME_VERSION_REVISION (0)
#define GAME_VERSION_BUILD (0)

#define cstr(s) #s
#define cstr2(s) cstr(s)
#define GAME_VERSION_STRING cstr2(GAME_VERSION_MAJOR) "." cstr2(GAME_VERSION_MINOR) "." cstr2(GAME_VERSION_REVISION) "." cstr2(GAME_VERSION_BUILD) "\0"
#define GAME_VERSION_STRING_SHORT "v" cstr2(GAME_VERSION_MAJOR) "." cstr2(GAME_VERSION_MINOR) "." cstr2(GAME_VERSION_REVISION) "\0"

#define VER_VERSION GAME_VERSION_MAJOR,GAME_VERSION_MINOR,GAME_VERSION_REVISION,GAME_VERSION_BUILD
#define VER_VERSION_STR GAME_VERSION_STRING
#define VER_COMPANYNAME_STR "Chaos Project"
#define VER_FILEDESCRIPTION_STR "Main Executable for Advanced RPG Creator"
#define VER_LEGALCOPYRIGHT_STR "© Chaos Project"
#define VER_PRODUCTNAME_STR "Advanced RPG Creator Executable"

// numeric system constants
#define TEXTURE_UNLOAD_TIME (5.0f)
#define E_TOLERANCE (0.01f)

#endif
