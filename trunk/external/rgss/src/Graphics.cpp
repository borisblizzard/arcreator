#include <ruby.h>

#include <april/RenderSystem.h>
#include <april/Window.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

#include "Graphics.h"
#include "Sprite.h"
#include "CodeSnippets.h"

namespace rgss
{
	unsigned int Graphics::frameCount;
	unsigned int Graphics::frameRate;
	bool Graphics::running;
	harray<Sprite*> sprites;

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

	void Graphics::addSprite(Sprite* sprite)
	{
		for_iter (i, 0, sprites.size())
		{
			if (sprite->z < sprites[i]->z)
			{
				sprites.insert_at(i, sprite);
				return;
			}
		}
		sprites += sprite;
	}

	void Graphics::removeSprite(Sprite* sprite)
	{
		sprites -= sprite;
	}

	void Graphics::updateSprite(Sprite* sprite)
	{
		removeSprite(sprite);
		addSprite(sprite);
	}

	VALUE Graphics::update(VALUE self)
	{
		if (!running)
		{
			rb_exit(0);
			return Qnil;
		}
		// some testing for now
		april::rendersys->clear();
		//harray<Sprite*> sprites
		foreach (Sprite*, it, sprites)
		{
			(*it)->draw();
		}
		april::rendersys->presentFrame();
		frameCount++;
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
		return Qnil;
	}

}
