#include <ruby.h>

#include "Graphics.h"
#include "Plane.h"
#include "Renderable.h"
#include "Sprite.h"
#include "Tilemap.h"
#include "Viewport.h"
#include "Window.h"
#include "CodeSnippets.h"
#include "RenderQueue.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	/// @todo Should be probably changed so the Renderable instance refers to the RenderQueue where it's stored.
	void Renderable::initializeRenderable()
	{
		this->disposed = false;
		this->visible = true;
		Graphics::renderQueue.add(this);
	}

	void Renderable::draw()
	{
		if (!this->visible)
		{
			return;
		}
		switch (this->type)
		{
		case TYPE_VIEWPORT:
			((Viewport*)this)->draw();
			break;
		case TYPE_SPRITE:
			((Sprite*)this)->draw();
			break;
		case TYPE_PLANE:
			((Plane*)this)->draw();
			break;
		case TYPE_WINDOW:
			((Window*)this)->draw();
			break;
		}
	}

	void Renderable::dispose()
	{
		if (!this->disposed)
		{
			this->disposed = true;
			Graphics::renderQueue.remove(this);
		}
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Renderable::gc_mark(Renderable* renderable)
	{
	}

	void Renderable::gc_free(Renderable* renderable)
	{
		Graphics::renderQueue.remove(renderable);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Renderable::rb_getVisible(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		return (renderable->visible ? Qtrue : Qfalse);
	}

	VALUE Renderable::rb_setVisible(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		renderable->visible = (value != Qfalse && value != Qnil);
		return value;
	}

	VALUE Renderable::rb_getZ(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		return INT2NUM(renderable->z);
	}

	VALUE Renderable::rb_setZ(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		int z = NUM2INT(value);
		if (renderable->z != z)
		{
			renderable->z = z;
			Graphics::renderQueue.update(renderable);
		}
		return value;
	}

	VALUE Renderable::rb_getOX(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		return INT2NUM(-renderable->ox);
	}

	VALUE Renderable::rb_setOX(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		renderable->ox = -NUM2INT(value);
		return value;
	}

	VALUE Renderable::rb_getOY(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		return INT2NUM(-renderable->oy);
	}

	VALUE Renderable::rb_setOY(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		renderable->oy = -NUM2INT(value);
		return value;
	}

	VALUE Renderable::rb_isDisposed(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		return (renderable->disposed ? Qtrue : Qfalse);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Renderable::rb_dispose(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		renderable->dispose();
		return Qnil;
	}

}
