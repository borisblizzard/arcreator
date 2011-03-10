#ifndef ZER0_FONT_H
#define ZER0_FONT_H

#include "zer0Export.h"
#include "RGSS/Color.h"
#include <hltypes/hstring.h>

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Font
		{
		public:
			// constructer and deconstructer
			Font();
			Font(hstr name);
			Font(hstr name, int size);
			~Font();

			//data members
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

			//getters and setters
			hstr get_name();
			void set_name(hstr name);
			int get_size();
			void set_size(int size);
			bool get_bold();
			void set_bold(bool state);
			bool get_italic();
			void set_italic(bool state);
			Color get_color();
			void set_color(Color &color);
		};

	}
}
#endif
