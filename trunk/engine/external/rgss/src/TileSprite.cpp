#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/hltypesUtil.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
/*
#include "Color.h"
#include "Graphics.h"
*/
#include "Rect.h"
#include "TileSprite.h"
/*
#include "Tone.h"
*/
#include "Viewport.h"
/*
#include "RGSSError.h"
*/

namespace rgss
{
	//VALUE rb_cSprite;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	TileSprite::TileSprite(Viewport* viewport) : SourceRenderer(viewport)
	{
		this->disposed = false;
		this->type = TYPE_SPRITE;
		this->typeName = "sprite";
		this->srcRect = new Rect();
	}
	
	TileSprite::~TileSprite()
	{
		delete this->srcRect;
	}

	void TileSprite::draw()
	{
		if (this->bitmap == NULL || this->bitmap->isDisposed() || this->opacity == 0 || this->srcRect->width <= 0 ||
			this->srcRect->height <= 0 || this->zoom.x == 0.0f || this->zoom.y == 0.0f)
		{
			return;
		}
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		gmat4 projectionMatrix = april::rendersys->getProjectionMatrix();
		if (this->x != 0 || this->y != 0) 
		{
			april::rendersys->translate((float)this->x, (float)this->y);
		}
		if (this->zoom.x != 1.0f || this->zoom.y != 1.0f)
		{
			april::rendersys->scale(this->zoom.x, this->zoom.y, 1.0f);
		}
		this->_render();
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void TileSprite::_render()
	{
		int dw = hmin(this->srcRect->width, this->bitmap->getWidth());
		int dh = hmin(this->srcRect->height, this->bitmap->getHeight());
		grect drawRect((float)this->ox, (float)this->oy, (float)dw, (float)dh);
		float sw = (float)this->bitmap->getWidth();
		float sh = (float)this->bitmap->getHeight();
		grect srcRect;
		srcRect.x = this->srcRect->x / sw;
		srcRect.y = this->srcRect->y / sh;
		srcRect.w = hmin(this->srcRect->width / sw, 1.0f - srcRect.x);
		srcRect.h = hmin(this->srcRect->height / sh, 1.0f - srcRect.y);
		this->_renderTexture(drawRect, srcRect, this->bitmap->getTexture(), this->opacity);
		april::rendersys->setBlendMode(april::DEFAULT);
	}

}
