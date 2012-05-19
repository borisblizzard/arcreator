#ifndef RGSS_CODE_SNIPPETS_H
#define RGSS_CODE_SNIPPETS_H

// iterator macro
#define for_iter(name, min, max) for (int name = min; name < max; name++)
#define for_iter_step(name, min, max, step) for (int name = min; name < max; name += step)

#define rb_ary_each_index(ary, name) for (int name = 0; name < NUM2INT(rb_ary_size(ary)); name++)

// missing C functions for commonly used classes

/// @brief Gets string size.
/// @param[in] str String to check.
#define rb_str_size(str) rb_funcall(str, rb_intern("size"), 0)
/// @brief Gets array size.
/// @param[in] ary Array to check.
#define rb_ary_size(ary) rb_funcall(ary, rb_intern("size"), 0)
/// @brief Gets hash size.
/// @param[in] ary Hash to check.
#define rb_hash_size(ary) rb_funcall(ary, rb_intern("size"), 0)
/// @brief Calls method with name.
/// @param[in] obj Object to call the method.
/// @param[in] name Name of the method.
#define rb_funcall_0(obj, name) rb_funcall(obj, rb_intern(name), 0)
/// @brief Calls method with name and one argument.
/// @param[in] obj Object to call the method.
/// @param[in] name Name of the method.
/// @param[in] arg First argument.
#define rb_funcall_1(obj, name, arg) rb_funcall(obj, rb_intern(name), 1, arg)
/// @brief Calls method with name and one argument.
/// @param[in] obj Object to call the method.
/// @param[in] name Name of the method.
/// @param[in] arg1 First argument.
/// @param[in] arg2 Second argument.
#define rb_funcall_2(obj, name, arg1, arg2) rb_funcall(obj, rb_intern(name), 2, arg1, arg2)
/// @brief Calls method with name and arguments.
/// @param[in] obj Object to call the method.
/// @param[in] name Name of the method.
/// @param[in] argc Number of arguments.
/// @param[in] argv Argument values.
#define rb_funcall_x(obj, name, argc, argv) rb_funcall2(obj, rb_intern(name), argc, argv)
/// @brief Calls to_s.
/// @param[in] obj Object to use.
#define rb_f_to_s(obj) rb_funcall(obj, rb_intern("to_s"), 0)
/// @brief Calls rb_to_sym.
/// @param[in] obj Object to use.
#define rb_f_to_sym(obj) rb_funcall(obj, rb_intern("to_sym"), 0)
/// @brief Calls inspect.
/// @param[in] obj Object to use.
#define rb_f_inspect(obj) rb_funcall(obj, rb_intern("inspect"), 0)
/// @brief Gets the object ID.
/// @param[in] obj Object to check.
#define rb_f_object_id(obj) rb_funcall(obj, rb_intern("object_id"), 0)
/// @brief Clones object.
/// @param[in] obj Object to clone.
#define rb_f_clone(obj) rb_funcall(obj, rb_intern("clone"), 0)

/// @brief Converts a VALUE to a pointer of type and name.
/// @param[in] value The Ruby VALUE.
/// @param[in] type Type of the C++ variable.
/// @param[in] name Name of the C++ variable.
#define RB_VAR2CPP(value, type, name) type* name; Data_Get_Struct(value, type, name);
/// @brief Directly converts self to a pointer of type and name.
/// @param[in] type Type of the C++ variable.
/// @param[in] name Name of the C++ variable.
#define RB_SELF2CPP(type, name) type* name; Data_Get_Struct(self, type, name);
/// @brief throws an Errno::ENOENT exception
/// @param[in] filename Filename C-string.
#define RB_RAISE_FILE_NOT_FOUND(filename) \
	{ \
		VALUE errnoModule = rb_funcall_1(rb_mKernel, "const_get", rb_f_to_sym(rb_str_new2("Errno"))); \
		VALUE enoentClass = rb_funcall_1(errnoModule, "const_get", rb_f_to_sym(rb_str_new2("ENOENT"))); \
		rb_raise(enoentClass, filename); \
	}

