#ifndef RGSS_INPUT_H
#define RGSS_INPUT_H

#include <ruby.h>

#include "rgssExport.h"

#define MAX_KEYS 256

namespace rgss
{
	extern VALUE rb_mInput;

	class rgssExport Input
	{
	public:
		/// @brief Initializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();

		static const int DOWN = 2;
		static const int LEFT = 4;
		static const int RIGHT = 6;
		static const int UP = 8;
		static const int A = 11;
		static const int B = 12;
		static const int C = 13;
		static const int X = 14;
		static const int Y = 15;
		static const int Z = 16;
		static const int L = 17;
		static const int R = 18;
		static const int SHIFT = 21;
		static const int CTRL = 22;
		static const int ALT = 23;
		static const int F5 = 25;
		static const int F6 = 26;
		static const int F7 = 27;
		static const int F8 = 28;
		static const int F9 = 29;

		/// @brief Updates input data. As a rule, this method is called once per frame.
		static VALUE rb_update(VALUE self);
		/// @brief Checks the status of the directional buttons, translates the data into a specialized 4-direction input format.
		/// @return int (2, 4, 6, 8) The state of the directional buttons.
		static VALUE rb_dir4(VALUE self);
		/// @brief Checks the status of the directional buttons, translates the data into a specialized 8-direction input format.
		/// @return int (1, 2, 3, 4, 6, 7, 8, 9) The state of the directional buttons
		static VALUE rb_dir8(VALUE self);
		/// @brief Determines whether a button is being pressed again.
		/// @param[in] value An integer indentifying the keyboard key.
		/// @return bool Boolean state of key being triggered.
		static VALUE rb_trigger(VALUE self, VALUE value);
		/// @brief Determines whether a button is currently being pressed.
		/// @param[in] value An integer indentifying the keyboard key.
		/// @return bool Boolean state of key being pressed.
		static VALUE rb_press(VALUE self, VALUE value);
		/// @brief Determines whether a button is being pressed again.
		/// @param[in] value An integer indentifying the keyboard key.
		/// @return bool Boolean state of key being triggered repeatedly.
		static VALUE rb_repeat(VALUE self, VALUE value);

		/// @brief Determines whether a specific functionality key is being pressed again.
		/// @param[in] value An integer indentifying the keyboard key.
		/// @return Boolean state of key being triggered.
		static bool isTriggered(unsigned char value);
		/// @brief Determines whether a specific functionality key is currently being pressed.
		/// @param[in] value An integer indentifying the keyboard key.
		/// @return Boolean state of key being pressed.
		static bool isPressed(unsigned char value);
		/// @brief Determines whether a specific functionality key is being pressed again.
		/// @param[in] keycode An integer indentifying the keyboard key.
		/// @return bool Boolean state of key being triggered repeatedly.
		static bool isRepeated(unsigned char keycode);
		/// @brief Key Down input callback.
		/// @param[in] value An integer indentifying the keyboard key.
		static void onKeyDown(unsigned int value);
		/// @brief Key Up input callback.
		/// @param[in] value An integer indentifying the keyboard key.
		static void onKeyUp(unsigned int value);

	};
	
}
#endif
