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
/// @brief Automatically does a type check (and throw an exception if failed) with 1 acceptable type.
/// @param[in] var Variable that needs to be type-checked.
/// @param[in] type1 First acceptable class.
#define RB_CHECK_TYPE_1(var, type1) \
	if (!rb_obj_is_kind_of(var, type1)) \
	{ \
		VALUE varClass = rb_funcall(rb_class_of(var), rb_intern("name"), 0, NULL); \
		VALUE class1 = rb_funcall(type1, rb_intern("name"), 0, NULL); \
		hstr message = hsprintf("cannot convert %s into %s", StringValuePtr(varClass), \
			StringValuePtr(class1)); \
		rb_raise(rb_eTypeError, message.c_str()); \
	}
/// @brief Automatically does a type check (and throw an exception if failed) with 1 acceptable type.
/// @param[in] var Variable that needs to be type-checked.
/// @param[in] type1 First acceptable class.
/// @param[in] type2 Second acceptable class.
#define RB_CHECK_TYPE_2(var, type1, type2) \
	if (!rb_obj_is_kind_of(var, type1) && !rb_obj_is_kind_of(var, type2)) \
	{ \
		VALUE varClass = rb_funcall(rb_class_of(var), rb_intern("name"), 0, NULL); \
		VALUE class1 = rb_funcall(type1, rb_intern("name"), 0, NULL); \
		VALUE class2 = rb_funcall(type2, rb_intern("name"), 0, NULL); \
		hstr message = hsprintf("cannot convert %s into %s or %s", StringValuePtr(varClass), \
			StringValuePtr(class1), StringValuePtr(class2)); \
		rb_raise(rb_eTypeError, message.c_str()); \
	}
/// @brief Automatically does a type check (and throw an exception if failed) with 1 acceptable type.
/// @param[in] var Variable that needs to be type-checked.
/// @param[in] type1 First acceptable class.
/// @param[in] type2 Second acceptable class.
/// @param[in] type3 Third acceptable class.
#define RB_CHECK_TYPE_3(var, type1, type2, type3) \
	if (!rb_obj_is_kind_of(var, type1) && !rb_obj_is_kind_of(var, type2) && \
		!rb_obj_is_kind_of(var, type3)) \
	{ \
		VALUE varClass = rb_funcall(rb_class_of(var), rb_intern("name"), 0, NULL); \
		VALUE class1 = rb_funcall(type1, rb_intern("name"), 0, NULL); \
		VALUE class2 = rb_funcall(type2, rb_intern("name"), 0, NULL); \
		VALUE class3 = rb_funcall(type3, rb_intern("name"), 0, NULL); \
		hstr message = hsprintf("cannot convert %s into %s, %s or %s", StringValuePtr(varClass), \
			StringValuePtr(class1), StringValuePtr(class2), StringValuePtr(class3)); \
		rb_raise(rb_eTypeError, message.c_str()); \
	}
/// @brief Automatically does a type check (and throw an exception if failed) with 1 acceptable type.
/// @param[in] var Variable that needs to be type-checked.
/// @param[in] type1 First acceptable class.
/// @param[in] type2 Second acceptable class.
/// @param[in] type3 Third acceptable class.
/// @param[in] type4 Fourth acceptable class.
#define RB_CHECK_TYPE_4(var, type1, type2, type3, type4) \
	if (!rb_obj_is_kind_of(var, type1) && !rb_obj_is_kind_of(var, type2) && \
		!rb_obj_is_kind_of(var, type3) && !rb_obj_is_kind_of(var, type4)) \
	{ \
		VALUE varClass = rb_funcall(rb_class_of(var), rb_intern("name"), 0, NULL); \
		VALUE class1 = rb_funcall(type1, rb_intern("name"), 0, NULL); \
		VALUE class2 = rb_funcall(type2, rb_intern("name"), 0, NULL); \
		VALUE class3 = rb_funcall(type3, rb_intern("name"), 0, NULL); \
		VALUE class4 = rb_funcall(type4, rb_intern("name"), 0, NULL); \
		hstr message = hsprintf("cannot convert %s into %s, %s, %s or %s", StringValuePtr(varClass), \
			StringValuePtr(class1), StringValuePtr(class2), StringValuePtr(class3), StringValuePtr(class4)); \
		rb_raise(rb_eTypeError, message.c_str()); \
	}


#endif

	