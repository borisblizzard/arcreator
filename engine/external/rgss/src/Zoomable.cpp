#include <ruby.h>

#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Graphics.h"
#include "Zoomable.h"
#include "Viewport.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Zoomable::initializeZoomable(VALUE rb_viewport)
	{
		this->initializeSourceRenderer(rb_viewport);
		this->zoomX = 1.0f;
		this->zoomY = 1.0f;
		this->blendType = Normal;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Zoomable::gc_mark(Zoomable* zoomable)
	{
		SourceRenderer::gc_mark(zoomable);
	}

	void Zoomable::gc_free(Zoomable* zoomable)
	{
		SourceRenderer::gc_free(zoomable);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Zoomable::rb_getZoomX(VALUE self)
	{
		RB_SELF2CPP(Zoomable, zoomable);
		return rb_float_new(zoomable->zoomX);
	}

	VALUE Zoomable::rb_setZoomX(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Zoomable, zoomable);
		zoomable->zoomX = (float)NUM2DBL(value);
		return value;
	}

	VALUE Zoomable::rb_getZoomY(VALUE self)
	{
		RB_SELF2CPP(Zoomable, zoomable);
		return rb_float_new(zoomable->zoomY);
	}

	VALUE Zoomable::rb_setZoomY(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Zoomable, zoomable);
		zoomable->zoomY = (float)NUM2DBL(value);
		return value;
	}

	VALUE Zoomable::rb_getBlendType(VALUE self)
	{
		RB_SELF2CPP(Zoomable, zoomable);
		return INT2NUM((int)zoomable->blendType);
	}

	VALUE Zoomable::rb_setBlendType(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Zoomable, zoomable);
		zoomable->blendType = (BlendType)hclamp(NUM2INT(value), 0, 2);
		return value;
	}


}
