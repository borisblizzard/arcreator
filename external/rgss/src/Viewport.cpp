#include <ruby.h>

#include <hltypes/hstring.h>

#include "Color.h"
#include "Rect.h"
#include "Tone.h"
#include "Viewport.h"
#include "CodeSnippets.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cViewport;

	void Viewport::draw()
	{
		this->_render();
	}

	void Viewport::_render()
	{
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Viewport::init()
	{
	}

	void Viewport::createRubyInterface()
	{
		rb_cViewport = rb_define_class("Viewport", rb_cObject);
		rb_define_alloc_func(rb_cViewport, &Viewport::rb_new);
		// initialize
		rb_define_method(rb_cViewport, "initialize", RUBY_METHOD_FUNC(&Viewport::rb_initialize), -1);
		rb_define_method(rb_cViewport, "dispose", RUBY_METHOD_FUNC(&Viewport::rb_dispose), 0);
		// getters and setters
		rb_define_method(rb_cViewport, "visible", RUBY_METHOD_FUNC(&Viewport::rb_getVisible), 0);
		rb_define_method(rb_cViewport, "visible=", RUBY_METHOD_FUNC(&Viewport::rb_setVisible), 1);
		rb_define_method(rb_cViewport, "z", RUBY_METHOD_FUNC(&Viewport::rb_getZ), 0);
		rb_define_method(rb_cViewport, "z=", RUBY_METHOD_FUNC(&Viewport::rb_setZ), 1);
		rb_define_method(rb_cViewport, "ox", RUBY_METHOD_FUNC(&Viewport::rb_getOX), 0);
		rb_define_method(rb_cViewport, "ox=", RUBY_METHOD_FUNC(&Viewport::rb_setOX), 1);
		rb_define_method(rb_cViewport, "oy", RUBY_METHOD_FUNC(&Viewport::rb_getOY), 0);
		rb_define_method(rb_cViewport, "oy=", RUBY_METHOD_FUNC(&Viewport::rb_setOY), 1);
		rb_define_method(rb_cViewport, "disposed?", RUBY_METHOD_FUNC(&Viewport::rb_isDisposed), 0);
		// methods
	}

	void Viewport::gc_mark(Viewport* viewport)
	{
		Renderable::gc_mark(viewport);
	}

	void Viewport::gc_free(Viewport* viewport)
	{
		Renderable::gc_free(viewport);
	}

	VALUE Viewport::rb_new(VALUE classe)
	{
		Viewport* viewport;
		VALUE result = Data_Make_Struct(rb_cViewport, Viewport, Viewport::gc_mark, Viewport::gc_free, viewport);
		viewport->disposed = true;
		viewport->type = TYPE_VIEWPORT;
		return result;
	}

	VALUE Viewport::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		if (argc != 1 && argc != 4)
		{
			hstr message = hsprintf("wrong number of arguments (%d for 1 or 4)", argc);
			rb_raise(rb_eArgError, message.c_str());
		}
		RB_SELF2CPP(Viewport, viewport);
		viewport->initializeRenderable();
		VALUE arg1, arg2, arg3, arg4;
		rb_scan_args(argc, argv, "13", &arg1, &arg2, &arg3, &arg4);
		if (NIL_P(arg2) && NIL_P(arg3) && NIL_P(arg4))
		{
			Viewport::rb_setRect(arg1, self);
		}
		else
		{
			Viewport::rb_setRect(Rect::create(arg1, arg2, arg3, arg4), self);
		}
		VALUE argv2[4] = {rb_float_new(0.0f), rb_float_new(0.0f), rb_float_new(0.0f), rb_float_new(0.0f)};
		Viewport::rb_setColor(Color::create(4, argv2), self);
		Viewport::rb_setTone(Tone::create(4, argv2), self);
		return self;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Viewport::rb_getColor(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		return viewport->rb_color;
	}

	VALUE Viewport::rb_setColor(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Viewport, sprite, Color, color);
		return value;
	}

	VALUE Viewport::rb_getRect(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		return viewport->rb_rect;
	}

	VALUE Viewport::rb_setRect(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Viewport, sprite, Rect, rect);
		return value;
	}

	VALUE Viewport::rb_getTone(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		return viewport->rb_tone;
	}

	VALUE Viewport::rb_setTone(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Viewport, sprite, Tone, tone);
		return value;
	}

	/****************************************************************************************
	 * TODO
	 ****************************************************************************************/

	void Viewport::flash(Color clr, int duration)
	{
			
	}
	
}
