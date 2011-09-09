#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/hstring.h>
#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Color.h"
#include "Graphics.h"
#include "Rect.h"
#include "RenderQueue.h"
#include "Tone.h"
#include "Viewport.h"
#include "RGSSError.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cViewport;

	void Viewport::draw()
	{
		bool needsTextureUpdate = false;
		if (this->texture == NULL)
		{
			needsTextureUpdate = true;
		}
		else if (this->rect->width != this->texture->getWidth() ||
			this->rect->height != this->texture->getHeight())
		{
			delete this->texture;
			needsTextureUpdate = true;
		}
		if (needsTextureUpdate)
		{
			this->texture = april::rendersys->createEmptyTexture(this->rect->width,
				this->rect->height, april::AT_ARGB, april::AT_RENDER_TARGET);
			this->texture->setTextureFilter(april::Nearest);
		}
		// rendering
		this->_renderToTexture();
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		gmat4 projectionMatrix = april::rendersys->getProjectionMatrix();
		if (this->rect->x != 0 || this->rect->y != 0)
		{
			april::rendersys->translate((float)this->rect->x, (float)this->rect->y);
		}
		this->_render();
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void Viewport::_renderToTexture()
	{
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		gmat4 projectionMatrix = april::rendersys->getProjectionMatrix();
		april::Texture* target = april::rendersys->getRenderTarget();
		april::rendersys->setRenderTarget(this->texture);
		april::rendersys->setIdentityTransform();
		april::rendersys->setOrthoProjection(grect(0.0f, 0.0f,
			(float)this->texture->getWidth(), (float)this->texture->getHeight()));
		april::rendersys->clear();
		april::rendersys->setBlendMode(april::DEFAULT);
		this->renderQueue->draw();
		april::rendersys->setRenderTarget(target);
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void Viewport::_render()
	{
		april::rendersys->setBlendMode(april::DEFAULT);
		april::rendersys->setTexture(this->texture);
		grect drawRect(0.0f, 0.0f, (float)this->rect->width, (float)this->rect->height);
		grect srcRect(0.0f, 0.0f, 1.0f, 1.0f);
		april::Color color = this->_getRenderColor();
		april::rendersys->drawTexturedQuad(drawRect, srcRect);
		/*
		if (color == APRIL_COLOR_CLEAR)
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
		}
		//*/
	}

	void Viewport::dispose()
	{
		if (this->texture != NULL)
		{
			delete this->texture;
			this->texture = NULL;
		}
		if (this->renderQueue != NULL)
		{
			delete this->renderQueue;
			this->renderQueue = NULL;
		}
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Viewport::init()
	{
	}

	void Viewport::createRubyInterface()
	{
		rb_cViewport = rb_define_class("Viewport", rb_cObject);
		rb_define_alloc_func(rb_cViewport, &Viewport::rb_new);
		// initialize
		rb_define_method(rb_cViewport, "initialize", RUBY_METHOD_FUNC(&Viewport::rb_initialize), -1);
		rb_define_method(rb_cViewport, "initialize_clone", RUBY_METHOD_FUNC(&Viewport::rb_initialize_clone), 1);
		rb_define_method(rb_cViewport, "initialize_dup", RUBY_METHOD_FUNC(&Viewport::rb_initialize_dup), 1);
		rb_define_method(rb_cViewport, "dispose", RUBY_METHOD_FUNC(&Viewport::rb_dispose), 0);
		// getters and setters (Renderable)
		rb_define_method(rb_cViewport, "disposed?", RUBY_METHOD_FUNC(&Viewport::rb_isDisposed), 0);
		rb_define_method(rb_cViewport, "visible", RUBY_METHOD_FUNC(&Viewport::rb_getVisible), 0);
		rb_define_method(rb_cViewport, "visible=", RUBY_METHOD_FUNC(&Viewport::rb_setVisible), 1);
		rb_define_method(rb_cViewport, "z", RUBY_METHOD_FUNC(&Viewport::rb_getZ), 0);
		rb_define_method(rb_cViewport, "z=", RUBY_METHOD_FUNC(&Viewport::rb_setZ), 1);
		rb_define_method(rb_cViewport, "ox", RUBY_METHOD_FUNC(&Viewport::rb_getOX), 0);
		rb_define_method(rb_cViewport, "ox=", RUBY_METHOD_FUNC(&Viewport::rb_setOX), 1);
		rb_define_method(rb_cViewport, "oy", RUBY_METHOD_FUNC(&Viewport::rb_getOY), 0);
		rb_define_method(rb_cViewport, "oy=", RUBY_METHOD_FUNC(&Viewport::rb_setOY), 1);
		rb_define_method(rb_cViewport, "color", RUBY_METHOD_FUNC(&Viewport::rb_getColor), 0);
		rb_define_method(rb_cViewport, "color=", RUBY_METHOD_FUNC(&Viewport::rb_setColor), 1);
		rb_define_method(rb_cViewport, "tone", RUBY_METHOD_FUNC(&Viewport::rb_getTone), 0);
		rb_define_method(rb_cViewport, "tone=", RUBY_METHOD_FUNC(&Viewport::rb_setTone), 1);
		// getters and setters
		rb_define_method(rb_cViewport, "rect", RUBY_METHOD_FUNC(&Viewport::rb_getRect), 0);
		rb_define_method(rb_cViewport, "rect=", RUBY_METHOD_FUNC(&Viewport::rb_setRect), 1);
		// methods
		rb_define_method(rb_cViewport, "flash", RUBY_METHOD_FUNC(&Viewport::rb_flash), 2);
		rb_define_method(rb_cViewport, "update", RUBY_METHOD_FUNC(&Viewport::rb_update), 0);
	}

	void Viewport::gc_mark(Viewport* viewport)
	{
		if (!NIL_P(viewport->rb_color))
		{
			rb_gc_mark(viewport->rb_color);
		}
		if (!NIL_P(viewport->rb_rect))
		{
			rb_gc_mark(viewport->rb_rect);
		}
		if (!NIL_P(viewport->rb_tone))
		{
			rb_gc_mark(viewport->rb_tone);
		}
		Renderable::gc_mark(viewport);
	}

	void Viewport::gc_free(Viewport* viewport)
	{
		viewport->rb_color = Qnil;
		viewport->color = NULL;
		viewport->rb_rect = Qnil;
		viewport->rect = NULL;
		viewport->rb_tone = Qnil;
		viewport->tone = NULL;
		Renderable::gc_free(viewport);
	}

	VALUE Viewport::rb_new(VALUE classe)
	{
		Viewport* viewport;
		VALUE result = Data_Make_Struct(classe, Viewport, Viewport::gc_mark, Viewport::gc_free, viewport);
		viewport->disposed = true;
		viewport->type = TYPE_VIEWPORT;
		viewport->typeName = "viewport";
		return result;
	}

	VALUE Viewport::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		if (argc != 1 && argc != 4)
		{
			hstr message = hsprintf("wrong number of arguments (%d for 1 or 4)", argc);
			rb_raise(rb_eArgError, message.c_str());
		}
		RB_SELF2CPP(Viewport, viewport);
		viewport->renderQueue = new RenderQueue();
		viewport->texture = NULL;
		viewport->initializeRenderable(Graphics::renderQueue);
		VALUE arg1, arg2, arg3, arg4;
		rb_scan_args(argc, argv, "13", &arg1, &arg2, &arg3, &arg4);
		if (NIL_P(arg2) && NIL_P(arg3) && NIL_P(arg4))
		{
			Viewport::rb_setRect(self, arg1);
		}
		else
		{
			Viewport::rb_setRect(self, Rect::create(arg1, arg2, arg3, arg4));
		}
		VALUE argv2[4] = {INT2FIX(0), INT2FIX(0), INT2FIX(0), INT2FIX(0)};
		Viewport::rb_setColor(self, Color::create(4, argv2));
		VALUE argv3[4] = {INT2FIX(0), INT2FIX(0), INT2FIX(0), INT2FIX(0)};
		Viewport::rb_setTone(self, Tone::create(4, argv3));
		return self;
	}

	VALUE Viewport::rb_initialize_clone(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Viewport, viewport);
		RB_CANT_CLONE_ERROR(viewport);
		return self;
	}

	VALUE Viewport::rb_initialize_dup(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Viewport, viewport);
		RB_CANT_DUP_ERROR(viewport);
		return self;
	}

	VALUE Viewport::rb_inspect(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		RB_CHECK_DISPOSED_1(viewport);
		return Color::rb_inspect(viewport->rb_color);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Viewport::rb_getColor(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		RB_CHECK_DISPOSED_1(viewport);
		return viewport->rb_color;
	}

	VALUE Viewport::rb_setColor(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Viewport, sprite, Color, color);
		RB_CHECK_DISPOSED_1(viewport);
		return value;
	}

	VALUE Viewport::rb_getRect(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		RB_CHECK_DISPOSED_1(viewport);
		return viewport->rb_rect;
	}

	VALUE Viewport::rb_setRect(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Viewport, sprite, Rect, rect);
		RB_CHECK_DISPOSED_1(viewport);
		return value;
	}

	VALUE Viewport::rb_getTone(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		RB_CHECK_DISPOSED_1(viewport);
		return viewport->rb_tone;
	}

	VALUE Viewport::rb_setTone(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Viewport, sprite, Tone, tone);
		RB_CHECK_DISPOSED_1(viewport);
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Viewport::rb_update(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		RB_CHECK_DISPOSED_1(viewport);
		viewport->updateFlash();
		return Qnil;
	}

}
