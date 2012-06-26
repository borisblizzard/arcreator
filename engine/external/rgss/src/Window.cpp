#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/hltypesUtil.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Graphics.h"
#include "Rect.h"
#include "RenderQueue.h"
#include "Sprite.h"
#include "Viewport.h"
#include "Window.h"
#include "RGSSError.h"

namespace rgss
{
	VALUE rb_cWindow;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	Window::Window() : SourceRenderer()
	{
		this->typeName = "window";
		this->active = true;
		this->pause = false;
		this->stretch = true;
		this->backOpacity = 255;
		this->contentsOpacity = 255;
		this->pauseUpdateCount = 0;
		this->cursorUpdateCount = 0;
		this->windowskinBackground = NULL;
		this->windowskinHorizontalBorders = NULL;
		this->windowskinVerticalBorders = NULL;
		this->windowskinCorners = NULL;
		this->windowskinCursor = NULL;
		this->rb_cursorRect = Qnil;
		this->cursorRect = NULL;
		this->rb_windowskin = Qnil;
		this->windowskin = NULL;
		this->cursorSprite = NULL;
		this->contentsSprite = NULL;
		for_iter (i, 0, MAX_BORDERS)
		{
			this->borderSprites[i] = NULL;
		}
		this->pauseSprite = NULL;
		this->cursorBitmap = NULL;
	}
	
	Window::~Window()
	{
		this->dispose();
		if (this->cursorSprite != NULL)
		{
			delete this->cursorSprite;
		}
		if (this->contentsSprite != NULL)
		{
			delete this->contentsSprite;
		}
		for_iter (i, 0, MAX_BORDERS)
		{
			if (this->borderSprites[i] != NULL)
			{
				delete this->borderSprites[i];
			}
		}
		if (this->pauseSprite != NULL)
		{
			delete this->pauseSprite;
		}
	}

