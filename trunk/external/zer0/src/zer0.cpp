#include <stdio.h>
#include <time.h>

#include <april/RenderSystem.h>
#include <april/Window.h>
#include <atres/atres.h>
#include <aprilui/aprilui.h>
#include <hltypes/exception.h>
#include <hltypes/hstring.h>
#include <xal/AudioManager.h>

#include <ruby/ruby.h>

#include "RGSS/Audio.h"
#include "RGSS/Bitmap.h"
#include "RGSS/Color.h"
#include "RGSS/Font.h"
#include "RGSS/Graphics.h"
#include "RGSS/Input.h"
#include "RGSS/Plane.h"
#include "RGSS/Rect.h"
#include "RGSS/RGSSError.h"
#include "RGSS/Sprite.h"
#include "RGSS/Table.h"
#include "RGSS/Tilemap.h"
#include "RGSS/Tone.h"
#include "RGSS/Viewport.h"
#include "RGSS/Window.h"

#include "CodeSnippets.h"
#include "Constants.h"
#include "Context.h"
#include "System.h"
#include "TransitionManager.h"
#include "zer0.h"

namespace zer0
{
	bool result;
	grect drawRect;
	void (*g_logFunction)(chstr);
	
	void log(chstr message, chstr prefix)
	{
		g_logFunction(prefix + message);
	}
	
	bool init(int width, int height, bool fullscreen, chstr name, chstr path, void (*logFunction)(chstr))
	{
		bool result = true;
		srand((unsigned int)time(NULL));
		try
		{
			g_logFunction = logFunction;
			april::setLogFunction(logFunction);
			atres::setLogFunction(logFunction);
			aprilui::setLogFunction(logFunction);
			xal::setLogFunction(logFunction);
			april::init("arc", width, height, fullscreen, name);
			atres::init();
			aprilui::init();
#ifndef _NOSOUND
#ifdef _THREADED_SOUND
			xal::init("", true);
#else
			xal::init("", false);
#endif
#else
			xal::init("nosound", false);
#endif
#ifndef __BIG_ENDIAN__
			april::rendersys->setIdleTextureUnloadTime(TEXTURE_UNLOAD_TIME);
#else
			april::rendersys->setIdleTextureUnloadTime(0);
#endif
			atres::setGlobalOffsets(true);
			aprilui::setLimitCursorToViewport(false);
			aprilui::setViewport(grect(0.0f, 0.0f, (float)width, (float)height));
			aprilui::setScreenViewport(aprilui::getViewport());
			april::rendersys->setOrthoProjection(aprilui::getViewport());
			april::rendersys->getWindow()->setKeyboardCallbacks(
				zer0::Context::onKeyDown, zer0::Context::onKeyUp, zer0::Context::onChar);
			// zer0 related data
			zer0::log("initializing Zer0 Division Engine");
			zer0::system = new zer0::System(path);
			zer0::context = new zer0::Context();
			zer0::transitionManager = new zer0::TransitionManager();
		}
		catch (hltypes::exception e)
		{
			zer0::log(e.message());
			result = false;
		}
		catch (hstr e)
		{
			zer0::log(e);
			result = false;
		}
		return result;
	}
	
	bool destroy()
	{
		bool result = true;
		try
		{
			zer0::log("destroying Zer0 Division Engine");
			delete zer0::system;
			delete zer0::context;
			delete zer0::transitionManager;
			xal::destroy();
			aprilui::destroy();
			atres::destroy();
			april::destroy();
		}
		catch (hltypes::exception e)
		{
			zer0::log(e.message());
			result = false;
		}
		catch (hstr e)
		{
			zer0::log(e);
			result = false;
		}
		return result;
	}
	
	VALUE embedded(VALUE ignore)
	{
		// initialization of modules
		RGSS::Audio::init();
		RGSS::Graphics::init();
		RGSS::Input::init();
		// creating Ruby interfaces of C++ classes created for Ruby
		RGSS::Audio::createRubyInterface();
		RGSS::Bitmap::createRubyInterface();
		RGSS::Color::createRubyInterface();
		RGSS::Font::createRubyInterface();
		RGSS::Graphics::createRubyInterface();
		RGSS::Input::createRubyInterface();
		RGSS::Plane::createRubyInterface();
		RGSS::Rect::createRubyInterface();
		RGSS::RGSSError::createRubyInterface();
		RGSS::Sprite::createRubyInterface();
		RGSS::Table::createRubyInterface();
		RGSS::Tilemap::createRubyInterface();
		RGSS::Tone::createRubyInterface();
		RGSS::Viewport::createRubyInterface();
		RGSS::Window::createRubyInterface();
		// running the Ruby scripts
		rb_require("./test.rb");
		return Qnil;
	}

	int enterMainLoop(int argc, char** argv)
	{
#ifdef HAVE_LOCALE_H
	    setlocale(LC_CTYPE, "");
#endif
		int state;
		ruby_sysinit(&argc, &argv);
		RUBY_INIT_STACK;
		ruby_init();
		ruby_init_loadpath();
		rb_protect(embedded, Qnil, &state);
		return ruby_cleanup(state);
	}

}
