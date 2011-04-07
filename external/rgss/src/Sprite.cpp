#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

#include "Bitmap.h"
#include "Color.h"
#include "Graphics.h"
#include "Rect.h"
#include "Sprite.h"
#include "Tone.h"
#include "Viewport.h"
#include "CodeSnippets.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cSprite;

	void Sprite::draw()
	{
		if (this->bitmap == NULL || this->opacity == 0 || this->srcRect->width <= 0 ||
			this->srcRect->height <= 0)
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
		this->_render();
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void Sprite::_render()
	{
		this->bitmap->updateTexture();
		april::rendersys->setTexture(this->bitmap->getTexture());
		grect drawRect;
		drawRect.x = (float)this->ox;
		drawRect.y = (float)this->oy;
		drawRect.w = (float)this->srcRect->width;
		drawRect.h = (float)this->srcRect->height;
		float w = (float)this->bitmap->getWidth();
		float h = (float)this->bitmap->getHeight();
		grect srcRect;
		srcRect.x = this->srcRect->x / w;
		srcRect.y = this->srcRect->y / h;
		srcRect.w = hmin(this->srcRect->width / w, 1.0f - srcRect.x);
		srcRect.h = hmin(this->srcRect->height / h, 1.0f - srcRect.y);
		april::rendersys->drawTexturedQuad(drawRect, srcRect);
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
		// getters and setters
		rb_define_method(rb_cSprite, "visible", RUBY_METHOD_FUNC(&Sprite::rb_getVisible), 0);
		rb_define_method(rb_cSprite, "visible=", RUBY_METHOD_FUNC(&Sprite::rb_setVisible), 1);
		rb_define_method(rb_cSprite, "opacity", RUBY_METHOD_FUNC(&Sprite::rb_getOpacity), 0);
		rb_define_method(rb_cSprite, "opacity=", RUBY_METHOD_FUNC(&Sprite::rb_setOpacity), 1);
		rb_define_method(rb_cSprite, "x", RUBY_METHOD_FUNC(&Sprite::rb_getX), 0);
		rb_define_method(rb_cSprite, "x=", RUBY_METHOD_FUNC(&Sprite::rb_setX), 1);
		rb_define_method(rb_cSprite, "y", RUBY_METHOD_FUNC(&Sprite::rb_getY), 0);
		rb_define_method(rb_cSprite, "y=", RUBY_METHOD_FUNC(&Sprite::rb_setY), 1);
		rb_define_method(rb_cSprite, "z", RUBY_METHOD_FUNC(&Sprite::rb_getZ), 0);
		rb_define_method(rb_cSprite, "z=", RUBY_METHOD_FUNC(&Sprite::rb_setZ), 1);
		rb_define_method(rb_cSprite, "ox", RUBY_METHOD_FUNC(&Sprite::rb_getOX), 0);
		rb_define_method(rb_cSprite, "ox=", RUBY_METHOD_FUNC(&Sprite::rb_setOX), 1);
		rb_define_method(rb_cSprite, "oy", RUBY_METHOD_FUNC(&Sprite::rb_getOY), 0);
		rb_define_method(rb_cSprite, "oy=", RUBY_METHOD_FUNC(&Sprite::rb_setOY), 1);
		rb_define_method(rb_cSprite, "angle", RUBY_METHOD_FUNC(&Sprite::rb_getAngle), 0);
		rb_define_method(rb_cSprite, "angle=", RUBY_METHOD_FUNC(&Sprite::rb_setAngle), 1);
		rb_define_method(rb_cSprite, "bitmap", RUBY_METHOD_FUNC(&Sprite::rb_getBitmap), 0);
		rb_define_method(rb_cSprite, "bitmap=", RUBY_METHOD_FUNC(&Sprite::rb_setBitmap), 1);
		rb_define_method(rb_cSprite, "viewport", RUBY_METHOD_FUNC(&Sprite::rb_getViewport), 0);
		rb_define_method(rb_cSprite, "src_rect", RUBY_METHOD_FUNC(&Sprite::rb_getSrcRect), 0);
		rb_define_method(rb_cSprite, "src_rect=", RUBY_METHOD_FUNC(&Sprite::rb_setSrcRect), 1);
		rb_define_method(rb_cSprite, "disposed?", RUBY_METHOD_FUNC(&Sprite::rb_isDisposed), 0);
		// methods
	}

	void Sprite::gc_mark(Sprite* sprite)
	{
		rb_gc_mark(sprite->rb_srcRect);
		SourceRenderer::gc_mark(sprite);
	}

	void Sprite::gc_free(Sprite* sprite)
	{
		sprite->rb_srcRect = Qnil;
		sprite->srcRect = NULL;
		SourceRenderer::gc_free(sprite);
	}

	VALUE Sprite::rb_new(VALUE classe)
	{
		Sprite* sprite;
		VALUE result = Data_Make_Struct(rb_cSprite, Sprite, Sprite::gc_mark, Sprite::gc_free, sprite);
		sprite->disposed = true;
		sprite->type = TYPE_SPRITE;
		return result;
	}

	VALUE Sprite::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		sprite->initializeSourceRenderer(viewport);
		Sprite::rb_setSrcRect(self, Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX(0), INT2FIX(0)));
		return self;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Sprite::rb_getX(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		return INT2NUM(sprite->x);
	}

	VALUE Sprite::rb_setX(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		sprite->x = NUM2INT(value);
		return value;
	}

	VALUE Sprite::rb_getY(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		return INT2NUM(sprite->y);
	}

	VALUE Sprite::rb_setY(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		sprite->y = NUM2INT(value);
		return value;
	}

	VALUE Sprite::rb_getAngle(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		return rb_float_new(sprite->angle);
	}

	VALUE Sprite::rb_setAngle(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Sprite, sprite);
		sprite->angle = (float)NUM2DBL(value);
		return value;
	}

	VALUE Sprite::rb_getSrcRect(VALUE self)
	{
		RB_SELF2CPP(Sprite, sprite);
		return sprite->rb_srcRect;
	}

	VALUE Sprite::rb_setSrcRect(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Sprite, sprite, Rect, srcRect);
		return value;
	}

	VALUE Sprite::rb_setBitmap(VALUE self, VALUE value)
	{
		SourceRenderer::rb_setBitmap(self, value);
		RB_SELF2CPP(Sprite, sprite);
		if (sprite->bitmap != NULL)
		{
			sprite->getSrcRect()->set(0, 0, sprite->bitmap->getWidth(), sprite->bitmap->getHeight());
		}
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	/****************************************************************************************
	 * TODO
	 ****************************************************************************************/





	VALUE Sprite::flash(VALUE self, VALUE color, VALUE duration)
	{
		/// @todo implement
		return Qnil;
	}

	VALUE Sprite::setZoomX(VALUE self, VALUE value)
	{
		return value;
	}

	VALUE Sprite::setZoomY(VALUE self, VALUE value)
	{
		return value;
	}

	VALUE Sprite::update(VALUE self)
	{
		/// @todo implement
		return Qnil;
	}

}
