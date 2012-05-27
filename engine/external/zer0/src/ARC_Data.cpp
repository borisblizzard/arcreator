#include <ruby.h>

#include <hltypes/harray.h>
#include <hltypes/hfile.h>
#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "ARC.h"
#include "ARC_Data.h"
#include "ARC_Error.h"
#include "CodeSnippets.h"
#include "zer0.h"

#define __MAP(data, obj) (data += obj)
#define __FIND_MAPPED(data, id) (id < data.size() ? data[id] : Qnil)
#define __DUMP_INT32(obj) (file.dump(obj))
#define __LOAD_INT32 (file.load_int())

namespace zer0
{
	VALUE rb_mARC_Data;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/
	
	hstr ARC_Data::Header;
	hstr ARC_Data::Version;
	hmap<VALUE, unsigned char> ARC_Data::Types;
	hfile ARC_Data::file;
	
	harray<VALUE> ARC_Data::strings;
	harray<VALUE> ARC_Data::arrays;
	harray<VALUE> ARC_Data::hashes;
	harray<VALUE> ARC_Data::objects;
	
	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void ARC_Data::init()
	{
		Header = "ARCD";
		Version = "1.0";
		Types[rb_cNilClass] = 0x10;
		Types[rb_cFalseClass] = 0x11;
		Types[rb_cTrueClass] = 0x12;
		Types[rb_cFixnum] = 0x21;
		Types[rb_cBignum] = 0x22;
		Types[rb_cFloat] = 0x23;
		Types[rb_cString] = 0x30;
		Types[rb_cArray] = 0x40;
		Types[rb_cHash] = 0x41;
		Types[rb_cObject] = 0x00;
		ARC_Data::_resetSerializer();
	}

	void ARC_Data::destroy()
	{
	}

	void ARC_Data::createRubyInterface()
	{
		rb_mARC_Data = rb_define_module_under(rb_mARC, "Data");
		rb_define_const(rb_mARC_Data, "Version", rb_str_new2(Version.c_str()));
		rb_define_module_function(rb_mARC_Data, "dump", RUBY_METHOD_FUNC(&ARC_Data::rb_dump), 2);
		rb_define_module_function(rb_mARC_Data, "load", RUBY_METHOD_FUNC(&ARC_Data::rb_load), 1);
	}

	/****************************************************************************************
	 * Utility Load/Dump Methods
	 ****************************************************************************************/

	void ARC_Data::_resetSerializer()
	{
		if (file.is_open())
		{
			file.close();
		}
		strings.clear();
		strings += Qnil;
		arrays.clear();
		arrays += Qnil;
		hashes.clear();
		hashes += Qnil;
		objects.clear();
		objects += Qnil;
	}

	VALUE ARC_Data::__get_class_object(hstr class_path)
	{
		harray<hstr> classes = class_path.split("::");
		VALUE symbol = rb_f_to_sym(rb_str_new2(classes[0].c_str()));
		if (!RTEST(rb_funcall_1(rb_mKernel, "const_defined?", symbol)))
		{
			rb_raise(rb_eARC_Error, ("Class not defined " + classes[0]).c_str());
		}
		classes.pop(0);
		VALUE classe = rb_funcall_1(rb_mKernel, "const_get", symbol);
		foreach (hstr, it, classes)
		{
			symbol = rb_f_to_sym(rb_str_new2((*it).c_str()));
			if (!RTEST(rb_funcall_1(classe, "const_defined?", symbol)))
			{
				rb_raise(rb_eARC_Error, ("Class not defined " + (*it)).c_str());
			}
			classe = rb_funcall_1(classe, "const_get", symbol);
		}
		return classe;
	}

	bool ARC_Data::__try_map(harray<VALUE>& data, VALUE obj)
	{
		int index = data.index_of(obj);
		if (index < 0)
		{
			__DUMP_INT32(data.size());
			data += obj;
			return true;
		}
		__DUMP_INT32(index);
		return false;
	}

	VALUE ARC_Data::__safe_dump(VALUE obj)
	{
		ARC_Data::_dump(obj);
		return Qnil;
	}

	VALUE ARC_Data::__safe_load(VALUE ignored)
	{
		return ARC_Data::_load();
	}

