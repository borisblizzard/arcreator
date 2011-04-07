#include <ruby.h>

#include <april/RenderSystem.h>
#include <april/Window.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

#include "Graphics.h"
#include "Renderable.h"
#include "CodeSnippets.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_mGraphics;

	unsigned int Graphics::frameCount;
	unsigned int Graphics::frameRate;
	bool Graphics::running;
	harray<Renderable*> renderables;

	void Graphics::addRenderable(Renderable* renderable)
	{
		for_iter (i, 0, renderables.size())
		{
			if (renderable->getZ() < renderables[i]->getZ())
			{
				renderables.insert_at(i, renderable);
				return;
			}
		}
		renderables += renderable;
	}

	void Graphics::removeRenderable(Renderable* renderable)
	{
		renderables -= renderable;
	}

	void Graphics::updateRenderable(Renderable* renderable)
	{
		removeRenderable(renderable);
		addRenderable(renderable);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/
	
	void Graphics::init()
	{
		frameCount = 0;
		frameRate = 40;
		running = true;
	}

	void Graphics::createRubyInterface()
	{
		rb_mGraphics = rb_define_module("Graphics");
		rb_define_module_function(rb_mGraphics, "update", RUBY_METHOD_FUNC(&Graphics::update), 0);
		rb_define_module_function(rb_mGraphics, "frame_count", RUBY_METHOD_FUNC(&Graphics::getFrameCount), 0);
		rb_define_module_function(rb_mGraphics, "frame_count=", RUBY_METHOD_FUNC(&Graphics::setFrameCount), 1);
		rb_define_module_function(rb_mGraphics, "frame_rate", RUBY_METHOD_FUNC(&Graphics::getFrameRate), 0);
		rb_define_module_function(rb_mGraphics, "frame_rate=", RUBY_METHOD_FUNC(&Graphics::setFrameRate), 1);
		rb_define_module_function(rb_mGraphics, "frame_reset", RUBY_METHOD_FUNC(&Graphics::frameReset), 0);
		rb_define_module_function(rb_mGraphics, "freeze", RUBY_METHOD_FUNC(&Graphics::freeze), 0);
		rb_define_module_function(rb_mGraphics, "transition", RUBY_METHOD_FUNC(&Graphics::transition), 3);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Graphics::getFrameCount(VALUE self)
	{
		return INT2NUM(frameCount);
	}

	VALUE Graphics::setFrameCount(VALUE self, VALUE value)
	{
		frameCount = NUM2UINT(value);
		return Qnil;
	}

	VALUE Graphics::getFrameRate(VALUE self)
	{
		return INT2NUM(frameRate);
	}

	VALUE Graphics::setFrameRate(VALUE self, VALUE value)
	{
		frameRate = hclamp(NUM2UINT(value), (unsigned int)10, (unsigned int)120);
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Graphics::update(VALUE self)
	{
		if (!running)
		{
			rb_exit(0);
			return Qnil;
		}
		april::rendersys->clear();
		foreach (Renderable*, it, renderables)
		{
			(*it)->draw();
		}
		april::rendersys->presentFrame();
		frameCount++;
		/// @todo - more often, less often?
		if (frameCount % 200 == 0)
		{
			rb_eval_string("GC.start");
		}
		return Qnil;
	}

	VALUE Graphics::frameReset(VALUE self)
	{
		frameCount = 0;
		return Qnil;
	}

	VALUE Graphics::freeze(VALUE self)
	{
		return Qnil;
	}

	VALUE Graphics::transition(VALUE self, VALUE duration, VALUE filename, VALUE vague)
	{
		return Qnil;
	}

}
