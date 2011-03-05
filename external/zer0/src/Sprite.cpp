#include <aprilui/ObjectImageBox.h>
#include <gtypes/Rectangle.h>

#include "Sprite.h"

namespace zer0
{
	
	Sprite::Sprite() : aprilui::ImageBox("", grect(0, 0, 1, 1))
	{
	}
	
	Sprite::~Sprite()
	{
	}
	
}
