#include <ruby.h>

#include "Bitmap.h"
#include "Graphics.h"
#include "Viewport.h"
#include "SourceRenderer.h"
#include "CodeSnippets.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void SourceRenderer::initializeSourceRenderer()
	{
		this->initializeRenderable();
		this->rb_bitmap = Qnil;
		this->bitmap = NULL;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void SourceRenderer::gc_mark(SourceRenderer* sourceRenderer)
	{
		if (!NIL_P(sourceRenderer->rb_bitmap))
		{
			rb_gc_mark(sourceRenderer->rb_bitmap);
		}
		Renderable::gc_mark(sourceRenderer);
	}

	void SourceRenderer::gc_free(SourceRenderer* sourceRenderer)
	{
		sourceRenderer->rb_bitmap = Qnil;
		sourceRenderer->bitmap = NULL;
		Renderable::gc_free(sourceRenderer);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE SourceRenderer::rb_getBitmap(VALUE self)
	{
		RB_SELF2CPP(SourceRenderer, sprite);
		return sprite->rb_bitmap;
	}

	VALUE SourceRenderer::rb_setBitmap(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(SourceRenderer, sourceRenderer, Bitmap, bitmap);
		return value;
	}

}
