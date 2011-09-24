#include <ruby.h>

#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "RGSSError.h"
#include "Table.h"

namespace rgss
{
	VALUE rb_cTable;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	short Table::getData(int x, int y, int z)
	{
		x = hclamp(x, 0, this->xSize - 1);
		y = hclamp(y, 0, this->ySize - 1);
		z = hclamp(z, 0, this->zSize - 1);
		return this->data[x + this->xSize * (y + this->ySize * z)];
	}

	short Table::getCircularData(int x, int y, int z)
	{
		x %= this->xSize;
		y %= this->ySize;
		z = hclamp(z, 0, this->zSize - 1);
		return this->data[x + this->xSize * (y + this->ySize * z)];
	}

	void Table::_resize(int xSize)
	{
		this->_resize(xSize, 1, 1);
		this->dimensions = 1;
	}
	
	void Table::_resize(int xSize, int ySize)
	{
		this->_resize(xSize, ySize, 1);
		this->dimensions = 2;
	}
	
	void Table::_resize(int xSize, int ySize, int zSize)
	{
		int oldXSize = this->xSize;
		int oldYSize = this->ySize;
		int copyXSize = hmin(this->xSize, xSize);
		int copyYSize = hmin(this->ySize, ySize);
		int copyZSize = hmin(this->zSize, zSize);
		// make sure xSize isn't <= 0 and none of the sizes are negative
		// store table sizes
		this->xSize = hmax(xSize, 1);
		this->ySize = hmax(ySize, 1);
		this->zSize = hmax(zSize, 1);
		// allocate space for the table
		short* newData = this->_createData(this->xSize, this->ySize, this->zSize);

		// copy the data from the old table, as much as fits
		for_iter (x, 0, copyXSize)
		{
			for_iter (y, 0, copyYSize)
			{
				for_iter (z, 0, copyZSize)
				{
					newData[x + this->xSize * (y + this->ySize * z)] =
						this->data[x + oldXSize * (y + oldYSize * z)];
				}
			}
		}
		// delete the old array
		delete [] this->data;
		// set the new data
		this->data = newData;
		this->dimensions = 3;
	}
	
