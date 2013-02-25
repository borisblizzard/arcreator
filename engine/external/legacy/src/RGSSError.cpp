#include <ruby.h>

#include "CodeSnippets.h"
#include "RGSSError.h"

namespace legacy
{
	VALUE rb_eRGSSError;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	RGSSError::RGSSError() : RubyObject()
	{
	}
	
	RGSSError::~RGSSError()
	{
	}

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

	VALUE RGSSError::rb_new(VALUE classe)
	{
		RGSSError* rgssError;
		return RB_OBJECT_NEW(classe, RGSSError, rgssError, &RGSSError::gc_mark, &RGSSError::gc_free);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE RGSSError::rb_arcDump(VALUE self)
	{
		rb_raise(rb_eTypeError, "Can't arc-dump: RGSSError");
		return Qnil;
	}

}
