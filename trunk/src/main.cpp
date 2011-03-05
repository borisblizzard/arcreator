#include <math.h>
#include <stdlib.h>
#include <time.h>
#ifdef _WIN32
#include <windows.h>
#endif

#include <april/RenderSystem.h>
#include <april/Window.h>
#include <april/main.h>
#include <aprilui/aprilui.h>
#include <aprilui/Exception.h>
#include <atres/Font.h>
#include <gtypes/Rectangle.h>
#include <gtypes/Vector2.h>
#include <hltypes/exception.h>
#include <hltypes/util.h>
#include <xal/AudioManager.h>

#include "System/Constants.h"
#include "System/Context.h"
#include "System/Main.h"
#include "System/Utility.h"

bool result;
grect drawRect;

bool update(float time)
{
	result = true;
#ifdef _DEBUG
	try
	{
#endif
		april::rendersys->clear(true, false);
		april::rendersys->setOrthoProjection(drawRect);
		result = System::main->update(time);
#ifdef _DESKTOP
		aprilui::drawCursor();
#endif
#ifdef _DEBUG
	}
	catch (hltypes::exception e)
	{
		System::log(e.message());
		result = false;
	}
	catch (hstr e)
	{
		System::log(e);
		result = false;
	}
#endif
	if (!result)
	{
		april::rendersys->getWindow()->terminateMainLoop();
	}
	return result;
}

#if !defined(_CONSOLE) && defined(_WIN32)
int CALLBACK WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
#else
int main(int argc, char** argv)
#endif
{
	srand(System::getTime());
	int width = 800;
	int height = 600;
	try
	{
		System::create();
		april::setLogFunction(&System::log);
		atres::setLogFunction(&System::log);
		aprilui::setLogFunction(&System::log);
		xal::setLogFunction(&System::log);
		april::init("mb_renderer", width, height, false, "Advanced RPG Creator");
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
		april::rendersys->getWindow()->setUpdateCallback(update);
		april::rendersys->getWindow()->setMouseCallbacks(&System::Main::onMouseDown, &System::Main::onMouseUp,
			&System::Main::onMouseMove);
		april::rendersys->getWindow()->setKeyboardCallbacks(&System::Main::onKeyDown, &System::Main::onKeyUp,
			&System::Main::onChar);
		april::rendersys->getWindow()->setQuitCallback(&System::Main::onQuit);
		april::rendersys->getWindow()->setWindowFocusCallback(&System::Main::onFocusChange);
#ifdef _DESKTOP
		april::rendersys->getWindow()->showSystemCursor(false);
#endif
		atres::setGlobalOffsets(true);
		aprilui::setLimitCursorToViewport(false);
		aprilui::setViewport(grect(0.0f, 0.0f, (float)width, (float)height));
		aprilui::setScreenViewport(aprilui::getViewport());
		april::rendersys->getWindow()->enterMainLoop();
		System::clear();
		xal::destroy();
		aprilui::destroy();
		atres::destroy();
		april::destroy();
		System::destroy();
	}
	catch (hltypes::exception e)
	{
		System::log(e.message());
	}
	catch (hstr e)
	{
		System::log(e);
	}
	return 0;
}
