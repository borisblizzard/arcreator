#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/hltypesUtil.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Color.h"
#include "Graphics.h"
#include "Plane.h"
#include "Tone.h"
#include "Viewport.h"

namespace legacy
{
	VALUE rb_cPlane;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	Plane::Plane() : Blendable()
	{
		this->typeName = "plane";
	}
	
	Plane::~Plane()
	{
		this->dispose();
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Plane::draw()
	{
		if (!this->_canDraw())
		{
			return;
		}
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		gmat4 projectionMatrix = april::rendersys->getProjectionMatrix();
		if (this->zoom.x != 1.0f || this->zoom.y != 1.0f)
		{
			april::rendersys->scale(this->zoom.x, this->zoom.y, 1.0f);
		}
		this->_render();
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void Plane::_render()
	{
		switch (this->blendType)
		{
		case Normal:
			april::rendersys->setTextureBlendMode(april::BM_DEFAULT);
			break;
		case Positive:
			april::rendersys->setTextureBlendMode(april::BM_ADD);
			break;
		case Negative:
			april::rendersys->setTextureBlendMode(april::BM_SUBTRACT);
			break;
		default:
			april::rendersys->setTextureBlendMode(april::BM_DEFAULT);
			break;
		}
		grect drawRect = this->_getRenderRect().toGRect();
		float w = (float)this->bitmap->getWidth();
		float h = (float)this->bitmap->getHeight();
		grect srcRect;
		srcRect.x = -this->ox / (this->zoom.x * w);
		srcRect.y = -this->oy / (this->zoom.y * h);
		srcRect.w = drawRect.w / w;
		srcRect.h = drawRect.h / h;
		this->_renderTexture(drawRect, srcRect, this->bitmap->getTexture(), this->opacity);
		april::rendersys->setTextureBlendMode(april::BM_DEFAULT);
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

	void Plane::destroy()
	{
	}

	void Plane::createRubyInterface()
	{
		rb_cPlane = rb_define_class("Plane", rb_cObject);
		rb_define_alloc_func(rb_cPlane, &Plane::rb_new);
		// initialize
		rb_define_method(rb_cPlane, "initialize", RUBY_METHOD_FUNC(&Plane::rb_initialize), -1);
		rb_define_method(rb_cPlane, "initialize_clone", RUBY_METHOD_FUNC(&Plane::rb_initialize_clone), 1);
		rb_define_method(rb_cPlane, "initialize_dup", RUBY_METHOD_FUNC(&Plane::rb_initialize_dup), 1);
		rb_define_method(rb_cPlane, "dispose", RUBY_METHOD_FUNC(&Plane::rb_dispose), 0);
		rb_define_method(rb_cPlane, "_arc_dump", RUBY_METHOD_FUNC(&Plane::rb_arcDump), 0);
		// getters and setters (Renderable)
		rb_define_method(rb_cPlane, "disposed?", RUBY_METHOD_FUNC(&Plane::rb_isDisposed), 0);
		rb_define_method(rb_cPlane, "visible", RUBY_METHOD_FUNC(&Plane::rb_getVisible), 0);
		rb_define_method(rb_cPlane, "visible=", RUBY_METHOD_FUNC(&Plane::rb_setVisible), 1);
		rb_define_method(rb_cPlane, "z", RUBY_METHOD_FUNC(&Plane::rb_getZ), 0);
		rb_define_method(rb_cPlane, "z=", RUBY_METHOD_FUNC(&Plane::rb_setZ), 1);
		rb_define_method(rb_cPlane, "ox", RUBY_METHOD_FUNC(&Plane::rb_getOX), 0);
		rb_define_method(rb_cPlane, "ox=", RUBY_METHOD_FUNC(&Plane::rb_setOX), 1);
		rb_define_method(rb_cPlane, "oy", RUBY_METHOD_FUNC(&Plane::rb_getOY), 0);
		rb_define_method(rb_cPlane, "oy=", RUBY_METHOD_FUNC(&Plane::rb_setOY), 1);
		rb_define_method(rb_cPlane, "zoom_x", RUBY_METHOD_FUNC(&Plane::rb_getZoomX), 0);
		rb_define_method(rb_cPlane, "zoom_x=", RUBY_METHOD_FUNC(&Plane::rb_setZoomX), 1);
		rb_define_method(rb_cPlane, "zoom_y", RUBY_METHOD_FUNC(&Plane::rb_getZoomY), 0);
		rb_define_method(rb_cPlane, "zoom_y=", RUBY_METHOD_FUNC(&Plane::rb_setZoomY), 1);
		rb_define_method(rb_cPlane, "color", RUBY_METHOD_FUNC(&Plane::rb_getColor), 0);
		rb_define_method(rb_cPlane, "color=", RUBY_METHOD_FUNC(&Plane::rb_setColor), 1);
		rb_define_method(rb_cPlane, "tone", RUBY_METHOD_FUNC(&Plane::rb_getTone), 0);
		rb_define_method(rb_cPlane, "tone=", RUBY_METHOD_FUNC(&Plane::rb_setTone), 1);
		// getters and setters (SourceRenderer)
		rb_define_method(rb_cPlane, "viewport", RUBY_METHOD_FUNC(&Plane::rb_getViewport), 0);
		rb_define_method(rb_cPlane, "opacity", RUBY_METHOD_FUNC(&Plane::rb_getOpacity), 0);
		rb_define_method(rb_cPlane, "opacity=", RUBY_METHOD_FUNC(&Plane::rb_setOpacity), 1);
		rb_define_method(rb_cPlane, "bitmap", RUBY_METHOD_FUNC(&Plane::rb_getBitmap), 0);
		rb_define_method(rb_cPlane, "bitmap=", RUBY_METHOD_FUNC(&Plane::rb_setBitmap), 1);
		// getters and setters (Blendable)
		rb_define_method(rb_cPlane, "blend_type", RUBY_METHOD_FUNC(&Plane::rb_getBlendType), 0);
		rb_define_method(rb_cPlane, "blend_type=", RUBY_METHOD_FUNC(&Plane::rb_setBlendType), 1);
	}

	VALUE Plane::rb_new(VALUE classe)
	{
		Plane* plane;
		return RB_OBJECT_NEW(classe, Plane, plane, Plane::gc_mark, &Plane::gc_free);
	}

	VALUE Plane::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Plane, plane);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		plane->initialize(viewport);
		return self;
	}

	VALUE Plane::rb_initialize_clone(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Plane, plane);
		RB_CANT_CLONE_ERROR(plane);
		return self;
	}

	VALUE Plane::rb_initialize_dup(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Plane, plane);
		RB_CANT_DUP_ERROR(plane);
		return self;
	}

}
