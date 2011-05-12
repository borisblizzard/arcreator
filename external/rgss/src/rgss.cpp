#include "Audio.h"
#include "Bitmap.h"
#include "Color.h"
#include "Font.h"
#include "Graphics.h"
#include "Input.h"
#include "Plane.h"
#include "Rect.h"
#include "RGSSError.h"
#include "Sprite.h"
#include "Table.h"
#include "Tilemap.h"
#include "Tone.h"
#include "Viewport.h"
#include "Window.h"

#include "rgss.h"

namespace rgss
{
	void (*g_logFunction)(chstr);
	
	void setLogFunction(void (*function)(chstr))
	{
		g_logFunction = function;
	}
	
	void log(chstr message, chstr prefix)
	{
		g_logFunction(prefix + message);
	}

	void init(void (*logFunction)(chstr))
	{
		g_logFunction = logFunction;
		// creating Ruby interfaces of C++ classes created for Ruby
		Audio::createRubyInterface();
		Bitmap::createRubyInterface();
		Color::createRubyInterface();
		Font::createRubyInterface();
		Graphics::createRubyInterface();
		Input::createRubyInterface();
		Plane::createRubyInterface();
		Rect::createRubyInterface();
		RGSSError::createRubyInterface();
		Sprite::createRubyInterface();
		Table::createRubyInterface();
		Tilemap::createRubyInterface();
		Tone::createRubyInterface();
		Viewport::createRubyInterface();
		Window::createRubyInterface();
		// initialization of RGSS classes
		Audio::init();
		Bitmap::init();
		Color::init();
		Font::init();
		Graphics::init();
		Input::init();
		Plane::init();
		Rect::init();
		RGSSError::init();
		Sprite::init();
		Table::init();
		Tilemap::init();
		Tone::init();
		Viewport::init();
		Window::init();
#ifdef _DEBUG
		rgss::log("initializing Zer0 RGSS");
#endif
	}

	void destroy()
	{
#ifdef _DEBUG
		rgss::log("destroying Zer0 RGSS");
#endif
	}

}