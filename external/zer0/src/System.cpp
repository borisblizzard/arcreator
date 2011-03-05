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

#include "Constants.h"
#include "Context.h"
#include "System.h"
#include "TransitionManager.h"

namespace zer0
{
	System* system = NULL;
	hstr path = "";

	/****************************************************************************************
	 * Construct/Destruct
	 ****************************************************************************************/

	System::System(chstr path) : Time(0.0f), exiting(false), focused(true)
	{
		this->Path = path;
	}
	
	System::~System()
	{
	}
	
	/****************************************************************************************
	 * Update
	 ****************************************************************************************/
	
	bool System::update(float k)
	{
		this->Time = hclamp(k, 0.0001f, 0.1f);
#ifndef _THREADED_SOUND
		xal::mgr->update(this->Time);
#endif
		return this->_update();
	}
	
	/// @brief System update loop for ARC.
	/// @return True if host application is still running, otherwise false.
	bool System::_update()
	{
		zer0::context->update();
		if (zer0::context->isKeyPressed(april::AK_ESCAPE))
		{
			return false;
		}
		return true;
	}
	
	/****************************************************************************************
	 * Events
	 ****************************************************************************************/

	void System::onMouseDown(float x, float y, int button)
	{
		zer0::context->onMouseDown(x, y, button);
	}

	void System::onMouseUp(float x, float y, int button)
	{
		zer0::context->onMouseUp(x, y, button);
	}

	void System::onMouseMove(float x, float y)
	{
		zer0::context->onMouseMove(x, y);
	}
	
	void System::onKeyDown(unsigned int keycode)
	{
		zer0::context->onKeyDown(keycode);
	}

	void System::onKeyUp(unsigned int keycode)
	{
		zer0::context->onKeyUp(keycode);
	}
	
	void System::onChar(unsigned int charcode)
	{
		zer0::context->onChar(charcode);
	}

	bool System::onQuit(bool canCancel)
	{
		return true;
	}
	
	void System::onFocusChange(bool focused)
	{
	}

}
