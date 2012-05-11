#include <ruby.h>

#include <april/Keys.h>
#include <april/RenderSystem.h>
#include <april/Window.h>
#include <hltypes/harray.h>
#include <hltypes/hmap.h>

#include "CodeSnippets.h"
#include "Graphics.h"
#include "Input.h"
#include "rgss.h"

namespace rgss
{
	VALUE rb_mInput;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	hmap<int, harray<unsigned int> > conversions;
	harray<unsigned int> controlKeys;
	bool triggered[MAX_KEYS];
	bool pressed[MAX_KEYS];
	int repeatedCount;
	unsigned int repeatedKey;
	bool released[MAX_KEYS];
	bool keys[MAX_KEYS];
	harray<unsigned int> repeatedOrder;

	bool Input::isTriggered(unsigned char keycode)
	{
		if (!conversions.has_key(keycode))
		{
			return false;
		}
		foreach (unsigned int, it, conversions[keycode])
		{
			if (triggered[*it])
			{
				return true;
			}
		}
		return false;
	}

	bool Input::isPressed(unsigned char keycode)
	{
		if (!conversions.has_key(keycode))
		{
			return false;
		}
		foreach (unsigned int, it, conversions[keycode])
		{
			if (pressed[*it])
			{
				return true;
			}
		}
		return false;
	}

	bool Input::isRepeated(unsigned char keycode)
	{
		if (!conversions.has_key(keycode))
		{
			return false;
		}
		if (repeatedKey < 0 || !conversions[keycode].contains(repeatedKey))
		{
			return false;
		}
		foreach (unsigned int, it, conversions[keycode])
		{
			if (repeatedCount == 1 || repeatedCount == 16)
			{
				return true;
			}
		}
		return false;
	}

	void Input::onKeyDown(unsigned int keycode)
	{
		keys[keycode] = true;
		if (keycode == april::AK_F2)
		{
			Graphics::toggleFpsDisplay();
		}
	}

