#ifndef ZER0_RGSS_GRAPHICS_H
#define ZER0_RGSS_GRAPHICS_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Graphics
		{
		public:
			/// @brief the number of frame updates per second
			static int frame_rate;
			/// @brief ???
			static bool visible;

			static VALUE getFrameCount(VALUE self);
			static VALUE setFrameCount(VALUE self, VALUE value);

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
			static VALUE update(VALUE self);
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();

		private:
			/// @brief the number of frames that have passed
			static unsigned int frameCount;
			

		};

	}
}
#endif
