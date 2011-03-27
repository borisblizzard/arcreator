#include <ruby.h>

#include <hltypes/hstring.h>

#include "RGSSError.h"
#include "CodeSnippets.h"

namespace rgss 
{
	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void RGSSError::init()
	{
	}

	void RGSSError::createRubyInterface()
	{
		rb_cRGSSError = rb_define_class("RGSSError", rb_cObject);
		rb_define_alloc_func(rb_cRGSSError, &RGSSError::rb_new);
		// initialize
		rb_define_method(rb_cRGSSError, "initialize", RUBY_METHOD_FUNC(&RGSSError::rb_initialize), -1);
		// getters/setters
		rb_define_method(rb_cRGSSError, "exception", RUBY_METHOD_FUNC(&RGSSError::rb_getException), 0);
		rb_define_method(rb_cRGSSError, "message", RUBY_METHOD_FUNC(&RGSSError::rb_getMessage), 0);
		rb_define_method(rb_cRGSSError, "backtrace", RUBY_METHOD_FUNC(&RGSSError::rb_getBacktrace), 0);
		rb_define_method(rb_cRGSSError, "to_s", RUBY_METHOD_FUNC(&RGSSError::rb_getString), 0);
		rb_define_method(rb_cRGSSError, "set_backtrace", RUBY_METHOD_FUNC(&RGSSError::rb_setBacktrace), 1);
	}

	VALUE RGSSError::wrap()
	{
		RGSSError* rgssError = this;
		return Data_Wrap_Struct(rb_cRGSSError, NULL, NULL, rgssError);
	}

	VALUE RGSSError::rb_new(VALUE classe)
	{
		return classe;
	}

	VALUE RGSSError::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		return self;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE RGSSError::rb_getException(VALUE self)
	{
		return self;
	}

	VALUE RGSSError::rb_getMessage(VALUE self)
	{
		return self;
	}

	VALUE RGSSError::rb_getBacktrace(VALUE self)
	{
		return self;
	}

	VALUE RGSSError::rb_getString(VALUE self)
	{
		return self;
	}

	VALUE RGSSError::rb_setBacktrace(VALUE self, VALUE value)
	{
		return self;
	}
	
}
