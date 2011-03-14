#include <ruby.h>

#include <april/RenderSystem.h>
#include <april/Window.h>
#include <gtypes/Rectangle.h>

#include "RGSS/Graphics.h"

namespace zer0
{
	namespace RGSS
	{
		void Graphics::createRubyInterface()
		{
			VALUE classe = rb_define_module("Graphics");
			rb_define_module_function(classe, "update", RUBY_METHOD_FUNC(Graphics::update), 0);
			rb_define_module_function(classe, "frame_count", RUBY_METHOD_FUNC(Graphics::getFrameCount), 0);
			rb_define_module_function(classe, "frame_count=", RUBY_METHOD_FUNC(Graphics::setFrameCount), 1);
		}

		unsigned int Graphics::frameCount = 0;

		void Graphics::frameReset()
		{
		}

		void Graphics::freeze()
		{
		}

		void Graphics::transition(int duration = 8, hstr filename = "", int vague = 40)
		{
		}

		VALUE Graphics::getFrameCount(VALUE self)
		{
			return INT2NUM(frameCount);
		}

		VALUE Graphics::setFrameCount(VALUE self, VALUE value)
		{
			frameCount = NUM2UINT(value);
			return Qnil;
		}

		VALUE Graphics::update(VALUE self)
		{
			// some testing for now
			april::rendersys->clear();
			april::rendersys->setOrthoProjection(grect(0.0f, 0.0f, 800.0f, 600.0f));
			april::rendersys->drawColoredQuad(grect(80.0f + frameCount * 10.0f, 80.0f + frameCount * 10.0f, 160.0f, 160.0f), april::Color::GREEN);
			april::rendersys->presentFrame();
			frameCount++;
			return Qnil;
		}
	}
}
