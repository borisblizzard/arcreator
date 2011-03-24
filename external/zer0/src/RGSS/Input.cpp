#include <ruby.h>

#include <april/Keys.h>
#include <april/RenderSystem.h>
#include <april/Window.h>
#include <hltypes/hmap.h>

#include "RGSS/Input.h"
#include "CodeSnippets.h"
#include "Context.h"
#include "zer0.h"

namespace zer0
{
	namespace RGSS
	{
		hmap<int, harray<unsigned char>> conversions;

		void Input::createRubyInterface()
		{
			rb_mInput = rb_define_module("Input");
			rb_define_module_function(rb_mInput, "update", RUBY_METHOD_FUNC(&Input::update), 0);
			rb_define_module_function(rb_mInput, "dir4", RUBY_METHOD_FUNC(&Input::dir4), 0);
			rb_define_module_function(rb_mInput, "dir8", RUBY_METHOD_FUNC(&Input::dir8), 0);
			rb_define_module_function(rb_mInput, "trigger?", RUBY_METHOD_FUNC(&Input::trigger), 1);
			rb_define_module_function(rb_mInput, "repeat?", RUBY_METHOD_FUNC(&Input::repeat), 1);
			rb_define_module_function(rb_mInput, "press?", RUBY_METHOD_FUNC(&Input::press), 1);
			rb_define_const(rb_mInput, "DOWN", INT2NUM(Input::DOWN));
			rb_define_const(rb_mInput, "LEFT", INT2NUM(Input::LEFT));
			rb_define_const(rb_mInput, "RIGHT", INT2NUM(Input::RIGHT));
			rb_define_const(rb_mInput, "UP", INT2NUM(Input::UP));
			rb_define_const(rb_mInput, "A", INT2NUM(Input::A));
			rb_define_const(rb_mInput, "B", INT2NUM(Input::B));
			rb_define_const(rb_mInput, "C", INT2NUM(Input::C));
			rb_define_const(rb_mInput, "X", INT2NUM(Input::X));
			rb_define_const(rb_mInput, "Y", INT2NUM(Input::Y));
			rb_define_const(rb_mInput, "Z", INT2NUM(Input::Z));
			rb_define_const(rb_mInput, "L", INT2NUM(Input::L));
			rb_define_const(rb_mInput, "R", INT2NUM(Input::R));
			rb_define_const(rb_mInput, "SHIFT", INT2NUM(Input::SHIFT));
			rb_define_const(rb_mInput, "CTRL", INT2NUM(Input::CTRL));
			rb_define_const(rb_mInput, "ALT", INT2NUM(Input::ALT));
			rb_define_const(rb_mInput, "F5", INT2NUM(Input::F5));
			rb_define_const(rb_mInput, "F6", INT2NUM(Input::F6));
			rb_define_const(rb_mInput, "F7", INT2NUM(Input::F7));
			rb_define_const(rb_mInput, "F8", INT2NUM(Input::F8));
			rb_define_const(rb_mInput, "F9", INT2NUM(Input::F9));
		}

		void Input::init()
		{
			harray<unsigned char> keys;
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
		}

		VALUE Input::update(VALUE self)
		{
			zer0::context->update();
			april::rendersys->getWindow()->doEvents();
			return Qnil;
		}
	
		VALUE Input::dir4(VALUE self)
		{
			if (Input::isPressed(DOWN))
			{
				return INT2NUM(2);
			}
			if (Input::isPressed(LEFT))
			{
				return INT2NUM(4);
			}
			if (Input::isPressed(RIGHT))
			{
				return INT2NUM(6);
			}
			if (Input::isPressed(UP))
			{
				return INT2NUM(8);
			}
			return INT2NUM(0);
		}

		VALUE Input::dir8(VALUE self)
		{
			bool down = Input::isPressed(DOWN);
			bool left = Input::isPressed(LEFT);
			if (down && left)
			{
				return INT2NUM(1);
			}
			bool right = Input::isPressed(RIGHT);
			if (down && right)
			{
				return INT2NUM(3);
			}
			bool up = Input::isPressed(UP);
			if (up && left)
			{
				return INT2NUM(7);
			}
			if (up && right)
			{
				return INT2NUM(9);
			}
			if (down)
			{
				return INT2NUM(2);
			}
			if (left)
			{
				return INT2NUM(4);
			}
			if (right)
			{
				return INT2NUM(6);
			}
			if (up)
			{
				return INT2NUM(8);
			}
			return INT2NUM(0);
		}

		VALUE Input::trigger(VALUE self, VALUE keycode)
		{
			return (Input::isTriggered((unsigned char)NUM2UINT(keycode)) ? Qtrue : Qfalse);
		}

		VALUE Input::press(VALUE self, VALUE keycode)
		{
			return (Input::isPressed((unsigned char)NUM2UINT(keycode)) ? Qtrue : Qfalse);
		}

		VALUE Input::repeat(VALUE self, VALUE keycode)
		{
			return (Input::isRepeated((unsigned char)NUM2UINT(keycode)) ? Qtrue : Qfalse);
		}

		bool Input::isTriggered(unsigned char keycode)
		{
			if (!conversions.has_key(keycode))
			{
				zer0::log("Warning! Key is undefined! " + keycode);
				return false;
			}
			foreach (unsigned char, it, conversions[keycode])
			{
				if (zer0::context->isKeyTriggered(*it))
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
				zer0::log("Warning! Key is undefined! " + keycode);
				return false;
			}
			foreach (unsigned char, it, conversions[keycode])
			{
				if (zer0::context->isKeyPressed(*it))
				{
					return true;
				}
			}
			return false;
		}

		/// @todo isKeyPressed shouldn't be used here.
		bool Input::isRepeated(unsigned char keycode)
		{
			if (!conversions.has_key(keycode))
			{
				zer0::log("Warning! Key is undefined! " + keycode);
				return false;
			}
			foreach (unsigned char, it, conversions[keycode])
			{
				if (zer0::context->isKeyPressed(*it))
				{
					return true;
				}
			}
			return false;
		}

	}
}