	void Window::initialize(VALUE rb_viewport)
	{
		SourceRenderer::initialize(rb_viewport);
		this->active = true;
		this->pause = false;
		this->stretch = true;
		this->backOpacity = 255;
		this->contentsOpacity = 255;
		this->pauseUpdateCount = 0;
		this->cursorUpdateCount = 0;
		this->windowskinBackground = NULL;
		this->windowskinHorizontalBorders = NULL;
		this->windowskinVerticalBorders = NULL;
		this->windowskinCorners = NULL;
		this->windowskinCursor = NULL;
		this->rb_cursorRect = Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX(0), INT2FIX(0));
		RB_VAR2CPP(this->rb_cursorRect, Rect, cursorRect);
		this->cursorRect = cursorRect;
		this->rb_windowskin = Qnil;
		this->windowskin = NULL;
		// order of sprite creation is important, don't change it!
		this->cursorSprite = new Sprite(this->viewport);
		this->cursorSprite->setZ(this->z + 2);
		this->contentsSprite = new Sprite(this->viewport);
		this->contentsSprite->setZ(this->z + 2);
		for_iter (i, 0, MAX_BORDERS)
		{
			this->borderSprites[i] = new Sprite(this->viewport);
			this->borderSprites[i]->setZ(this->z + 2);
		}
		this->pauseSprite = new Sprite(this->viewport);
		this->pauseSprite->setZ(this->z + 2);
		this->cursorBitmap = NULL;
	}

	void Window::dispose()
	{
		if (!this->disposed)
		{
			CPP_VAR_DELETE(cursorRect);
			this->rb_cursorRect = Qnil;
			this->cursorRect = NULL;
			this->rb_windowskin = Qnil;
			this->windowskin = NULL;
			if (this->cursorSprite != NULL)
			{
				this->cursorSprite->dispose();
			}
			if (this->contentsSprite != NULL)
			{
				this->contentsSprite->dispose();
			}
			for_iter (i, 0, MAX_BORDERS)
			{
				if (this->borderSprites[i] != NULL)
				{
					this->borderSprites[i]->dispose();
				}
			}
			if (this->pauseSprite != NULL)
			{
				this->pauseSprite->dispose();
			}
			if (this->cursorBitmap != NULL)
			{
				delete this->cursorBitmap;
				this->cursorBitmap = NULL;
			}
			if (this->windowskinBackground != NULL)
			{
				delete this->windowskinBackground;
				this->windowskinBackground = NULL;
				delete this->windowskinHorizontalBorders;
				this->windowskinHorizontalBorders = NULL;
				delete this->windowskinVerticalBorders;
				this->windowskinVerticalBorders = NULL;
				delete this->windowskinCorners;
				this->windowskinCorners = NULL;
				delete this->windowskinCursor;
				this->windowskinCursor = NULL;
			}
		}
		SourceRenderer::dispose();
	}

	void Window::mark()
	{
		SourceRenderer::mark();
		RB_GC_MARK(cursorRect);
		RB_GC_MARK(windowskin);
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Window::draw()
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
		this->_render();
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	bool Window::_canDraw()
	{
		return Renderable::_canDraw();
	}

	void Window::_render()
	{
		if (this->windowskin != NULL && this->opacity > 0)
		{
			this->_renderWindowskinBackground();
			this->_renderWindowskinBorders();
			this->_renderWindowskinCorners();
		}
		this->_updateContentsSprite();
		this->_updateCursorSprite();
		this->_updatePauseSprite();
		this->_updateBorderSprites();
	}

	void Window::_renderWindowskinBackground()
	{
		if (this->backOpacity == 0)
		{
			return;
		}
		april::Texture* texture = this->windowskinBackground->getTexture();
		april::Texture::Filter filter = texture->getFilter();
		texture->setFilter(april::Texture::FILTER_LINEAR);
		april::rendersys->setTexture(texture);
		grect drawRect(2.0f, 2.0f, this->width - 4.0f, this->height - 4.0f);
		grect srcRect(0.0f, 0.0f, 1.0f, 1.0f);
		if (!this->stretch)
		{
			srcRect.w = drawRect.w / 127.0f;
			srcRect.h = drawRect.h / 127.0f;
		}
		if (this->opacity == 255 && this->backOpacity == 255)
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect);
		}
		else
		{
			april::Color color(APRIL_COLOR_WHITE, (unsigned char)(this->opacity * this->backOpacity / 255));
			april::rendersys->drawTexturedRect(drawRect, srcRect, color);
		}
		texture->setFilter(filter);
	}

	void Window::_renderWindowskinBorders()
	{
		grect drawRect;
		grect srcRect;
		float w = this->width - 16.0f;
		float h = this->height - 16.0f;
		april::Color color(APRIL_COLOR_WHITE, (unsigned char)this->opacity);
		// horizontal borders
		april::rendersys->setTexture(this->windowskinHorizontalBorders->getTexture());
		// top border
		drawRect.set(8.0f, 0.0f, w, 16.0f);
		srcRect.set(0.0f, 0.0f, w / 32, 0.5f);
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect, color);
		}
		// bottom border
		drawRect.y = h;
		srcRect.y = 0.5f;
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect, color);
		}
		// vertical borders
		april::rendersys->setTexture(this->windowskinVerticalBorders->getTexture());
		// left border
		drawRect.set(0.0f, 8.0f, 16.0f, h);
		srcRect.set(0.0f, 0.0f, 0.5f, h / 32);
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect, color);
		}
		// right border
		drawRect.x = w;
		srcRect.x = 0.5f;
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect, color);
		}
	}

	void Window::_renderWindowskinCorners()
	{
		grect drawRect;
		grect srcRect;
		float w = this->width - 16.0f;
		float h = this->height - 16.0f;
		april::Color color(APRIL_COLOR_WHITE, (unsigned char)this->opacity);
		april::rendersys->setTexture(this->windowskinCorners->getTexture());
		// top left corner
		drawRect.set(0.0f, 0.0f, 16.0f, 16.0f);
		srcRect.set(0.0f, 0.0f, 0.5f, 0.5f);
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect, color);
		}
		// top right corner
		drawRect.x = w;
		srcRect.x = 0.5f;
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect, color);
		}
		// top right corner
		drawRect.set(0.0f, h, 16.0f, 16.0f);
		srcRect.set(0.0f, 0.5f, 0.5f, 0.5f);
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect, color);
		}
		// top right corner
		drawRect.x = w;
		srcRect.x = 0.5f;
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(drawRect, srcRect, color);
		}
	}

	void Window::_updateWindowskin()
	{
		if (this->windowskinBackground != NULL)
		{
			delete this->windowskinBackground;
			this->windowskinBackground = NULL;
			delete this->windowskinHorizontalBorders;
			this->windowskinHorizontalBorders = NULL;
			delete this->windowskinVerticalBorders;
			this->windowskinVerticalBorders = NULL;
			delete this->windowskinCorners;
			this->windowskinCorners = NULL;
			delete this->windowskinCursor;
			this->windowskinCursor = NULL;
		}
		if (this->windowskin == NULL)
		{
			return;
		}
		// windowskin background
		this->windowskinBackground = new Bitmap(127, 127);
		this->windowskinBackground->bltOver(0, 0, this->windowskin, 0, 0, 127, 127);
		// windowskin horizontal borders
		this->windowskinHorizontalBorders = new Bitmap(32, 32);
		this->windowskinHorizontalBorders->bltOver(0, 0, this->windowskin, 144, 0, 32, 16);
		this->windowskinHorizontalBorders->bltOver(0, 16, this->windowskin, 144, 48, 32, 16);
		// windowskin vertical borders
		this->windowskinVerticalBorders = new Bitmap(32, 32);
		this->windowskinVerticalBorders->bltOver(0, 0, this->windowskin, 128, 16, 16, 32);
		this->windowskinVerticalBorders->bltOver(16, 0, this->windowskin, 176, 16, 16, 32);
		// corners
		this->windowskinCorners = new Bitmap(32, 32);
		this->windowskinCorners->bltOver(0, 0, this->windowskin, 128, 0, 16, 16);
		this->windowskinCorners->bltOver(16, 0, this->windowskin, 176, 0, 16, 16);
		this->windowskinCorners->bltOver(0, 16, this->windowskin, 128, 48, 16, 16);
		this->windowskinCorners->bltOver(16, 16, this->windowskin, 176, 48, 16, 16);
		// cursor
		this->windowskinCursor = new Bitmap(32, 32);
		this->windowskinCursor->bltOver(0, 0, this->windowskin, 128, 64, 32, 32);
	}

	void Window::_updateContentsSprite()
	{
		this->contentsSprite->setX(this->x + 16);
		this->contentsSprite->setY(this->y + 16);
		this->contentsSprite->setOpacity(this->contentsOpacity);
		Rect* rect = this->contentsSprite->getSrcRect();
		rect->set(-this->ox, -this->oy, this->width - 32, this->height - 32);
	}

	void Window::_updateCursorSprite()
	{
		//Rect* srcRect = this->cursorSprite->getSrcRect();
		// remove bitmap if no windowskin or cursorRect has an incorrect size
		if (this->windowskin == NULL || this->cursorRect->width <= 0 || this->cursorRect->height <= 0)
		{
			if (this->cursorBitmap != NULL)
			{
				delete this->cursorBitmap;
				this->cursorBitmap = NULL;
				this->cursorSprite->setBitmap(NULL);
			}
			this->cursorSprite->getSrcRect()->set(0, 0, 0, 0);
			return;
		}
		// set sprite to correct position and dimensions
		this->cursorSprite->setX(this->x + 16 + this->cursorRect->x);
		this->cursorSprite->setY(this->y + 16 + this->cursorRect->y);
		int count = (this->cursorUpdateCount < 16 ? this->cursorUpdateCount : 32 - this->cursorUpdateCount);
		this->cursorSprite->setOpacity(this->contentsOpacity * (32 - count) / 32);
		this->cursorSprite->getSrcRect()->set(0, 0, this->cursorRect->width, this->cursorRect->height);
		// stop if bitmap exists and dimensions have not changed
		if (this->cursorBitmap != NULL && this->cursorBitmap->getWidth() == this->cursorRect->width &&
			this->cursorBitmap->getHeight() == this->cursorRect->height)
		{
			return;
		}
		// dispose old bitmap for better memory management
		if (this->cursorBitmap != NULL)
		{
			delete this->cursorBitmap;
			this->cursorBitmap = NULL;
		}
		// create new bitmap
		this->cursorBitmap = new Bitmap(this->cursorRect->width, this->cursorRect->height);
		this->cursorSprite->setBitmap(this->cursorBitmap);
		// blit cursor image onto new bitmap
		int w = hmax(this->cursorRect->width - 4, 0);
		int h = hmax(this->cursorRect->height - 4, 0);
		this->cursorBitmap->bltOver(0, 0, this->windowskinCursor, 0, 0, 2, 2);
		this->cursorBitmap->bltOver(w + 2, 0, this->windowskinCursor, 30, 0, 2, 2);
		this->cursorBitmap->bltOver(0, h + 2, this->windowskinCursor, 0, 30, 2, 2);
		this->cursorBitmap->bltOver(w + 2, h + 2, this->windowskinCursor, 30, 30, 2, 2);
		if (w > 0)
		{
			this->cursorBitmap->stretchBltOver(2, 0, w, 2, this->windowskinCursor, 2, 0, 28, 2);
			this->cursorBitmap->stretchBltOver(2, h + 2, w, 2, this->windowskinCursor, 2, 30, 28, 2);
		}
		if (h > 0)
		{
			this->cursorBitmap->stretchBltOver(0, 2, 2, h, this->windowskinCursor, 0, 2, 2, 28);
			this->cursorBitmap->stretchBltOver(w + 2, 2, 2, h, this->windowskinCursor, 30, 2, 2, 28);
		}
		if (w > 0 && h > 0)
		{
			this->cursorBitmap->stretchBltOver(2, 2, w, h, this->windowskinCursor, 2, 2, 28, 28);
		}
	}

	void Window::_updatePauseSprite()
	{
		this->pauseSprite->setBitmap(this->windowskin);
		this->pauseSprite->setX(this->x + this->width / 2 - 8);
		this->pauseSprite->setY(this->y + this->height - 16);
		int index = this->pauseUpdateCount % 32 / 8;
		this->pauseSprite->getSrcRect()->set(160 + index % 2 * 16, 64 + index / 2 * 16, 16, 16);
		this->pauseSprite->setOpacity(hmax(this->pauseUpdateCount * 64 - 1, 0));
	}

	void Window::_updateBorderSprites()
	{
		for_iter (i, 0, MAX_BORDERS)
		{
			this->borderSprites[i]->setBitmap(this->windowskin);
		}
		Bitmap* bitmap = this->contentsSprite->getBitmap();
		if (bitmap == NULL)
		{
			for_iter (i, 0, MAX_BORDERS)
			{
				this->borderSprites[i]->setOpacity(0);
			}
			return;
		}
		if (this->oy < 0)
		{
			this->borderSprites[0]->setOpacity(255);
			this->borderSprites[0]->setX(this->x + this->width / 2 - 8);
			this->borderSprites[0]->setY(this->y + 4);
			this->borderSprites[0]->getSrcRect()->set(152, 16, 16, 8);
		}
		else
		{
			this->borderSprites[0]->setOpacity(0);
		}
		if (bitmap->getHeight() + this->oy > this->height - 32)
		{
			this->borderSprites[1]->setOpacity(255);
			this->borderSprites[1]->setX(this->x + this->width / 2 - 8);
			this->borderSprites[1]->setY(this->y + this->height - 12);
			this->borderSprites[1]->getSrcRect()->set(152, 40, 16, 8);
		}
		else
		{
			this->borderSprites[1]->setOpacity(0);
		}
		if (this->ox < 0)
		{
			this->borderSprites[2]->setOpacity(255);
			this->borderSprites[2]->setX(this->x + 4);
			this->borderSprites[2]->setY(this->y + this->height / 2 - 8);
			this->borderSprites[2]->getSrcRect()->set(144, 24, 8, 16);
		}
		else
		{
			this->borderSprites[2]->setOpacity(0);
		}
		if (bitmap->getWidth() + this->ox > this->width - 32)
		{
			this->borderSprites[3]->setOpacity(255);
			this->borderSprites[3]->setX(this->x + this->width - 12);
			this->borderSprites[3]->setY(this->y + this->height / 2 - 8);
			this->borderSprites[3]->getSrcRect()->set(168, 24, 8, 16);
		}
		else
		{
			this->borderSprites[3]->setOpacity(0);
		}
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Window::init()
	{
	}

	void Window::destroy()
	{
	}

	void Window::createRubyInterface()
	{
		rb_cWindow = rb_define_class("Window", rb_cObject);
		rb_define_alloc_func(rb_cWindow, &Window::rb_new);
		// initialize
		rb_define_method(rb_cWindow, "initialize", RUBY_METHOD_FUNC(&Window::rb_initialize), -1);
		rb_define_method(rb_cWindow, "initialize_clone", RUBY_METHOD_FUNC(&Window::rb_initialize_clone), 1);
		rb_define_method(rb_cWindow, "initialize_dup", RUBY_METHOD_FUNC(&Window::rb_initialize_dup), 1);
		rb_define_method(rb_cWindow, "dispose", RUBY_METHOD_FUNC(&Window::rb_dispose), 0);
		rb_define_method(rb_cWindow, "_arc_dump", RUBY_METHOD_FUNC(&Window::rb_arcDump), 0);
		// getters and setters (Renderable)
		rb_define_method(rb_cWindow, "disposed?", RUBY_METHOD_FUNC(&Window::rb_isDisposed), 0);
		rb_define_method(rb_cWindow, "visible", RUBY_METHOD_FUNC(&Window::rb_getVisible), 0);
		rb_define_method(rb_cWindow, "visible=", RUBY_METHOD_FUNC(&Window::rb_setVisible), 1);
		rb_define_method(rb_cWindow, "z", RUBY_METHOD_FUNC(&Window::rb_getZ), 0);
		rb_define_method(rb_cWindow, "z=", RUBY_METHOD_FUNC(&Window::rb_setZ), 1);
		rb_define_method(rb_cWindow, "ox", RUBY_METHOD_FUNC(&Window::rb_getOX), 0);
		rb_define_method(rb_cWindow, "ox=", RUBY_METHOD_FUNC(&Window::rb_setOX), 1);
		rb_define_method(rb_cWindow, "oy", RUBY_METHOD_FUNC(&Window::rb_getOY), 0);
		rb_define_method(rb_cWindow, "oy=", RUBY_METHOD_FUNC(&Window::rb_setOY), 1);
		// getters and setters (SourceRenderer)
		rb_define_method(rb_cWindow, "viewport", RUBY_METHOD_FUNC(&Window::rb_getViewport), 0);
		rb_define_method(rb_cWindow, "opacity", RUBY_METHOD_FUNC(&Window::rb_getOpacity), 0);
		rb_define_method(rb_cWindow, "opacity=", RUBY_METHOD_FUNC(&Window::rb_setOpacity), 1);
		rb_define_method(rb_cWindow, "contents", RUBY_METHOD_FUNC(&Window::rb_getBitmap), 0);
		rb_define_method(rb_cWindow, "contents=", RUBY_METHOD_FUNC(&Window::rb_setBitmap), 1);
		// getters and setters
		rb_define_method(rb_cWindow, "x", RUBY_METHOD_FUNC(&Window::rb_getX), 0);
		rb_define_method(rb_cWindow, "x=", RUBY_METHOD_FUNC(&Window::rb_setX), 1);
		rb_define_method(rb_cWindow, "y", RUBY_METHOD_FUNC(&Window::rb_getY), 0);
		rb_define_method(rb_cWindow, "y=", RUBY_METHOD_FUNC(&Window::rb_setY), 1);
		rb_define_method(rb_cWindow, "width", RUBY_METHOD_FUNC(&Window::rb_getWidth), 0);
		rb_define_method(rb_cWindow, "width=", RUBY_METHOD_FUNC(&Window::rb_setWidth), 1);
		rb_define_method(rb_cWindow, "height", RUBY_METHOD_FUNC(&Window::rb_getHeight), 0);
		rb_define_method(rb_cWindow, "height=", RUBY_METHOD_FUNC(&Window::rb_setHeight), 1);
		rb_define_method(rb_cWindow, "active", RUBY_METHOD_FUNC(&Window::rb_getActive), 0);
		rb_define_method(rb_cWindow, "active=", RUBY_METHOD_FUNC(&Window::rb_setActive), 1);
		rb_define_method(rb_cWindow, "pause", RUBY_METHOD_FUNC(&Window::rb_getPause), 0);
		rb_define_method(rb_cWindow, "pause=", RUBY_METHOD_FUNC(&Window::rb_setPause), 1);
		rb_define_method(rb_cWindow, "stretch", RUBY_METHOD_FUNC(&Window::rb_getStretch), 0);
		rb_define_method(rb_cWindow, "stretch=", RUBY_METHOD_FUNC(&Window::rb_setStretch), 1);
		rb_define_method(rb_cWindow, "back_opacity", RUBY_METHOD_FUNC(&Window::rb_getBackOpacity), 0);
		rb_define_method(rb_cWindow, "back_opacity=", RUBY_METHOD_FUNC(&Window::rb_setBackOpacity), 1);
		rb_define_method(rb_cWindow, "contents_opacity", RUBY_METHOD_FUNC(&Window::rb_getContentsOpacity), 0);
		rb_define_method(rb_cWindow, "contents_opacity=", RUBY_METHOD_FUNC(&Window::rb_setContentsOpacity), 1);
		rb_define_method(rb_cWindow, "cursor_rect", RUBY_METHOD_FUNC(&Window::rb_getCursorRect), 0);
		rb_define_method(rb_cWindow, "cursor_rect=", RUBY_METHOD_FUNC(&Window::rb_setCursorRect), 1);
		rb_define_method(rb_cWindow, "windowskin", RUBY_METHOD_FUNC(&Window::rb_getWindowskin), 0);
		rb_define_method(rb_cWindow, "windowskin=", RUBY_METHOD_FUNC(&Window::rb_setWindowskin), 1);
		// methods
		rb_define_method(rb_cWindow, "update", RUBY_METHOD_FUNC(&Window::rb_update), 0);
	}
	
	VALUE Window::rb_new(VALUE classe)
	{
		Window* window;
		return RB_OBJECT_NEW(classe, Window, window, &Window::gc_mark, &Window::gc_free);
	}

	VALUE Window::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Window, window);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		window->initialize(viewport);
		return self;
	}

	VALUE Window::rb_initialize_clone(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Window, window);
		RB_CANT_CLONE_ERROR(window);
		return self;
	}

	VALUE Window::rb_initialize_dup(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Window, window);
		RB_CANT_DUP_ERROR(window);
		return self;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Window::rb_setVisible(VALUE self, VALUE value)
	{
		SourceRenderer::rb_setVisible(self, value);
		RB_SELF2CPP(Window, window);
		bool visible = (bool)RTEST(value);
		window->contentsSprite->setVisible(visible);
		window->cursorSprite->setVisible(visible);
		window->pauseSprite->setVisible(visible);
		for_iter (i, 0, MAX_BORDERS)
		{
			window->borderSprites[i]->setVisible(visible);
		}
		return value;
	}

	VALUE Window::rb_setBitmap(VALUE self, VALUE value)
	{
		SourceRenderer::rb_setBitmap(self, value);
		RB_SELF2CPP(Window, window);
		if (!NIL_P(value))
		{
			RB_VAR2CPP(value, Bitmap, bitmap);
			window->contentsSprite->setBitmap(bitmap);
			window->contentsSprite->getSrcRect()->set(0, 0, bitmap->getWidth(), bitmap->getHeight());
		}
		else
		{
			window->contentsSprite->setBitmap(NULL);
		}
		return value;
	}

	VALUE Window::rb_setZ(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		SourceRenderer::rb_setZ(self, value);
		window->cursorSprite->setZ(window->z + 2);
		window->contentsSprite->setZ(window->z + 2);
		window->pauseSprite->setZ(window->z + 2);
		for_iter (i, 0, MAX_BORDERS)
		{
			window->borderSprites[i]->setZ(window->z + 2);
		}
		return value;
	}

	VALUE Window::rb_getWidth(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		return INT2NUM(window->width);
	}

	VALUE Window::rb_setWidth(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		window->width = NUM2INT(value);
		return value;
	}

	VALUE Window::rb_getHeight(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		return INT2NUM(window->height);
	}

	VALUE Window::rb_setHeight(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		window->height = NUM2INT(value);
		return value;
	}

	VALUE Window::rb_getActive(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		return (window->active ? Qtrue : Qfalse);
	}

	VALUE Window::rb_setActive(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		window->active = (bool)RTEST(value);
		return value;
	}

	VALUE Window::rb_getPause(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		return (window->pause ? Qtrue : Qfalse);
	}

	VALUE Window::rb_setPause(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		bool pause = (bool)RTEST(value);
		if (window->pause != pause)
		{
			window->pause = pause;
			window->pauseUpdateCount = (pause ? hmax(window->pauseUpdateCount, 0) : hmin(window->pauseUpdateCount, 4));
		}
		return value;
	}

	VALUE Window::rb_getStretch(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		return (window->stretch ? Qtrue : Qfalse);
	}

	VALUE Window::rb_setStretch(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		window->stretch = (bool)RTEST(value);
		return value;
	}

	VALUE Window::rb_getBackOpacity(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		return INT2NUM(window->backOpacity);
	}

	VALUE Window::rb_setBackOpacity(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		window->backOpacity = hclamp(NUM2INT(value), 0, 255);
		return value;
	}

	VALUE Window::rb_getContentsOpacity(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		return INT2NUM(window->contentsOpacity);
	}

	VALUE Window::rb_setContentsOpacity(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		window->contentsOpacity = hclamp(NUM2INT(value), 0, 255);
		return value;
	}

	VALUE Window::rb_getCursorRect(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		return window->rb_cursorRect;
	}

	VALUE Window::rb_setCursorRect(VALUE self, VALUE value)
	{
		{
			RB_SELF2CPP(Window, window);
			RB_CHECK_DISPOSED(window);
		}
		RB_GENERATE_SETTER(Window, window, Rect, cursorRect);
		return value;
	}

	VALUE Window::rb_getWindowskin(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		return window->rb_windowskin;
	}

	VALUE Window::rb_setWindowskin(VALUE self, VALUE value)
	{
		{
			RB_SELF2CPP(Window, window);
			RB_CHECK_DISPOSED(window);
		}
		VALUE rb_oldWindowskin = Window::rb_getWindowskin(self);
		RB_GENERATE_SETTER(Window, window, Bitmap, windowskin);
		if (rb_oldWindowskin != value)
		{
			window->_updateWindowskin();
			window->_updateCursorSprite();
			window->_updatePauseSprite();
			window->_updateBorderSprites();
		}
		return value;
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Window::rb_update(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		RB_CHECK_DISPOSED(window);
		window->pause ? window->pauseUpdateCount++ : window->pauseUpdateCount--;
		if (window->active)
		{
			window->cursorUpdateCount = (window->cursorUpdateCount + 1) % 32;
		}
		return Qnil;
	}

}