	void ARC_Data::_dump(VALUE obj)
	{
		if (rb_obj_is_instance_of(obj, rb_cNilClass)) return ARC_Data::_dump_nil(obj);
		if (rb_obj_is_instance_of(obj, rb_cFalseClass)) return ARC_Data::_dump_false(obj);
		if (rb_obj_is_instance_of(obj, rb_cTrueClass)) return ARC_Data::_dump_true(obj);
		if (rb_obj_is_instance_of(obj, rb_cFixnum)) return ARC_Data::_dump_fixnum(obj);
		if (rb_obj_is_instance_of(obj, rb_cBignum)) return ARC_Data::_dump_bignum(obj);
		if (rb_obj_is_instance_of(obj, rb_cFloat)) return ARC_Data::_dump_float(obj);
		if (rb_obj_is_instance_of(obj, rb_cString)) return ARC_Data::_dump_string(obj);
		if (rb_obj_is_instance_of(obj, rb_cArray)) return ARC_Data::_dump_array(obj);
		if (rb_obj_is_instance_of(obj, rb_cHash)) return ARC_Data::_dump_hash(obj);
		if (rb_obj_is_instance_of(obj, rb_cObject)) return ARC_Data::_dump_object(obj);
		VALUE class_name = rb_class_name(obj);
		rb_raise(rb_eARC_Error, hsprintf("Error: %s cannot be dumped!", StringValueCStr(class_name)).c_str());
	}
		
	VALUE ARC_Data::_load()
	{
		unsigned char type = file.load_uchar();
		if (type == Types[rb_cNilClass]) return ARC_Data::_load_nil();
		if (type == Types[rb_cFalseClass]) return ARC_Data::_load_false();
		if (type == Types[rb_cTrueClass]) return ARC_Data::_load_true();
		if (type == Types[rb_cFixnum]) return ARC_Data::_load_fixnum();
		if (type == Types[rb_cBignum]) return ARC_Data::_load_bignum();
		if (type == Types[rb_cFloat]) return ARC_Data::_load_float();
		if (type == Types[rb_cString]) return ARC_Data::_load_string();
		if (type == Types[rb_cArray]) return ARC_Data::_load_array();
		if (type == Types[rb_cHash]) return ARC_Data::_load_hash();
		if (type == Types[rb_cObject]) return ARC_Data::_load_object();
		rb_raise(rb_eARC_Error, hsprintf("Error: Unknown type 0x%02X detected!", type).c_str());
		return Qnil;
	}

	void ARC_Data::_dump_nil(VALUE obj)
	{
		file.dump(Types[rb_cNilClass]);
	}

	void ARC_Data::_dump_false(VALUE obj)
	{
		file.dump(Types[rb_cFalseClass]);
	}

	void ARC_Data::_dump_true(VALUE obj)
	{
		file.dump(Types[rb_cTrueClass]);
	}
		
	void ARC_Data::_dump_fixnum(VALUE obj)
	{
		file.dump(Types[rb_cFixnum]);
		__DUMP_INT32(NUM2INT(obj));
	}
		
	void ARC_Data::_dump_bignum(VALUE obj)
	{
		file.dump(Types[rb_cBignum]);
		__DUMP_INT32(NUM2INT(obj)); // the C++ implementation uses a "long" of 32 bit
	}
		
	void ARC_Data::_dump_float(VALUE obj)
	{
		file.dump(Types[rb_cFloat]);
		file.dump((float)NUM2DBL(obj));
	}
		
	void ARC_Data::_dump_string(VALUE obj)
	{
		file.dump(Types[rb_cString]);
		int size = NUM2INT(rb_str_size(obj));
		if (size > 0)
		{
			if (ARC_Data::__try_map(strings, obj))
			{
				file.dump(hstr(StringValueCStr(obj)));
			}
		}
		else
		{
			__DUMP_INT32(0);
		}
	}
		
	void ARC_Data::_dump_array(VALUE obj)
	{
		file.dump(Types[rb_cArray]);
		int size = NUM2INT(rb_ary_size(obj));
		if (size > 0)
		{
			if (ARC_Data::__try_map(arrays, obj))
			{
				__DUMP_INT32(size);
				rb_ary_each_index(obj, i)
				{
					ARC_Data::_dump(rb_ary_entry(obj, i));
				}
			}
		}
		else
		{
			__DUMP_INT32(0);
		}
	}
		
