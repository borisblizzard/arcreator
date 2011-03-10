#ifndef ZER0_RGSS_FONT_H
#define ZER0_RGSS_FONT_H

#include <hltypes/hstring.h>

#include "RGSS/Color.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		/// @brief Emulates RGSS's Font class.
		class zer0Export Font
		{
		public:
			/// @brief Font name.
			hstr name;
			/// @brief Font size.
			int size;
			/// @brief Bold flag.
			bool bold;
			/// @brief Italic flag.
			bool italic;
			/// @brief Font Color.
			Color color;

			/// @brief Default Font name.
			static hstr default_name;
			/// @brief Default Font size.
			static int default_size;
			/// @brief Default bold flag.
			static bool default_bold;
			/// @brief Default italic flag.
			static bool default_italic;
			/// @brief Default Font Color.
			static Color default_color;

			/// @brief Empty constructor.
			Font();
			/// @brief Basic constructor.
			/// @param[in] name Font name.
			Font(chstr name);
			/// @brief Basic constructor.
			/// @param[in] name Font name.
			/// @param[in] size Font size.
			Font(chstr name, int size);
			/// @brief Destructor
			~Font();

		};

	}
}
#endif
