#include <ruby.h>

#include <april/ImageSource.h>
#include <april/RenderSystem.h>
#include <april/Texture.h>
#include <april/Timer.h>
#include <april/Window.h>
#include <gtypes/Rectangle.h>
#include <hltypes/hthread.h>
#include <hltypes/util.h>
#include <xal/AudioManager.h>

#include "ApplicationExitException.h"
#include "Bitmap.h"
#include "CodeSnippets.h"
#include "Graphics.h"
#include "Renderable.h"
#include "RenderQueue.h"
#include "rgss.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_mGraphics;

	RenderQueue* Graphics::renderQueue;
	int Graphics::width;
	int Graphics::height;
	bool Graphics::active;
	unsigned int Graphics::frameCount;
	unsigned int Graphics::frameRate;
	bool Graphics::running;
	bool Graphics::focused;
	april::Timer* Graphics::timer;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/
	
	void Graphics::_waitForFrameSync()
	{
#ifndef _DEBUG
		float waitTime = 1000.0f / frameRate - timer->diff();
		if (waitTime > 0.0f)
		{
			hthread::sleep(waitTime);
		}
#endif
	}

	void Graphics::_handleFocusChange()
	{
		if (!running)
		{
			throw ApplicationExitException();
		}
		if (focused)
		{
			april::rendersys->getWindow()->doEvents();
		}
		else
		{
			while (!focused)
			{
				april::rendersys->getWindow()->doEvents();
				hthread::sleep(40);
			}
		}
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/
	
	void Graphics::init()
	{
		april::Window* window = april::rendersys->getWindow();
		width = window->getWidth();
		height = window->getHeight();
		active = true;
		frameCount = 0;
		frameRate = 40;
		running = true;
		focused = true;
		renderQueue = new RenderQueue();
		timer = new april::Timer();
		timer->diff();
		Renderable::CounterProgress = 0;
	}

	void Graphics::createRubyInterface()
	{
		rb_mGraphics = rb_define_module("Graphics");
		rb_define_module_function(rb_mGraphics, "update", RUBY_METHOD_FUNC(&Graphics::rb_update), 0);
		rb_define_module_function(rb_mGraphics, "frame_count", RUBY_METHOD_FUNC(&Graphics::rb_getFrameCount), 0);
		rb_define_module_function(rb_mGraphics, "frame_count=", RUBY_METHOD_FUNC(&Graphics::rb_setFrameCount), 1);
		rb_define_module_function(rb_mGraphics, "frame_rate", RUBY_METHOD_FUNC(&Graphics::rb_getFrameRate), 0);
		rb_define_module_function(rb_mGraphics, "frame_rate=", RUBY_METHOD_FUNC(&Graphics::rb_setFrameRate), 1);
		rb_define_module_function(rb_mGraphics, "frame_reset", RUBY_METHOD_FUNC(&Graphics::rb_frameReset), 0);
		rb_define_module_function(rb_mGraphics, "freeze", RUBY_METHOD_FUNC(&Graphics::rb_freeze), 0);
		rb_define_module_function(rb_mGraphics, "transition", RUBY_METHOD_FUNC(&Graphics::rb_transition), -1);
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Graphics::rb_getFrameCount(VALUE self)
	{
		return INT2NUM(frameCount);
	}

	VALUE Graphics::rb_setFrameCount(VALUE self, VALUE value)
	{
		frameCount = (unsigned int)hmax(NUM2INT(value), 0);
		return Qnil;
	}

	VALUE Graphics::rb_getFrameRate(VALUE self)
	{
		return INT2NUM(frameRate);
	}

	VALUE Graphics::rb_setFrameRate(VALUE self, VALUE value)
	{
		frameRate = hclamp(NUM2UINT(value), (unsigned int)10, (unsigned int)120);
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Graphics::rb_update(VALUE self)
	{
		Graphics::_handleFocusChange();
		if (active)
		{
			april::rendersys->clear();
			renderQueue->draw();
			april::rendersys->presentFrame();
		}
		_waitForFrameSync();
		frameCount++;
		/// @todo - more often, less often?
		if (frameCount % 200 == 0)
		{
			rb_eval_string("GC.start");
		}
		return Qnil;
	}

	VALUE Graphics::rb_frameReset(VALUE self)
	{
		frameCount = 0;
		return Qnil;
	}

	VALUE Graphics::rb_freeze(VALUE self)
	{
		active = false;
		return Qnil;
	}

	VALUE Graphics::rb_transition(int argc, VALUE* argv, VALUE self)
	{
		VALUE arg1, arg2, arg3;
		rb_scan_args(argc, argv, "03", &arg1, &arg2, &arg3);
		int duration = hmax((NIL_P(arg1) ? 8 : NUM2INT(arg1)), 0);
		if (duration == 0)
		{
			active = true;
			return Graphics::rb_update(self);
		}
		hstr filename = (NIL_P(arg2) ? "" : StringValuePtr(arg2));
		int vague = (NIL_P(arg3) ? 40 : NUM2INT(arg3));
		grect drawRect(0.0f, 0.0f, (float)width, (float)height);
		grect srcRect(0.0f, 0.0f, 1.0f, 1.0f);
		april::Color color = APRIL_COLOR_WHITE;
		// capture old screen
		april::ImageSource* imageSource = april::rendersys->grabScreenshot(4);
		april::Texture* oldScreen = april::rendersys->createTextureFromMemory(imageSource->data, width, height);
		delete imageSource;
		// capture new screen
		april::rendersys->clear();
		renderQueue->draw();
		imageSource = april::rendersys->grabScreenshot(4);
		april::Texture* newScreen = april::rendersys->createTextureFromMemory(imageSource->data, width, height);
		delete imageSource;
		if (filename == "")
		{
			// fade between old and new screen
			for_iter (i, 0, duration)
			{
				Graphics::_handleFocusChange();
				april::rendersys->clear();
				april::rendersys->setTexture(oldScreen);
				april::rendersys->drawTexturedQuad(drawRect, srcRect);
				april::rendersys->setTexture(newScreen);
				color.a = (i + 1) * 255 / duration;
				april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
				april::rendersys->presentFrame();
				_waitForFrameSync();
				frameCount++;
				/// @todo - more often, less often?
				if (frameCount % 200 == 0)
				{
					rb_eval_string("GC.start");
				}
			}
		}
		else if (vague >= 0) // skip if vague is not 0 or greater
		{
			// small hack to make use of the safe texture loading code in Bitmap class
			Bitmap* bitmap = new Bitmap(filename);
			april::Texture* transition = bitmap->getTexture();
			bitmap->setTexture(NULL);
			delete bitmap;
			april::rendersys->setBlendMode(april::DEFAULT);
			int ambiguity = vague * 2;
			// fade between old and new screen
			for_iter (i, 0, duration)
			{
				Graphics::_handleFocusChange();
				april::rendersys->clear();
				april::rendersys->setTexture(oldScreen);
				april::rendersys->drawTexturedQuad(drawRect, srcRect);
				newScreen->insertAsAlphaMap(transition, (i + 1) * 255 / duration, ambiguity);
				april::rendersys->setTexture(newScreen);
				april::rendersys->drawTexturedQuad(drawRect, srcRect);
				april::rendersys->presentFrame();
				_waitForFrameSync();
				frameCount++;
				/// @todo - more often, less often?
				if (frameCount % 200 == 0)
				{
					rb_eval_string("GC.start");
				}
			}
			delete transition;
		}
		delete oldScreen;
		delete newScreen;
		active = true;
		return Qnil;
	}

}
