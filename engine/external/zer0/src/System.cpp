#include <stdio.h>

#include <april/Keys.h>
#include <april/RenderSystem.h>
#ifndef LEGACY_ONLY
#include <aprilui/Animator.h>
#include <aprilui/aprilui.h>
#include <aprilui/Dataset.h>
#include <aprilui/Objects.h>
#endif
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

#define SYSTEM_PATH_BASE "ARC"

namespace zer0
{
	System* system = NULL;
	/****************************************************************************************
	 * Construct/Destruct
	 ****************************************************************************************/

	System::System() : Time(0.0f), Exiting(false), Focused(true)
	{
		this->Parameters = this->_readCfgFile("arc.cfg");
		this->Title = this->Parameters[CFG_TITLE];
		this->Path = this->_setupSystemPath(this->Title);
	}
	
	System::~System()
	{
	}
	
	// TODO Add Linux and Mac variants.
	hstr System::_setupSystemPath(chstr title)
	{
		hstr path;
#ifdef _DEBUG
		path = "log";
#elif defined(_WIN32)
		path = getenv("ALLUSERSPROFILE");
		path = path.replace("\\", "/");
		if (getenv("LOCALAPPDATA") == NULL) // Vista / 7
		{
			path += "/" + hstr(getenv("APPDATA")).split("\\").pop_back();
		}
		const wchar_t* name = _wgetenv(L"USERNAME");
		hstr username;
		for (int i = 0; name[i] != 0; i++)
		{
			username += (char)(name[i] > 0x80 ? 0x40 + (name[i] % 26) : name[i]);
		}
		path += hsprintf("/%s/%s/%s", SYSTEM_PATH_BASE, title.c_str(), username.c_str());
#elif defined(__APPLE__)
		{	// curly braces in order to localize variables
#if !TARGET_OS_IPHONE
			// mac
			NSSearchPathDirectory destDir = NSApplicationSupportDirectory;
#else
			// iphone
			NSSearchPathDirectory destDir = NSApplicationSupportDirectory; // game already released so we cant just move to NSDocumentDirectory
#endif
            NSAutoreleasePool *arp = [[NSAutoreleasePool alloc] init]; 

			CFArrayRef destDirArr = (CFArrayRef)NSSearchPathForDirectoriesInDomains(destDir, NSUserDomainMask, YES);
			CFStringRef destDirPath = (CFStringRef)CFArrayGetValueAtIndex(destDirArr, 0);
			const char* cpath = NULL; // we will always use getmaximumsizeoffilesystemrepresentation //CFStringGetCStringPtr(destDirPath, kCFStringEncodingUTF8);
			char* cpath_alloc = 0;
			if (!cpath)
			{
				// CFStringGetCStringPtr is allowed to return NULL. bummer.
				// we need to use CFStringGetCString instead.
				int buffersize = CFStringGetMaximumSizeOfFileSystemRepresentation(destDirPath) + 1;
				cpath_alloc = (char*)malloc(buffersize);
				CFStringGetFileSystemRepresentation(destDirPath, cpath_alloc, buffersize);
			}
			else
			{
				// NEVER USED!
				// even though it didn't return NULL, we still want to slice off bundle name.
				cpath_alloc = (char*)malloc(strlen(cpath) + 1);
				strcpy(cpath_alloc, cpath);
			}
			path = cpath_alloc;
			free(cpath_alloc); // even if null, still ok
			[arp release];
			
#ifdef XCODE_CONFIGURATION
			hstr xcode_configuration(XCODE_CONFIGURATION);
#else
			hstr xcode_configuration;
#endif
			if (xcode_configuration != "App Store" || hdir::exists(hsprintf("%s/%s/%s", path.c_str(), SYSTEM_PATH_BASE, title.c_str()))
			{
				path += hsprintf("/%s", SYSTEM_PATH_BASE);
			}
			path += hsprintf("/%s", title.c_str());
		}
#endif
		hdir::create(path);
		path += "/";
		hfile::create_new(path + "log.txt");
		return path;
	}

	hmap<hstr, hstr> System::_readCfgFile(chstr filename)
	{
		hmap<hstr, hstr> result;
		result[CFG_TITLE] = "ARC Game";
		result[CFG_RESOLUTION] = "640x480";
		result[CFG_FULLSCREEN] = "false";
		result[CFG_FRAME_RATE] = "60";
		result[CFG_GAME_VERSION] = "1.0.0";
		if (hfile::exists(filename))
		{
			hfile f(filename);
			harray<hstr> lines = f.read_lines();
			f.close();
			// ignore file header. utf-8 encoded text files have 2-3 char markers
			while (lines[0].size() > 0 && lines[0][0] < 0)
			{
				lines[0] = lines[0](1, lines[0].size() - 1);
			}
			harray<hstr> data;
			foreach (hstr, it, lines)
			{
				data = (*it).split(":", 1);
				if (data.size() == 2)
				{
					result[data[0]] = data[1];
				}
			}
			// fixing some special variables
			if (result[CFG_RESOLUTION].split("x").size() != 2)
			{
				result[CFG_RESOLUTION] = "640x480";
			}
			else
			{
				harray<int> resolution = result[CFG_RESOLUTION].split("x").cast<int>();
				if (resolution[0] <= 0 || resolution[1] <= 0)
				{
					result[CFG_RESOLUTION] = "640x480";
				}
			}
			result[CFG_FULLSCREEN] = ((bool)result[CFG_FULLSCREEN] ? "true" : "false");
		}
		return result;
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
		rgss::Graphics::setFocused(focused);
	}

}
