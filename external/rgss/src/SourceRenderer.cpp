#include <ruby.h>

#include <hltypes/util.h>

#include "Bitmap.h"
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
		this->opacity = 255;
		this->rb_bitmap = Qnil;
		this->bitmap = NULL;
		this->rb_viewport = Qnil;
		this->viewport = NULL;
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
		if (!NIL_P(sourceRenderer->rb_viewport))
		{
			rb_gc_mark(sourceRenderer->rb_viewport);
		}
		Renderable::gc_mark(sourceRenderer);
	}

	void SourceRenderer::gc_free(SourceRenderer* sourceRenderer)
	{
		sourceRenderer->rb_bitmap = Qnil;
		sourceRenderer->bitmap = NULL;
		sourceRenderer->rb_viewport = Qnil;
		sourceRenderer->viewport = NULL;
		Renderable::gc_free(sourceRenderer);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE SourceRenderer::rb_getOpacity(VALUE self)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		return INT2NUM(sourceRenderer->opacity);
	}

	VALUE SourceRenderer::rb_setOpacity(VALUE self, VALUE value)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		sourceRenderer->opacity = hclamp(NUM2INT(value), 0, 255);
		return value;
	}

	VALUE SourceRenderer::rb_getBitmap(VALUE self)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		return sourceRenderer->rb_bitmap;
	}

	VALUE SourceRenderer::rb_setBitmap(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(SourceRenderer, sourceRenderer, Bitmap, bitmap);
		return value;
	}

	VALUE SourceRenderer::rb_getViewport(VALUE self)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		return sourceRenderer->rb_viewport;
	}

	VALUE SourceRenderer::rb_setViewport(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(SourceRenderer, sourceRenderer, Viewport, viewport);
		return value;
	}

}
