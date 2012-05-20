#include <april/PixelShader.h>

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
	hmap<hstr, hstr> parameters;
	bool debugMode;
	april::PixelShader* pixelShader;
	
	void rgss_writelog(chstr message)
	{
	}

	void (*g_logFunction)(chstr) = rgss_writelog;
	
	void setLogFunction(void (*function)(chstr))
	{
		g_logFunction = function;
	}
	
	void log(chstr message, chstr prefix)
	{
		g_logFunction(prefix + message);
	}

	bool isDebugMode()
	{
		return debugMode;
	}
	
	void setDebugMode(bool value)
	{
		debugMode = value;
	}

	void init(hmap<hstr, hstr> parameters)
	{
		rgss::parameters = parameters;
		rgss::log("initializing Zer0 RGSS");
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
		// initialization of Ruby classes
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
	}

	void destroy()
	{
		rgss::log("destroying Zer0 RGSS");
		Audio::destroy();
		Bitmap::destroy();
		Color::destroy();
		Font::destroy();
		Graphics::destroy();
		Input::destroy();
		Plane::destroy();
		Rect::destroy();
		RGSSError::destroy();
		Sprite::destroy();
		Table::destroy();
		Tilemap::destroy();
		Tone::destroy();
		Viewport::destroy();
		Window::destroy();
	}

	void setPixelShader(april::PixelShader* value)
	{
		rgss::pixelShader = value;
	}

}