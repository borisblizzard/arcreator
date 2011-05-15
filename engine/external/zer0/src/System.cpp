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
#include <rgss/Graphics.h>
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

	System::System(chstr path) : Time(0.0f), Exiting(false), Focused(true)
	{
		this->Path = path;
	}
	
	System::~System()
	{
	}
	
	/****************************************************************************************
	 * Events
	 ****************************************************************************************/

	bool System::onQuit(bool canCancel)
	{
		zer0::system->Exiting = true;
		rgss::Graphics::setRunning(false);
		return true;
	}
	
	void System::onFocusChange(bool focused)
	{
		zer0::system->Focused = focused;
	}

}
