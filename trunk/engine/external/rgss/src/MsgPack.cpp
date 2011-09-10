#include <ruby.h>

#include <hltypes/harray.h>
#include <hltypes/util.h>

#include "MsgPack.h"
#include "CodeSnippets.h"

namespace rgss
{
	VALUE MsgPack::io;
	hmap<VALUE, VALUE> MsgPack::symbols;
	hmap<VALUE, VALUE> MsgPack::strings;
	hmap<VALUE, VALUE> MsgPack::ids;
	harray<VALUE> MsgPack::stack;
	hmap<VALUE, VALUE> MsgPack::finaldump;
	int MsgPack::sym_count;
	harray<VALUE> MsgPack::pending_objects;
	harray<VALUE> MsgPack::post_load_objects;

	unsigned char* MsgPack::stream;

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	VALUE rb_mMsgPack;

	void MsgPack::init()
	{
		io = Qnil;
		sym_count = 0;
	}

	void MsgPack::destroy()
	{
		// not being called at all
	}

	void MsgPack::createRubyInterface()
	{
		rb_mMsgPack = rb_define_module("MsgPack");
		rb_define_module_function(rb_mMsgPack, "dump", RUBY_METHOD_FUNC(&MsgPack::rb_dump), 2);
		rb_define_module_function(rb_mMsgPack, "load", RUBY_METHOD_FUNC(&MsgPack::rb_load), 1);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE MsgPack::rb_dump(VALUE self, VALUE stream, VALUE object)
	{
		io = stream;
		MsgPack::_queue_dump_object(object);
		MsgPack::_start_dump();
		MsgPack::_write_dump();
		MsgPack::_reset();
		return Qnil;
	}

	VALUE MsgPack::rb_load(VALUE self, VALUE stream)
	{
		io = stream;
		MsgPack::_build_object_table();
		MsgPack::_link_objects();
		MsgPack::_call_arc_post_load();
		VALUE object = symbols[0];
		int codeValue = rb_ary_entry(object, 0);
		int code = NUM2INT(codeValue);
		VALUE return_obj;
		if (is_between(code, 0, 4)) // False, True, Nil, String, Numeric
		{
			return_obj = rb_ary_entry(object, 1);
		}
		else if (is_between(code, 5, 7)) // Array, Hash, Class
		{
			return_obj = rb_ary_entry(rb_ary_entry(object, 1), 0);
		}
		else
		{
			return_obj = Qnil;
		}
		MsgPack::_reset();
		return return_obj;
	}

	void MsgPack::_build_object_table()
	{
		VALUE load_string = rb_funcall_0(io, "read");
		unsigned char* data = (unsigned char*)StringValuePtr(load_string);
		VALUE values = MsgPack::_unpack(data);
		VALUE keys = rb_funcall_0(values, "keys");
		hmap<VALUE, VALUE> objects;
		VALUE key;
		rb_ary_each_index (keys, i)
		{
			key = rb_ary_entry(keys, i);
			objects[key] = rb_hash_aref(values, key);
		}
		int type;
		VALUE pair;
		foreach_map (VALUE, VALUE, it, objects)
		{
			symbols[it->first] = it->second;
			type = NUM2INT(rb_ary_entry(it->second, 0));
			if (is_between(type, 0, 4)) // False, True, Nil, String, Numeric
			{
				continue;
			}
			else if (is_between(type, 5, 6)) // Array, Hash
			{
				if (NUM2INT(rb_ary_size(rb_ary_entry(it->second, 1))) > 0)
				{
					pending_objects += it->first;
				}
			}
			else if (type == 7) // Class
			{
				VALUE pair = rb_ary_entry(it->second, 1);
				VALUE class_path = rb_ary_entry(pair, 0);
				hstr class_name = StringValuePtr(class_path);
				harray<hstr> classes = class_name.split("::");
				class_name = classes.pop(0);
				VALUE class_symbol = rb_f_to_sym(rb_str_new2(class_name.c_str()));
				if (!RTEST(rb_funcall_1(rb_mKernel, "const_defined?", class_symbol)))
				{
					rb_raise(rb_eTypeError, "Class not defined: %s", class_name.c_str());
				}
				VALUE classe = rb_funcall_1(rb_mKernel, "const_get", class_symbol);
				foreach (hstr, it, classes)
				{
					class_symbol = rb_f_to_sym(rb_str_new2((*it).c_str()));
					classe = rb_funcall_1(classe, "const_get", class_symbol);
				}
				VALUE class_obj = rb_funcall_0(classe, "allocate");
				rb_ary_store(pair, 0, class_obj);
				pending_objects += it->first;
			}
			else
			{
				VALUE str = rb_f_inspect(it->second);
				rb_raise(rb_eTypeError, ("Unrecognized object declaration: " + hstr(StringValuePtr(str))).c_str());
			}
		}
	}
	
	void MsgPack::_link_objects()
	{
		VALUE obj;
		VALUE subobj;
		VALUE new_obj;
		VALUE entry;
		VALUE items;
		VALUE name;
		VALUE key;
		VALUE value;
		VALUE _at_str = rb_str_new2("@");
		VALUE args[2] = {Qnil, Qnil};
		int type;
		foreach (VALUE, it, pending_objects)
		{
			obj = symbols[*it];
			type = NUM2INT(rb_ary_entry(obj, 0));
			subobj = rb_ary_entry(obj, 1);
			switch (type)
			{
			case 5:
				new_obj = rb_ary_entry(subobj, 0);
				items = rb_ary_entry(subobj, 1);
				rb_ary_each_index (items, i)
				{
					type = NUM2INT(rb_ary_entry(rb_ary_entry(items, i), 0));
					entry = rb_ary_entry(rb_ary_entry(items, i), 1);
					switch (type)
					{
					case 0: // actual object
						value = entry;
						break;
					case 1: // link to array, hash or user object
						value = rb_ary_entry(rb_ary_entry(symbols[entry], 1), 0);
						break;
					case 2: // string
						value = rb_ary_entry(symbols[entry], 1);
						break;
					}
					rb_ary_push(new_obj, value);
				}
				break;
			case 6:
				new_obj = rb_ary_entry(subobj, 0);
				items = rb_ary_entry(subobj, 1);
				rb_ary_each_index (items, i)
				{
					type = NUM2INT(rb_ary_entry(rb_ary_entry(rb_ary_entry(items, i), 0), 0));
					entry = rb_ary_entry(rb_ary_entry(rb_ary_entry(items, i), 0), 1);
					switch (type)
					{
					case 0:
						key = entry;
						break;
					case 1:
						key = rb_ary_entry(rb_ary_entry(symbols[entry], 1), 0);
						break;
					case 2:
						key = rb_ary_entry(symbols[entry], 1);
						break;
					}
					type = rb_ary_entry(rb_ary_entry(rb_ary_entry(items, i), 1), 0);
					entry = rb_ary_entry(rb_ary_entry(rb_ary_entry(items, i), 1), 1);
					switch (type)
					{
					case 0:
						value = entry;
						break;
					case 1:
						value = rb_ary_entry(rb_ary_entry(symbols[entry], 1), 0);
						break;
					case 2:
						value = rb_ary_entry(symbols[entry], 1);
						break;
					}
					rb_hash_aset(new_obj, key, value);
				}
				break;
			case 7:
				new_obj = rb_ary_entry(subobj, 0);
				items = rb_ary_entry(subobj, 1);
				if (rb_respond_to(new_obj, rb_intern("_arc_load")))
				{
					rb_funcall_1(new_obj, "_arc_load", items);
				}
				else
				{
					rb_ary_each_index(items, i)
					{
						name = rb_ary_entry(rb_ary_entry(items, i), 0);
						type = NUM2INT(rb_ary_entry(rb_ary_entry(rb_ary_entry(items, i), 1), 0));
						entry = rb_ary_entry(rb_ary_entry(rb_ary_entry(items, i), 1), 1);
						switch (type)
						{
						case 0:
							value = entry;
							break;
						case 1:
							value = rb_ary_entry(rb_ary_entry(symbols[entry], 1), 0);
							break;
						case 2:
							value = rb_ary_entry(symbols[entry], 1);
							break;
						}
						args[0] = rb_f_to_sym(rb_str_concat(_at_str, rb_funcall_0(name, "strip")));
						args[1] = value;
						rb_funcall_x(new_obj, "instance_variable_set", 2, args);
					}
				}
				if (rb_respond_to(new_obj, rb_intern("_post_arc_load")))
				{
					post_load_objects += new_obj;
				}
				break;
			}
    	}
	}

	void MsgPack::_call_arc_post_load()
	{
		foreach (VALUE, it, post_load_objects)
		{
			rb_funcall_0((*it), "_post_arc_load");
		}
	}

	void MsgPack::_reset()
	{
		io = Qnil;
		symbols.clear();
		strings.clear();
		ids.clear();
		stack.clear();
		finaldump.clear();
		sym_count = 0;
		pending_objects.clear();
	}

	void MsgPack::_start_dump()
	{
		while (stack.size() > 0)
		{
			MsgPack::_dump_object(stack.pop(0));
		}
	}
  
	void MsgPack::_write_dump()
	{
		return;

		/*
		msgpack::sbuffer buffer;
		msgpack::pack(buffer, (std::map<VALUE, VALUE>)finaldump);
		*/
		/*
		VALUE map = rb_hash_new();
		foreach_map (VALUE, VALUE, it, finaldump)
		{
			rb_hash_aset(map, it->first, it->second);
		}
		*/
		/*
		VALUE MessagePack = rb_intern("MessagePack");
		rb_funcall(MessagePack, "pack", 
		*/
		//VALUE dump_string = rb_funcall_0(map, "to_msgpack");
		//VALUE dump_string = rb_str_new2(buffer.data());
		//rb_funcall_1(io, "write", dump_string);
	}

	VALUE MsgPack::_queue_dump_object(VALUE obj)
	{
		VALUE result;
		if (rb_obj_is_instance_of(obj, rb_cFalseClass))
		{
			result = MsgPack::_dump_false_object(obj);
		}
		else if (rb_obj_is_instance_of(obj, rb_cTrueClass))
		{
			result = MsgPack::_dump_true_object(obj);
		}
		else if (rb_obj_is_instance_of(obj, rb_cNilClass))
		{
			result = MsgPack::_dump_nil_object(obj);
		}
		else if (rb_obj_is_instance_of(obj, rb_cNumeric))
		{
			result = MsgPack::_dump_numeric_object(obj);
		}
		else if (rb_obj_is_instance_of(obj, rb_cString))
		{
			result = MsgPack::_dump_string_object(obj);
		}
		else if (rb_obj_is_instance_of(obj, rb_cFalseClass))
		{
			result = MsgPack::_queue_dump_array_object(obj);
		}
		else if (rb_obj_is_instance_of(obj, rb_cFalseClass))
		{
			result = MsgPack::_queue_dump_hash_object(obj);
		}
		else
		{
			result = MsgPack::_queue_dump_nonstandard_object(obj);
		}
		return result;
	}
  
	void MsgPack::_dump_object(VALUE obj)
	{
		if (rb_obj_is_instance_of(obj, rb_cArray))
		{
			MsgPack::_dump_array_object(obj);
		}
		else if (rb_obj_is_instance_of(obj, rb_cHash))
		{
			MsgPack::_dump_hash_object(obj);
		}
		else
		{
			MsgPack::_dump_nonstandard_object(obj);
		}
	}

	VALUE MsgPack::_dump_true_object(VALUE obj)
	{
		return rb_ary_new3(2, INT2FIX(0), obj);
	}
  
	VALUE MsgPack::_dump_false_object(VALUE obj)
	{
		return rb_ary_new3(2, INT2FIX(0), obj);
	}
  
	VALUE MsgPack::_dump_nil_object(VALUE obj)
	{
		return rb_ary_new3(2, INT2FIX(0), obj);
	}
  
	VALUE MsgPack::_dump_numeric_object(VALUE obj)
	{
		return rb_ary_new3(2, INT2FIX(0), obj);
	}

	VALUE MsgPack::_dump_string_object(VALUE obj)
	{
		if (strings.has_key(obj))
		{
			strings[obj] = rb_f_object_id(obj);
			VALUE dump_array = MsgPack::_enter_obj(obj);
			rb_ary_store(dump_array, 0, INT2FIX(4));
			rb_ary_store(dump_array, 1, obj);
		}
	    return rb_ary_new3(2, INT2FIX(2), ids[strings[obj]]);
	}

	VALUE MsgPack::_queue_dump_array_object(VALUE obj)
	{
		VALUE object_id = rb_f_object_id(obj);
		if (symbols.has_key(object_id))
		{
			stack += obj;
			VALUE dump_array = MsgPack::_enter_obj(obj);
			rb_ary_store(dump_array, 0, INT2FIX(5));
			rb_ary_store(dump_array, 1, rb_ary_new3(2, rb_ary_new(), rb_ary_new()));
		}
	    return rb_ary_new3(2, INT2FIX(1), ids[object_id]);
	}

	void MsgPack::_dump_array_object(VALUE obj)
	{
		VALUE dump_array = rb_ary_entry(symbols[rb_f_object_id(obj)], 1);
		VALUE ary;
		rb_ary_each_index (obj, i)
		{
			ary = rb_ary_entry(rb_ary_entry(dump_array, 1), 1);
			rb_ary_push(ary, MsgPack::_queue_dump_object(rb_ary_entry(obj, i)));
		}
    }
  
	VALUE MsgPack::_queue_dump_hash_object(VALUE obj)
	{
		VALUE object_id = rb_f_object_id(obj);
		if (symbols.has_key(object_id))
		{
			stack += obj;
			VALUE dump_array = MsgPack::_enter_obj(obj);
			rb_ary_store(dump_array, 0, INT2FIX(6));
			rb_ary_store(dump_array, 1, rb_ary_new3(2, rb_hash_new(), rb_ary_new()));
		}
	    return rb_ary_new3(2, INT2FIX(1), ids[object_id]);
	}
 
	void MsgPack::_dump_hash_object(VALUE obj)
	{
		VALUE dump_array = rb_ary_entry(symbols[rb_f_object_id(obj)], 1);
		VALUE keys = NUM2INT(rb_funcall_0(obj, "keys"));
		VALUE ary;
		VALUE key;
		VALUE value;
		rb_ary_each_index (keys, i)
		{
			key = rb_ary_entry(keys, i);
			value = rb_hash_aref(obj, key);
			ary = rb_ary_entry(rb_ary_entry(dump_array, 1), 1);
			rb_ary_push(ary, rb_ary_new3(2, MsgPack::_queue_dump_object(key), MsgPack::_queue_dump_object(value)));
		}
    }
  
	VALUE MsgPack::_queue_dump_nonstandard_object(VALUE obj)
	{
		VALUE object_id = rb_f_object_id(obj);
		if (symbols.has_key(object_id))
		{
			stack += obj;
			VALUE dump_array = MsgPack::_enter_obj(obj);
			VALUE klass_path = rb_f_to_s(rb_class_of(obj));
			rb_ary_store(dump_array, 0, INT2FIX(7));
			rb_ary_store(dump_array, 1, rb_ary_new3(2, klass_path, rb_ary_new()));
		}
		return rb_ary_new3(2, INT2FIX(2), ids[object_id]);
	}

	void MsgPack::_dump_nonstandard_object(VALUE obj)
	{
		VALUE dump_array = rb_ary_entry(symbols[rb_f_object_id(obj)], 1);
		if (rb_respond_to(obj, rb_intern("_prep_arc_dump")))
		{
			rb_funcall_0(obj, "_prep_arc_dump");
		}
		if (rb_respond_to(obj, rb_intern("_arc_dump")))
		{
			rb_ary_store(rb_ary_entry(dump_array, 1), 1, rb_funcall_0(obj, "_arc_dump"));
		}
		else
		{
			VALUE excludes = rb_ary_new();
			if (rb_respond_to(obj, rb_intern("_arc_exclude")))
			{
				excludes = rb_funcall_0(obj, "_arc_exclude");
			}
			VALUE instance_variables = rb_funcall_0(obj, "instance_variables");
			VALUE subs[2] = {rb_str_new2("@"), rb_str_new2("")};
			VALUE name;
			VALUE variable;
			VALUE ary;
			VALUE value;
			rb_ary_each_index (instance_variables, i)
			{
				variable = rb_ary_entry(instance_variables, i);
				name = rb_funcall_x(rb_f_to_s(variable), "gsub", 2, subs);
				if (!RTEST(rb_funcall_1(excludes, "include?", name)))
				{
					value = rb_funcall_1(obj, "instance_variable_get", &variable);
					ary = rb_ary_entry(rb_ary_entry(dump_array, 1), 1);
					rb_ary_push(ary, rb_ary_new3(2, name, MsgPack::_queue_dump_object(value)));
				}
			}
		}
	}
	
 	VALUE MsgPack::_enter_obj(VALUE obj)
	{
		VALUE key = rb_f_object_id(obj);
		VALUE dump_array = rb_ary_new3(2, Qnil, Qnil);
		symbols[key] = rb_ary_new3(2, obj, dump_array);
		ids[key] = sym_count;
		finaldump[sym_count] = dump_array;
		sym_count++;
		return dump_array;
	}
	
}
