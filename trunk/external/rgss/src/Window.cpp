#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

#include "Window.h"
#include "Bitmap.h"
#include "Rect.h"
#include "Viewport.h"
#include "CodeSnippets.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cWindow;

	void Window::draw()
	{
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		if (this->x != 0 || this->y != 0)
		{
			april::rendersys->translate((float)this->x, (float)this->y);
		}
		this->_render();
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void Window::_render()
	{
		//this->bitmap->updateTexture();
		//april::rendersys->setTexture(this->bitmap->getTexture());
		//april::rendersys->draw>drawTexturedQuad(drawRect, srcRect);
		april::rendersys->drawColoredQuad(grect(0, 0, 32, 32), april::Color::PURPLE);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Window::init()
	{
	}

	void Window::createRubyInterface()
	{
		rb_cWindow = rb_define_class("Window", rb_cObject);
		rb_define_alloc_func(rb_cWindow, &Window::rb_new);
		// initialize
		rb_define_method(rb_cWindow, "initialize", RUBY_METHOD_FUNC(&Window::rb_initialize), 0);
		rb_define_method(rb_cWindow, "dispose", RUBY_METHOD_FUNC(&Window::rb_dispose), 0);
		// getters and setters
		rb_define_method(rb_cWindow, "visible", RUBY_METHOD_FUNC(&Window::rb_getVisible), 0);
		rb_define_method(rb_cWindow, "visible=", RUBY_METHOD_FUNC(&Window::rb_setVisible), 1);
		rb_define_method(rb_cWindow, "opacity", RUBY_METHOD_FUNC(&Window::rb_getOpacity), 0);
		rb_define_method(rb_cWindow, "opacity=", RUBY_METHOD_FUNC(&Window::rb_setOpacity), 1);
		//rb_define_method(rb_cWindow, "x", RUBY_METHOD_FUNC(&Window::rb_getX), 0);
		//rb_define_method(rb_cWindow, "x=", RUBY_METHOD_FUNC(&Window::rb_setX), 1);
		//rb_define_method(rb_cWindow, "y", RUBY_METHOD_FUNC(&Window::rb_getY), 0);
		//rb_define_method(rb_cWindow, "y=", RUBY_METHOD_FUNC(&Window::rb_setY), 1);
		rb_define_method(rb_cWindow, "z", RUBY_METHOD_FUNC(&Window::rb_getZ), 0);
		rb_define_method(rb_cWindow, "z=", RUBY_METHOD_FUNC(&Window::rb_setZ), 1);
		rb_define_method(rb_cWindow, "ox", RUBY_METHOD_FUNC(&Window::rb_getOX), 0);
		rb_define_method(rb_cWindow, "ox=", RUBY_METHOD_FUNC(&Window::rb_setOX), 1);
		rb_define_method(rb_cWindow, "oy", RUBY_METHOD_FUNC(&Window::rb_getOY), 0);
		rb_define_method(rb_cWindow, "oy=", RUBY_METHOD_FUNC(&Window::rb_setOY), 1);
		rb_define_method(rb_cWindow, "contents", RUBY_METHOD_FUNC(&Window::rb_getBitmap), 0);
		rb_define_method(rb_cWindow, "contents=", RUBY_METHOD_FUNC(&Window::rb_setBitmap), 1);
		rb_define_method(rb_cWindow, "viewport", RUBY_METHOD_FUNC(&Window::rb_getViewport), 0);
		rb_define_method(rb_cWindow, "disposed?", RUBY_METHOD_FUNC(&Window::rb_isDisposed), 0);

		// todo
		/*
		rb_define_attr(rb_cWindow, "active", 1, 1);
		rb_define_attr(rb_cWindow, "back_opacity", 1, 0);
		rb_define_attr(rb_cWindow, "contents_opacity", 1, 0);
		rb_define_attr(rb_cWindow, "cursor_rect", 1, 1);
		rb_define_attr(rb_cWindow, "height", 1, 1);
		rb_define_attr(rb_cWindow, "pause", 1, 1);
		rb_define_attr(rb_cWindow, "stretch", 1, 1);
		rb_define_attr(rb_cWindow, "width", 1, 1);
		rb_define_attr(rb_cWindow, "windowskin", 1, 0);
		rb_define_method(rb_cWindow, "back_opacity=", RUBY_METHOD_FUNC(&Window::setBackOpacity), 1);
		rb_define_method(rb_cWindow, "contents_opacity=", RUBY_METHOD_FUNC(&Window::setContentsOpacity), 1);
		rb_define_method(rb_cWindow, "windowskin=", RUBY_METHOD_FUNC(&Window::setWindowskin), 1);
		*/
	}
	
	void Window::gc_mark(Window* window)
	{
		//rb_gc_mark(window->rb_srcRect);
		SourceRenderer::gc_mark(window);
	}

	void Window::gc_free(Window* window)
	{
		//window->rb_srcRect = Qnil;
		//window->srcRect = NULL;
		SourceRenderer::gc_free(window);
	}

	VALUE Window::rb_new(VALUE classe)
	{
		Window* window;
		VALUE result = Data_Make_Struct(rb_cWindow, Window, Window::gc_mark, Window::gc_free, window);
		window->disposed = true;
		window->type = TYPE_WINDOW;
		return result;
	}

	VALUE Window::rb_initialize(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		window->initializeSourceRenderer(Qnil);
		return self;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	/****************************************************************************************
	 * TODO
	 ****************************************************************************************/

	VALUE Window::setBackOpacity(VALUE self, VALUE value)
	{
		value = rb_float_new(hclamp(NUM2DBL(value), 0.0, 255.0));
		rb_iv_set(self, "@back_opacity", value);
		return value;
	}

	VALUE Window::setContentsOpacity(VALUE self, VALUE value)
	{
		value = rb_float_new(hclamp(NUM2DBL(value), 0.0, 255.0));
		rb_iv_set(self, "@opacity", value);
		return value;
	}

	VALUE Window::setWindowskin(VALUE self, VALUE* value)
	{
		rb_iv_set(self, "@windowskin", *value);
		return *value;
	}

	VALUE Window::update(VALUE self)
	{
		return self;
	}

}
