#include <stdio.h>

#include <april/Keys.h>
#include <april/RenderSystem.h>
#include <aprilui/Animator.h>
#include <aprilui/aprilui.h>
#include <aprilui/Dataset.h>
#include <aprilui/Objects.h>
#include <hltypes/harray.h>
#include <hltypes/hdir.h>
#include <hltypes/hfile.h>
#include <hltypes/hstring.h>
#include <hltypes/util.h>
#include <xal/AudioManager.h>

#include "System/Constants.h"
#include "System/Context.h"
#include "System/Main.h"
#include "System/TransitionManager.h"
#include "System/Utility.h"

namespace System
{
	Main* main = NULL;
	hstr path = "";

	/****************************************************************************************
	 * Construct/Destruct
	 ****************************************************************************************/

	Main::Main() : Time(0.0f), exiting(false), focused(true)
	{
	}
	
	Main::~Main()
	{
	}
	
	/// @todo Add Linux and Mac variants.
	void _setupSystemPath()
	{
#ifdef _DEBUG
		System::path = "bin/log";
#elif defined(_WIN32)
		System::path = getenv("ALLUSERSPROFILE");
		System::path = System::path.replace("\\", "/");
		if (getenv("LOCALAPPDATA") == NULL) // Vista / 7
		{
			System::path += "/" + hstr(getenv("APPDATA")).split("\\").pop_back();
		}
		const wchar_t* name = _wgetenv(L"USERNAME");
		hstr username;
		for (int i = 0; name[i] != 0; i++)
		{
			username += (char)(name[i] > 0x80 ? 0x40 + (name[i] % 26) : name[i]);
		}
		System::path += hsprintf("/%s/%s/%s", "ARC", "ExampleGameName", username.c_str());
#endif
		hdir::create(System::path);
		System::path += "/";
	}

	void create()
	{
		_setupSystemPath();
		hfile::create_new(System::path + "log.txt");
		System::main = new System::Main();
		System::context = new System::Context();
		System::transitionManager = new System::TransitionManager();
	}
	
	void init()
	{
	}
	
	void clear()
	{
		delete System::main;
	}
	
	void destroy()
	{
		delete System::context;
		delete System::transitionManager;
	}
	
	/****************************************************************************************
	 * Update
	 ****************************************************************************************/
	
	bool Main::update(float k)
	{
		this->Time = hclamp(k, 0.0001f, 0.1f);
#ifndef _THREADED_SOUND
		xal::mgr->update(this->Time);
#endif
		return this->_update();
	}
	
	/// @brief Main update loop for ARC.
	/// @return True if host application is still running, otherwise false.
	bool Main::_update()
	{
		System::context->update();
		if (System::context->isKeyPressed(april::AK_ESCAPE))
		{
			return false;
		}
		return true;
	}
	
	/****************************************************************************************
	 * Events
	 ****************************************************************************************/

	void Main::onMouseDown(float x, float y, int button)
	{
		System::context->onMouseDown(x, y, button);
	}

	void Main::onMouseUp(float x, float y, int button)
	{
		System::context->onMouseUp(x, y, button);
	}

	void Main::onMouseMove(float x, float y)
	{
		System::context->onMouseMove(x, y);
	}
	
	void Main::onKeyDown(unsigned int keycode)
	{
		System::context->onKeyDown(keycode);
	}

	void Main::onKeyUp(unsigned int keycode)
	{
		System::context->onKeyUp(keycode);
	}
	
	void Main::onChar(unsigned int charcode)
	{
		System::context->onChar(charcode);
	}

	bool Main::onQuit(bool canCancel)
	{
		return true;
	}
	
	void Main::onFocusChange(bool focused)
	{
	}

}
