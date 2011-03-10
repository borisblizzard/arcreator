#ifndef ZER0_RGSS_TABLE_H
#define ZER0_RGSS_TABLE_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Table
		{
		public:
			// constructor / destructor
			Table(int xSize, int ySize = 1, int zSize = 1);
			~Table();
			// getters & setters
			int getXSize() { return this->xSize; }
			int getYSize() { return this->xSize; }
			int getZSize() { return this->xSize; }
			// getter setter functions for table data
			short getData(int x);
			short getData(int x, int y);
			short getData(int x, int y, int z);
			void setData(int x, short value);
			void setData(int x, int y, short value);
			void setData(int x, int y, int z, short value);
			// functions
			void resize(int xSize, int ySize = 1, int zSize = 1);

		protected:
			// data
			int xSize;
			int ySize;
			int zSize;
			// pointer for data
			short *data;

			short* _createData(int xSize, int ySize, int zSize);
			
		};

	}
}
#endif
