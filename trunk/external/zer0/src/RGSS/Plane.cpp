#include <ruby.h>

#include <hltypes/util.h>

#include "RGSS/Plane.h"
#include "RGSS/Bitmap.h"
#include "RGSS/Color.h"
#include "RGSS/Tone.h"
#include "RGSS/Viewport.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Plane::createRubyInterface()
		{
			rb_cPlane = rb_define_class("Plane", rb_cObject);
			rb_define_alloc_func(rb_cPlane, &Plane::rb_new);
			// initialize
			rb_define_method(rb_cPlane, "initialize", RUBY_METHOD_FUNC(&Plane::rb_initialize), -1);
			rb_define_method(rb_cPlane, "inspect", RUBY_METHOD_FUNC(&Plane::rb_inspect), 0);
			// getters and setters
			rb_define_method(rb_cPlane, "bitmap", RUBY_METHOD_FUNC(&Plane::rb_getBitmap), 0);
			rb_define_method(rb_cPlane, "bitmap=", RUBY_METHOD_FUNC(&Plane::rb_setBitmap), 1);
			rb_define_method(rb_cPlane, "blend_type", RUBY_METHOD_FUNC(&Plane::rb_getBlendType), 0);
			rb_define_method(rb_cPlane, "blend_type=", RUBY_METHOD_FUNC(&Plane::rb_setBlendType), 1);		
			rb_define_method(rb_cPlane, "color", RUBY_METHOD_FUNC(&Plane::rb_getColor), 0);
			rb_define_method(rb_cPlane, "color=", RUBY_METHOD_FUNC(&Plane::rb_setColor), 1);
			rb_define_method(rb_cPlane, "opacity", RUBY_METHOD_FUNC(&Plane::rb_getOpacity), 0);
			rb_define_method(rb_cPlane, "opacity=", RUBY_METHOD_FUNC(&Plane::rb_setOpacity), 1);
			rb_define_method(rb_cPlane, "ox", RUBY_METHOD_FUNC(&Plane::rb_getOX), 0);
			rb_define_method(rb_cPlane, "ox=", RUBY_METHOD_FUNC(&Plane::rb_setOX), 1);
			rb_define_method(rb_cPlane, "oy", RUBY_METHOD_FUNC(&Plane::rb_getOY), 0);
			rb_define_method(rb_cPlane, "oy=", RUBY_METHOD_FUNC(&Plane::rb_setOY), 1);
			rb_define_method(rb_cPlane, "tone", RUBY_METHOD_FUNC(&Plane::rb_getTone), 0);
			rb_define_method(rb_cPlane, "tone=", RUBY_METHOD_FUNC(&Plane::rb_setTone), 1);
			rb_define_method(rb_cPlane, "viewport", RUBY_METHOD_FUNC(&Plane::rb_getViewport), 0);
			rb_define_method(rb_cPlane, "visible", RUBY_METHOD_FUNC(&Plane::rb_getVisible), 0);
			rb_define_method(rb_cPlane, "visible=", RUBY_METHOD_FUNC(&Plane::rb_setVisible), 1);
			rb_define_method(rb_cPlane, "z", RUBY_METHOD_FUNC(&Plane::rb_getZ), 0);
			rb_define_method(rb_cPlane, "z=", RUBY_METHOD_FUNC(&Plane::rb_setZ), 1);
			rb_define_method(rb_cPlane, "zoom_x", RUBY_METHOD_FUNC(&Plane::rb_getZoomX), 0);
			rb_define_method(rb_cPlane, "zoom_x=", RUBY_METHOD_FUNC(&Plane::rb_setZoomX), 1);
			rb_define_method(rb_cPlane, "zoom_y", RUBY_METHOD_FUNC(&Plane::rb_getZoomY), 0);
			rb_define_method(rb_cPlane, "zoom_y=", RUBY_METHOD_FUNC(&Plane::rb_setZoomY), 1);
			// methods
			rb_define_method(rb_cPlane, "dispose", RUBY_METHOD_FUNC(&Plane::rb_dispose), 0);
			rb_define_method(rb_cPlane, "disposed?", RUBY_METHOD_FUNC(&Plane::rb_isDisposed), 0);
		}

		VALUE Plane::wrap()
		{
			Plane* plane = this;
			return Data_Wrap_Struct(rb_cPlane, NULL, NULL, plane);
		}

		void Plane::gc_free(Plane* plane)
		{
		}

		VALUE Plane::rb_new(VALUE classe)
		{
			return classe;
		}

		VALUE Plane::rb_initialize(int argc, VALUE* argv, VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_inspect(VALUE self)
		{
			return self;
		}



		VALUE Plane::rb_getBitmap(VALUE self)
		{
			return self;
		}
		
		VALUE Plane::rb_setBitmap(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getBlendType(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setBlendType(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getColor(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setColor(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getOpacity(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setOpacity(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getOX(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setOX(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getOY(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setOY(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getTone(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setTone(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getViewport(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_getVisible(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setVisible(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getZ(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setZ(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getZoomX(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setZoomX(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_getZoomY(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_setZoomY(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Plane::rb_dispose(VALUE self)
		{
			return self;
		}

		VALUE Plane::rb_isDisposed(VALUE self)
		{
			return self;
		}
	}
}
