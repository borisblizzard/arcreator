#include <ruby.h>

#include <april/Color.h>
#include <april/PixelShader.h>
#include <april/RenderSystem.h>
#include <gtypes/Rectangle.h>

#include "CodeSnippets.h"
#include "Plane.h"
#include "Rect.h"
#include "Renderable.h"
#include "RenderQueue.h"
#include "legacy.h"
#include "RGSSError.h"
#include "Sprite.h"
#include "SystemSprite.h"
#include "Tilemap.h"
#include "Tone.h"
#include "Viewport.h"
#include "Window.h"

namespace legacy
{
	unsigned int Renderable::CounterProgress;
	extern april::PixelShader* pixelShader;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	Renderable::Renderable() : RubyObject()
	{
		this->disposed = true;
		this->visible = true;
		this->z = 0;
		this->ox = 0;
		this->oy = 0;
		this->zoom.set(1.0f, 1.0f);
		this->rb_color = Qnil;
		this->color = NULL;
		this->rb_tone = Qnil;
		this->tone = NULL;
		this->rb_flashColor = Qnil;
		this->flashColor = NULL;
		this->flashDuration = 0;
		this->flashTimer = 0;
		this->counterId = CounterProgress;
		CounterProgress++;
		this->renderQueue = NULL;
	}
	
	Renderable::Renderable(RenderQueue* renderQueue) : RubyObject()
	{
		this->disposed = false;
		this->visible = true;
		this->z = 0;
		this->ox = 0;
		this->oy = 0;
		this->zoom.set(1.0f, 1.0f);
		this->rb_color = Qnil;
		this->color = new Color(0.0f, 0.0f, 0.0f, 0.0f);
		this->rb_tone = Qnil;
		this->tone = new Tone(0.0f, 0.0f, 0.0f, 0.0f);
		this->rb_flashColor = Qnil;
		this->flashColor = NULL;
		this->flashDuration = 0;
		this->flashTimer = 0;
		this->counterId = CounterProgress;
		CounterProgress++;
		this->renderQueue = renderQueue;
		this->renderQueue->add(this);
	}

	Renderable::~Renderable()
	{
		this->dispose();
	}

	void Renderable::initialize(RenderQueue* renderQueue)
	{
		this->disposed = false;
		this->visible = true;
		this->z = 0;
		this->ox = 0;
		this->oy = 0;
		this->zoom.set(1.0f, 1.0f);
		VALUE argv[4] = {INT2FIX(0), INT2FIX(0), INT2FIX(0), INT2FIX(0)};
		this->rb_color = Color::create(4, argv);
		RB_VAR2CPP(this->rb_color, Color, color);
		this->color = color;
		this->rb_tone = Tone::create(4, argv);
		RB_VAR2CPP(this->rb_tone, Tone, tone);
		this->tone = tone;
		this->rb_flashColor = Qnil;
		this->flashColor = NULL;
		this->flashDuration = 0;
		this->flashTimer = 0;
		this->renderQueue = renderQueue;
		this->renderQueue->add(this);
	}

	void Renderable::dispose()
	{
		if (!this->disposed)
		{
			CPP_VAR_DELETE(color);
			CPP_VAR_DELETE(tone);
			this->rb_color = Qnil;
			this->color = NULL;
			this->rb_tone = Qnil;
			this->tone = NULL;
			this->rb_flashColor = Qnil;
			this->flashColor = NULL;
			this->disposed = true;
			this->renderQueue->remove(this);
		}
	}