	short* Table::_createData(int xSize, int ySize, int zSize) const
	{
		// allocate table space filled with 0
		int size = xSize * ySize * zSize;
		short* data = new short[size];
		memset(data, 0, size * sizeof(short));
		return data;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Table::init()
	{
	}

	void Table::destroy()
	{
	}

	void Table::createRubyInterface()
	{
		rb_cTable = rb_define_class("Table", rb_cObject);
		rb_define_alloc_func(rb_cTable, &Table::rb_new);
		// initialize
		rb_define_method(rb_cTable, "initialize", RUBY_METHOD_FUNC(&Table::rb_initialize), -1);
		rb_define_method(rb_cTable, "initialize_copy", RUBY_METHOD_FUNC(&Table::rb_initialize_copy), 1);
		rb_define_method(rb_cTable, "_dump", RUBY_METHOD_FUNC(&Table::rb_dump), -1);
		rb_define_singleton_method(rb_cTable, "_load", RUBY_METHOD_FUNC(&Table::rb_load), 1);
		rb_define_method(rb_cTable, "_arc_dump", RUBY_METHOD_FUNC(&Table::rb_arcDump), 0);
		rb_define_singleton_method(rb_cTable, "_arc_load", RUBY_METHOD_FUNC(&Table::rb_arcLoad), 1);
		// getters and setters
		rb_define_method(rb_cTable, "xsize", RUBY_METHOD_FUNC(&Table::rb_getXSize), 0);
		rb_define_method(rb_cTable, "ysize", RUBY_METHOD_FUNC(&Table::rb_getYSize), 0);
		rb_define_method(rb_cTable, "zsize", RUBY_METHOD_FUNC(&Table::rb_getZSize), 0);
		rb_define_method(rb_cTable, "[]", RUBY_METHOD_FUNC(&Table::rb_getData), -1);
		rb_define_method(rb_cTable, "[]=", RUBY_METHOD_FUNC(&Table::rb_setData), -1);
		// all other methods
		rb_define_method(rb_cTable, "resize", RUBY_METHOD_FUNC(&Table::rb_resize), -1);
	}
	
	void Table::gc_free(Table* table)
	{
		if (table->data != NULL)
		{
			delete [] table->data;
			table->data = NULL;
		}
	}

	VALUE Table::rb_new(VALUE classe)
	{
		Table* table;
		return Data_Make_Struct(classe, Table, NULL, &Table::gc_free, table);
	}

	VALUE Table::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Table, table);
		VALUE arg1, arg2, arg3;
		rb_scan_args(argc, argv, "12", &arg1, &arg2, &arg3);
		table->xSize = hmax(NUM2INT(arg1), 1);
		table->ySize = hmax(NIL_P(arg2) ? 1 : NUM2INT(arg2), 1);
		table->zSize = hmax(NIL_P(arg3) ? 1 : NUM2INT(arg3), 1);
		table->data = table->_createData(table->xSize, table->ySize, table->zSize);
		table->dimensions = argc;
		return self;
	}

	VALUE Table::rb_initialize_copy(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Table, table);
		RB_VAR2CPP(original, Table, other);
		table->xSize = other->xSize;
		table->ySize = other->ySize;
		table->zSize = other->zSize;
		table->data = table->_createData(table->xSize, table->ySize, table->zSize);
		table->dimensions = other->dimensions;
		memcpy(table->data, other->data, table->xSize * table->ySize * table->zSize * sizeof(short));
		return self;
	}

	VALUE Table::create(int argc, VALUE* argv)
	{
		VALUE object = Table::rb_new(rb_cTable);
		object = Table::rb_initialize(argc, argv, object);
		return object;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Table::rb_getXSize(VALUE self)
	{
		RB_SELF2CPP(Table, table);
		return INT2NUM(table->xSize);
	}

	VALUE Table::rb_getYSize(VALUE self)
	{
		RB_SELF2CPP(Table, table);
		return INT2NUM(table->ySize);
	}

	VALUE Table::rb_getZSize(VALUE self)
	{
		RB_SELF2CPP(Table, table);
		return INT2NUM(table->zSize);
	}

	VALUE Table::rb_getData(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Table, table);
		VALUE arg1 = Qnil;
		VALUE arg2 = Qnil;
		VALUE arg3 = Qnil;
		rb_scan_args(argc, argv, hstr(table->dimensions).c_str(), &arg1, &arg2, &arg3);
		int x = NUM2INT(arg1);
		int y = (NIL_P(arg2) ? 0 : NUM2INT(arg2));
		int z = (NIL_P(arg3) ? 0 : NUM2INT(arg3));
		if (!is_between(x, 0, table->xSize - 1) || !is_between(y, 0, table->ySize - 1) || !is_between(z, 0, table->zSize - 1))
		{
			return Qnil;
		}
		return INT2FIX(table->data[x + table->xSize * (y + table->ySize * z)]);
	}
		
	VALUE Table::rb_setData(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Table, table);
		VALUE arg1 = Qnil;
		VALUE arg2 = Qnil;
		VALUE arg3 = Qnil;
		VALUE arg4 = Qnil;
		rb_scan_args(argc, argv, hstr(table->dimensions + 1).c_str(), &arg1, &arg2, &arg3, &arg4);
		int x = NUM2INT(arg1);
		int y = 0;
		int z = 0;
		int value = 0;
		if (table->dimensions == 1)
		{
			value = NUM2INT(arg2);
		}
		else if (table->dimensions == 2)
		{
			y = NUM2INT(arg2);
			value = NUM2INT(arg3);
		}
		else
		{
			y = NUM2INT(arg2);
			z = NUM2INT(arg3);
			value = NUM2INT(arg4);
		}
		if (!is_between(x, 0, table->xSize - 1) || !is_between(y, 0, table->ySize - 1) || !is_between(z, 0, table->zSize - 1))
		{
			return Qnil;
		}
		table->data[x + table->xSize * (y + table->ySize * z)] = (short)hclamp(value, -32768, 32767);
		return Qnil;
	}
		
	VALUE Table::rb_resize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Table, table);
		VALUE rb_xSize, rb_ySize, rb_zSize;
		rb_scan_args(argc, argv, "12", &rb_xSize, &rb_ySize, &rb_zSize);
		int xSize = hmax(NUM2INT(rb_xSize), 1);
		int ySize = hmax(NIL_P(rb_ySize) ? 1 : NUM2INT(rb_ySize), 1);
		int zSize = hmax(NIL_P(rb_zSize) ? 1 : NUM2INT(rb_zSize), 1);
		table->_resize(xSize, ySize, zSize);
		table->dimensions = argc;
		return Qnil;
	}

	/****************************************************************************************
	 * Serialization
	 ****************************************************************************************/

	VALUE Table::rb_dump(int argc, VALUE* argv, VALUE self)
	{
		VALUE d;
		rb_scan_args(argc, argv, "01", &d);
		if (NIL_P(d))
		{
			d = INT2FIX(-1);
		}
		RB_SELF2CPP(Table, table);
		int size = table->xSize * table->ySize * table->zSize;
		// store sizes
		VALUE data = rb_ary_new();
		rb_ary_push(data, INT2FIX(table->dimensions));
		rb_ary_push(data, INT2FIX(table->xSize));
		rb_ary_push(data, INT2FIX(table->ySize));
		rb_ary_push(data, INT2FIX(table->zSize));
		rb_ary_push(data, INT2FIX(size));
		// store data
		for_iter (i, 0, size)
		{
			rb_ary_push(data, INT2FIX(table->data[i]));
		}
		// convert data array into data stream
		hstr format = "LLLLL" + hstr('S', size);
		VALUE data_fmt = rb_str_new2(format.c_str());
		VALUE byte_string = rb_funcall_1(data, "pack", data_fmt);
		return byte_string;
	}

	VALUE Table::rb_load(VALUE self, VALUE value)
	{
		// load Table size data
		VALUE sliced_string = rb_funcall_2(value, "[]", INT2FIX(0), INT2FIX(20));
		VALUE data = rb_funcall_1(sliced_string, "unpack", rb_str_new2("LLLLL"));
		int dimensions = NUM2INT(rb_ary_shift(data));
		VALUE rb_xSize = rb_ary_shift(data);
		VALUE rb_ySize = rb_ary_shift(data);
		VALUE rb_zSize = rb_ary_shift(data);
		int size = NUM2INT(rb_xSize) * NUM2INT(rb_ySize) * NUM2INT(rb_zSize);
		// create the table
		VALUE rb_table;
		if (dimensions == 1)
		{
			rb_table = Table::create(1, &rb_xSize);
		}
		else if (dimensions == 2)
		{
			VALUE argv[2] = {rb_xSize, rb_ySize};
			rb_table = Table::create(2, argv);
		}
		else
		{
			VALUE argv[3] = {rb_xSize, rb_ySize, rb_zSize};
			rb_table = Table::create(3, argv);
		}
		RB_VAR2CPP(rb_table, Table, table);
		// loading data entries
		VALUE data_fmt = rb_str_new2(hstr('S', size).c_str());
		sliced_string = rb_funcall_2(value, "[]", INT2FIX(20), INT2FIX(size * 2));
		data = rb_funcall_1(sliced_string, "unpack", data_fmt);
		for_iter (i, 0, size)
		{
			table->data[i] = (short)NUM2INT(rb_ary_shift(data));
		}
		return rb_table;
	}
	
	VALUE Table::rb_arcDump(VALUE self)
	{
		RB_SELF2CPP(Table, table);
		// store sizes
		VALUE data = rb_ary_new();
		rb_ary_push(data, INT2FIX(table->dimensions));
		rb_ary_push(data, INT2FIX(table->xSize));
		rb_ary_push(data, INT2FIX(table->ySize));
		rb_ary_push(data, INT2FIX(table->zSize));
		// store data
		int size = table->xSize * table->ySize * table->zSize;
		for_iter (i, 0, size)
		{
			rb_ary_push(data, INT2FIX(table->data[i]));
		}
		// convert data array into data stream
		VALUE data_fmt = rb_str_new2(("VVVV" + hstr('v', size)).c_str());
		VALUE byte_string = rb_funcall_1(data, "pack", data_fmt);
		return byte_string;
	}

	VALUE Table::rb_arcLoad(VALUE self, VALUE value)
	{
		// load Table size data
		VALUE sliced_string = rb_funcall_2(value, "[]", INT2FIX(0), INT2FIX(16));
		VALUE data = rb_funcall_1(sliced_string, "unpack", rb_str_new2("VVVV"));
		int dimensions = NUM2INT(rb_ary_shift(data));
		VALUE rb_xSize = rb_ary_shift(data);
		VALUE rb_ySize = rb_ary_shift(data);
		VALUE rb_zSize = rb_ary_shift(data);
		int size = NUM2INT(rb_xSize) * NUM2INT(rb_ySize) * NUM2INT(rb_zSize);
		// create the table
		VALUE argv[3] = {rb_xSize, rb_ySize, rb_zSize};
		VALUE rb_table = Table::create(dimensions, argv);
		RB_VAR2CPP(rb_table, Table, table);
		// loading data entries
		VALUE data_fmt = rb_str_new2(hstr('v', size).c_str());
		sliced_string = rb_funcall_2(value, "[]", INT2FIX(16), INT2FIX(size * 2));
		data = rb_funcall_1(sliced_string, "unpack", data_fmt);
		for_iter (i, 0, size)
		{
			table->data[i] = (short)NUM2INT(rb_ary_shift(data));
		}
		return rb_table;
	}
	
}
