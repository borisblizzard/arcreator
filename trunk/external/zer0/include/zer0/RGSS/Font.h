#ifndef ZER0_RGSS_FONT_H
#define ZER0_RGSS_FONT_H

#include <hltypes/hstring.h>

#include "RGSS/Color.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Font
		{
		public:
			hstr name;
			int size;
			bool bold;
			bool italic;
			Color color;

			//static members
			static hstr default_name;
			static int default_size;
			static bool default_bold;
			static bool default_italic;
			static Color default_color;

			// constructer and deconstructer
			Font();
			Font(chstr name);
			Font(chstr name, int size);
			~Font();

		};

	}
}
#endif
