#include <ruby.h>

#include "ARC.h"
#include "ARC_Error.h"

namespace reactor
{
	VALUE rb_eARC_Error;

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void ARC_Error::init()
	{
	}

	void ARC_Error::destroy()
	{
	}

	void ARC_Error::createRubyInterface()
	{
		rb_eARC_Error = rb_define_class_under(rb_mARC, "Error", rb_eStandardError);
	}

}
