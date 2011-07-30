#include <ruby.h>

#include <april/RenderSystem.h>
#include <gtypes/Matrix4.h>
#include <gtypes/Rectangle.h>
#include <hltypes/util.h>

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
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cWindow;

	void Window::draw()
	{
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
		april::rendersys->setTexture(this->windowskinBackground->getTexture());
		grect drawRect(2.0f, 2.0f, this->width - 4.0f, this->height - 4.0f);
		grect srcRect(0.0f, 0.0f, 1.0f, 1.0f);
		if (!this->stretch)
		{
			srcRect.w = drawRect.w / 127.0f;
			srcRect.h = drawRect.h / 127.0f;
		}
		if (this->opacity == 255 && this->backOpacity == 255)
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::Color color(APRIL_COLOR_WHITE, (unsigned char)(this->opacity * this->backOpacity / 255));
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
		}
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
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
		}
		// bottom border
		drawRect.y = h;
		srcRect.y = 0.5f;
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
		}
		// vertical borders
		april::rendersys->setTexture(this->windowskinVerticalBorders->getTexture());
		// left border
		drawRect.set(0.0f, 8.0f, 16.0f, h);
		srcRect.set(0.0f, 0.0f, 0.5f, h / 32);
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
		}
		// right border
		drawRect.x = w;
		srcRect.x = 0.5f;
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
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
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
		}
		// top right corner
		drawRect.x = w;
		srcRect.x = 0.5f;
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
		}
		// top right corner
		drawRect.set(0.0f, h, 16.0f, 16.0f);
		srcRect.set(0.0f, 0.5f, 0.5f, 0.5f);
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
		}
		// top right corner
		drawRect.x = w;
		srcRect.x = 0.5f;
		if (this->opacity == 255)
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedQuad(drawRect, srcRect, color);
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
		}
		if (this->windowskin == NULL)
		{
			return;
		}
		// windowskin background
		this->windowskinBackground = new Bitmap(127, 127);
		this->windowskinBackground->blt(0, 0, this->windowskin, 0, 0, 127, 127);
		// windowskin horizontal borders
		this->windowskinHorizontalBorders = new Bitmap(32, 32);
		this->windowskinHorizontalBorders->blt(0, 0, this->windowskin, 144, 0, 32, 16);
		this->windowskinHorizontalBorders->blt(0, 16, this->windowskin, 144, 48, 32, 16);
		// windowskin vertical borders
		this->windowskinVerticalBorders = new Bitmap(32, 32);
		this->windowskinVerticalBorders->blt(0, 0, this->windowskin, 128, 16, 16, 32);
		this->windowskinVerticalBorders->blt(16, 0, this->windowskin, 176, 16, 16, 32);
		// corners
		this->windowskinCorners = new Bitmap(32, 32);
		this->windowskinCorners->blt(0, 0, this->windowskin, 128, 0, 16, 16);
		this->windowskinCorners->blt(16, 0, this->windowskin, 176, 0, 16, 16);
		this->windowskinCorners->blt(0, 16, this->windowskin, 128, 48, 16, 16);
		this->windowskinCorners->blt(16, 16, this->windowskin, 176, 48, 16, 16);
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
		Rect* srcRect = this->cursorSprite->getSrcRect();
		Bitmap* cursorBitmap = this->cursorSprite->getBitmap();
		VALUE rb_bitmap = Sprite::rb_getBitmap(this->rb_cursorSprite);
		// remove bitmap if no windowskin or cursorRect has an incorrect size
		if (this->windowskin == NULL || this->cursorRect->width <= 0 || this->cursorRect->height <= 0)
		{
			if (cursorBitmap != NULL)
			{
				Bitmap::rb_dispose(rb_bitmap);
				Sprite::rb_setBitmap(this->rb_cursorSprite, Qnil);
			}
			srcRect->set(0, 0, 0, 0);
			return;
		}
		// set sprite to correct position and dimensions
		this->cursorSprite->setX(this->x + 16 + this->cursorRect->x);
		this->cursorSprite->setY(this->y + 16 + this->cursorRect->y);
		int count = (this->cursorCount < 16 ? this->cursorCount : 32 - this->cursorCount);
		this->cursorSprite->setOpacity(this->contentsOpacity * (32 - count) / 32);
		srcRect->width = this->cursorRect->width;
		srcRect->height = this->cursorRect->height;
		// stop if bitmap exists and dimensions have not changed
		if (cursorBitmap != NULL && cursorBitmap->getWidth() == this->cursorRect->width &&
			cursorBitmap->getHeight() == this->cursorRect->height)
		{
			return;
		}
		// dispose old bitmap for better memory management
		if (cursorBitmap != NULL)
		{
			Bitmap::rb_dispose(rb_bitmap);
		}
		// create new bitmap
		VALUE argv[2] = {INT2FIX(this->cursorRect->width), INT2FIX(this->cursorRect->height)};
		rb_bitmap = Bitmap::create(2, argv);
		Sprite::rb_setBitmap(this->rb_cursorSprite, rb_bitmap);
		// set the srcRect of the cursor Sprite
		srcRect->set(0, 0, this->cursorRect->width, this->cursorRect->height);
		// blit cursor image onto new bitmap
		RB_VAR2CPP(rb_bitmap, Bitmap, bitmap);
		int w = hmax(this->cursorRect->width - 4, 0);
		int h = hmax(this->cursorRect->height - 4, 0);
		bitmap->blt(0, 0, this->windowskin, 128, 64, 2, 2);
		bitmap->blt(w + 2, 0, this->windowskin, 158, 64, 2, 2);
		bitmap->blt(0, h + 2, this->windowskin, 128, 94, 2, 2);
		bitmap->blt(w + 2, h + 2, this->windowskin, 158, 94, 2, 2);
		if (w > 0)
		{
			bitmap->stretchBlt(2, 0, w, 2, this->windowskin, 130, 64, 28, 2);
			bitmap->stretchBlt(2, h + 2, w, 2, this->windowskin, 130, 94, 28, 2);
		}
		if (h > 0)
		{
			bitmap->stretchBlt(0, 2, 2, h, this->windowskin, 128, 66, 2, 28);
			bitmap->stretchBlt(w + 2, 2, 2, h, this->windowskin, 158, 66, 2, 28);
		}
		if (w > 0 && h > 0)
		{
			bitmap->stretchBlt(2, 2, w, h, this->windowskin, 130, 66, 28, 28);
		}
	}

	void Window::_updatePauseSprite()
	{
		SourceRenderer::rb_setBitmap(this->rb_pauseSprite, this->rb_windowskin);
		this->pauseSprite->setX(this->x + this->width / 2 - 8);
		this->pauseSprite->setY(this->y + this->height - 16);
		int index = this->pauseCount % 32 / 8;
		this->pauseSprite->getSrcRect()->set(160 + index % 2 * 16, 64 + index / 2 * 16, 16, 16);
		this->pauseSprite->setOpacity(hmax(this->pauseCount * 64 - 1, 0));
	}

	void Window::_updateBorderSprites()
	{
		for_iter (i, 0, 4)
		{
			SourceRenderer::rb_setBitmap(this->rb_borderSprites[i], this->rb_windowskin);
		}
		Bitmap* bitmap = this->contentsSprite->getBitmap();
		if (bitmap == NULL)
		{
			for_iter (i, 0, 4)
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

	void Window::dispose()
	{
		this->rb_cursorRect = Qnil;
		this->cursorRect = NULL;
		this->rb_windowskin = Qnil;
		this->windowskin = NULL;
		if (!NIL_P(this->rb_contentsSprite))
		{
			this->contentsSprite->setVisible(false);
		}
		this->rb_contentsSprite = Qnil;
		this->contentsSprite = NULL;
		if (!NIL_P(this->rb_cursorSprite))
		{
			this->cursorSprite->setVisible(false);
		}
		this->rb_cursorSprite = Qnil;
		this->cursorSprite = NULL;
		if (!NIL_P(this->rb_pauseSprite))
		{
			this->pauseSprite->setVisible(false);
		}
		this->rb_pauseSprite = Qnil;
		this->pauseSprite = NULL;
		for_iter (i, 0, 4)
		{
			if (!NIL_P(this->rb_borderSprites[i]))
			{
				this->borderSprites[i]->setVisible(false);
			}
			this->rb_borderSprites[i] = Qnil;
			this->borderSprites[i] = NULL;
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
		}
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Window::init()
	{
	}

	void Window::createRubyInterface()
	{
		rb_cWindow = rb_define_class("Window", rb_cObject);
		rb_define_alloc_func(rb_cWindow, &Window::rb_new);
		// initialize
		rb_define_method(rb_cWindow, "initialize", RUBY_METHOD_FUNC(&Window::rb_initialize), -1);
		rb_define_method(rb_cWindow, "dispose", RUBY_METHOD_FUNC(&Window::rb_dispose), 0);
		// getters and setters (Renderable)
		rb_define_method(rb_cWindow, "visible", RUBY_METHOD_FUNC(&Window::rb_getVisible), 0);
		rb_define_method(rb_cWindow, "visible=", RUBY_METHOD_FUNC(&Window::rb_setVisible), 1);
		rb_define_method(rb_cWindow, "z", RUBY_METHOD_FUNC(&Window::rb_getZ), 0);
		rb_define_method(rb_cWindow, "z=", RUBY_METHOD_FUNC(&Window::rb_setZ), 1);
		rb_define_method(rb_cWindow, "ox", RUBY_METHOD_FUNC(&Window::rb_getOX), 0);
		rb_define_method(rb_cWindow, "ox=", RUBY_METHOD_FUNC(&Window::rb_setOX), 1);
		rb_define_method(rb_cWindow, "oy", RUBY_METHOD_FUNC(&Window::rb_getOY), 0);
		rb_define_method(rb_cWindow, "oy=", RUBY_METHOD_FUNC(&Window::rb_setOY), 1);
		rb_define_method(rb_cWindow, "disposed?", RUBY_METHOD_FUNC(&Window::rb_isDisposed), 0);
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
	
	void Window::gc_mark(Window* window)
	{
		if (!NIL_P(window->rb_cursorRect))
		{
			rb_gc_mark(window->rb_cursorRect);
		}
		if (!NIL_P(window->rb_windowskin))
		{
			rb_gc_mark(window->rb_windowskin);
		}
		if (!NIL_P(window->rb_contentsSprite))
		{
			rb_gc_mark(window->rb_contentsSprite);
		}
		if (!NIL_P(window->rb_cursorSprite))
		{
			rb_gc_mark(window->rb_cursorSprite);
		}
		if (!NIL_P(window->rb_pauseSprite))
		{
			rb_gc_mark(window->rb_pauseSprite);
		}
		for_iter (i, 0, 4)
		{
			if (!NIL_P(window->rb_borderSprites[i]))
			{
				rb_gc_mark(window->rb_borderSprites[i]);
			}
		}
		SourceRenderer::gc_mark(window);
	}

	void Window::gc_free(Window* window)
	{
		SourceRenderer::gc_free(window);
	}

	VALUE Window::rb_new(VALUE classe)
	{
		Window* window;
		VALUE result = Data_Make_Struct(classe, Window, Window::gc_mark, Window::gc_free, window);
		window->disposed = true;
		window->type = TYPE_WINDOW;
		return result;
	}

	VALUE Window::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Window, window);
		VALUE viewport;
		rb_scan_args(argc, argv, "01", &viewport);
		window->initializeSourceRenderer(viewport);
		window->active = true;
		window->stretch = true;
		window->backOpacity = 255;
		window->contentsOpacity = 255;
		window->pauseCount = 0;
		window->cursorCount = 0;
		window->windowskinBackground = NULL;
		window->windowskinHorizontalBorders = NULL;
		window->windowskinVerticalBorders = NULL;
		window->windowskinCorners = NULL;
		// order of sprite creation is important, don't change it!
		// cursor sprite
		window->rb_cursorSprite = Sprite::create(argc, argv);
		RB_VAR2CPP(window->rb_cursorSprite, Sprite, cursorSprite);
		window->cursorSprite = cursorSprite;
		window->cursorSprite->setZ(window->z + 2);
		// contents sprite
		window->rb_contentsSprite = Sprite::create(argc, argv);
		RB_VAR2CPP(window->rb_contentsSprite, Sprite, contentsSprite);
		window->contentsSprite = contentsSprite;
		window->contentsSprite->setZ(window->z + 2);
		// bitmap border sprites
		for_iter (i, 0, 4)
		{
			window->rb_borderSprites[i] = Sprite::create(argc, argv);
			RB_VAR2CPP(window->rb_borderSprites[i], Sprite, borderSprite);
			window->borderSprites[i] = borderSprite;
			window->borderSprites[i]->setZ(window->z + 2);
		}
		// pause sprite
		window->rb_pauseSprite = Sprite::create(argc, argv);
		RB_VAR2CPP(window->rb_pauseSprite, Sprite, pauseSprite);
		window->pauseSprite = pauseSprite;
		window->pauseSprite->setZ(window->z + 2);
		Window::rb_setCursorRect(self, Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX(0), INT2FIX(0)));
		Window::rb_setWindowskin(self, Qnil);
		return self;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Window::rb_setVisible(VALUE self, VALUE value)
	{
		SourceRenderer::rb_setVisible(self, value);
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		Sprite::rb_setVisible(window->rb_contentsSprite, value);
		Sprite::rb_setVisible(window->rb_cursorSprite, value);
		Sprite::rb_setVisible(window->rb_pauseSprite, value);
		for_iter (i, 0, 4)
		{
			Sprite::rb_setVisible(window->rb_borderSprites[i], value);
		}
		return value;
	}

	VALUE Window::rb_setBitmap(VALUE self, VALUE value)
	{
		SourceRenderer::rb_setBitmap(self, value);
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		Sprite::rb_setBitmap(window->rb_contentsSprite, value);
		return value;
	}

	VALUE Window::rb_setZ(VALUE self, VALUE value)
	{
		SourceRenderer::rb_setZ(self, value);
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		window->cursorSprite->setZ(window->z + 2);
		window->contentsSprite->setZ(window->z + 2);
		window->pauseSprite->setZ(window->z + 2);
		for_iter (i, 0, 4)
		{
			window->borderSprites[i]->setZ(window->z + 2);
		}
		return value;
	}

	VALUE Window::rb_getWidth(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return INT2NUM(window->width);
	}

	VALUE Window::rb_setWidth(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		window->width = NUM2INT(value);
		return value;
	}

	VALUE Window::rb_getHeight(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return INT2NUM(window->height);
	}

	VALUE Window::rb_setHeight(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		window->height = NUM2INT(value);
		return value;
	}

	VALUE Window::rb_getActive(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return (window->active ? Qtrue : Qfalse);
	}

	VALUE Window::rb_setActive(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		window->active = (bool)RTEST(value);
		return value;
	}

	VALUE Window::rb_getPause(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return (window->pause ? Qtrue : Qfalse);
	}

	VALUE Window::rb_setPause(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		bool pause = (bool)RTEST(value);
		if (window->pause != pause)
		{
			window->pause = pause;
			window->pauseCount = (pause ? hmax(window->pauseCount, 0) : hmin(window->pauseCount, 4));
		}
		return value;
	}

	VALUE Window::rb_getStretch(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return (window->stretch ? Qtrue : Qfalse);
	}

	VALUE Window::rb_setStretch(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		window->stretch = (bool)RTEST(value);
		return value;
	}

	VALUE Window::rb_getBackOpacity(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return INT2NUM(window->backOpacity);
	}

	VALUE Window::rb_setBackOpacity(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		window->backOpacity = hclamp(NUM2INT(value), 0, 255);
		return value;
	}

	VALUE Window::rb_getContentsOpacity(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return INT2NUM(window->contentsOpacity);
	}

	VALUE Window::rb_setContentsOpacity(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		window->contentsOpacity = hclamp(NUM2INT(value), 0, 255);
		return value;
	}

	VALUE Window::rb_getCursorRect(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return window->rb_cursorRect;
	}

	VALUE Window::rb_setCursorRect(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Window, window, Rect, cursorRect);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return value;
	}

	VALUE Window::rb_getWindowskin(VALUE self)
	{
		RB_SELF2CPP(Window, window);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		return window->rb_windowskin;
	}

	VALUE Window::rb_setWindowskin(VALUE self, VALUE value)
	{
		VALUE rb_oldWindowskin = Window::rb_getWindowskin(self);
		RB_GENERATE_SETTER(Window, window, Bitmap, windowskin);
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
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
		if (window->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed window");
		}
		window->pause ? window->pauseCount++ : window->pauseCount--;
		if (window->active)
		{
			window->cursorCount = (window->cursorCount + 1) % 32;
		}
		return Qnil;
	}

}
