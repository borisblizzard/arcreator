#ifndef ZER0_TABLE_H
#define ZER0_TABLE_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Table
		{
		public:
			// data 
			int xsize;
			int ysize;
			int zsize;
			// getters & setters
			int get_xsize();
			int get_ysize();
			int get_zsize();
			// getter setter functions for table data
			short get_data(int x, int y, int z);
			void set_data(int x, int y, int z, short data);
			// constructor / destructor
			Table(int xsize, int ysize, int zsize);
			~Table();
			//functions
			void resize(int xsize, int ysize, int zsize);

		private:
			// pointer for data
			short *data;
			
		};

	}
}
#endif
