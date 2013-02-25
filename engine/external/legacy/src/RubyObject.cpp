#include "CodeSnippets.h"
#include "RubyObject.h"

namespace legacy
{
	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	RubyObject::RubyObject()
	{
	}
	
	RubyObject::~RubyObject()
	{
	}

	void RubyObject::mark()
	{
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void RubyObject::gc_mark(RubyObject* rubyObject)
	{
		rubyObject->mark();
	}

	void RubyObject::gc_free(RubyObject* rubyObject)
	{
		RB_OBJECT_DELETE(rubyObject);
	}

}