	void Input::onKeyUp(unsigned int keycode)
	{
		keys[keycode] = false;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/
	
	void Input::init()
	{
		harray<unsigned int> keys;
		keys += april::AK_DOWN;
		conversions[DOWN] = keys;
		keys.clear();
		keys += april::AK_LEFT;
		conversions[LEFT] = keys;
		keys.clear();
		keys += april::AK_RIGHT;
		conversions[RIGHT] = keys;
		keys.clear();
		keys += april::AK_UP;
		conversions[UP] = keys;
		keys.clear();
		keys += april::AK_SHIFT;
		keys += 'Z';
		conversions[A] = keys;
		keys.clear();
		keys += april::AK_ESCAPE;
		keys += april::AK_NUMPAD0;
		keys += 'X';
		conversions[B] = keys;
		keys.clear();
		keys += april::AK_SPACE;
		keys += april::AK_RETURN;
		keys += 'C';
		conversions[C] = keys;
		keys.clear();
		keys += 'A';
		conversions[X] = keys;
		keys.clear();
		keys += 'S';
		conversions[Y] = keys;
		keys.clear();
		keys += 'D';
		conversions[Z] = keys;
		keys.clear();
		keys += april::AK_PRIOR;
		keys += 'Q';
		conversions[L] = keys;
		keys.clear();
		keys += april::AK_NEXT;
		keys += 'W';
		conversions[R] = keys;
		keys.clear();
		keys += april::AK_SHIFT;
		conversions[SHIFT] = keys;
		keys.clear();
		keys += april::AK_CONTROL;
		conversions[CTRL] = keys;
		keys.clear();
		keys += april::AK_MENU;
		conversions[ALT] = keys;
		keys.clear();
		keys += april::AK_F5;
		conversions[F5] = keys;
		keys.clear();
		keys += april::AK_F6;
		conversions[F6] = keys;
		keys.clear();
		keys += april::AK_F7;
		conversions[F7] = keys;
		keys.clear();
		keys += april::AK_F8;
		conversions[F8] = keys;
		keys.clear();
		keys += april::AK_F9;
		conversions[F9] = keys;
		// adding keys to check for
		foreach_map (int, harray<unsigned int>, it, conversions)
		{
			controlKeys += it->second;
		}
		controlKeys.removed_duplicates();
		controlKeys.sort();
		repeatedKey = -1;
		repeatedCount = 0;
	}

	void Input::destroy()
	{
	}

	void Input::createRubyInterface()
	{
		rb_mInput = rb_define_module("Input");
		rb_define_module_function(rb_mInput, "update", RUBY_METHOD_FUNC(&Input::rb_update), 0);
		rb_define_module_function(rb_mInput, "dir4", RUBY_METHOD_FUNC(&Input::rb_dir4), 0);
		rb_define_module_function(rb_mInput, "dir8", RUBY_METHOD_FUNC(&Input::rb_dir8), 0);
		rb_define_module_function(rb_mInput, "trigger?", RUBY_METHOD_FUNC(&Input::rb_trigger), 1);
		rb_define_module_function(rb_mInput, "repeat?", RUBY_METHOD_FUNC(&Input::rb_repeat), 1);
		rb_define_module_function(rb_mInput, "press?", RUBY_METHOD_FUNC(&Input::rb_press), 1);
		rb_define_const(rb_mInput, "DOWN", INT2FIX(Input::DOWN));
		rb_define_const(rb_mInput, "LEFT", INT2FIX(Input::LEFT));
		rb_define_const(rb_mInput, "RIGHT", INT2FIX(Input::RIGHT));
		rb_define_const(rb_mInput, "UP", INT2FIX(Input::UP));
		rb_define_const(rb_mInput, "A", INT2FIX(Input::A));
		rb_define_const(rb_mInput, "B", INT2FIX(Input::B));
		rb_define_const(rb_mInput, "C", INT2FIX(Input::C));
		rb_define_const(rb_mInput, "X", INT2FIX(Input::X));
		rb_define_const(rb_mInput, "Y", INT2FIX(Input::Y));
		rb_define_const(rb_mInput, "Z", INT2FIX(Input::Z));
		rb_define_const(rb_mInput, "L", INT2FIX(Input::L));
		rb_define_const(rb_mInput, "R", INT2FIX(Input::R));
		rb_define_const(rb_mInput, "SHIFT", INT2FIX(Input::SHIFT));
		rb_define_const(rb_mInput, "CTRL", INT2FIX(Input::CTRL));
		rb_define_const(rb_mInput, "ALT", INT2FIX(Input::ALT));
		rb_define_const(rb_mInput, "F5", INT2FIX(Input::F5));
		rb_define_const(rb_mInput, "F6", INT2FIX(Input::F6));
		rb_define_const(rb_mInput, "F7", INT2FIX(Input::F7));
		rb_define_const(rb_mInput, "F8", INT2FIX(Input::F8));
		rb_define_const(rb_mInput, "F9", INT2FIX(Input::F9));
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Input::rb_update(VALUE self)
	{
		april::window->doEvents();
		foreach (unsigned int, it, controlKeys)
		{
            if (keys[*it])
			{
                released[*it] = false;
                if (!pressed[*it])
				{
                    pressed[*it] = true;
                    triggered[*it] = true;
					repeatedKey = (*it);
					repeatedCount = 0;
				}
                else
				{
                    triggered[*it] = false;
				}
				if ((*it) == repeatedKey)
				{
					repeatedCount < 17 ? repeatedCount += 1 : repeatedCount = 15;
				}
			}
            else if (!released[*it])
			{
                if (pressed[*it])
				{
	                triggered[*it] = false;
                    pressed[*it] = false;
                    released[*it] = true;
					if ((*it) == repeatedKey)
					{
						repeatedKey = -1;
						repeatedCount = 0;
					}
				}
			}
            else
			{
                released[*it] = false;
			}
		}
		return Qnil;
	}
	
	VALUE Input::rb_dir4(VALUE self)
	{
		if (Input::isPressed(DOWN))
		{
			return INT2FIX(2);
		}
		if (Input::isPressed(LEFT))
		{
			return INT2FIX(4);
		}
		if (Input::isPressed(RIGHT))
		{
			return INT2FIX(6);
		}
		if (Input::isPressed(UP))
		{
			return INT2FIX(8);
		}
		return INT2FIX(0);
	}

	VALUE Input::rb_dir8(VALUE self)
	{
		bool down = Input::isPressed(DOWN);
		bool left = Input::isPressed(LEFT);
		if (down && left)
		{
			return INT2FIX(1);
		}
		bool right = Input::isPressed(RIGHT);
		if (down && right)
		{
			return INT2FIX(3);
		}
		bool up = Input::isPressed(UP);
		if (up && left)
		{
			return INT2FIX(7);
		}
		if (up && right)
		{
			return INT2FIX(9);
		}
		if (down)
		{
			return INT2FIX(2);
		}
		if (left)
		{
			return INT2FIX(4);
		}
		if (right)
		{
			return INT2FIX(6);
		}
		if (up)
		{
			return INT2FIX(8);
		}
		return INT2FIX(0);
	}

	VALUE Input::rb_trigger(VALUE self, VALUE keycode)
	{
		return (Input::isTriggered((unsigned char)NUM2UINT(keycode)) ? Qtrue : Qfalse);
	}

	VALUE Input::rb_press(VALUE self, VALUE keycode)
	{
		return (Input::isPressed((unsigned char)NUM2UINT(keycode)) ? Qtrue : Qfalse);
	}

	VALUE Input::rb_repeat(VALUE self, VALUE keycode)
	{
		return (Input::isRepeated((unsigned char)NUM2UINT(keycode)) ? Qtrue : Qfalse);
	}

}
