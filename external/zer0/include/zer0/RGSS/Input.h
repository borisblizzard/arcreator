#ifndef ZER0_RGSS_INPUT_H
#define ZER0_RGSS_INPUT_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Input
		{
		public:

			const int DOWN = 2, LEFT = 4, RIGHT = 6, UP = 8;
			const int A = 11, B = 12, C = 13, X = 14, Y = 15, Z = 16, L = 17, R = 18;
			const int SHIFT = 21, CTRL = 22, ALT = 23;
			const int F5 = 25, F6 = 26, F7 = 27, F8 = 28, F9 = 29;

			// @brief Checks the status of the directional buttons, translates the data into a specialized 4-direction input format.
			// @return int (2, 4, 6, 8) The state of the directional buttons
			static int Dir4();
			// @brief Checks the status of the directional buttons, translates the data into a specialized 8-direction input format.
			// @return int  (1, 2, 3, 4, 6, 7, 8, 9) The state of the directional buttons
			static int Dir8();
			// @brief Determines whether the button num is currently being pressed.
			// @param[in] num An interger indentifing the keybord key
			// @return bool true if the key is being pressed false if not
			static bool Press(int num);
			// @brief Determines whether the button num is being pressed again.
			// @param[in] num An interger indentifing the keybord key
			// @return bool true if the key is being pressed false if not
			static bool Trigger(int num);
			// @brief Determines whether the button num is being pressed again.
			// @param[in] num An interger indentifing the keybord key
			// @return bool true if the key is being pressed false if not
			static bool Repeat(int num);
			// @brief Updates input data. As a rule, this method is called once per frame.
			static void Update();

		/*
		dir4
		dir8
		press?
		repeat?
		trigger?
		update
		*/
		protected:
			Input();
			~Input();

		};
	
	}
}
#endif
