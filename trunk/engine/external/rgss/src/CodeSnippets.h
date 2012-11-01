#ifndef RGSS_CODE_SNIPPETS_H
#define RGSS_CODE_SNIPPETS_H

#define rb_b_ary_each_index(ary, name) for (int name = 0; name < NUM2INT(rb_f_size(ary)); name++)

/// @brief Calls the to_s method.
/// @param[in] obj Object to use.
#define rb_f_to_s(obj) rb_funcall_0(obj, "to_s")
/// @brief Calls the to_sym method.
/// @param[in] obj Object to use.
#define rb_f_to_sym(obj) rb_funcall_0(obj, "to_sym")
/// @brief Gets object size.
/// @param[in] str Object to check.
#define rb_f_size(str) rb_funcall_0(str, "size")
/// @brief Packs an array into a bytestream in the given format.
/// @param[in] ary Array to pack.
/// @param[in] format Packing format.
#define rb_f_ary_pack(ary, format) rb_funcall_1(ary, "pack", rb_str_new2(format))
/// @brief Unpacks a bytestream into an array in the given format.
/// @param[in] str String to unpack.
/// @param[in] format Unpacking format.
#define rb_f_str_unpack(str, format) rb_funcall_1(str, "unpack", rb_str_new2(format))
/// @brief Checks if a constant is defined.
/// @param[in] obj Object to check.
/// @param[in] name Name of the constant.
#define rb_f_const_defined(obj, name) rb_funcall_1(obj, "const_defined?", rb_f_to_sym(rb_str_new2(name)))
/// @brief Checks if a method can be called.
/// @param[in] obj Object to check.
/// @param[in] name Name of the method.
#define rb_f_respond_to(obj, name) rb_funcall_1(obj, "respond_to?", rb_f_to_sym(rb_str_new2(name)))
/// @brief Checks if two objects are equal.
/// @param[in] obj1 First object.
/// @param[in] obj2 Second object.
#define rb_f_equal(obj1, obj2) rb_funcall_1(obj1, "==", obj2)
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
		VALUE errnoModule = rb_const_get(rb_mKernel, rb_intern("Errno")); \
		VALUE enoentClass = rb_const_get(errnoModule, rb_intern("ENOENT")); \
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
		RB_CHECK_TYPE(value, rb_c ## type2); \
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
		RB_CHECK_TYPE(rb_ ## name, rb_c ## type); \
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
	rb_raise(rb_eTypeError, ("Can't clone: " + value->typeName).c_str());
/// @brief Throws a duping error.
/// @param[in] value Value that can't be duplicated.
#define RB_CANT_DUP_ERROR(value) \
	rb_raise(rb_eTypeError, ("Can't dup: " + value->typeName).c_str());

/// @brief Automatically does a disposed check.
/// @param[in] value Value to check.
#define RB_CHECK_DISPOSED(value) \
	if (value->disposed) \
	{ \
		rb_raise(rb_eRGSSError, ("Disposed: " + value->typeName).c_str()); \
	}

/// @brief Automatically does a type check (and throw an exception if failed) with 1 acceptable type.
/// @param[in] var Variable that needs to be type-checked.
/// @param[in] type1 First acceptable class.
#define RB_CHECK_TYPE(var, type1) \
	if (!rb_obj_is_kind_of(var, type1)) \
	{ \
		VALUE varClass = rb_class_name(rb_class_of(var)); \
		VALUE class1 = rb_class_name(type1); \
		hstr message = hsprintf("Cannot convert: %s into %s", StringValueCStr(varClass), \
			StringValueCStr(class1)); \
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

	