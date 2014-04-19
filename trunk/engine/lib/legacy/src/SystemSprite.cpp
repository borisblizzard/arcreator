#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/hltypesUtil.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Rect.h"
#include "SystemSprite.h"
#include "Viewport.h"

namespace legacy
{
	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	SystemSprite::SystemSprite(Viewport* viewport) : SourceRenderer(viewport)
	{
		this->typeName = "system sprite";
		this->srcRect = new Rect();
	}
	
	SystemSprite::~SystemSprite()
	{
		this->dispose();
	}

	void SystemSprite::dispose()
	{
		if (!this->disposed)
		{
			delete this->srcRect;
			this->srcRect = NULL;
		}
		SourceRenderer::dispose();
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void SystemSprite::draw()
	{
		if (!this->_canDraw())
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

	bool SystemSprite::_canDraw()
	{
		return (this->srcRect->width > 0 && this->srcRect->height > 0 && SourceRenderer::_canDraw());
	}

	void SystemSprite::_render()
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
		april::rendersys->setTextureBlendMode(april::DEFAULT);
	}

}
