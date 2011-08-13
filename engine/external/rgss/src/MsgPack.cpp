#include <ruby.h>

#include "MsgPack.h"
#include "CodeSnippets.h"

namespace rgss
{
	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	VALUE rb_mMsgPack;

	void MsgPack::init()
	{
		// not being called at all
	}

	void MsgPack::destroy()
	{
		// not being called at all
	}

	void MsgPack::createRubyInterface()
	{
		rb_mMsgPack = rb_define_module("MsgPack");
		rb_define_module_function(rb_mMsgPack, "dump", RUBY_METHOD_FUNC(&MsgPack::rb_dump), 2);
		rb_define_module_function(rb_mMsgPack, "load", RUBY_METHOD_FUNC(&MsgPack::rb_load), 1);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE MsgPack::rb_dump(VALUE self, VALUE stream, VALUE object)
	{
		/// @todo
		return Qnil;
	}

	VALUE MsgPack::rb_load(VALUE self, VALUE stream)
	{
		/// @todo
		return Qnil;
	}
	
}
