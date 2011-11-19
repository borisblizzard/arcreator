#include <ruby.h>

#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Blendable.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Blendable::initializeBlendable(VALUE rb_viewport)
	{
		this->initializeSourceRenderer(rb_viewport);
		this->blendType = Normal;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Blendable::gc_mark(Blendable* blendable)
	{
		SourceRenderer::gc_mark(blendable);
	}

	void Blendable::gc_free(Blendable* blendable)
	{
		SourceRenderer::gc_free(blendable);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Blendable::rb_getBlendType(VALUE self)
	{
		RB_SELF2CPP(Blendable, blendable);
		return INT2NUM((int)blendable->blendType);
	}

	VALUE Blendable::rb_setBlendType(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Blendable, blendable);
		blendable->blendType = (BlendType)hclamp(NUM2INT(value), 0, 2);
		return value;
	}


}
