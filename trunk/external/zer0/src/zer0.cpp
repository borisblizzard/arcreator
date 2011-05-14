#include <stdio.h>
#include <time.h>

#include <ruby/extensions.h>
#include <ruby/ruby.h>

#include <april/RenderSystem.h>
#include <april/Window.h>
#include <atres/atres.h>
#include <aprilui/aprilui.h>
#include <hltypes/exception.h>
#include <hltypes/hfile.h>
#include <hltypes/hstring.h>
#include <hltypes/util.h>
#include <rgss/rgss.h>
#include <xal/AudioManager.h>
#include <xal/xal.h>

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
	
	void setLogFunction(void (*function)(chstr))
	{
		g_logFunction = function;
	}
	
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
			xal::init(XAL_AS_DEFAULT, (unsigned long)april::rendersys->getWindow()->getIDFromBackend(), true);
#else
			xal::init(XAL_AS_DEFAULT, (unsigned long)april::rendersys->getWindow()->getIDFromBackend(), false);
#endif
#else
			xal::init(XAL_AS_DISABLED, (unsigned long)april::rendersys->getWindow()->getIDFromBackend(), false);
#endif
#ifndef __BIG_ENDIAN__
			april::rendersys->setIdleTextureUnloadTime(TEXTURE_UNLOAD_TIME);
#else
			april::rendersys->setIdleTextureUnloadTime(0);
#endif
			atres::setGlobalOffsets(true);
			atres::loadFont("Graphics/Fonts/Arial.font");
			aprilui::setLimitCursorToViewport(false);
			aprilui::setViewport(grect(0.0f, 0.0f, (float)width, (float)height));
			aprilui::setScreenViewport(aprilui::getViewport());
			april::rendersys->setOrthoProjection(aprilui::getViewport());
			april::rendersys->getWindow()->setKeyboardCallbacks(
				zer0::Context::onKeyDown, zer0::Context::onKeyUp, zer0::Context::onChar);
			april::rendersys->getWindow()->setQuitCallback(&System::onQuit);
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
		rgss::init(g_logFunction);
		// running the Ruby scripts
		//rb_require("./test.rb");
		rb_load(rb_str_new2("./Data/RMXP.rb"), 0);
		rb_load(rb_str_new2("./Data/System.rb"), 0);
		rb_load(rb_str_new2("./Data/Scripts.rb"), 0);
		rgss::destroy();
		return Qnil;
	}

	void displayRubyError()
	{
		VALUE error = rb_gv_get("$!");
		VALUE message = rb_funcall(error, rb_intern("message"), 0, NULL);
		hstr title = april::rendersys->getWindow()->getWindowTitle();
		hstr text = StringValuePtr(message);
		april::messageBox(title, text, april::AMSGBTN_OK, april::AMSGSTYLE_WARNING);
	}

	int enterMainLoop(int argc, char** argv)
	{
		// initialization of all Ruby related parts
#ifdef HAVE_LOCALE_H
	    setlocale(LC_CTYPE, "");
#endif
		int state;
		ruby_sysinit(&argc, &argv);
		RUBY_INIT_STACK;
		ruby_init();
		ruby_init_loadpath();
		ruby_script("ARC");
#ifndef _DEBUG
		if (argc >= 2 && hstr(argv[1]).lower() == "-debug")
#endif
		{
			rb_eval_string("$DEBUG = true");
		}
		// initializing statically linked Ruby extensions
		Init_api();
		// running everything
		rb_protect(embedded, Qnil, &state);
		if (state != 0)
		{
			displayRubyError();
		}
		return ruby_cleanup(state);
	}

}
