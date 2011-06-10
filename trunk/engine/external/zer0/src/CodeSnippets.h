#ifndef ZER0_CODE_SNIPPETS_H
#define ZER0_CODE_SNIPPETS_H

// iterator macro
#define for_iter(name, min, max) for (int name = min; name < max; name++)

/// @brief Converts a VALUE to a pointer of type and name
/// @param[in] value The Ruby VALUE.
/// @param[in] type Type of the C++ variable.
/// @param[in] name Name of the C++ variable.
#define RB_VAR2CPP(value, type, name) type* name; Data_Get_Struct(value, type, name);
/// @brief Directly converts self to a pointer of type and name
/// @param[in] type Type of the C++ variable.
/// @param[in] name Name of the C++ variable.
#define RB_SELF2CPP(type, name) type* name; Data_Get_Struct(self, type, name);

#endif
