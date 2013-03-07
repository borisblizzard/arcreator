#include <stdio.h>

#include <ruby/ruby.h>
#include <ruby/_extensions.h>

#include <april/april.h>
#include <april/PixelShader.h>
#include <april/Platform.h>
#include <april/RenderSystem.h>
#include <april/VertexShader.h>
#include <april/Window.h>
#include <atres/atres.h>
#include <atres/Renderer.h>
#include <atresttf/atresttf.h>
#include <atresttf/FontResourceTtf.h>
#ifndef LEGACY_ONLY
#include <aprilui/aprilui.h>
#endif
#include <hltypes/exception.h>
#include <hltypes/hdir.h>
#include <hltypes/hfile.h>
#include <hltypes/hlog.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>
#include <legacy/ApplicationExitException.h>
#include <legacy/legacy.h>
#include <xal/AudioManager.h>
#include <xal/xal.h>

#include "ApplicationExitException.h"
#include "ARC.h"
#include "ARC_Data.h"
#include "ARC_Error.h"
#include "CodeSnippets.h"
#include "Constants.h"
#include "Context.h"
#include "System.h"
#include "TransitionManager.h"
#include "reactor.h"

namespace reactor
{
	hstr logTag = "reactor";

	bool result;
	grect drawRect;
	bool debugMode;
	april::VertexShader* vertexShader = NULL;
	april::PixelShader* pixelShader = NULL;
	
