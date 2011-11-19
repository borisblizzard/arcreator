#include <stdio.h>
#include <time.h>

#include <ruby/extensions.h>
#include <ruby/ruby.h>

#include <april/RenderSystem.h>
#include <april/Window.h>
#include <atres/atres.h>
#include <atres/Renderer.h>
#include <atresttf/atresttf.h>
#include <atresttf/FontResourceTtf.h>
#include <aprilui/aprilui.h>
#include <hltypes/exception.h>
#include <hltypes/hdir.h>
#include <hltypes/hfile.h>
#include <hltypes/hstring.h>
#include <hltypes/util.h>
#include <rgss/ApplicationExitException.h>
#include <rgss/rgss.h>
#include <xal/AudioManager.h>
#include <xal/xal.h>

#include "ARC.h"
#include "ARC_Data.h"
#include "ARC_Error.h"
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
	bool debugMode;
	void (*g_logFunction)(chstr, chstr);
	
	void logLib(chstr message)
	{
		g_logFunction(zer0::system->Path, message);
	}

	void log(chstr message, chstr prefix)
	{
		g_logFunction(zer0::system->Path, prefix + message);
	}

	void displayRubyError()
	{
		VALUE error = rb_gv_get("$!");
		VALUE message = rb_funcall_0(error, "message");
		hstr text = StringValueCStr(message);
		VALUE backtrace = rb_funcall_0(error, "backtrace");
		VALUE backtraceMessage = rb_funcall_1(backtrace, "join", rb_str_new2("\n"));
		VALUE rb_mDir = rb_funcall_1(rb_mKernel, "const_get", rb_f_to_sym(rb_str_new2("Dir")));
		rb_funcall_2(backtraceMessage, "gsub!", rb_funcall_0(rb_mDir, "pwd"), rb_str_new2(""));
		text += hstr("\n") + StringValueCStr(backtraceMessage);
		zer0::log(text, "");
		april::messageBox(zer0::system->Title, text, april::AMSGBTN_OK, april::AMSGSTYLE_WARNING);
	}

	VALUE rb_Kernel_print(int argc, VALUE* argv, VALUE self)
	{
		VALUE arg1 = Qnil;
		VALUE args = Qnil;
		rb_scan_args(argc, argv, "1*", &arg1, &args);
		if (NIL_P(args))
		{
			args = rb_ary_new();
		}
		rb_ary_unshift(args, arg1);
		VALUE rb_delimiter = rb_gv_get("$,");
		hstr delimiter = (NIL_P(rb_delimiter) ? ", " : StringValueCStr(rb_delimiter));
		harray<hstr> data;
		VALUE string;
		for_iter (i, 0, argc)
		{
			string = rb_ary_shift(args);
			if (!rb_obj_is_instance_of(string, rb_cString))
			{
				string = rb_f_to_s(string);
			}
			data += StringValueCStr(string);
		}
		hstr text = data.join(delimiter);
		zer0::log(text, "");
		return Qnil;
	}
	
	VALUE rb_Kernel_p(int argc, VALUE* argv, VALUE self)
	{
		VALUE result = Qnil;
		VALUE args = Qnil;
		rb_scan_args(argc, argv, "0*", &args);
		hstr text = "nil";
		if (argc > 0)
		{
			if (argc == 1)
			{
				result = rb_ary_entry(args, 0);
			}
			else
			{
				result = rb_f_clone(args);
			}
			VALUE rb_delimiter = rb_gv_get("$,");
			hstr delimiter = (NIL_P(rb_delimiter) ? ", " : StringValueCStr(rb_delimiter));
			harray<hstr> data;
			VALUE string;
			for_iter (i, 0, argc)
			{
				string = rb_ary_shift(args);
				string = rb_f_inspect(string);
				data += StringValueCStr(string);
			}
			text = data.join(delimiter);
		}
		zer0::log(text, "");
		april::messageBox(zer0::system->Title, text, april::AMSGBTN_OK, april::AMSGSTYLE_INFORMATION);
		return result;
	}
	
	VALUE rb_Kernel_loadData(VALUE self, VALUE filename)
	{
		// TODO - unsafe, should be done with a rb_protect block
		VALUE rb_mMarshal = rb_funcall_1(rb_mKernel, "const_get", rb_f_to_sym(rb_str_new2("Marshal")));
		VALUE file = rb_funcall_2(rb_cFile, "open", filename, rb_str_new2("rb"));
		VALUE data = rb_funcall_1(rb_mMarshal, "load", file);
		rb_funcall_0(file, "close");
		return data;
		//*/
	}
	
	bool isDebugMode()
	{
		return debugMode;
	}
	
	void setDebugMode(bool value)
	{
		debugMode = value;
	}

	bool init(void (*function)(chstr, chstr))
	{
		g_logFunction = function;
		zer0::system = new zer0::System();
		harray<int> resolution = zer0::system->Parameters[CFG_RESOLUTION].split("x").cast<int>();
		bool fullscreen = (bool)zer0::system->Parameters[CFG_FULLSCREEN];
		debugMode = false;
		bool result = true;
		srand((unsigned int)time(NULL));
		try
		{
#ifdef _DEBUG
			april::setLogFunction(&zer0::logLib);
			atres::setLogFunction(&zer0::logLib);
			aprilui::setLogFunction(&zer0::logLib);
			xal::setLogFunction(&zer0::logLib);
#endif
			// april
			april::init();
			april::createRenderSystem("");
			april::createRenderTarget(resolution[0], resolution[1], fullscreen, zer0::system->Title);
#ifndef __BIG_ENDIAN__
			april::rendersys->setIdleTextureUnloadTime(TEXTURE_UNLOAD_TIME);
#else
			april::rendersys->setIdleTextureUnloadTime(0);
#endif
			grect viewport(0.0f, 0.0f, (float)resolution[0], (float)resolution[1]);
			april::rendersys->setOrthoProjection(viewport);
			april::rendersys->getWindow()->setKeyboardCallbacks(
				zer0::Context::onKeyDown, zer0::Context::onKeyUp, zer0::Context::onChar);
			april::rendersys->getWindow()->setQuitCallback(&System::onQuit);
			april::rendersys->getWindow()->setWindowFocusCallback(&System::onFocusChange);
			// atres
			atres::init();
			atresttf::init();
			atres::renderer->setGlobalOffsets(true);
			atres::renderer->registerFontResource(new atresttf::FontResourceTtf(
				"Graphics/Fonts/arial_1.ttf", "Arial", 48.0f, 1.0f, 56.0f));
			atres::renderer->registerFontResource(new atresttf::FontResourceTtf(
				"Graphics/Fonts/ariblk.ttf", "Arial Black", 64.0f, 1.0f));
			// aprilui
#ifndef LEGACY_ONLY
			aprilui::init();
			aprilui::setLimitCursorToViewport(false);
			aprilui::setViewport(viewport);
			aprilui::setScreenViewport(aprilui::getViewport());
#endif
			// xal
#ifndef _NOSOUND
			xal::init(XAL_AS_DEFAULT, (unsigned long)april::rendersys->getWindow()->getIDFromBackend(), true);
#else
			xal::init(XAL_AS_DISABLED, (unsigned long)april::rendersys->getWindow()->getIDFromBackend(), false);
#endif
			// zer0 related data
			zer0::log("initializing Zer0 Division Engine");
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
			// destroy other
			delete zer0::context;
			delete zer0::transitionManager;
			xal::destroy();
#ifndef LEGACY_ONLY
			aprilui::destroy();
#endif
			atresttf::destroy();
			atres::destroy();
			april::destroy();
			delete zer0::system;
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
		// creating Ruby interfaces of C++ classes created for Ruby
		ARC::createRubyInterface();
		ARC_Data::createRubyInterface();
		ARC_Error::createRubyInterface();
		// initialization of Ruby classes
		ARC::init();
		ARC_Data::init();
		ARC_Error::init();
		// running RGSS
#ifdef _DEBUG
		rgss::setLogFunction(&zer0::logLib);
#endif
		rgss::init(zer0::system->Parameters);
		// running the Ruby scripts
		harray<hstr> files = hdir::files("./Data/Scripts");
		harray<hstr> scripts;
		harray<hstr> parts;
		foreach (hstr, it, files)
		{
			parts = (*it).split("-", 1, true);
			if (parts.size() == 2 && parts[0].size() == 4 && parts[0].is_number() && parts[1].ends_with(".rb"))
			{
				scripts += "./Data/Scripts/" + (*it);
			}
		}
		scripts.sort();
		rb_load(rb_str_new2("./Data/RMXP.rb"), 0); // TODO - will be removed later
		rb_load(rb_str_new2("./Data/System.rb"), 0); // TODO - will be removed later
		foreach (hstr, it, scripts)
		{
			rb_load(rb_str_new2((*it).c_str()), 0);
		}
		rgss::destroy();
		ARC::destroy();
		ARC_Data::destroy();
		ARC_Error::destroy();
		return Qnil;
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
			zer0::setDebugMode(true);
			rgss::setDebugMode(true);
		}
		// initializing statically linked Ruby extensions
		Init_api();
		// additional Ruby stuff
		rb_define_method(rb_mKernel, "print", RUBY_METHOD_FUNC(&rb_Kernel_print), -1);
		rb_define_method(rb_mKernel, "puts", RUBY_METHOD_FUNC(&rb_Kernel_print), -1);
		rb_define_method(rb_mKernel, "p", RUBY_METHOD_FUNC(&rb_Kernel_p), -1);
		rb_define_method(rb_mKernel, "load_data", RUBY_METHOD_FUNC(&rb_Kernel_loadData), 1);
		// running everything
		try
		{
			rb_protect(embedded, Qnil, &state);
			if (state != 0)
			{
				displayRubyError();
			}
			ruby_cleanup(state);
		}
		catch (rgss::ApplicationExitException e)
		{
			// ALT+F4 exit or window close button exit
		}
		catch (hltypes::exception e)
		{
			zer0::log(e.message());
		}
		catch (hstr e)
		{
			zer0::log(e);
		}
		return 0;
	}

}
