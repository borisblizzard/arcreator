#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Color.h"
#include "Graphics.h"
#include "Plane.h"
#include "Tone.h"
#include "Viewport.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cPlane;

	void Plane::draw()
	{
		if (this->bitmap == NULL)
		{
			return;
		}
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		this->_render();
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void Plane::_render()
	{
		this->bitmap->updateTexture();
		april::rendersys->setTexture(this->bitmap->getTexture());
		grect drawRect = this->_getRenderRect().toGRect();
		float w = (float)this->bitmap->getWidth();
		float h = (float)this->bitmap->getHeight();
		grect srcRect;
		srcRect.x = -this->ox / w;
		srcRect.y = -this->oy / h;
		srcRect.w = drawRect.w / w;
		srcRect.h = drawRect.h / h;
		april::rendersys->drawTexturedQuad(drawRect, srcRect);
	}

	Rect Plane::_getRenderRect()
	{
		Rect rect;
		if (this->viewport != NULL)
		{
			Rect* vRect = this->viewport->getRect();
			rect.set(0, 0, vRect->width, vRect->height);
		}
		else
		{
			rect.set(0, 0, Graphics::getWidth(), Graphics::getHeight());
		}
		return rect;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Plane::init()
	{
	}

	void Plane::createRubyInterface()
	{
		rb_cPlane = rb_define_class("Plane", rb_cObject);
		rb_define_alloc_func(rb_cPlane, &Plane::rb_new);
		// initialize
		rb_define_method(rb_cPlane, "initialize", RUBY_METHOD_FUNC(&Plane::rb_initialize), -1);
		rb_define_method(rb_cPlane, "dispose", RUBY_METHOD_FUNC(&Plane::rb_dispose), 0);
		// getters and setters
		rb_define_method(rb_cPlane, "visible", RUBY_METHOD_FUNC(&Plane::rb_getVisible), 0);
		rb_define_method(rb_cPlane, "visible=", RUBY_METHOD_FUNC(&Plane::rb_setVisible), 1);
		rb_define_method(rb_cPlane, "opacity", RUBY_METHOD_FUNC(&Plane::rb_getOpacity), 0);
		rb_define_method(rb_cPlane, "opacity=", RUBY_METHOD_FUNC(&Plane::rb_setOpacity), 1);
		rb_define_method(rb_cPlane, "z", RUBY_METHOD_FUNC(&Plane::rb_getZ), 0);
		rb_define_method(rb_cPlane, "z=", RUBY_METHOD_FUNC(&Plane::rb_setZ), 1);
		rb_define_method(rb_cPlane, "ox", RUBY_METHOD_FUNC(&Plane::rb_getOX), 0);
		rb_define_method(rb_cPlane, "ox=", RUBY_METHOD_FUNC(&Plane::rb_setOX), 1);
		rb_define_method(rb_cPlane, "oy", RUBY_METHOD_FUNC(&Plane::rb_getOY), 0);
		rb_define_method(rb_cPlane, "oy=", RUBY_METHOD_FUNC(&Plane::rb_setOY), 1);
		rb_define_method(rb_cPlane, "bitmap", RUBY_METHOD_FUNC(&Plane::rb_getBitmap), 0);
		rb_define_method(rb_cPlane, "bitmap=", RUBY_METHOD_FUNC(&Plane::rb_setBitmap), 1);
		rb_define_method(rb_cPlane, "viewport", RUBY_METHOD_FUNC(&Plane::rb_getViewport), 0);
		rb_define_method(rb_cPlane, "disposed?", RUBY_METHOD_FUNC(&Plane::rb_isDisposed), 0);
		// methods
	}

	void Plane::gc_mark(Plane* plane)
	{
		if (!NIL_P(plane->rb_viewport))
		{
			//rb_gc_mark(plane->rb_viewport);
		}
		SourceRenderer::gc_mark(plane);
	}

	void Plane::gc_free(Plane* plane)
	{
		//plane->rb_viewport = Qnil;
		//plane->viewport = NULL;
		SourceRenderer::gc_free(plane);
	}

	VALUE Plane::rb_new(VALUE classe)
	{
		Plane* plane;
		VALUE result = Data_Make_Struct(rb_cPlane, Plane, Plane::gc_mark, Plane::gc_free, plane);
		plane->disposed = true;
		plane->type = TYPE_PLANE;
		return result;
	}

	VALUE Plane::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Plane, plane);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		plane->initializeSourceRenderer(viewport);
		return self;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	/****************************************************************************************
	 * TODO
	 ****************************************************************************************/



	VALUE Plane::rb_getBlendType(VALUE self)
	{
		return Qnil;
	}

	VALUE Plane::rb_setBlendType(VALUE self, VALUE value)
	{
		return Qnil;
	}

	VALUE Plane::rb_getColor(VALUE self)
	{
		return Qnil;
	}

	VALUE Plane::rb_setColor(VALUE self, VALUE value)
	{
		return Qnil;
	}

	VALUE Plane::rb_getTone(VALUE self)
	{
		return Qnil;
	}

	VALUE Plane::rb_setTone(VALUE self, VALUE value)
	{
		return Qnil;
	}

	VALUE Plane::rb_getZoomX(VALUE self)
	{
		return Qnil;
	}

	VALUE Plane::rb_setZoomX(VALUE self, VALUE value)
	{
		return Qnil;
	}

	VALUE Plane::rb_getZoomY(VALUE self)
	{
		return Qnil;
	}

	VALUE Plane::rb_setZoomY(VALUE self, VALUE value)
	{
		return Qnil;
	}

}
