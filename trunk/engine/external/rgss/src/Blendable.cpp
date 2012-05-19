#include <ruby.h>

#include <hltypes/hltypesUtil.h>

#include "Blendable.h"
#include "CodeSnippets.h"
#include "RGSSError.h"

namespace rgss
{
	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	Blendable::Blendable() : SourceRenderer()
	{
		this->blendType = Normal;
	}

	Blendable::Blendable(Viewport* viewport) : SourceRenderer(viewport)
	{
		this->blendType = Normal;
	}

	Blendable::~Blendable()
	{
		this->dispose();
	}

	void Blendable::initialize(VALUE rb_viewport)
	{
		SourceRenderer::initialize(rb_viewport);
		this->blendType = Normal;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Blendable::rb_getBlendType(VALUE self)
	{
		RB_SELF2CPP(Blendable, blendable);
		RB_CHECK_DISPOSED(blendable);
		return INT2NUM((int)blendable->blendType);
	}

	VALUE Blendable::rb_setBlendType(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Blendable, blendable);
		RB_CHECK_DISPOSED(blendable);
		blendable->blendType = (BlendType)hclamp(NUM2INT(value), 0, 2);
		return value;
	}


}
