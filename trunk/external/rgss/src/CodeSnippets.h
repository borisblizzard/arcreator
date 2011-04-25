#ifndef RGSS_CODE_SNIPPETS_H
#define RGSS_CODE_SNIPPETS_H

// iterator macro
#define for_iter(name, min, max) for (int name = min; name < max; name++)

/// @brief Converts a VALUE to a pointer of type and name.
/// @param[in] value The Ruby VALUE.
/// @param[in] type Type of the C++ variable.
/// @param[in] name Name of the C++ variable.
#define RB_VAR2CPP(value, type, name) type* name; Data_Get_Struct(value, type, name);
/// @brief Directly converts self to a pointer of type and name.
/// @param[in] type Type of the C++ variable.
/// @param[in] name Name of the C++ variable.
#define RB_SELF2CPP(type, name) type* name; Data_Get_Struct(self, type, name);
/// @brief Generates an entire Ruby setter method in C++.
/// @param[in] type1 Type of the C++ variable.
/// @param[in] name1 Name of the C++ variable.
/// @param[in] type2 Type of the C++ variable that is being set.
/// @param[in] name2 Name of the C++ variable that is being set.
#define RB_GENERATE_SETTER(type1, name1, type2, name2) \
	RB_SELF2CPP(type1, name1); \
	name1->rb_ ## name2 = value; \
	if (!NIL_P(value)) \
	{ \
		RB_VAR2CPP(value, type2, name2); \
		name1->name2 = name2; \
	} \
	else \
	{ \
		name1->name2 = NULL; \
	}
/// @brief Generates an entire initializer for Ruby in C++.
/// @param[in] type1 Type of the C++ variable.
/// @param[in] name1 Name of the C++ variable.
/// @param[in] type2 Type of the C++ variable that is being set.
/// @param[in] name2 Name of the C++ variable that is being set.
#define CPP_GENERATE_INITIALIZER(type, name) \
	this->rb_ ## name = rb_ ## name; \
	if (!NIL_P(rb_ ## name)) \
	{ \
		RB_VAR2CPP(rb_ ## name, type, name); \
		this->name = name; \
	} \
	else \
	{ \
		this->name = NULL; \
	}

#endif