	void Renderable::mark()
	{
		RubyObject::mark();
		RB_GC_MARK(color);
		RB_GC_MARK(tone);
		RB_GC_MARK(flashColor);
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Renderable::setZ(int value)
	{
		if (this->z != value)
		{
			this->z = value;
			this->renderQueue->reorder(this);
		}
	}

	void Renderable::draw()
	{
	}

	void Renderable::update()
	{
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

	bool Renderable::_canDraw()
	{
		return (this->visible && !this->disposed && this->zoom.x != 0.0f && this->zoom.y != 0.0f);
	}

	april::Color Renderable::_getRenderColor()
	{
		april::Color result = this->color->toAprilColor();
		if (this->flashDuration > 0 && this->flashTimer < this->flashDuration)
		{
			float ratio = (float)this->flashTimer / this->flashDuration;
			result = result * ratio + this->flashColor->toAprilColor() * (1.0f - ratio);
		}
		return result;
	}

	void Renderable::_renderTexture(grect drawRect, grect srcRect, april::Texture* texture, unsigned char opacity)
	{
		april::rendersys->setTexture(texture);
		april::rendersys->setPixelShader(legacy::pixelShader);
		static float quadVectors[12] = {0.0f};
		quadVectors[3] = opacity / 255.0f;
		april::Color color = this->_getRenderColor();
		quadVectors[4] = color.r_f();
		quadVectors[5] = color.g_f();
		quadVectors[6] = color.b_f();
		quadVectors[7] = color.a_f();
		quadVectors[8] = (this->tone->red + 255) / 510.0f;
		quadVectors[9] = (this->tone->green + 255) / 510.0f;
		quadVectors[10] = (this->tone->blue + 255) / 510.0f;
		quadVectors[11] = (255 - this->tone->gray) / 255.0f;
		legacy::pixelShader->setConstantsF(quadVectors, 3);
		april::rendersys->drawTexturedRect(drawRect, srcRect);
		april::rendersys->setPixelShader(NULL);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

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
		RB_CHECK_DISPOSED(renderable);
		return (renderable->visible ? Qtrue : Qfalse);
	}

	VALUE Renderable::rb_setVisible(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		renderable->visible = (bool)RTEST(value);
		return value;
	}

	VALUE Renderable::rb_getZ(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		return INT2NUM(renderable->z);
	}

	VALUE Renderable::rb_setZ(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		renderable->setZ(NUM2INT(value));
		return value;
	}

	VALUE Renderable::rb_getOX(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		return INT2NUM(-renderable->ox);
	}

	VALUE Renderable::rb_setOX(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		renderable->ox = -NUM2INT(value);
		return value;
	}

	VALUE Renderable::rb_getOY(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		return INT2NUM(-renderable->oy);
	}

	VALUE Renderable::rb_setOY(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		renderable->oy = -NUM2INT(value);
		return value;
	}

	VALUE Renderable::rb_getZoomX(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		return rb_float_new(renderable->zoom.x);
	}

	VALUE Renderable::rb_setZoomX(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		renderable->zoom.x = (float)NUM2DBL(value);
		return value;
	}

	VALUE Renderable::rb_getZoomY(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		return rb_float_new(renderable->zoom.y);
	}

	VALUE Renderable::rb_setZoomY(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		renderable->zoom.y = (float)NUM2DBL(value);
		return value;
	}

	VALUE Renderable::rb_getColor(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		return renderable->rb_color;
	}

	VALUE Renderable::rb_setColor(VALUE self, VALUE value)
	{
		{
			RB_SELF2CPP(Renderable, renderable);
			RB_CHECK_DISPOSED(renderable);
		}
		RB_GENERATE_SETTER(Renderable, renderable, Color, color);
		return value;
	}

	VALUE Renderable::rb_getTone(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		return renderable->rb_tone;
	}

	VALUE Renderable::rb_setTone(VALUE self, VALUE value)
	{
		{
			RB_SELF2CPP(Renderable, renderable);
			RB_CHECK_DISPOSED(renderable);
		}
		RB_GENERATE_SETTER(Renderable, renderable, Tone, tone);
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Renderable::rb_flash(VALUE self, VALUE color, VALUE duration)
	{
		RB_SELF2CPP(Renderable, renderable);
		RB_CHECK_DISPOSED(renderable);
		int flashDuration = hmax(NUM2INT(duration), 0);
		if (!NIL_P(color) && flashDuration > 0)
		{
			RB_CHECK_TYPE(color, rb_cColor);
			renderable->rb_flashColor = color;
			RB_VAR2CPP(color, Color, flashColor);
			renderable->flashColor = flashColor;
		}
		else
		{
			renderable->rb_flashColor = Qnil;
			renderable->flashColor = NULL;
		}
		renderable->flashTimer = 0;
		renderable->flashDuration = flashDuration;
		return Qnil;
	}

	VALUE Renderable::rb_arcDump(VALUE self)
	{
		RB_SELF2CPP(Renderable, renderable);
		rb_raise(rb_eTypeError, ("Can't arc-dump: " + renderable->typeName).c_str());
		return Qnil;
	}

}
