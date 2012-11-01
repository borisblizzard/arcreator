#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#include "CodeSnippets.h"
#include "Color.h"
#include "Graphics.h"
#include "Rect.h"
#include "RenderQueue.h"
#include "Viewport.h"
#include "RGSSError.h"

namespace rgss
{
	VALUE rb_cViewport;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	Viewport::Viewport() : Renderable()
	{
		this->typeName = "viewport";
		this->renderQueue = new RenderQueue();
		this->texture = NULL;
		this->rb_rect = Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX(0), INT2FIX(0));
		RB_VAR2CPP(this->rb_rect, Rect, rect);
		this->rect = rect;
	}
	
	Viewport::~Viewport()
	{
		this->dispose();
	}

	void Viewport::initialize(int argc, VALUE* argv)
	{
		Renderable::initialize(Graphics::renderQueue);
		VALUE arg1, arg2, arg3, arg4;
		rb_scan_args(argc, argv, "13", &arg1, &arg2, &arg3, &arg4);
		if (NIL_P(arg2) && NIL_P(arg3) && NIL_P(arg4))
		{
			this->rb_rect = arg1;
		}
		else
		{
			this->rb_rect = Rect::create(arg1, arg2, arg3, arg4);
		}
		RB_VAR2CPP(this->rb_rect, Rect, rect);
		this->rect = rect;
	}

	void Viewport::dispose()
	{
		if (!this->disposed)
		{
			this->rb_rect = Qnil;
			this->rect = NULL;
			delete this->renderQueue;
			this->renderQueue = NULL;
			if (this->texture != NULL)
			{
				delete this->texture;
				this->texture = NULL;
			}
		}
		Renderable::dispose();
	}

	void Viewport::mark()
	{
		Renderable::mark();
		RB_GC_MARK(rect);
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Viewport::draw()
	{
		if (!this->_canDraw())
		{
			return;
		}
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
			this->texture = april::rendersys->createTexture(this->rect->width,
				this->rect->height, april::Texture::FORMAT_ARGB, april::Texture::TYPE_RENDER_TARGET);
			this->texture->setFilter(april::Texture::FILTER_NEAREST);
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
		grect drawRect(0.0f, 0.0f,
			(float)this->texture->getWidth(), (float)this->texture->getHeight());
		april::rendersys->setOrthoProjection(drawRect);
		april::rendersys->clear();
		april::rendersys->setTextureBlendMode(april::DEFAULT);
		if (this->zoom.x != 1.0f || this->zoom.y != 1.0f)
		{
			april::rendersys->translate((float)this->ox, (float)this->oy);
			april::rendersys->scale(this->zoom.x, this->zoom.y, 1.0f);
		}
		this->renderQueue->draw();
		april::rendersys->setRenderTarget(target);
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void Viewport::_render()
	{
		april::rendersys->setTextureBlendMode(april::DEFAULT);
		grect drawRect(0.0f, 0.0f, (float)this->rect->width, (float)this->rect->height);
		grect srcRect(0.0f, 0.0f, 1.0f, 1.0f);
		this->_renderTexture(drawRect, srcRect, this->texture, 255);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Viewport::init()
	{
	}

	void Viewport::destroy()
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
		rb_define_method(rb_cViewport, "_arc_dump", RUBY_METHOD_FUNC(&Viewport::rb_arcDump), 0);
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
		rb_define_method(rb_cViewport, "zoom_x", RUBY_METHOD_FUNC(&Viewport::rb_getZoomX), 0);
		rb_define_method(rb_cViewport, "zoom_x=", RUBY_METHOD_FUNC(&Viewport::rb_setZoomX), 1);
		rb_define_method(rb_cViewport, "zoom_y", RUBY_METHOD_FUNC(&Viewport::rb_getZoomY), 0);
		rb_define_method(rb_cViewport, "zoom_y=", RUBY_METHOD_FUNC(&Viewport::rb_setZoomY), 1);
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

	VALUE Viewport::rb_new(VALUE classe)
	{
		Viewport* viewport;
		return RB_OBJECT_NEW(classe, Viewport, viewport, &Viewport::gc_mark, &Viewport::gc_free);
	}

	VALUE Viewport::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		if (argc != 1 && argc != 4)
		{
			rb_raise(rb_eArgError, hsprintf("Wrong number of arguments: %d for 1 or 4", argc).c_str());
		}
		RB_SELF2CPP(Viewport, viewport);
		viewport->initialize(argc, argv);
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
		RB_CHECK_DISPOSED(viewport);
		return Rect::rb_inspect(viewport->rb_rect);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Viewport::rb_getRect(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		RB_CHECK_DISPOSED(viewport);
		return viewport->rb_rect;
	}

	VALUE Viewport::rb_setRect(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Viewport, viewport, Rect, rect);
		RB_CHECK_DISPOSED(viewport);
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Viewport::rb_update(VALUE self)
	{
		RB_SELF2CPP(Viewport, viewport);
		RB_CHECK_DISPOSED(viewport);
		viewport->updateFlash();
		return Qnil;
	}

}
