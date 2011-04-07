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
	
}
