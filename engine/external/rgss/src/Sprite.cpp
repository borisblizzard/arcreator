#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Color.h"
#include "Graphics.h"
#include "Rect.h"
#include "Sprite.h"
#include "Tone.h"
#include "Viewport.h"
#include "RGSSError.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cSprite;

	void Sprite::draw()
	{
		if (this->bitmap == NULL || this->bitmap->isDisposed() || this->opacity == 0 || this->srcRect->width <= 0 ||
			this->srcRect->height <= 0 || this->zoomX == 0.0f || this->zoomY == 0.0f)
		{
			return;
		}
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		if (this->x != 0 || this->y != 0) 
		{
			april::rendersys->translate((float)this->x, (float)this->y);
		}
		if (this->angle != 0.0f) 
		{
			april::rendersys->rotate(this->angle);
		}
		if (this->zoomX != 1.0f || this->zoomY != 1.0f)
		{
			april::rendersys->scale(this->zoomX, this->zoomY, 1.0f);
		}
		this->_render();
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void Sprite::_render()
	{
		this->bitmap->updateTexture();
		april::rendersys->setTexture(this->bitmap->getTexture());
		if (this->blendType == Positive)
		{
			april::rendersys->setBlendMode(april::ADD);
		}
		grect drawRect((float)this->ox, (float)this->oy,
			(float)this->srcRect->width, (float)this->srcRect->height);
		float w = (float)this->bitmap->getWidth();
		float h = (float)this->bitmap->getHeight();
		grect srcRect;
		srcRect.x = this->srcRect->x / w;
		srcRect.y = this->srcRect->y / h;
		srcRect.w = hmin(this->srcRect->width / w, 1.0f - srcRect.x);
		srcRect.h = hmin(this->srcRect->height / h, 1.0f - srcRect.y);
		april::rendersys->drawTexturedQuad(drawRect, srcRect,
			april::Color(APRIL_COLOR_WHITE, (unsigned char)this->opacity));
		april::rendersys->setBlendMode(april::DEFAULT);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Sprite::init()
	{
	}

	void Sprite::createRubyInterface()
	{
		rb_cSprite = rb_define_class("Sprite", rb_cObject);
		rb_define_alloc_func(rb_cSprite, &Sprite::rb_new);
		// initialize
		rb_define_method(rb_cSprite, "initialize", RUBY_METHOD_FUNC(&Sprite::rb_initialize), -1);
		rb_define_method(rb_cSprite, "dispose", RUBY_METHOD_FUNC(&Sprite::rb_dispose), 0);
		// getters and setters (Renderable)
		rb_define_method(rb_cSprite, "visible", RUBY_METHOD_FUNC(&Sprite::rb_getVisible), 0);
		rb_define_method(rb_cSprite, "visible=", RUBY_METHOD_FUNC(&Sprite::rb_setVisible), 1);
		rb_define_method(rb_cSprite, "z", RUBY_METHOD_FUNC(&Sprite::rb_getZ), 0);
		rb_define_method(rb_cSprite, "z=", RUBY_METHOD_FUNC(&Sprite::rb_setZ), 1);
		rb_define_method(rb_cSprite, "ox", RUBY_METHOD_FUNC(&Sprite::rb_getOX), 0);
		rb_define_method(rb_cSprite, "ox=", RUBY_METHOD_FUNC(&Sprite::rb_setOX), 1);
		rb_define_method(rb_cSprite, "oy", RUBY_METHOD_FUNC(&Sprite::rb_getOY), 0);
		rb_define_method(rb_cSprite, "oy=", RUBY_METHOD_FUNC(&Sprite::rb_setOY), 1);
		rb_define_method(rb_cSprite, "disposed?", RUBY_METHOD_FUNC(&Sprite::rb_isDisposed), 0);
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
		// getters and setters (Zoomable)
		rb_define_method(rb_cSprite, "zoom_x", RUBY_METHOD_FUNC(&Sprite::rb_getZoomX), 0);
		rb_define_method(rb_cSprite, "zoom_x=", RUBY_METHOD_FUNC(&Sprite::rb_setZoomX), 1);
		rb_define_method(rb_cSprite, "zoom_y", RUBY_METHOD_FUNC(&Sprite::rb_getZoomY), 0);
		rb_define_method(rb_cSprite, "zoom_y=", RUBY_METHOD_FUNC(&Sprite::rb_setZoomY), 1);
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

	void Sprite::gc_mark(Sprite* sprite)
	{
		rb_gc_mark(sprite->rb_srcRect);
		Zoomable::gc_mark(sprite);
	}

	void Sprite::gc_free(Sprite* sprite)
	{
		sprite->rb_srcRect = Qnil;
		sprite->srcRect = NULL;
		Zoomable::gc_free(sprite);
	}

	VALUE Sprite::rb_new(VALUE classe)
	{
		Sprite* sprite;
		VALUE result = Data_Make_Struct(classe, Sprite, Sprite::gc_mark, Sprite::gc_free, sprite);
		sprite->disposed = true;
		sprite->type = TYPE_SPRITE;
		return result;
	}

	VALUE Sprite::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		sprite->initializeZoomable(viewport);
		Sprite::rb_setSrcRect(self, Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX(0), INT2FIX(0)));
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
		Zoomable::rb_setBitmap(self, value);
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed sprite");
		}
		if (sprite->bitmap != NULL && !sprite->bitmap->isDisposed())
		{
			sprite->getSrcRect()->set(0, 0, sprite->bitmap->getWidth(), sprite->bitmap->getHeight());
		}
		return value;
	}

	VALUE Sprite::rb_getAngle(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed sprite");
		}
		return rb_float_new(sprite->angle);
	}

	VALUE Sprite::rb_setAngle(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed sprite");
		}
		sprite->angle = (float)NUM2DBL(value);
		return value;
	}

	VALUE Sprite::rb_getMirror(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed sprite");
		}
		return (sprite->mirror ? Qtrue : Qfalse);
	}

	VALUE Sprite::rb_setMirror(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed sprite");
		}
		sprite->mirror = (bool)RTEST(value);
		return value;
	}

	VALUE Sprite::rb_getBushDepth(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed sprite");
		}
		return INT2NUM(sprite->bushDepth);
	}

	VALUE Sprite::rb_setBushDepth(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed sprite");
		}
		sprite->bushDepth = NUM2INT(value);
		return value;
	}

	VALUE Sprite::rb_getSrcRect(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed sprite");
		}
		return sprite->rb_srcRect;
	}

	VALUE Sprite::rb_setSrcRect(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Sprite, sprite, Rect, srcRect);
		if (sprite->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed sprite");
		}
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	/****************************************************************************************
	 * TODO
	 ****************************************************************************************/

	VALUE Sprite::rb_flash(VALUE self, VALUE color, VALUE duration)
	{
		/// @todo implement
		return Qnil;
	}

	VALUE Sprite::rb_update(VALUE self)
	{
		/// @todo implement
		return Qnil;
	}

}
