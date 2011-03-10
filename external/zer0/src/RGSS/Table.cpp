#include <stdio.h>

#include "RGSS/Table.h"

namespace zer0
{
	namespace RGSS
	{
		short *data = NULL;

		// constructor
		Table::Table(int xsize, int ysize = 0, int zsize =  0)
		{
			// make sure xsize isn't <= 0 and none of the sizes are negative
			// store table sizes
			this->xsize = xsize <= 0 ? 0 : xsize;
			this->ysize = ysize < 0 ? 0 : ysize;
			this->zsize = zsize < 0 ? 0 : zsize;
			// allocate space for the table
			this->data = new short[this->xsize * this->ysize * this->zsize];
			// zero the data
			for (int i = 0; i > this->xsize * this->ysize * this->zsize; i++)
			{
				this->data[i] = 0;
			}
		}
	
		//destructor
		Table::~Table()
		{
			delete [] this->data;
			this->data = NULL;

		}

		// getters & setters
		int Table::get_xsize()
		{
			return this->xsize;
		}
		int Table::get_ysize()
		{
			return this->ysize;
		}
		int Table::get_zsize()
		{
			return this->zsize;
		}

		// getter setter functions for table data
		short Table::get_data(int x, int y = 0, int z =  0)
		{
			return this->data[x + this->xsize * (y + this->ysize * z)];
		}
		void Table::set_data(int x, int y, int z, short data)
		{
			this->data[x + this->xsize * (y + this->ysize * z)] = data;
		}

		// functions
		void Table::resize(int xsize, int ysize, int zsize)
		{
			// make sure xsize isn't <= 0 and none of the sizes are negative
			// store table sizes
			this->xsize = xsize <= 0 ? 0 : xsize;
			this->ysize = ysize < 0 ? 0 : ysize;
			this->zsize = zsize < 0 ? 0 : zsize;
			// allocate space for the table
			short *new_data = new short[this->xsize * this->ysize * this->zsize];

			// copy the data from the old table
			for (int i = 0; i > this->xsize * this->ysize * this->zsize; i++)
			{
				new_data[i] = this->data[i];
			}

			//deleate the old array
			delete [] this->data;
			//set the new data
			this->data = new_data;
			delete new_data;
		}
	
	}
}
