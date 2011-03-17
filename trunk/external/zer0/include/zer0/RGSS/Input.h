#ifndef ZER0_RGSS_INPUT_H
#define ZER0_RGSS_INPUT_H

#include <ruby.h>

#include <april/Keys.h>

#include "Context.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		static VALUE rb_mInput;

		class zer0Export Input
		{
		public:
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Intializes the module.
			static void init();

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

			// @brief Updates input data. As a rule, this method is called once per frame.
			static VALUE update(VALUE self);
			// @brief Checks the status of the directional buttons, translates the data into a specialized 4-direction input format.
			// @return int (2, 4, 6, 8) The state of the directional buttons.
			static VALUE dir4(VALUE self);
			// @brief Checks the status of the directional buttons, translates the data into a specialized 8-direction input format.
			// @return int (1, 2, 3, 4, 6, 7, 8, 9) The state of the directional buttons
			static VALUE dir8(VALUE self);
			// @brief Determines whether a button is being pressed again.
			// @param[in] keycode An interger indentifing the keyboard key.
			// @return bool true if the key is being pressed false if not.
			static VALUE trigger(VALUE self, VALUE keycode);
			// @brief Determines whether a button is currently being pressed.
			// @param[in] keycode An interger indentifing the keyboard key.
			// @return bool true if the key is being pressed false if not.
			static VALUE press(VALUE self, VALUE keycode);
			// @brief Determines whether a button is being pressed again.
			// @param[in] keycode An interger indentifing the keyboard key.
			// @return bool true if the key is being pressed false if not.
			static VALUE repeat(VALUE self, VALUE keycode);
			// @brief Determines whether a specific functionaly key is being pressed again.
			// @param[in] keycode An interger indentifing the keyboard key.
			// @return bool true if the key is being pressed false if not.
			static bool isTriggered(unsigned char keycode);
			// @brief Determines whether a specific functionaly key is currently being pressed.
			// @param[in] keycode An interger indentifing the keyboard key.
			// @return bool true if the key is being pressed false if not.
			static bool isPressed(unsigned char keycode);
			// @brief Determines whether a specific functionaly key is being pressed again.
			// @param[in] keycode An interger indentifing the keyboard key.
			// @return bool true if the key is being pressed false if not.
			static bool isRepeated(unsigned char keycode);

		/*
		dir4
		dir8
		press?
		repeat?
		trigger?
		update
		*/
			/*
		protected:
			Input();
			~Input();
			*/
		};
	
	}
}
#endif