	void ARC_Data::_dump_hash(VALUE obj)
	{
		file.dump(Types[rb_cHash]);
		int size = NUM2INT(rb_hash_size(obj));
		if (size > 0)
		{
			if (ARC_Data::__try_map(hashes, obj))
			{
				__DUMP_INT32(size);
				VALUE keys = rb_funcall_0(obj, "keys");
				VALUE key;
				rb_ary_each_index(keys, i)
				{
					key = rb_ary_entry(keys, i);
					ARC_Data::_dump(key);
					ARC_Data::_dump(rb_hash_aref(obj, key));
				}
			}
		}
		else
		{
			__DUMP_INT32(0);
		}
	}
		
	void ARC_Data::_dump_object(VALUE obj)
	{
		file.dump(Types[rb_cObject]);
		// first the string path because this is required to load the object
		VALUE class_name = rb_class_name(obj);
		file.dump(hstr(StringValueCStr(class_name)));
		if (ARC_Data::__try_map(objects, obj))
		{
			if (RTEST(rb_funcall_1(obj, "respond_to?", rb_str_new2("_arc_dump"))))
			{
				VALUE data = rb_funcall_0(obj, "_arc_dump");
				int size = NUM2INT(rb_str_size(data));
				__DUMP_INT32(size);
				unsigned char* raw_data = (unsigned char*)StringValueCStr(data);
				file.write_raw(raw_data, size);
			}
			else
			{
				VALUE variables = rb_funcall_0(obj, "instance_variables");
				int size = NUM2INT(rb_ary_size(variables));
				__DUMP_INT32(size);
				VALUE variable;
				rb_ary_each_index(variables, i)
				{
					variable = rb_ary_entry(variables, i);
					ARC_Data::_dump_string(rb_funcall_2(rb_f_to_s(variable), "gsub", rb_str_new2("@"), rb_str_new2("")));
					ARC_Data::_dump(rb_funcall_1(obj, "instance_variable_get", variable));
				}
			}
		}
	}

	VALUE ARC_Data::_load_nil()
	{
		return Qnil;
	}

	VALUE ARC_Data::_load_false()
	{
		return Qfalse;
	}

	VALUE ARC_Data::_load_true()
	{
		return Qtrue;
	}
		
	VALUE ARC_Data::_load_fixnum()
	{
		return INT2FIX(__LOAD_INT32);
	}
		
	VALUE ARC_Data::_load_bignum()
	{
		return INT2FIX(__LOAD_INT32); // the C++ implementation uses a "long" of 32 bit
	}
		
	VALUE ARC_Data::_load_float()
	{
		return rb_float_new((double)file.load_float());
	}
	
	VALUE ARC_Data::_load_string()
	{
		int id = __LOAD_INT32;
		if (id == 0)
		{
			return rb_str_new2("");
		}
		VALUE obj = __FIND_MAPPED(strings, id);
		if (!NIL_P(obj))
		{
			return rb_str_new2(StringValueCStr(obj));
		}
		hstr value = file.load_hstr();
		obj = rb_str_new2(value.c_str());
		__MAP(strings, obj);
		return obj;
	}
		
	VALUE ARC_Data::_load_array()
	{
		int id = __LOAD_INT32;
		if (id == 0)
		{
			return rb_ary_new();
		}
		VALUE obj = __FIND_MAPPED(arrays, id);
		if (!NIL_P(obj))
		{
			return obj;
		}
		int size = __LOAD_INT32;
		obj = rb_ary_new();
		__MAP(arrays, obj);
		for_iter (i, 0, size)
		{
			rb_ary_push(obj, ARC_Data::_load());
		}
		return obj;
	}
		
	VALUE ARC_Data::_load_hash()
	{
		int id = __LOAD_INT32;
		if (id == 0)
		{
			return rb_hash_new();
		}
		VALUE obj = __FIND_MAPPED(hashes, id);
		if (!NIL_P(obj))
		{
			return obj;
		}
		int size = __LOAD_INT32;
		obj = rb_hash_new();
		__MAP(hashes, obj);
		VALUE key;
		for_iter (i, 0, size)
		{
			key = ARC_Data::_load(); // making sure key is always loaded first
			rb_hash_aset(obj, key, ARC_Data::_load());
		}
		return obj;
	}
		
