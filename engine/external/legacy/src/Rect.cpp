#include <ruby.h>

#include <gtypes/Rectangle.h>
#include <hltypes/hltypesUtil.h>

#include "CodeSnippets.h"
#include "Rect.h"

namespace legacy
{
	VALUE rb_cRect;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	Rect::Rect() : RubyObject()
	{
		this->set(0, 0, 0, 0);
	}
	
	Rect::Rect(int x, int y, int width, int height) : RubyObject()
	{
		this->set(x, y, width, height);
	}
	
	Rect::~Rect()
	{
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Rect::set(int x, int y, int width, int height)
	{
		this->x = x;
		this->y = y;
		this->width = width;
		this->height = height;
	}

	grect Rect::toGRect()
	{
		return grect((float)this->x, (float)this->y, (float)this->width, (float)this->height);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Rect::init()
	{
	}

	void Rect::destroy()
	{
	}

	void Rect::createRubyInterface()
	{
		rb_cRect = rb_define_class("Rect", rb_cObject);
		rb_define_alloc_func(rb_cRect, &Rect::rb_new);
		// initialize
		rb_define_method(rb_cRect, "initialize", RUBY_METHOD_FUNC(&Rect::rb_initialize), 4);
		rb_define_method(rb_cRect, "initialize_copy", RUBY_METHOD_FUNC(&Rect::rb_initialize_copy), 1);
		rb_define_method(rb_cRect, "inspect", RUBY_METHOD_FUNC(&Rect::rb_inspect), 0);
		rb_define_method(rb_cRect, "_arc_dump", RUBY_METHOD_FUNC(&Rect::rb_arcDump), 0);
		// getters and setters
		rb_define_method(rb_cRect, "x", RUBY_METHOD_FUNC(&Rect::rb_getX), 0);
		rb_define_method(rb_cRect, "x=", RUBY_METHOD_FUNC(&Rect::rb_setX), 1);
		rb_define_method(rb_cRect, "y", RUBY_METHOD_FUNC(&Rect::rb_getY), 0);
		rb_define_method(rb_cRect, "y=", RUBY_METHOD_FUNC(&Rect::rb_setY), 1);
		rb_define_method(rb_cRect, "width", RUBY_METHOD_FUNC(&Rect::rb_getWidth), 0);
		rb_define_method(rb_cRect, "width=", RUBY_METHOD_FUNC(&Rect::rb_setWidth), 1);
		rb_define_method(rb_cRect, "height", RUBY_METHOD_FUNC(&Rect::rb_getHeight), 0);
		rb_define_method(rb_cRect, "height=", RUBY_METHOD_FUNC(&Rect::rb_setHeight), 1);
		// methods
		rb_define_method(rb_cRect, "set", RUBY_METHOD_FUNC(&Rect::rb_set), 4);
		rb_define_method(rb_cRect, "empty", RUBY_METHOD_FUNC(&Rect::rb_empty), 0);
	}

	VALUE Rect::rb_new(VALUE classe)
	{
		Rect* rect;
		return RB_OBJECT_NEW(classe, Rect, rect, &Rect::gc_mark, &Rect::gc_free);
	}

	VALUE Rect::rb_initialize(VALUE self, VALUE x, VALUE y, VALUE width, VALUE height)
	{
		Rect::rb_set(self, x, y, width, height);
		return self;
	}

	VALUE Rect::rb_initialize_copy(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Rect, rect);
		RB_VAR2CPP(original, Rect, other);
		rect->x = other->x;
		rect->y = other->y;
		rect->width = other->width;
		rect->height = other->height;
		return self;
	}

	VALUE Rect::rb_inspect(VALUE self)
	{
		RB_SELF2CPP(Rect, rect);
		hstr result = hsprintf("(%d,%d,%d,%d)", rect->x, rect->y, rect->width, rect->height);
		return rb_str_new2(result.c_str());
	}

	VALUE Rect::create(VALUE x, VALUE y, VALUE width, VALUE height)
	{
		VALUE object = Rect::rb_new(rb_cRect);
		object = Rect::rb_initialize(object, x, y, width, height);
		return object;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Rect::rb_getX(VALUE self)
	{
		RB_SELF2CPP(Rect, rect);
		return INT2FIX(rect->x);
	}

	VALUE Rect::rb_setX(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Rect, rect);
		rect->x = NUM2INT(value);
		return value;
	}

	VALUE Rect::rb_getY(VALUE self)
	{
		RB_SELF2CPP(Rect, rect);
		return INT2FIX(rect->y);
	}

	VALUE Rect::rb_setY(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Rect, rect);
		rect->y = NUM2INT(value);
		return value;
	}

	VALUE Rect::rb_getWidth(VALUE self)
	{
		RB_SELF2CPP(Rect, rect);
		return INT2FIX(rect->width);
	}

	VALUE Rect::rb_setWidth(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Rect, rect);
		rect->width = INT2FIX(value);
		return value;
	}

	VALUE Rect::rb_getHeight(VALUE self)
	{
		RB_SELF2CPP(Rect, rect);
		return INT2FIX(rect->height);
	}

	VALUE Rect::rb_setHeight(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Rect, rect);
		rect->height = NUM2INT(value);
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Rect::rb_set(VALUE self, VALUE x, VALUE y, VALUE width, VALUE height)
	{
		RB_SELF2CPP(Rect, rect);
		rect->x = NUM2INT(x);
		rect->y = NUM2INT(y);
		rect->width = NUM2INT(width);
		rect->height = NUM2INT(height);
		return Qnil;
	}

	VALUE Rect::rb_empty(VALUE self)
	{
		RB_SELF2CPP(Rect, rect);
		rect->set(0, 0, 0, 0);
		return Qnil;
	}

	VALUE Rect::rb_arcDump(VALUE self)
	{
		rb_raise(rb_eTypeError, "Can't arc-dump: Rect");
		return Qnil;
	}

}
