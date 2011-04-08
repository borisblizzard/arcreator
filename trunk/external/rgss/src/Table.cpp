#include <ruby.h>

#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "RGSSError.h"
#include "Table.h"

namespace rgss
{

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cTable;

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
	}
	
	short* Table::_createData(int xSize, int ySize, int zSize) const
	{
		// allocate space for the table
		short* data = new short[xSize * ySize * zSize];
		// zero the data
		memset(data, 0, xSize * ySize * zSize * sizeof(short));
		return data;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Table::init()
	{
	}

	void Table::createRubyInterface()
	{
		rb_cTable = rb_define_class("Table", rb_cObject);
		rb_define_alloc_func(rb_cTable, &Table::rb_new);
		// initialize
		rb_define_method(rb_cTable, "initialize", RUBY_METHOD_FUNC(&Table::rb_initialize), -1);
		// getters and setters
		rb_define_method(rb_cTable, "[]", RUBY_METHOD_FUNC(&Table::rb_getData), -1);
		rb_define_method(rb_cTable, "[]=", RUBY_METHOD_FUNC(&Table::rb_setData), -1);
		// all other methods
		rb_define_method(rb_cTable, "resize", RUBY_METHOD_FUNC(&Table::rb_resize), -1);
		rb_define_method(rb_cTable, "_dump", RUBY_METHOD_FUNC(&Table::rb_dump), -1);
		rb_define_singleton_method(rb_cTable, "_load", RUBY_METHOD_FUNC(&Table::rb_load), 1);
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

	VALUE Table::rb_getData(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Table, table);
		VALUE arg1, arg2, arg3;
		if (table->zSize > 1)
		{
			rb_scan_args(argc, argv, "3", &arg1, &arg2, &arg3);
		}
		else if (table->ySize > 1)
		{
			rb_scan_args(argc, argv, "2", &arg1, &arg2);
		}
		else
		{
			rb_scan_args(argc, argv, "1", &arg1);
		}
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
		VALUE arg1, arg2, arg3, arg4;
		if (table->zSize > 1)
		{
			rb_scan_args(argc, argv, "4", &arg1, &arg2, &arg3, &arg4);
		}
		else if (table->ySize > 1)
		{
			rb_scan_args(argc, argv, "3", &arg1, &arg2, &arg4);
		}
		else
		{
			rb_scan_args(argc, argv, "2", &arg1, &arg4);
		}
		int x = NUM2INT(arg1);
		int y = (NIL_P(arg2) ? 0 : NUM2INT(arg2));
		int z = (NIL_P(arg3) ? 0 : NUM2INT(arg3));
		if (!is_between(x, 0, table->xSize - 1) || !is_between(y, 0, table->ySize - 1) || !is_between(z, 0, table->zSize - 1))
		{
			return Qnil;
		}
		int value = (short)hclamp(NUM2INT(arg4), -32768, 32767);
		table->data[x + table->xSize * (y + table->ySize * z)] = value;
		return Qnil;
	}
		
	VALUE Table::rb_resize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Table, table);
		VALUE xSize, ySize, zSize;
		rb_scan_args(argc, argv, "12", &xSize, &ySize, &zSize);
		table->xSize = hmax(NUM2INT(xSize), 1);
		table->ySize = hmax(NIL_P(ySize) ? 1 : NUM2INT(ySize), 1);
		table->zSize = hmax(NIL_P(zSize) ? 1 : NUM2INT(zSize), 1);
		table->_resize(NUM2INT(xSize), NUM2INT(ySize), NUM2INT(zSize));
		return Qnil;
		
	}

	VALUE Table::rb_dump(int argc, VALUE* argv, VALUE self)
	{
		VALUE d;
		rb_scan_args(argc, argv, "01", &d);
		if (NIL_P(d))
		{
			d = INT2FIX(0);
		}
		RB_SELF2CPP(Table, table);

		// create the byte string that will be returned
		VALUE byte_string = rb_str_new2("");
		// get the method id
		ID pack_id = rb_intern("pack");
		// create the ruby pack format strings 
		VALUE long_format_str = rb_str_new2("L");
		VALUE short_format_str = rb_str_new2("S");

		// create array
		VALUE arr = rb_ary_new();
		rb_ary_push(arr, INT2FIX(3));
		rb_str_concat(byte_string, rb_funcall(arr, pack_id, 1, long_format_str));
		// xSize
		VALUE xSize_arr = rb_ary_new();
		rb_ary_push(xSize_arr, INT2FIX(table->xSize));
		rb_str_concat(byte_string, rb_funcall(xSize_arr, pack_id, 1, long_format_str));
		// ySize
		VALUE ySize_arr = rb_ary_new();
		rb_ary_push(ySize_arr, INT2FIX(table->ySize));
		rb_str_concat(byte_string, rb_funcall(ySize_arr, pack_id, 1, long_format_str));
		// zSize
		VALUE zSize_arr = rb_ary_new();
		rb_ary_push(zSize_arr, INT2FIX(table->zSize));
		rb_str_concat(byte_string, rb_funcall(zSize_arr, pack_id, 1, long_format_str));
		// size
		VALUE size_arr = rb_ary_new();
		rb_ary_push(size_arr, INT2FIX(table->xSize * table->ySize * table->zSize));
		rb_str_concat(byte_string, rb_funcall(size_arr, pack_id, 1, long_format_str));
		// table data
		for_iter (x, 0, table->xSize)
		{
			for_iter (y, 0, table->ySize)
			{
				for_iter (z, 0, table->zSize)
				{
					VALUE data_arr = rb_ary_new();
					rb_ary_push(data_arr, INT2FIX(table->data[x + table->xSize * (y + table->ySize * z)]));
					rb_str_concat(byte_string, rb_funcall(data_arr, pack_id, 1, short_format_str));
				}
			}
		}
		// return the byte string
		return byte_string;
	}

	VALUE Table::rb_load(VALUE self, VALUE value)
	{
		// get the method ids
		ID unpack_id = rb_intern("unpack");
		ID slice_id = rb_intern("[]");
		// create the ruby pack format strings 
		VALUE long_format_str = rb_str_new2("L");
		VALUE short_format_str = rb_str_new2("S");

		VALUE size, nx, ny, nz;
		VALUE data = rb_ary_new();

		// size
		VALUE sliced_string = rb_funcall(value, slice_id, 2, INT2FIX(0), INT2FIX(4));
		size = rb_ary_shift(rb_funcall(sliced_string, unpack_id, 1, long_format_str));
		// nx
		sliced_string = rb_funcall(value, slice_id, 2, INT2FIX(4), INT2FIX(4));
		nx = rb_ary_shift(rb_funcall(sliced_string, unpack_id, 1, long_format_str));
		// ny
		sliced_string = rb_funcall(value, slice_id, 2, INT2FIX(8), INT2FIX(4));
		ny = rb_ary_shift(rb_funcall(sliced_string, unpack_id, 1, long_format_str));
		// nz
		sliced_string = rb_funcall(value, slice_id, 2, INT2FIX(12), INT2FIX(4));
		nz = rb_ary_shift(rb_funcall(sliced_string, unpack_id, 1, long_format_str));

		int pointer = 20;
		// collect table data
		while (true)
		{
			VALUE sliced_string = rb_funcall(value, slice_id, 2, INT2FIX(pointer), INT2FIX(2));
			rb_ary_push(data,  rb_ary_shift(rb_funcall(sliced_string, unpack_id, 1, short_format_str)));
			pointer += 2;
			if (pointer > (rb_str_strlen(value) - 1) )
			{
				break;
			}
		}
		// create c array of arguments
		VALUE c_arr[3];
		c_arr[0] = nx;
		c_arr[1] = ny;
		c_arr[2] = nz;
		// create the table
		VALUE rb_table = Table::create(3, c_arr);
		// get the C++ version
		Table* table; 
		Data_Get_Struct(rb_table, Table, table);
		// set the data
		long n = 0;
		for_iter (z, 0, FIX2LONG(nz))
		{
			for_iter (y, 0, FIX2LONG(ny))
			{
				for_iter (x, 0, FIX2LONG(nx))
				{
					table->data[x + table->xSize * (y + table->ySize * z)] = (short)hclamp(NUM2INT(rb_ary_entry(data, n)), -32768, 32767);
					n += 1;
				}
			}
		}
		// return the ruby table
		return rb_table;
	}
	
}
