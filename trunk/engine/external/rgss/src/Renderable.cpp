#include <ruby.h>

#include "CodeSnippets.h"
#include "Plane.h"
#include "Renderable.h"
#include "RenderQueue.h"
#include "Sprite.h"
#include "Tilemap.h"
#include "Viewport.h"
#include "Window.h"

namespace rgss
{
	unsigned int Renderable::CounterProgress;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Renderable::initializeRenderable(RenderQueue* renderQueue)
	{
		this->disposed = false;
		this->visible = true;
		this->z = 0;
		VALUE argv[3] = {INT2FIX(255), INT2FIX(255), INT2FIX(255)};
		this->rb_color = Color::create(3, argv);
		RB_VAR2CPP(this->rb_color, Color, color);
		this->color = color;
		this->rb_tone = Tone::create(3, argv);
		RB_VAR2CPP(this->rb_tone, Tone, tone);
		this->tone = tone;
		this->rb_flashColor = Qnil;
		this->flashColor = NULL;
		this->flashDuration = 0;
		this->flashTimer = 0;
		this->counterId = CounterProgress;
		CounterProgress++;
		this->renderQueue = renderQueue;
		this->renderQueue->add(this);
	}

	void Renderable::setZ(int value)
	{
		if (this->z != value)
		{
			this->z = value;
			this->renderQueue->update(this);
		}
	}

	void Renderable::draw()
	{
		if (!this->visible || this->isDisposed())
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

	void Renderable::update()
	{
		if (this->isDisposed() || !this->visible)
		{
			return;
		}
		switch (this->type)
		{
		case TYPE_TILEMAP:
			((Tilemap*)this)->update();
			break;
		}
	}

	void Renderable::updateFlash()
	{
		this->flashTimer++;
		if (this->flashTimer >= this->flashDuration && this->flashColor != NULL)
		{
			this->rb_flashColor = Qnil;
			this->flashColor = NULL;
		}
	}

	void Renderable::dispose()
	{
		this->rb_color = Qnil;
		this->color = NULL;
		this->rb_tone = Qnil;
		this->tone = NULL;
		if (!this->disposed)
		{
			this->disposed = true;
			this->renderQueue->remove(this);
			switch (this->type)
			{
			case TYPE_VIEWPORT:
				((Viewport*)this)->dispose();
				break;
			case TYPE_WINDOW:
				((Window*)this)->dispose();
				break;
			}
		}
	}

	april::Color Renderable::_getRenderColor()
	{
		april::Color result = this->color->toAprilColor();
		if (this->flashTimer < this->flashDuration)
		{
			float ratio = (float)this->flashTimer / this->flashDuration;
			result = result * ratio + this->flashColor->toAprilColor() * (1.0f - ratio);
		}
		return result;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Renderable::gc_mark(Renderable* renderable)
	{
		if (!NIL_P(renderable->rb_color))
		{
			rb_gc_mark(renderable->rb_color);
		}
		if (!NIL_P(renderable->rb_tone))
		{
			rb_gc_mark(renderable->rb_tone);
		}
		if (!NIL_P(renderable->rb_flashColor))
		{
			rb_gc_mark(renderable->rb_flashColor);
		}
	}

	void Renderable::gc_free(Renderable* renderable)
	{
		renderable->dispose();
	}

	VALUE Renderable::rb_dispose(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		renderable->dispose();
		return Qnil;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Renderable::rb_isDisposed(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		return (renderable->disposed ? Qtrue : Qfalse);
	}

	VALUE Renderable::rb_getVisible(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		return (renderable->visible ? Qtrue : Qfalse);
	}

	VALUE Renderable::rb_setVisible(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		renderable->visible = (bool)RTEST(value);
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
		renderable->setZ(NUM2INT(value));
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

	VALUE Renderable::rb_getColor(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		return renderable->rb_color;
	}

	VALUE Renderable::rb_setColor(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Renderable, renderable, Color, color);
		return value;
	}

	VALUE Renderable::rb_getTone(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		return renderable->rb_tone;
	}

	VALUE Renderable::rb_setTone(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Renderable, renderable, Tone, tone);
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Renderable::rb_flash(VALUE self, VALUE color, VALUE duration)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED_1(renderable);
		renderable->flashTimer = 0;
		renderable->flashDuration = hmax(NUM2INT(duration), 0);
		renderable->rb_flashColor = color;
		if (!NIL_P(color) && renderable->flashDuration > 0)
		{
			renderable->rb_flashColor = color;
			RB_VAR2CPP(color, Color, flashColor);
			renderable->flashColor = flashColor;
		}
		else
		{
			renderable->rb_flashColor = Qnil;
			renderable->flashColor = NULL;
		}
		return Qnil;
	}

	VALUE Renderable::rb_arcDump(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		rb_raise(rb_eTypeError, ("can't arc-dump " + renderable->typeName).c_str());
		return Qnil;
	}

}
