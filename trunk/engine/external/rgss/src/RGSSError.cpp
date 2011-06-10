#include <ruby.h>

#include "RGSSError.h"

namespace rgss 
{
	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	VALUE rb_eRGSSError;

	void RGSSError::init()
	{
	}

	void RGSSError::createRubyInterface()
	{
		rb_eRGSSError = rb_define_class("RGSSError", rb_eStandardError);
	}

}
