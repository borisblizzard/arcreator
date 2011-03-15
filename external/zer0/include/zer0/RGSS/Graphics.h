#ifndef ZER0_RGSS_GRAPHICS_H
#define ZER0_RGSS_GRAPHICS_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		extern VALUE rb_mGraphics;

		class zer0Export Graphics
		{
		public:
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Intializes the module.
			static void init();
			/// @brief ???
			//static bool visible;

			/// @brief Gets the frame count.
			static VALUE getFrameCount(VALUE self);
			/// @brief Sets the frame count.
			/// @param[in] value The new frame count.
			static VALUE setFrameCount(VALUE self, VALUE value);
			/// @brief Gets the frame rate.
			static VALUE getFrameRate(VALUE self);
			/// @brief Sets the frame rate.
			/// @param[in] value The new frame rate.
			static VALUE setFrameRate(VALUE self, VALUE value);

			/// @brief Resets the screen refresh timing.
			static VALUE frameReset(VALUE self);
			/// @brief Fixes the current screen in preparation for transitions.
			static VALUE freeze(VALUE self);
			/// @brief Carries out a transition from the screen fixed in Graphics.freeze to the current screen.
			/// @param[in] duration The number of frames the transition will last. 
			/// @param[in] filename The transition graphic file name.
			/// @param[in] vague Sets the ambiguity of the borderline between the graphic's starting and ending points.
			static VALUE transition(VALUE self, VALUE duration, VALUE filename, VALUE vague);
			/// @brief Refreshes the game screen and advances time by 1 frame.
			static VALUE update(VALUE self);

		private:
			/// @brief the number of frames that have passed
			static unsigned int frameCount;
			static unsigned int frameRate;
			

		};

	}
}
#endif
