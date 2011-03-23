#include <ruby.h>
#include <stdio.h>

#include <hltypes/util.h>

#include "RGSS/RGSSError.h"
#include "RGSS/Table.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Table::createRubyInterface()
		{
			rb_cTable = rb_define_class("Table", rb_cObject);
			rb_define_alloc_func(rb_cTable, &Table::rb_new);
			// initialize
			rb_define_method(rb_cTable, "initialize", RUBY_METHOD_FUNC(&Table::rb_initialize), -1);
			rb_define_method(rb_cTable, "inspect", RUBY_METHOD_FUNC(&Table::rb_inspect), 0);
			// getters and setters
			rb_define_method(rb_cTable, "[]", RUBY_METHOD_FUNC(&Table::rb_getData), -1);
			rb_define_method(rb_cTable, "[]=", RUBY_METHOD_FUNC(&Table::rb_setData), -1);
			// all other methods
			rb_define_method(rb_cTable, "resize", RUBY_METHOD_FUNC(&Table::rb_resize), -1);
			// static methods
		}
	
		/*
		Table::~Table()
		{
			delete [] this->data;
			this->data = NULL;
		}
		*/

		void Table::gc_mark(Table* table) { }

		VALUE Table::rb_new(VALUE classe)
		{
			Table* table;
			return Data_Make_Struct(classe, Table, NULL, NULL, table);
		}

		VALUE Table::rb_initialize(int argc, VALUE* argv, VALUE self)
		{
			VALUE xSize, ySize, zSize;
			RB_VAR2CPP(Table, table);
			rb_scan_args(argc, argv, "12", &xSize, &ySize, &zSize);
			table->xSize = hmax((int)NUM2UINT(xSize), 1);
			table->ySize = hmax(NIL_P(ySize) ? 1 : (int)NUM2UINT(ySize), 1);
			table->zSize = hmax(NIL_P(zSize) ? 1 : (int)NUM2UINT(zSize), 1);
			table->data = table->_createData(table->xSize, table->ySize, table->zSize);
			return self;
		}

		VALUE Table::rb_inspect(VALUE self)
		{
			RB_VAR2CPP(Table, table);
			//hstr result = hsprintf("(%.1f,%.1f,%.1f,%.1f)", table->xSize, table->ySize, table->zSize, table->data);
			//return rb_str_new2(result.c_str());
			return self;
		}

		VALUE Table::rb_getData(int argc, VALUE* argv, VALUE self)
		{
			VALUE x, y, z = INT2NUM(0);
			RB_VAR2CPP(Table, table);
			if (table->zSize > 1)
			{
				rb_scan_args(argc, argv, "3", &x, &y, &z);
			}
			else if (table->ySize > 1)
			{
				rb_scan_args(argc, argv, "2", &x, &y);
			}
			else
			{
				rb_scan_args(argc, argv, "1", &x);
			}
			return INT2NUM(
				table->data[(int)NUM2UINT(x) + table->xSize * ((int)NUM2UINT(y) + table->ySize * (int)NUM2UINT(z))]
			);
		}
		
		VALUE Table::rb_setData(int argc, VALUE* argv, VALUE self)
		{
			VALUE x, y, z, value = INT2NUM(0);
			RB_VAR2CPP(Table, table);
			if (table->zSize > 1)
			{
				rb_scan_args(argc, argv, "4", &x, &y, &z, &value);
			}
			else if (table->ySize > 1)
			{
				rb_scan_args(argc, argv, "3", &x, &y, &value);
			}
			else
			{
				rb_scan_args(argc, argv, "2", &x, &value);
			}

			table->data[(int)NUM2UINT(x) + table->xSize * ((int)NUM2UINT(y) + table->ySize * (int)NUM2UINT(z))] = (short)NUM2UINT(value);
			return self;
		}
		
		VALUE Table::rb_resize(int argc, VALUE* argv, VALUE self)
		{
			VALUE xSize, ySize, zSize = INT2NUM(1);
			RB_VAR2CPP(Table, table);
			if (table->zSize > 1)
			{
				rb_scan_args(argc, argv, "3", &xSize, &ySize, &zSize);
			}
			else if (table->ySize > 1)
			{
				rb_scan_args(argc, argv, "2", &xSize, &ySize);
			}
			else
			{
				rb_scan_args(argc, argv, "1", &xSize);
			}
			table->_resize((int)NUM2UINT(xSize), (int)NUM2UINT(ySize), (int)NUM2UINT(zSize));
			return self;
		
		}
		// functions
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

	}
}
