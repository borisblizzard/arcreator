#include <ruby.h>

#include "Color.h"
#include "Rect.h"
#include "Tone.h"
#include "Viewport.h"
#include "CodeSnippets.h"

namespace rgss
{
	void Viewport::init()
	{
	}

	void Viewport::createRubyInterface()
	{
	}

	void Viewport::setColor(float r, float g, float b, float a)
	{
		//this->color.set(r, g, b, a);
	}
	void Viewport::setTone(float r, float g, float b, float gr)
	{
		this->tone.set(r, g, b, gr);
	}
	void Viewport::setRect(int x, int y, int width, int height)
	{
		this->rect.set(x, y, width, height);
	}
	void Viewport::setOX(int value)
	{
		this->ox = value;
	}
	void Viewport::setOY(int value)
	{
		this->oy = value;
	}
	void Viewport::setZ(int value)
	{
		this->z = value;
	}
	void Viewport::setVisible(bool value)
	{
		this->visible = value;
	}
	void Viewport::flash(Color clr, int duration)
	{
			
	}
	
}
