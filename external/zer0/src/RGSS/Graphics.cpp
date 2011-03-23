#include <ruby.h>

#include <april/RenderSystem.h>
#include <april/Window.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

#include "RGSS/Graphics.h"
#include "RGSS/Sprite.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		unsigned int Graphics::frameCount = 0;
		unsigned int Graphics::frameRate = 40;
		harray<RGSS::Sprite*> sprites;

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

		void Graphics::init()
		{
		}

		void Graphics::addSprite(RGSS::Sprite* sprite)
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

		void Graphics::removeSprite(RGSS::Sprite* sprite)
		{
			sprites -= sprite;
		}

		void Graphics::updateSprite(RGSS::Sprite* sprite)
		{
			removeSprite(sprite);
			addSprite(sprite);
		}

		VALUE Graphics::update(VALUE self)
		{
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
}
