#include <ruby.h>

#include <hltypes/harray.h>
#include <hltypes/hfile.h>
#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "ARC.h"

namespace zer0
{
	VALUE rb_mARC;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	hstr ARC::Version;
	
	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void ARC::init()
	{
		Version = "1.0.0";
	}

	void ARC::destroy()
	{
	}

	void ARC::createRubyInterface()
	{
		rb_mARC = rb_define_module("ARC");
		rb_define_const(rb_mARC, "Version", rb_str_new2(Version.c_str()));
		rb_define_module_function(rb_mARC, "test", RUBY_METHOD_FUNC(&ARC::rb_test), 1);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE ARC::rb_test(VALUE self, VALUE param)
	{
		return rb_str_new2("works");
	}

}
