#include <ruby.h>

#include <hltypes/harray.h>
#include <hltypes/hfile.h>
#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "ARC.h"
#include "ARC_Data.h"
#include "ARC_Error.h"
#include "CodeSnippets.h"

namespace zer0
{
	VALUE rb_mARC_Data;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

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
			if (!RTEST(rb_funcall_1(classe, "const_defined", symbol)))
			{
				rb_raise(rb_eARC_Error, ("Class not defined " + (*it)).c_str());
			}
			classe = rb_funcall_1(classe, "const_get", symbol);
		}
		return classe;
	}

	bool ARC_Data::__try_map(harray<VALUE> data, VALUE obj)
	{
		int index = data.index_of(obj);
		if (index < 0)
		{
			ARC_Data::__dump_int32(data.size());
			data += obj;
			return true;
		}
		ARC_Data::__dump_int32(index);
		return false;
	}

	void ARC_Data::__map(harray<VALUE> data, VALUE obj)
	{
		data += obj;
	}

	VALUE ARC_Data::__find_mapped(harray<VALUE> data, int id)
	{
		return (id < data.size() ? data[id] : Qnil);
	}
	
	void ARC_Data::__dump_int32(int obj)
	{
		file.dump(NUM2INT(obj));
	}

	int ARC_Data::__load_int32()
	{
		return INT2FIX(file.load_int());
	}

	void ARC_Data::_dump(VALUE obj)
	{
		/*
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
		*/
		VALUE class_name = rb_class_name(obj);
		rb_raise(rb_eARC_Error, hsprintf("Error: %s cannot be dumped!", StringValuePtr(class_name)).c_str());
	}
		
	VALUE ARC_Data::_load()
	{
		unsigned char type = file.load_uchar();
		/*
		switch (type)
		{
		case Types[rb_cNilClass]: return ARC_Data::_load_nil();
		case Types[rb_cFalseClass]: return ARC_Data::_load_false();
		case Types[rb_cTrueClass]: return ARC_Data::_load_true();
		case Types[rb_cFixnum]: return ARC_Data::_load_fixnum();
		case Types[rb_cBignum]: return ARC_Data::_load_bignum();
		case Types[rb_cFloat]: return ARC_Data::_load_float();
		case Types[rb_cString]: return ARC_Data::_load_string();
		case Types[rb_cArray]: return ARC_Data::_load_array();
		case Types[rb_cHash]: return ARC_Data::_load_hash();
		case Types[rb_cObject]: return ARC_Data::_load_object();
		}
		*/
		rb_raise(rb_eARC_Error, hsprintf("Error: Unknown type 0x%02X detected!", type).c_str());
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE ARC_Data::rb_dump(VALUE self, VALUE filename, VALUE obj)
	{
		file.open(StringValuePtr(filename));
		harray<hstr> versions = Version.split(".");
		file.dump((unsigned char)(int)versions[0]);
		file.dump((unsigned char)(int)versions[1]);
		ARC_Data::_dump(obj);
		ARC_Data::_resetSerializer();
		return Qnil;
	}

	VALUE ARC_Data::rb_load(VALUE self, VALUE filename)
	{
		file.open(StringValuePtr(filename));
		unsigned major = file.load_uchar();
		unsigned minor = file.load_uchar();
		hstr version = hstr((int)major) + "." + hstr((int)minor);
		if (Version != version)
		{
			rb_raise(rb_eARC_Error, hsprintf("Error: ARC::Data version mismatch! Excepted: %s Found: %s",
				Version.c_str(), version.c_str()).c_str());
		}
		VALUE data = ARC_Data::_load();
		ARC_Data::_resetSerializer();
		return data;
	}

}
