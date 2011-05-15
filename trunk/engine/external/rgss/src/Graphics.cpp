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

	int Graphics::width;
	int Graphics::height;
	bool Graphics::active;
	unsigned int Graphics::frameCount;
	unsigned int Graphics::frameRate;
	bool Graphics::running;
	april::Timer* Graphics::timer;
	RenderQueue* Graphics::renderQueue;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/
	
	void Graphics::_waitForFrameSync()
	{
		float time = timer->diff();
		float waitTime = 1000.0f / frameRate - hmax(time, 16.66667f);
		if (waitTime > 0.0f)
		{
			hthread::sleep(waitTime);
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
		if (!running)
		{
			rb_exit(0);
			return Qnil;
		}
		april::rendersys->getWindow()->doEvents();
		if (active)
		{
			april::rendersys->clear();
			renderQueue->draw();
			april::rendersys->presentFrame();
		}
		_waitForFrameSync();
		frameCount++;
		/// @todo - remove once threaded XAL works 100% fine
		xal::mgr->update(1000.0f / frameRate);
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
		int duration = (NIL_P(arg1) ? 8 : NUM2INT(arg1));
		hstr filename = (NIL_P(arg2) ? "" : StringValuePtr(arg2));
		if (filename != "")
		{
			hstr fullFilename = april::rendersys->findTextureFile(filename);
			/// @todo Implement bitmap loading and usage for transition
		}
		/// @todo Int or float?
		int vague = (NIL_P(arg3) ? 0 : NUM2INT(arg3));
		/*
		grect drawRect(0.0f, 0.0f, (float)width, (float)height);
		grect srcRect(0.0f, 0.0f, 1.0f, 1.0f);
		april::Color color = APRIL_COLOR_BLACK;
		april::ImageSource* screenshot = april::rendersys->grabScreenshot();
		april::ImageSource* imageSource = april::createEmptyImage(width, height);
		imageSource->copyImage(screenshot, 4);
		delete screenshot;
		april::Texture* texture = april::rendersys->createTextureFromMemory(imageSource->data, width, height);
		delete imageSource;
		*/
		int duration0 = duration / 2;
		int duration1 = duration - duration / 2;
		for_iter (i, 0, duration0)
		{
			april::rendersys->getWindow()->doEvents();
			april::rendersys->clear();
			/*
			april::rendersys->setTexture(texture);
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
			color.a = i * 255 / duration0;
			april::rendersys->drawColoredQuad(drawRect, color);
			*/
			april::rendersys->presentFrame();
			_waitForFrameSync();
			/// @todo - remove once threaded XAL works 100% fine
			xal::mgr->update(1000.0f / frameRate);
		}
		/*
		delete texture;
		april::rendersys->clear();
		renderQueue->draw();
		screenshot = april::rendersys->grabScreenshot();
		april::rendersys->clear();
		imageSource = april::createEmptyImage(width, height);
		imageSource->copyImage(screenshot, 4);
		delete screenshot;
		texture = april::rendersys->createTextureFromMemory(imageSource->data, width, height);
		delete imageSource;
		*/
		for_iter (i, 0, duration1)
		{
			april::rendersys->getWindow()->doEvents();
			april::rendersys->clear();
			/*
			april::rendersys->setTexture(texture);
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
			color.a = (duration1 - i) * 255 / duration1;
			april::rendersys->drawColoredQuad(drawRect, color);
			*/
			april::rendersys->presentFrame();
			_waitForFrameSync();
			/// @todo - remove once threaded XAL works 100% fine
			xal::mgr->update(1000.0f / frameRate);
		}
		//delete texture;
		active = true;
		return Qnil;
	}

}
