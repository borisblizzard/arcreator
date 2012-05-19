#include <ruby.h>

#include <hltypes/hltypesUtil.h>

#include "Bitmap.h"
#include "CodeSnippets.h"
#include "Graphics.h"
#include "RGSSError.h"
#include "SourceRenderer.h"
#include "Viewport.h"

namespace rgss
{
	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	SourceRenderer::SourceRenderer() : Renderable()
	{
		this->rb_viewport = Qnil;
		this->viewport = NULL;
		this->x = 0;
		this->y = 0;
		this->opacity = 255;
		this->rb_bitmap = Qnil;
		this->bitmap = NULL;
	}
	
	SourceRenderer::SourceRenderer(Viewport* viewport) :
		Renderable(viewport == NULL ? Graphics::renderQueue : viewport->renderQueue)
	{
		this->rb_viewport = Qnil;
		this->viewport = viewport;
		this->x = 0;
		this->y = 0;
		this->opacity = 255;
		this->rb_bitmap = Qnil;
		this->bitmap = NULL;
	}
	
	SourceRenderer::~SourceRenderer()
	{
		this->dispose();
		this->rb_bitmap = Qnil;
		this->bitmap = NULL;
	}

	void SourceRenderer::initialize(VALUE rb_viewport)
	{
		CPP_GENERATE_INITIALIZER(Viewport, viewport);
		Renderable::initialize(NIL_P(this->rb_viewport) ? Graphics::renderQueue : this->viewport->renderQueue);
		this->x = 0;
		this->y = 0;
		this->opacity = 255;
		this->rb_bitmap = Qnil;
		this->bitmap = NULL;
	}

	void SourceRenderer::dispose()
	{
		if (!this->disposed)
		{
			this->rb_viewport = Qnil;
			this->viewport = NULL;
		}
		Renderable::dispose();
	}

	void SourceRenderer::mark()
	{
		Renderable::mark();
		RB_GC_MARK(viewport);
		RB_GC_MARK(bitmap);
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void SourceRenderer::setOpacity(int value)
	{
		this->opacity = hclamp(value, 0, 255);
	}

	bool SourceRenderer::_canDraw()
	{
		return (this->opacity > 0 && this->bitmap != NULL && !this->bitmap->isDisposed() &&
			Renderable::_canDraw());
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE SourceRenderer::rb_getX(VALUE self)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED(sourceRenderer);
		return INT2NUM(sourceRenderer->x);
	}

	VALUE SourceRenderer::rb_setX(VALUE self, VALUE value)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED(sourceRenderer);
		sourceRenderer->x = NUM2INT(value);
		return value;
	}

	VALUE SourceRenderer::rb_getY(VALUE self)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED(sourceRenderer);
		return INT2NUM(sourceRenderer->y);
	}

	VALUE SourceRenderer::rb_setY(VALUE self, VALUE value)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED(sourceRenderer);
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
		RB_CHECK_DISPOSED(sourceRenderer);
		return INT2NUM(sourceRenderer->opacity);
	}

	VALUE SourceRenderer::rb_setOpacity(VALUE self, VALUE value)
	{
		RB_SELF2CPP(SourceRenderer, sourceRenderer);
		RB_CHECK_DISPOSED(sourceRenderer);
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
		RB_CHECK_DISPOSED(sourceRenderer);
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
