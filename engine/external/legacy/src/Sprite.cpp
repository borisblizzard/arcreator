#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/hltypesUtil.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Color.h"
#include "Graphics.h"
#include "Rect.h"
#include "Sprite.h"
#include "Tone.h"
#include "Viewport.h"
#include "RGSSError.h"

namespace legacy
{
	VALUE rb_cSprite;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	Sprite::Sprite() : Blendable()
	{
		this->typeName = "sprite";
		this->angle = 0.0f;
		this->mirror = false;
		this->bushDepth = 0;
		this->rb_srcRect = Qnil;
		this->srcRect = NULL;
	}
	
	Sprite::Sprite(Viewport* viewport) : Blendable(viewport)
	{
		this->typeName = "sprite";
		this->angle = 0.0f;
		this->mirror = false;
		this->bushDepth = 0;
		this->rb_srcRect = Qnil;
		this->srcRect = new Rect(0, 0, 0, 0);
	}

	Sprite::~Sprite()
	{
		this->dispose();
	}

	void Sprite::initialize(VALUE rb_viewport)
	{
		Blendable::initialize(rb_viewport);
		this->angle = 0.0f;
		this->mirror = false;
		this->bushDepth = 0;
		this->rb_srcRect = Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX(0), INT2FIX(0));
		RB_VAR2CPP(this->rb_srcRect, Rect, rect);
		this->srcRect = rect;
	}

	void Sprite::dispose()
	{
		if (!this->disposed)
		{
			CPP_VAR_DELETE(srcRect);
			this->rb_srcRect = Qnil;
			this->srcRect = NULL;
		}
		Blendable::dispose();
	}

	void Sprite::mark()
	{
		Blendable::mark();
		RB_GC_MARK(srcRect);
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Sprite::draw()
	{
		if (!this->_canDraw())
		{
			return;
		}
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		gmat4 projectionMatrix = april::rendersys->getProjectionMatrix();
		if (this->x != 0 || this->y != 0) 
		{
			april::rendersys->translate((float)this->x, (float)this->y);
		}
		if (this->angle != 0.0f) 
		{
			april::rendersys->rotate(this->angle);
		}
		if (this->zoom.x != 1.0f || this->zoom.y != 1.0f)
		{
			april::rendersys->scale(this->zoom.x, this->zoom.y, 1.0f);
		}
		this->_render();
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	bool Sprite::_canDraw()
	{
		return (this->srcRect->width > 0 && this->srcRect->height > 0 && Blendable::_canDraw());
	}

	void Sprite::_render()
	{
		switch (this->blendType)
		{
		case Normal:
			april::rendersys->setTextureBlendMode(april::DEFAULT);
			break;
		case Positive:
			april::rendersys->setTextureBlendMode(april::ADD);
			break;
		case Negative:
			april::rendersys->setTextureBlendMode(april::SUBTRACT);
			break;
		default:
			april::rendersys->setTextureBlendMode(april::DEFAULT);
			break;
		}
		int dw = hmin(this->srcRect->width, this->bitmap->getWidth());
		int dh = hmin(this->srcRect->height, this->bitmap->getHeight());
		grect drawRect((float)this->ox, (float)this->oy, (float)dw, (float)dh);
		float sw = (float)this->bitmap->getWidth();
		float sh = (float)this->bitmap->getHeight();
		grect srcRect;
		srcRect.x = this->srcRect->x / sw;
		srcRect.y = this->srcRect->y / sh;
		srcRect.w = hmin(this->srcRect->width / sw, 1.0f - srcRect.x);
		srcRect.h = hmin(this->srcRect->height / sh, 1.0f - srcRect.y);
		this->_renderTexture(drawRect, srcRect, this->bitmap->getTexture(), this->opacity);
		april::rendersys->setTextureBlendMode(april::DEFAULT);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Sprite::init()
	{
	}

	void Sprite::destroy()
	{
	}

	void Sprite::createRubyInterface()
	{
		rb_cSprite = rb_define_class("Sprite", rb_cObject);
		rb_define_alloc_func(rb_cSprite, &Sprite::rb_new);
		// initialize
		rb_define_method(rb_cSprite, "initialize", RUBY_METHOD_FUNC(&Sprite::rb_initialize), -1);
		rb_define_method(rb_cSprite, "initialize_clone", RUBY_METHOD_FUNC(&Sprite::rb_initialize_clone), 1);
		rb_define_method(rb_cSprite, "initialize_dup", RUBY_METHOD_FUNC(&Sprite::rb_initialize_dup), 1);
		rb_define_method(rb_cSprite, "dispose", RUBY_METHOD_FUNC(&Sprite::rb_dispose), 0);
		rb_define_method(rb_cSprite, "_arc_dump", RUBY_METHOD_FUNC(&Sprite::rb_arcDump), 0);
		// getters and setters (Renderable)
		rb_define_method(rb_cSprite, "disposed?", RUBY_METHOD_FUNC(&Sprite::rb_isDisposed), 0);
		rb_define_method(rb_cSprite, "visible", RUBY_METHOD_FUNC(&Sprite::rb_getVisible), 0);
		rb_define_method(rb_cSprite, "visible=", RUBY_METHOD_FUNC(&Sprite::rb_setVisible), 1);
		rb_define_method(rb_cSprite, "z", RUBY_METHOD_FUNC(&Sprite::rb_getZ), 0);
		rb_define_method(rb_cSprite, "z=", RUBY_METHOD_FUNC(&Sprite::rb_setZ), 1);
		rb_define_method(rb_cSprite, "ox", RUBY_METHOD_FUNC(&Sprite::rb_getOX), 0);
		rb_define_method(rb_cSprite, "ox=", RUBY_METHOD_FUNC(&Sprite::rb_setOX), 1);
		rb_define_method(rb_cSprite, "oy", RUBY_METHOD_FUNC(&Sprite::rb_getOY), 0);
		rb_define_method(rb_cSprite, "oy=", RUBY_METHOD_FUNC(&Sprite::rb_setOY), 1);
		rb_define_method(rb_cSprite, "zoom_x", RUBY_METHOD_FUNC(&Sprite::rb_getZoomX), 0);
		rb_define_method(rb_cSprite, "zoom_x=", RUBY_METHOD_FUNC(&Sprite::rb_setZoomX), 1);
		rb_define_method(rb_cSprite, "zoom_y", RUBY_METHOD_FUNC(&Sprite::rb_getZoomY), 0);
		rb_define_method(rb_cSprite, "zoom_y=", RUBY_METHOD_FUNC(&Sprite::rb_setZoomY), 1);
		rb_define_method(rb_cSprite, "color", RUBY_METHOD_FUNC(&Sprite::rb_getColor), 0);
		rb_define_method(rb_cSprite, "color=", RUBY_METHOD_FUNC(&Sprite::rb_setColor), 1);
		rb_define_method(rb_cSprite, "tone", RUBY_METHOD_FUNC(&Sprite::rb_getTone), 0);
		rb_define_method(rb_cSprite, "tone=", RUBY_METHOD_FUNC(&Sprite::rb_setTone), 1);
		// getters and setters (SourceRenderer)
		rb_define_method(rb_cSprite, "viewport", RUBY_METHOD_FUNC(&Sprite::rb_getViewport), 0);
		rb_define_method(rb_cSprite, "x", RUBY_METHOD_FUNC(&Sprite::rb_getX), 0);
		rb_define_method(rb_cSprite, "x=", RUBY_METHOD_FUNC(&Sprite::rb_setX), 1);
		rb_define_method(rb_cSprite, "y", RUBY_METHOD_FUNC(&Sprite::rb_getY), 0);
		rb_define_method(rb_cSprite, "y=", RUBY_METHOD_FUNC(&Sprite::rb_setY), 1);
		rb_define_method(rb_cSprite, "opacity", RUBY_METHOD_FUNC(&Sprite::rb_getOpacity), 0);
		rb_define_method(rb_cSprite, "opacity=", RUBY_METHOD_FUNC(&Sprite::rb_setOpacity), 1);
		rb_define_method(rb_cSprite, "bitmap", RUBY_METHOD_FUNC(&Sprite::rb_getBitmap), 0);
		rb_define_method(rb_cSprite, "bitmap=", RUBY_METHOD_FUNC(&Sprite::rb_setBitmap), 1);
		// getters and setters (Blendable)
		rb_define_method(rb_cSprite, "blend_type", RUBY_METHOD_FUNC(&Sprite::rb_getBlendType), 0);
		rb_define_method(rb_cSprite, "blend_type=", RUBY_METHOD_FUNC(&Sprite::rb_setBlendType), 1);
		// getters and setters
		rb_define_method(rb_cSprite, "angle", RUBY_METHOD_FUNC(&Sprite::rb_getAngle), 0);
		rb_define_method(rb_cSprite, "angle=", RUBY_METHOD_FUNC(&Sprite::rb_setAngle), 1);
		rb_define_method(rb_cSprite, "mirror", RUBY_METHOD_FUNC(&Sprite::rb_getMirror), 0);
		rb_define_method(rb_cSprite, "mirror=", RUBY_METHOD_FUNC(&Sprite::rb_setMirror), 1);
		rb_define_method(rb_cSprite, "bush_depth", RUBY_METHOD_FUNC(&Sprite::rb_getBushDepth), 0);
		rb_define_method(rb_cSprite, "bush_depth=", RUBY_METHOD_FUNC(&Sprite::rb_setBushDepth), 1);
		rb_define_method(rb_cSprite, "src_rect", RUBY_METHOD_FUNC(&Sprite::rb_getSrcRect), 0);
		rb_define_method(rb_cSprite, "src_rect=", RUBY_METHOD_FUNC(&Sprite::rb_setSrcRect), 1);
		// methods
		rb_define_method(rb_cSprite, "flash", RUBY_METHOD_FUNC(&Sprite::rb_flash), 2);
		rb_define_method(rb_cSprite, "update", RUBY_METHOD_FUNC(&Sprite::rb_update), 0);
	}

	VALUE Sprite::rb_new(VALUE classe)
	{
		Sprite* sprite;
		return RB_OBJECT_NEW(classe, Sprite, sprite, &Sprite::gc_mark, &Sprite::gc_free);
	}

	VALUE Sprite::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		sprite->initialize(viewport);
		return self;
	}

	VALUE Sprite::rb_initialize_clone(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CANT_CLONE_ERROR(sprite);
		return self;
	}

	VALUE Sprite::rb_initialize_dup(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CANT_DUP_ERROR(sprite);
		return self;
	}

	VALUE Sprite::create(int argc, VALUE* argv)
	{
		VALUE object = Sprite::rb_new(rb_cSprite);
		object = Sprite::rb_initialize(argc, argv, object);
		return object;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Sprite::rb_setBitmap(VALUE self, VALUE value)
	{
		Blendable::rb_setBitmap(self, value);
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->bitmap != NULL && !sprite->bitmap->isDisposed())
		{
			sprite->getSrcRect()->set(0, 0, sprite->bitmap->getWidth(), sprite->bitmap->getHeight());
		}
		return value;
	}

	VALUE Sprite::rb_getAngle(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CHECK_DISPOSED(sprite);
		return rb_float_new(sprite->angle);
	}

	VALUE Sprite::rb_setAngle(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CHECK_DISPOSED(sprite);
		sprite->angle = (float)NUM2DBL(value);
		return value;
	}

	VALUE Sprite::rb_getMirror(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CHECK_DISPOSED(sprite);
		return (sprite->mirror ? Qtrue : Qfalse);
	}

	VALUE Sprite::rb_setMirror(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CHECK_DISPOSED(sprite);
		sprite->mirror = (bool)RTEST(value);
		return value;
	}

	VALUE Sprite::rb_getBushDepth(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CHECK_DISPOSED(sprite);
		return INT2NUM(sprite->bushDepth);
	}

	VALUE Sprite::rb_setBushDepth(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CHECK_DISPOSED(sprite);
		sprite->bushDepth = NUM2INT(value);
		return value;
	}

	VALUE Sprite::rb_getSrcRect(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CHECK_DISPOSED(sprite);
		return sprite->rb_srcRect;
	}

	VALUE Sprite::rb_setSrcRect(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Sprite, sprite, Rect, srcRect);
		RB_CHECK_DISPOSED(sprite);
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Sprite::rb_update(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		RB_CHECK_DISPOSED(sprite);
		sprite->updateFlash();
		return Qnil;
	}

}
