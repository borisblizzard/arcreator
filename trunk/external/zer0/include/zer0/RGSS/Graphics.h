#ifndef ZER0_RGSS_GRAPHICS_H
#define ZER0_RGSS_GRAPHICS_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		namespace Graphics
		{
			/// @brief the number of frames that have passed
			static int frame_count;
			/// @brief the number of frame updates per second
			static int frame_rate;
			/// @brief ???
			static bool visible;

			/// @brief Resets the screen refresh timing.
			static void frameReset();
			/// @brief Fixes the current screen in preparation for transitions.
			static void freeze();
			/// @brief Carries out a transition from the screen fixed in Graphics.freeze to the current screen.
			/// @param[in] duration The number of frames the transition will last. 
			/// @param[in] filename The transition graphic file name.
			/// @param[in] vague Sets the ambiguity of the borderline between the graphic's starting and ending points.
			static void transition(int duration, hstr filename, int vague);
			/// @brief Refreshes the game screen and advances time by 1 frame.
			extern "C"
			VALUE update(...);
			/// @brief Exposes this class to Ruby.
			void createRubyInterface();

		};

	}
}
#endif
