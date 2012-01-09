#include <ruby.h>

#include <hltypes/util.h>

#include "Bitmap.h"
#include "CodeSnippets.h"
#include "Graphics.h"
#include "RGSSError.h"
#include "SourceRenderer.h"
#include "Viewport.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void SourceRenderer::initializeSourceRenderer(VALUE rb_viewport)
	{
		CPP_GENERATE_INITIALIZER(Viewport, viewport);
		this->initializeRenderable(NIL_P(this->rb_viewport) ? Graphics::renderQueue : this->viewport->renderQueue);
		this->opacity = 255;
		this->rb_bitmap = Qnil;
		this->bitmap = NULL;
	}

	void SourceRenderer::setOpacity(int value)
	{
		this->opacity = hclamp(value, 0, 255);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void SourceRenderer::gc_mark(SourceRenderer* sourceRenderer)
	{
		if (!NIL_P(sourceRenderer->rb_viewport))
		{
			rb_gc_mark(sourceRenderer->rb_viewport);
		}
		if (!NIL_P(sourceRenderer->rb_bitmap))
		{
			rb_gc_mark(sourceRenderer->rb_bitmap);
		}
		Renderable::gc_mark(sourceRenderer);
	}

	void SourceRenderer::gc_free(SourceRenderer* sourceRenderer)
	{
		sourceRenderer->rb_viewport = Qnil;
		sourceRenderer->viewport = NULL;
		sourceRenderer->rb_bitmap = Qnil;
		sourceRenderer->bitmap = NULL;
		Renderable::gc_free(sourceRenderer);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE SourceRenderer::rb_getX(VALUE self)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED_1(sourceRenderer);
		return INT2NUM(sourceRenderer->x);
	}

	VALUE SourceRenderer::rb_setX(VALUE self, VALUE value)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED_1(sourceRenderer);
		sourceRenderer->x = NUM2INT(value);
		return value;
	}

	VALUE SourceRenderer::rb_getY(VALUE self)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED_1(sourceRenderer);
		return INT2NUM(sourceRenderer->y);
	}

	VALUE SourceRenderer::rb_setY(VALUE self, VALUE value)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED_1(sourceRenderer);
		sourceRenderer->y = NUM2INT(value);
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

	VALUE SourceRenderer::rb_getOpacity(VALUE self)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED_1(sourceRenderer);
		return INT2NUM(sourceRenderer->opacity);
	}

	VALUE SourceRenderer::rb_setOpacity(VALUE self, VALUE value)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED_1(sourceRenderer);
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
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED_1(sourceRenderer);
		if (!NIL_P(value))
		{
			RB_CHECK_TYPE_1(value, rb_cBitmap);
			RB_VAR2CPP(value, Bitmap, bitmap);
			sourceRenderer->bitmap = bitmap;
		}
		else
		{
			sourceRenderer->bitmap = NULL;
		}
		sourceRenderer->rb_bitmap = value;
		return value;
	}

}