/// @brief Generates an entire Ruby setter method in C++.
/// @param[in] type1 Type of the C++ variable.
/// @param[in] name1 Name of the C++ variable.
/// @param[in] type2 Type of the C++ variable that is being set.
/// @param[in] name2 Name of the C++ variable that is being set.
#define RB_GENERATE_SETTER(type1, name1, type2, name2) \
	RB_SELF2CPP(type1, name1); \
	if (!NIL_P(value)) \
	{ \
		RB_CHECK_TYPE_1(value, rb_c ## type2); \
		RB_VAR2CPP(value, type2, name2); \
		name1->name2 = name2; \
	} \
	else \
	{ \
		name1->name2 = NULL; \
	} \
	name1->rb_ ## name2 = value;
/// @brief Generates an entire initializer for Ruby in C++.
/// @param[in] type1 Type of the C++ variable.
/// @param[in] name1 Name of the C++ variable.
/// @param[in] type2 Type of the C++ variable that is being set.
/// @param[in] name2 Name of the C++ variable that is being set.
#define CPP_GENERATE_INITIALIZER(type, name) \
	if (!NIL_P(rb_ ## name)) \
	{ \
		RB_CHECK_TYPE_1(rb_ ## name, rb_c ## type); \
		RB_VAR2CPP(rb_ ## name, type, name); \
		this->name = name; \
	} \
	else \
	{ \
		this->name = NULL; \
	} \
	this->rb_ ## name = rb_ ## name;

/// @brief Throws a cloning error.
/// @param[in] value Value that can't be cloned.
#define RB_CANT_CLONE_ERROR(value) \
	rb_raise(rb_eTypeError, ("can't clone " + value->typeName).c_str());
/// @brief Throws a duping error.
/// @param[in] value Value that can't be duplicated.
#define RB_CANT_DUP_ERROR(value) \
	rb_raise(rb_eTypeError, ("can't dup " + value->typeName).c_str());

/// @brief Automatically does a disposed check.
/// @param[in] value Value to check.
#define RB_CHECK_DISPOSED(value) \
	if (value->disposed) \
	{ \
		rb_raise(rb_eRGSSError, ("disposed " + value->typeName).c_str()); \
	}

/// @brief Automatically does a type check (and throw an exception if failed) with 1 acceptable type.
/// @param[in] var Variable that needs to be type-checked.
/// @param[in] type1 First acceptable class.
#define RB_CHECK_TYPE_1(var, type1) \
	if (!rb_obj_is_kind_of(var, type1)) \
	{ \
		VALUE varClass = rb_funcall(rb_class_of(var), rb_intern("name"), 0, NULL); \
		VALUE class1 = rb_funcall(type1, rb_intern("name"), 0, NULL); \
		hstr message = hsprintf("cannot convert %s into %s", StringValueCStr(varClass), \
			StringValueCStr(class1)); \
		rb_raise(rb_eTypeError, message.c_str()); \
	}
/// @brief Automatically does a type check (and throw an exception if failed) with 2 acceptable types.
/// @param[in] var Variable that needs to be type-checked.
/// @param[in] type1 First acceptable class.
/// @param[in] type2 Second acceptable class.
#define RB_CHECK_TYPE_2(var, type1, type2) \
	if (!rb_obj_is_kind_of(var, type1) && !rb_obj_is_kind_of(var, type2)) \
	{ \
		VALUE varClass = rb_funcall(rb_class_of(var), rb_intern("name"), 0, NULL); \
		VALUE class1 = rb_funcall(type1, rb_intern("name"), 0, NULL); \
		VALUE class2 = rb_funcall(type2, rb_intern("name"), 0, NULL); \
		hstr message = hsprintf("cannot convert %s into %s or %s", StringValueCStr(varClass), \
			StringValueCStr(class1), StringValueCStr(class2)); \
		rb_raise(rb_eTypeError, message.c_str()); \
	}
/// @brief Automatically does a type check (and throw an exception if failed) with 3 acceptable types.
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
		hstr message = hsprintf("cannot convert %s into %s, %s or %s", StringValueCStr(varClass), \
			StringValueCStr(class1), StringValueCStr(class2), StringValueCStr(class3)); \
		rb_raise(rb_eTypeError, message.c_str()); \
	}
/// @brief Automatically does a type check (and throw an exception if failed) with 4 acceptable types.
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
		hstr message = hsprintf("cannot convert %s into %s, %s, %s or %s", StringValueCStr(varClass), \
			StringValueCStr(class1), StringValueCStr(class2), StringValueCStr(class3), StringValueCStr(class4)); \
		rb_raise(rb_eTypeError, message.c_str()); \
	}

/// @brief Creates a C++ object with a Ruby reference.
/// @param[in] classe Ruby class VALUE.
/// @param[in] type C++ type.
/// @param[in] var Variable to store the object.
/// @param[in] mark Mark function.
/// @param[in] free Free function.
#define RB_OBJECT_NEW(classe, type, var, mark, free) \
	( \
		var = new type(), \
		Data_Wrap_Struct(classe, mark, free, var) \
	)
/// @brief Deletes the C++ object after the Ruby reference has been destroyed.
/// @param[in] var Variable of the object.
#define RB_OBJECT_DELETE(var) delete var

/// @brief Marks the object for the GC if it exists.
/// @param[in] object The Ruby object to mark.
#define RB_GC_MARK(object) \
	if (!NIL_P(this->rb_ ## object)) \
	{ \
		rb_gc_mark(this->rb_ ## object); \
	}

/// @brief Deletes the variable since it was created for C++ only.
/// @param[in] object The C++ object to delete.
#define CPP_VAR_DELETE(object) \
	if (NIL_P(this->rb_ ## object) && this->object != NULL) \
	{ \
		delete this->object; \
	}

#endif

	