#ifndef RGSS_GRAPHICS_H
#define RGSS_GRAPHICS_H

#include <ruby.h>

#include "rgssExport.h"

namespace april
{
	class Timer;
}

namespace rgss
{
	extern VALUE rb_mGraphics;

	class Renderable;
	class RenderQueue;

	class rgssExport Graphics
	{
	public:
		/// @brief RenderQueue for all renderable objects.
		static RenderQueue* renderQueue;

		/// @brief Gets the render window width.
		/// @result The render window width.
		static int getWidth() { return width; }
		/// @brief Sets the render window height.
		/// @result The render window height.
		static int getHeight() { return height; }
		/// @brief Sets whether Graphics is still running.
		/// @param[in] value The new value.
		static void setRunning(bool value) { running = value; }
		/// @brief Sets whether the window is in focus.
		/// @param[in] value The new value.
		static void setFocused(bool value) { focused = value; }

		/// @brief Toggles the FPS display.
		static void toggleFpsDisplay();

		/// @brief Initializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();

		/// @brief Gets the frame count.
		/// @return int Returns the frame-count.
		static VALUE rb_getFrameCount(VALUE self);
		/// @brief Sets the frame count.
		/// @param[in] value The new frame count.
		static VALUE rb_setFrameCount(VALUE self, VALUE value);
		/// @brief Gets the frame rate.
		/// @return int Returns the frame rate.
		static VALUE rb_getFrameRate(VALUE self);
		/// @brief Sets the frame rate.
		/// @param[in] value The new frame rate.
		static VALUE rb_setFrameRate(VALUE self, VALUE value);

		/// @brief Refreshes the game screen and advances time by 1 frame.
		static VALUE rb_update(VALUE self);
		/// @brief Resets the screen refresh timing.
		static VALUE rb_frameReset(VALUE self);
		/// @brief Fixes the current screen in preparation for transitions.
		static VALUE rb_freeze(VALUE self);
		/// @brief Carries out a transition from the screen fixed in Graphics.freeze to the current screen.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[duration[, filename[, vague]]]".
		static VALUE rb_transition(int argc, VALUE* argv, VALUE self);

	private:
		/// @brief Render window width.
		static int width;
		/// @brief Render window height.
		static int height;
		/// @brief Flag whether rendering is active.
		static bool active;
		/// @brief The number of frames that have passed.
		static unsigned int frameCount;
		/// @brief The frame rate.
		static unsigned int frameRate;
		/// @brief Flag whether it is still running.
		static bool running;
		/// @brief Flag whether window is in focus.
		static bool focused;
		/// @brief Timer for frame limiation.
		static april::Timer* timer;
		/// @brief FPS display flag.
		static bool fpsDisplay;
		/// @brief Timer for FPS counting.
		static april::Timer* fpsTimer;
		/// @brief FPS time;
		static float fpsTime;
		/// @brief FPS count.
		static int fpsCount;
		/// @brief Window title;
		static hstr windowTitle;
		
		/// @brief Waits for the frame sync for FPS limitation.
		static void _waitForFrameSync();
		/// @brief Handles focus change and application finish.
		static void _handleFocusChange();
		/// @brief Updates FPS counter.
		static void _updateFpsCounter(float time);

	};

}
#endif