	VALUE ARC_Data::_load_object()
	{
		VALUE class_path = ARC_Data::_load();
		int id = __LOAD_INT32;
		VALUE obj = __FIND_MAPPED(objects, id);
		if (!NIL_P(obj))
		{
			return obj;
		}
		VALUE classe = ARC_Data::__get_class_object(hstr(StringValueCStr(class_path)));
		int size = __LOAD_INT32;
		if (rb_funcall_1(classe, "respond_to?", rb_str_new2("_arc_load")))
		{
			unsigned char* data = new unsigned char[size];
			file.read_raw(data, size);
			obj = rb_funcall_1(classe, "_arc_load", rb_str_new((const char*)data, size));
			__MAP(objects, obj);
			delete data;
			return obj;
		}
		obj = rb_funcall_0(classe, "allocate");
		__MAP(objects, obj);
		VALUE variable;
		VALUE symbol;
		VALUE value;
		for_iter (i, 0, size)
		{
			variable = ARC_Data::_load();
			symbol = rb_f_to_sym(rb_str_new2(("@" + hstr(StringValueCStr(variable))).c_str()));
			value = ARC_Data::_load();
			rb_funcall_2(obj, "instance_variable_set", symbol, value);
		}
		return obj;
	}
		
	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE ARC_Data::rb_dump(VALUE self, VALUE filename, VALUE obj)
	{
		try
		{
			file.open(StringValueCStr(filename));
		}
		catch (hltypes::_file_not_found e)
		{
			RB_RAISE_FILE_NOT_FOUND(StringValueCStr(filename));
		}
		rb_funcall_0(rb_mGC, "disable"); // to prevent GC destroying temp data
		file.dump((unsigned char)Header[0]);
		file.dump((unsigned char)Header[1]);
		file.dump((unsigned char)Header[2]);
		file.dump((unsigned char)Header[3]);
		harray<unsigned char> versions = Version.split(".").cast<int>().cast<unsigned char>();
		file.dump(versions[0]);
		file.dump(versions[1]);
		int exception;
		rb_protect(&ARC_Data::__safe_dump, obj, &exception);
		ARC_Data::_resetSerializer();
		rb_funcall_0(rb_mGC, "enable");
		if (exception != 0)
		{
			rb_jump_tag(exception);
		}
		return Qnil;
	}

	VALUE ARC_Data::rb_load(VALUE self, VALUE filename)
	{
		try
		{
			file.open(StringValueCStr(filename));
		}
		catch (hltypes::_file_not_found e)
		{
			RB_RAISE_FILE_NOT_FOUND(StringValueCStr(filename));
		}
		rb_funcall_0(rb_mGC, "disable"); // to prevent GC destroying temp data
		bool failed = (file.size() < 4);
		char chars[5] = {'\0'};
		hstr header;
		if (!failed)
		{
			chars[0] = (char)file.load_uchar();
			chars[1] = (char)file.load_uchar();
			chars[2] = (char)file.load_uchar();
			chars[3] = (char)file.load_uchar();
			header = hstr(chars);
			failed = (Header != header);
		}
		if (failed)
		{
			ARC_Data::_resetSerializer();
			rb_funcall_0(rb_mGC, "enable");
			rb_raise(rb_eARC_Error, hsprintf("Error: ARC::Data header mismatch! Excepted: \"ARCD\" Found: \"%s\"",
				Header.c_str(), header.c_str()).c_str());
			return Qnil;
		}
		failed = (file.size() < 6);
		unsigned char major;
		unsigned char minor;
		hstr version;
		if (!failed)
		{
			major = file.load_uchar();
			minor = file.load_uchar();
			version = hstr((int)major) + "." + hstr((int)minor);
			failed = (Version != version);
		}
		if (failed)
		{
			ARC_Data::_resetSerializer();
			rb_funcall_0(rb_mGC, "enable");
			rb_raise(rb_eARC_Error, hsprintf("Error: ARC::Data version mismatch! Excepted: \"%s\" Found: \"%s\"",
				Version.c_str(), version.c_str()).c_str());
			return Qnil;
		}
		int exception;
		VALUE data = rb_protect(&ARC_Data::__safe_load, Qnil, &exception);
		ARC_Data::_resetSerializer();
		rb_funcall_0(rb_mGC, "enable");
		if (exception != 0)
		{
			rb_jump_tag(exception);
			return Qnil;
		}
		return data;
	}

}
