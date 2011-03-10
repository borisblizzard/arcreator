#include <stdio.h>

#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "RGSS/RGSSError.h"
#include "RGSS/Table.h"

namespace zer0
{
	namespace RGSS
	{
		// constructor
		Table::Table(int xSize, int ySize, int zSize)
		{
			// make sure xSize isn't <= 0 and none of the sizes are negative
			// store table sizes
			this->xSize = hmax(xSize, 1);
			this->ySize = hmax(ySize, 1);
			this->zSize = hmax(zSize, 1);
			this->data = this->_createData(this->xSize, this->ySize, this->zSize);
		}
	
		//destructor
		Table::~Table()
		{
			delete [] this->data;
			this->data = NULL;
		}

		// getter setter functions for table data
		/// @todo Add out-of-range exception
		short Table::getData(int x)
		{
			if (this->zSize > 1)
			{
				throw RGSSError("wrong # of arguments (1 for 3)");
			}
			if (this->ySize > 1)
			{
				throw RGSSError("wrong # of arguments (1 for 2)");
			}
			return this->data[x];
		}
		/// @todo Add out-of-range exception
		short Table::getData(int x, int y)
		{
			if (this->zSize > 1)
			{
				throw RGSSError("wrong # of arguments (2 for 3)");
			}
			if (this->ySize == 1)
			{
				throw RGSSError("wrong # of arguments (2 for 1)");
			}
			return this->data[x + this->xSize * y];
		}
		/// @todo Add out-of-range exception
		short Table::getData(int x, int y, int z)
		{
			if (this->zSize == 1)
			{
				if (this->ySize == 1)
				{
					throw RGSSError("wrong # of arguments (3 for 1)");
				}
				throw RGSSError("wrong # of arguments (3 for 2)");
			}
			return this->data[x + this->xSize * (y + this->ySize * z)];
		}
		/// @todo Add out-of-range exception
		void Table::setData(int x, short value)
		{
			if (this->zSize > 1)
			{
				throw RGSSError("wrong # of arguments (1 for 3)");
			}
			if (this->ySize > 1)
			{
				throw RGSSError("wrong # of arguments (1 for 2)");
			}
			this->data[x] = value;
		}
		/// @todo Add out-of-range exception
		void Table::setData(int x, int y, short value)
		{
			if (this->zSize > 1)
			{
				throw RGSSError("wrong # of arguments (2 for 3)");
			}
			if (this->ySize == 1)
			{
				throw RGSSError("wrong # of arguments (2 for 1)");
			}
			this->data[x + this->xSize * y] = value;
		}
		/// @todo Add out-of-range exception
		void Table::setData(int x, int y, int z, short value)
		{
			if (this->zSize == 1)
			{
				if (this->ySize == 1)
				{
					throw RGSSError("wrong # of arguments (3 for 1)");
				}
				throw RGSSError("wrong # of arguments (3 for 2)");
			}
			this->data[x + this->xSize * (y + this->ySize * z)] = value;
		}

		// functions
		void Table::resize(int xSize, int ySize, int zSize)
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
	
		short* Table::_createData(int xSize, int ySize, int zSize)
		{
			// allocate space for the table
			short* data = new short[xSize * ySize * zSize];
			// zero the data
			memset(data, 0, xSize * ySize * zSize * sizeof(short));
			return data;
		}

	}
}
