#include <ruby.h>

#include "RGSSError.h"

namespace rgss
{
	VALUE rb_eRGSSError;

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void RGSSError::init()
	{
	}

	void RGSSError::destroy()
	{
	}

	void RGSSError::createRubyInterface()
	{
		rb_eRGSSError = rb_define_class("RGSSError", rb_eStandardError);
		rb_define_method(rb_eRGSSError, "_arc_dump", RUBY_METHOD_FUNC(&RGSSError::rb_arcDump), 0);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE RGSSError::rb_arcDump(VALUE self)
	{
		rb_raise(rb_eTypeError, "can't arc-dump RGSSError");
		return Qnil;
	}

}