	void displayRubyError()
	{
		VALUE error = rb_gv_get("$!");
		VALUE message = rb_funcall_0(error, "message");
		hstr text = StringValueCStr(message);
		VALUE backtrace = rb_funcall_0(error, "backtrace");
		VALUE backtraceMessage = rb_ary_join(backtrace, rb_str_new2("\n"));
		VALUE rb_mDir = rb_const_get(rb_mKernel, rb_intern("Dir")); \
		rb_funcall_2(backtraceMessage, "gsub!", rb_funcall_0(rb_mDir, "pwd"), rb_str_new2(""));
		text += hstr("\n") + StringValueCStr(backtraceMessage);
		hlog::error(reactor::logTag, text);
		april::messageBox(reactor::system->Title, text, april::AMSGBTN_OK, april::AMSGSTYLE_WARNING);
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
		hlog::write(reactor::logTag, text);
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
				result = rb_obj_clone(args);
			}
			VALUE rb_delimiter = rb_gv_get("$,");
			hstr delimiter = (NIL_P(rb_delimiter) ? ", " : StringValueCStr(rb_delimiter));
			harray<hstr> data;
			VALUE string;
			for_iter (i, 0, argc)
			{
				string = rb_inspect(rb_ary_shift(args));
				data += StringValueCStr(string);
			}
			text = data.join(delimiter);
		}
		hlog::write(reactor::logTag, text);
		april::messageBox(reactor::system->Title, text, april::AMSGBTN_OK, april::AMSGSTYLE_INFORMATION);
		return result;
	}
	
	VALUE _safe_loadData(VALUE file)
	{
		VALUE rb_mMarshal = rb_const_get(rb_mKernel, rb_intern("Marshal"));
		return rb_funcall_1(rb_mMarshal, "load", file);
	}
	
	VALUE rb_Kernel_loadData(VALUE self, VALUE filename)
	{
		VALUE file = rb_file_open(StringValueCStr(filename), "rb");
		int exception;
		VALUE data = rb_protect(&_safe_loadData, file, &exception);
		rb_io_close(file);
		if (exception != 0)
		{
			rb_jump_tag(exception);
		}
		return data;
	}
	
	VALUE rb_Kernel_exit(int argc, VALUE* argv, VALUE self)
	{
		throw ApplicationExitException();
	}
	
	VALUE rb_Kernel_exit1(VALUE self, VALUE args)
	{
		throw ApplicationExitException();
	}
	
	bool isDebugMode()
	{
		return debugMode;
	}
	
	void setDebugMode(bool value)
	{
		debugMode = value;
	}

	bool init()
	{
		reactor::system = new reactor::System();
		harray<int> resolution = reactor::system->Parameters[CFG_RESOLUTION].split("x").cast<int>();
		bool fullscreen = (bool)reactor::system->Parameters[CFG_FULLSCREEN];
		debugMode = false;
		bool result = true;
		srand(get_system_time());
		if ((bool)reactor::system->Parameters[CFG_LOGGING])
		{
			hlog::setFilename(reactor::system->Path + "log.txt");
		}
		try
		{
			// april
			april::init(april::RS_DEFAULT, april::WS_DEFAULT);
			april::createRenderSystem();
			april::createWindow(resolution[0], resolution[1], fullscreen, reactor::system->Title);
			grect viewport(0.0f, 0.0f, (float)resolution[0], (float)resolution[1]);
			april::rendersys->setOrthoProjection(viewport);
			april::window->setKeyboardCallbacks(&reactor::Context::onKeyDown, &reactor::Context::onKeyUp, &reactor::Context::onChar);
			april::window->setQuitCallback(&System::onQuit);
			april::window->setFocusChangeCallback(&System::onFocusChange);
			// TODO
			reactor::vertexShader = april::rendersys->createVertexShader();
			reactor::vertexShader->compile(ARC_VERTEX_SHADER);
			reactor::pixelShader = april::rendersys->createPixelShader();
			reactor::pixelShader->compile(ARC_PIXEL_SHADER);
			// atres
			atres::init();
			atresttf::init();
			atres::renderer->setGlobalOffsets(true);
			// aprilui
#ifndef LEGACY_ONLY
			aprilui::init();
			aprilui::setLimitCursorToViewport(false);
			aprilui::setViewport(viewport);
			aprilui::setTextureIdleUnloadTime(TEXTURE_UNLOAD_TIME);
#endif
			// xal
#ifndef _NOSOUND
			xal::init(XAL_AS_DEFAULT, april::window->getBackendId(), true);
#else
			xal::init(XAL_AS_DISABLED, april::window->getBackendId(), false);
#endif
			// reactor related data
			hlog::write(reactor::logTag, "Initializing ARC Reactor Engine.");
			reactor::context = new reactor::Context();
			reactor::transitionManager = new reactor::TransitionManager();
		}
		catch (hltypes::exception& e)
		{
			hlog::error(reactor::logTag, e.message());
			result = false;
		}
		catch (hstr e)
		{
			hlog::error(reactor::logTag, e);
			result = false;
		}
		return result;
	}
	
	bool destroy()
	{
		bool result = true;
		try
		{
			delete reactor::vertexShader;
			delete reactor::pixelShader;
			hlog::write(reactor::logTag, "Destroying ARC Reactor Engine.");
			// destroy other
			delete reactor::context;
			delete reactor::transitionManager;
			xal::destroy();
#ifndef LEGACY_ONLY
			aprilui::destroy();
#endif
			atresttf::destroy();
			atres::destroy();
			april::destroy();
			delete reactor::system;
		}
		catch (hltypes::exception& e)
		{
			hlog::error(reactor::logTag, e.message());
			result = false;
		}
		catch (hstr e)
		{
			hlog::error(reactor::logTag, e);
			result = false;
		}
		return result;
	}
	
	VALUE embedded(VALUE ignored)
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
		legacy::init(reactor::system->Parameters);
		legacy::setPixelShader(reactor::pixelShader);
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
		legacy::destroy();
		ARC::destroy();
		ARC_Data::destroy();
		ARC_Error::destroy();
		return Qnil;
	}

	int enterMainLoop(harray<hstr> args)
	{
		// initialization of all Ruby related parts
#ifdef HAVE_LOCALE_H
	    setlocale(LC_CTYPE, "");
#endif
		// argc/argv
		const char** cArgs = new const char*[args.size()];
		for_iter (i, 0, args.size())
		{
			cArgs[i] = args[i].c_str();
		}
		int argc = args.size();
		char** argv = (char**)cArgs;
		ruby_sysinit(&argc, &argv);
		delete [] cArgs;
		// Ruby
		int exception = 0;
		RUBY_INIT_STACK;
		ruby_init();
		ruby_init_loadpath();
		ruby_script(reactor::system->Parameters[CFG_TITLE].c_str());
#ifndef _DEBUG
		if (args.size() >= 2 && args[1].lower() == "-debug")
#endif
		{
			rb_eval_string("$DEBUG = true");
			reactor::setDebugMode(true);
			legacy::setDebugMode(true);
		}
		// initializing extensions
		Init_xwin32api();
		Init_socket();
		Init_zlib();
		// additional Ruby stuff
		rb_define_method(rb_mKernel, "print", RUBY_METHOD_FUNC(&rb_Kernel_print), -1);
		rb_define_method(rb_mKernel, "puts", RUBY_METHOD_FUNC(&rb_Kernel_print), -1);
		rb_define_method(rb_mKernel, "p", RUBY_METHOD_FUNC(&rb_Kernel_p), -1);
		rb_define_method(rb_mKernel, "load_data", RUBY_METHOD_FUNC(&rb_Kernel_loadData), 1);
		rb_define_method(rb_mKernel, "exit", RUBY_METHOD_FUNC(&rb_Kernel_exit), -1);
		rb_define_method(rb_mKernel, "exit!", RUBY_METHOD_FUNC(&rb_Kernel_exit), -1);
		// running everything
		try
		{
			rb_protect(&embedded, Qnil, &exception);
			if (exception != 0)
			{
				displayRubyError();
			}
		}
		catch (legacy::ApplicationExitException&)
		{
			// ALT+F4 exit or window close button exit
			hlog::write(reactor::logTag, "Application Exit.");
		}
		catch (hltypes::exception& e)
		{
			hlog::error(reactor::logTag, e.message());
		}
		catch (hstr e)
		{
			hlog::error(reactor::logTag, e);
		}
		rb_gc();
		return ruby_cleanup(exception);
	}

}
