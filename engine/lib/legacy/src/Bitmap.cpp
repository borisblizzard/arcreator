#include <ruby.h>

#include <april/RenderSystem.h>
#include <april/Texture.h>
#include <atres/atres.h>
#include <atres/FontResourceBitmap.h>
#include <atres/Renderer.h>
#include <gtypes/Rectangle.h>
#include <gtypes/Vector2.h>
#include <hltypes/exception.h>
#include <hltypes/harray.h>
#include <hltypes/hfile.h>
#include <hltypes/hlog.h>
#include <hltypes/hltypesUtil.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Color.h"
#include "Font.h"
#include "Rect.h"
#include "legacy.h"
#include "RGSSError.h"

namespace legacy
{
	VALUE rb_cBitmap;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/
	
	Bitmap::Bitmap() : RubyObject()
	{
		this->typeName = "bitmap";
		this->disposed = true;
		this->texture = NULL;
		this->rb_font = Qnil;
		this->font = NULL;
	}

	Bitmap::Bitmap(int width, int height) : RubyObject(), texture(NULL)
	{
		this->typeName = "bitmap";
		this->disposed = false;
		this->texture = april::rendersys->createTexture(width, height, april::Color::Clear,
			april::Image::FORMAT_RGBA, april::Texture::TYPE_RENDER_TARGET);
		this->texture->setFilter(april::Texture::FILTER_NEAREST);
		this->rb_font = Qnil;
		this->font = new Font(Font::defaultName);
	}

	Bitmap::Bitmap(chstr fullFilename) : RubyObject(), texture(NULL)
	{
		this->typeName = "bitmap";
		this->disposed = false;
		this->_loadTexture(fullFilename);
		this->rb_font = Qnil;
		this->font = new Font(Font::defaultName);
	}

	Bitmap::~Bitmap()
	{
		this->dispose();
	}

	void Bitmap::initialize(int argc, VALUE* argv)
	{
		this->disposed = false;
		VALUE arg1, arg2;
		rb_scan_args(argc, argv, "11", &arg1, &arg2);
		if (NIL_P(arg2))
		{
			RB_CHECK_TYPE(arg1, rb_cString);
			hstr filename = StringValueCStr(arg1);
			hstr fullFilename = Bitmap::getFullFilename(filename);
			this->_loadTexture(fullFilename);
		}
		else
		{
			int w = NUM2INT(arg1);
			int h = NUM2INT(arg2);
			if (w < 1 || h < 1)
			{
				rb_raise(rb_eRGSSError, hsprintf("Failed to create Bitmap %dx%d!", w, h).c_str());
			}
			this->texture = april::rendersys->createTexture(w, h, april::Color::Clear,
				april::Image::FORMAT_RGBA, april::Texture::TYPE_RENDER_TARGET);
			this->texture->setFilter(april::Texture::FILTER_NEAREST);
		}
		this->rb_font = Font::create(0, NULL);
		RB_VAR2CPP(this->rb_font, Font, font);
		this->font = font;
	}

	void Bitmap::dispose()
	{
		if (!this->disposed)
		{
			CPP_VAR_DELETE(font);
			this->rb_font = Qnil;
			this->font = NULL;
			if (this->texture != NULL)
			{
				delete this->texture;
				this->texture = NULL;
			}
			this->disposed = true;
		}
	}

	void Bitmap::mark()
	{
		RubyObject::mark();
		RB_GC_MARK(font);
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/
	
	int Bitmap::getWidth()
	{
		return this->texture->getWidth();
	}

	int Bitmap::getHeight()
	{
		return this->texture->getHeight();
	}

	void Bitmap::clear()
	{
		this->texture->clear();
	}

	hstr Bitmap::getFullFilename(chstr filename)
	{
		hstr fullFilename = april::rendersys->findTextureResource(filename);
		if (fullFilename == "")
		{
			RB_RAISE_FILE_NOT_FOUND(filename.c_str());
		}
		return fullFilename;
	}

	void Bitmap::_drawText(int x, int y, int w, int h, chstr text, int align)
	{
		hstr fontName = this->font->getAtresFontName();
		if (fontName == "") // font does not exist
		{
			hlog::warn(legacy::logTag, "Font could not be found: " + this->font->getName());
			return;
		}
		atres::Alignment horizontal;
		switch (align)
		{
		case 0:
			horizontal = atres::LEFT;
			break;
		case 1:
			horizontal = atres::CENTER;
			break;
		case 2:
			horizontal = atres::RIGHT;
			break;
		case 3:
			horizontal = atres::LEFT_WRAPPED;
			break;
		case 4:
			horizontal = atres::CENTER_WRAPPED;
			break;
		case 5:
			horizontal = atres::RIGHT_WRAPPED;
			break;
		case 6:
			horizontal = atres::JUSTIFIED;
			break;
		default:
			horizontal = atres::LEFT;
			break;
		}
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		gmat4 projectionMatrix = april::rendersys->getProjectionMatrix();
		april::Texture::Filter filter = this->texture->getFilter();
		this->texture->setFilter(april::Texture::FILTER_LINEAR);
		april::Texture* target = april::rendersys->getRenderTarget();
		april::rendersys->setRenderTarget(this->texture);
		april::rendersys->setIdentityTransform();
		april::rendersys->setOrthoProjection(grect(0.0f, 0.0f,
			(float)this->texture->getWidth(), (float)this->texture->getHeight()));
		grect destRect((float)x, (float)y, (float)w,
			hmax((float)h, atres::renderer->getFontResource(fontName)->getLineHeight()));
		atres::renderer->drawText(fontName, destRect, text, horizontal,
			atres::CENTER, this->font->getColor()->toAprilColor());
		april::rendersys->setRenderTarget(target);
		this->texture->setFilter(filter);
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	void Bitmap::_loadTexture(chstr filename)
	{
		//april::Texture* loadTexture = april::rendersys->createTextureFromResource(filename, april::Image::FORMAT_RGBA);


		this->texture = april::rendersys->createTextureFromResource(filename,
			april::Image::FORMAT_RGBA, april::Texture::TYPE_RENDER_TARGET);
		// TODO - remove
		/*
		april::Texture* loadTexture = april::rendersys->loadTexture(filename);
		int w = loadTexture->getWidth();
		int h = loadTexture->getHeight();
		this->texture = april::rendersys->createTexture(
			w, h, april::Texture::FORMAT_ARGB, april::Texture::TYPE_RENDER_TARGET);
		// TODO - the texture should always be blitted to prevent problems
		if (loadTexture->getBpp() >= 3)
		{
			this->texture->blit(0, 0, loadTexture, 0, 0, w, h);
		}
		else // palette-based textures need to be rendered after all
		{
			this->texture->setFilter(april::Texture::FILTER_NEAREST);
			april::rendersys->setTextureBlendMode(april::OVERWRITE);
			this->_renderToTexture(0, 0, loadTexture, 0, 0, w, h);
			april::rendersys->setTextureBlendMode(april::DEFAULT);
		}
		delete loadTexture;
		*/
	}

	void Bitmap::_renderToTexture(int sx, int sy, int sw, int sh, int dx, int dy, april::Texture* source, unsigned char alpha)
	{
		if (alpha == 0)
		{
			return;
		}
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		gmat4 projectionMatrix = april::rendersys->getProjectionMatrix();
		april::Texture::Filter filter = source->getFilter();
		source->setFilter(april::Texture::FILTER_NEAREST);
		april::Texture* target = april::rendersys->getRenderTarget();
		april::rendersys->setRenderTarget(this->texture);
		april::rendersys->setTexture(source);
		april::rendersys->setIdentityTransform();
		april::rendersys->setOrthoProjection(grect(0.0f, 0.0f,
			(float)this->texture->getWidth(), (float)this->texture->getHeight()));
		float width = (float)source->getWidth();
		float height = (float)source->getHeight();
		grect destRect((float)dx, (float)dy, (float)sw, (float)sh);
		grect srcRect(sx / width, sy / height, sw / width, sh / height);
		if (alpha == 255)
		{
			april::rendersys->drawTexturedRect(destRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(destRect, srcRect, april::Color(april::Color::White, alpha));
		}
		april::rendersys->setRenderTarget(target);
		source->setFilter(filter);
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	// TODO - might be obsolete
	void Bitmap::_renderToTexture(int sx, int sy, int sw, int sh, int dx, int dy, int dw, int dh, april::Texture* source, unsigned char alpha)
	{
		if (alpha == 0)
		{
			return;
		}
		if (dw == sw && dh == sh)
		{
			this->_renderToTexture(sx, sy, sw, sh, dx, dy, source, alpha);
			return;
		}
		gmat4 viewMatrix = april::rendersys->getModelviewMatrix();
		gmat4 projectionMatrix = april::rendersys->getProjectionMatrix();
		april::Texture::Filter filter = source->getFilter();
		source->setFilter(april::Texture::FILTER_LINEAR);
		april::Texture* target = april::rendersys->getRenderTarget();
		april::rendersys->setRenderTarget(this->texture);
		april::rendersys->setIdentityTransform();
		april::rendersys->setOrthoProjection(grect(0.0f, 0.0f,
			(float)this->texture->getWidth(), (float)this->texture->getHeight()));
		april::rendersys->setTexture(source);
		float width = (float)source->getWidth();
		float height = (float)source->getHeight();
		grect destRect((float)dx, (float)dy, (float)dw, (float)dh);
		grect srcRect(sx / width, sy / height, sw / width, sh / height);
		if (alpha == 255)
		{
			april::rendersys->drawTexturedRect(destRect, srcRect);
		}
		else
		{
			april::rendersys->drawTexturedRect(destRect, srcRect, april::Color(april::Color::White, alpha));
		}
		april::rendersys->setRenderTarget(target);
		source->setFilter(filter);
		april::rendersys->setProjectionMatrix(projectionMatrix);
		april::rendersys->setModelviewMatrix(viewMatrix);
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/
	
	void Bitmap::init()
	{
	}

	void Bitmap::destroy()
	{
	}

	void Bitmap::createRubyInterface()
	{
		rb_cBitmap = rb_define_class("Bitmap", rb_cObject);
		rb_define_alloc_func(rb_cBitmap, &Bitmap::rb_new);
		// initialize
		rb_define_method(rb_cBitmap, "initialize", RUBY_METHOD_FUNC(&Bitmap::rb_initialize), -1);
		rb_define_method(rb_cBitmap, "initialize_copy", RUBY_METHOD_FUNC(&Bitmap::rb_initialize_copy), 1);
		rb_define_method(rb_cBitmap, "_arc_dump", RUBY_METHOD_FUNC(&Bitmap::rb_arcDump), 0);
		// getters and setters
		rb_define_method(rb_cBitmap, "width", RUBY_METHOD_FUNC(&Bitmap::rb_getWidth), 0);
		rb_define_method(rb_cBitmap, "height", RUBY_METHOD_FUNC(&Bitmap::rb_getHeight), 0);
		rb_define_method(rb_cBitmap, "rect", RUBY_METHOD_FUNC(&Bitmap::rb_getRect), 0);
		rb_define_method(rb_cBitmap, "font", RUBY_METHOD_FUNC(&Bitmap::rb_getFont), 0);
		rb_define_method(rb_cBitmap, "font=", RUBY_METHOD_FUNC(&Bitmap::rb_setFont), 1);
		// methods
		rb_define_method(rb_cBitmap, "get_pixel", RUBY_METHOD_FUNC(&Bitmap::rb_getPixel), 2);
		rb_define_method(rb_cBitmap, "set_pixel", RUBY_METHOD_FUNC(&Bitmap::rb_setPixel), 3);
		rb_define_method(rb_cBitmap, "fill_rect", RUBY_METHOD_FUNC(&Bitmap::rb_fillRect), -1); 
		rb_define_method(rb_cBitmap, "clear", RUBY_METHOD_FUNC(&Bitmap::rb_clear), 0); 
		rb_define_method(rb_cBitmap, "blt", RUBY_METHOD_FUNC(&Bitmap::rb_blt), -1); 
		rb_define_method(rb_cBitmap, "stretch_blt", RUBY_METHOD_FUNC(&Bitmap::rb_stretchBlt), -1); 
		rb_define_method(rb_cBitmap, "draw_text", RUBY_METHOD_FUNC(&Bitmap::rb_drawText), -1); 
		rb_define_method(rb_cBitmap, "dispose", RUBY_METHOD_FUNC(&Bitmap::rb_dispose), 0); 
		rb_define_method(rb_cBitmap, "disposed?", RUBY_METHOD_FUNC(&Bitmap::rb_isDisposed), 0); 
		rb_define_method(rb_cBitmap, "hue_change", RUBY_METHOD_FUNC(&Bitmap::rb_changeHue), 1); 
		rb_define_method(rb_cBitmap, "text_size", RUBY_METHOD_FUNC(&Bitmap::rb_textSize), 1); 
	}
	
	VALUE Bitmap::rb_new(VALUE classe) 
	{
		Bitmap* bitmap;
		return RB_OBJECT_NEW(classe, Bitmap, bitmap, &Bitmap::gc_mark, &Bitmap::gc_free);
	}

	VALUE Bitmap::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		bitmap->initialize(argc, argv);
		return self;
	}

	VALUE Bitmap::rb_initialize_copy(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_VAR2CPP(original, Bitmap, other);
		bitmap->disposed = false;
		int w = other->texture->getWidth();
		int h = other->texture->getHeight();
		bitmap->texture = april::rendersys->createTexture(w, h, april::Color::Clear,
			april::Image::FORMAT_RGBA, april::Texture::TYPE_RENDER_TARGET);
		bitmap->texture->setFilter(april::Texture::FILTER_NEAREST);
		bitmap->texture->write(0, 0, w, h, 0, 0, other->texture);
		Bitmap::rb_setFont(self, rb_obj_clone(other->rb_font));
		return self;
	}

	VALUE Bitmap::rb_dispose(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		bitmap->dispose();
		return Qnil;
	}

	VALUE Bitmap::create(int argc, VALUE* argv)
	{
		VALUE object = Bitmap::rb_new(rb_cBitmap);
		object = Bitmap::rb_initialize(argc, argv, object);
		return object;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Bitmap::rb_getWidth(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		return INT2FIX(bitmap->getWidth());
	}

	VALUE Bitmap::rb_getHeight(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		return INT2FIX(bitmap->getHeight());
	}

	VALUE Bitmap::rb_getRect(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		return Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX(bitmap->getWidth()), INT2FIX(bitmap->getHeight()));
	}

	VALUE Bitmap::rb_getFont(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		return bitmap->rb_font;
	}

	VALUE Bitmap::rb_setFont(VALUE self, VALUE value)
	{
		{
			RB_SELF2CPP(Bitmap, bitmap);
			RB_CHECK_DISPOSED(bitmap);
		}
		RB_GENERATE_SETTER(Bitmap, bitmap, Font, font);
		return value;
	}

	VALUE Bitmap::rb_isDisposed(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		return (bitmap->disposed ? Qtrue : Qfalse);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Bitmap::rb_getPixel(VALUE self, VALUE x, VALUE y)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		april::Color color = bitmap->texture->getPixel(NUM2INT(x), NUM2INT(y));
		VALUE argv[4] = {INT2FIX(color.r), INT2FIX(color.g), INT2FIX(color.b), INT2FIX(color.a)};
		return Color::create(4, argv);
	}

	VALUE Bitmap::rb_setPixel(VALUE self, VALUE x, VALUE y, VALUE color)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		RB_CHECK_TYPE(color, rb_cColor);
		RB_VAR2CPP(color, Color, cColor);
		bitmap->texture->setPixel(NUM2INT(x), NUM2INT(y), cColor->toAprilColor());
		return Qnil;
	}

	VALUE Bitmap::rb_fillRect(int argc, VALUE* argv, VALUE self)
	{
		if (argc != 2 && argc != 5)
		{
			rb_raise(rb_eArgError, hsprintf("Wrong number of arguments: %d for 2 or 5", argc).c_str());
		}
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		int x, y, w, h;
		VALUE arg1, arg2, arg3, arg4, color;
		rb_scan_args(argc, argv, "23", &arg1, &arg2, &arg3, &arg4, &color);
		if (NIL_P(arg3) && NIL_P(arg4) && NIL_P(color))
		{
			RB_CHECK_TYPE(arg1, rb_cRect);
			color = arg2;
			RB_VAR2CPP(arg1, Rect, rect);
			x = rect->x;
			y = rect->y;
			w = rect->width;
			h = rect->height;
		}
		else
		{
			x = NUM2INT(arg1);
			y = NUM2INT(arg2);
			w = NUM2INT(arg3);
			h = NUM2INT(arg4);
		}
		RB_CHECK_TYPE(color, rb_cColor);
		RB_VAR2CPP(color, Color, cColor);
		bitmap->texture->fillRect(x, y, w, h, cColor->toAprilColor());
		return Qnil;
	}

	VALUE Bitmap::rb_clear(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		bitmap->clear();
		return Qnil;
	}

	VALUE Bitmap::rb_blt(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		VALUE arg1, arg2, arg3, arg4, arg5;
		rb_scan_args(argc, argv, "41", &arg1, &arg2, &arg3, &arg4, &arg5);
		int x = NUM2INT(arg1);
		int y = NUM2INT(arg2);
		RB_CHECK_TYPE(arg3, rb_cBitmap);
		RB_CHECK_TYPE(arg4, rb_cRect);
		RB_VAR2CPP(arg3, Bitmap, source);
		RB_VAR2CPP(arg4, Rect, rect);
		if (NIL_P(arg5))
		{
			bitmap->_renderToTexture(rect->x, rect->y, rect->width, rect->height, x, y, source->texture);
		}
		else
		{
			bitmap->_renderToTexture(rect->x, rect->y, rect->width, rect->height, x, y, source->texture, (unsigned char)NUM2INT(arg5));
		}
		return Qnil;
	}

	VALUE Bitmap::rb_stretchBlt(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		VALUE arg1, arg2, arg3, arg4;
		rb_scan_args(argc, argv, "31", &arg1, &arg2, &arg3, &arg4);
		RB_CHECK_TYPE(arg1, rb_cRect);
		RB_CHECK_TYPE(arg2, rb_cBitmap);
		RB_CHECK_TYPE(arg3, rb_cRect);
		RB_VAR2CPP(arg1, Rect, dest_rect);
		RB_VAR2CPP(arg2, Bitmap, source);
		RB_VAR2CPP(arg3, Rect, src_rect);
		if (NIL_P(arg4))
		{
			bitmap->_renderToTexture(src_rect->x, src_rect->y, src_rect->width, src_rect->height,
				dest_rect->x, dest_rect->y, dest_rect->width, dest_rect->height, source->texture);
		}
		else
		{
			bitmap->_renderToTexture(src_rect->x, src_rect->y, src_rect->width, src_rect->height,
				dest_rect->x, dest_rect->y, dest_rect->width, dest_rect->height, source->texture,
				(unsigned char)NUM2INT(arg4));
		}
		return Qnil;
	}

	VALUE Bitmap::rb_drawText(int argc, VALUE* argv, VALUE self)
	{
		if (argc != 2 && argc != 3 && argc != 5 && argc != 6)
		{
			rb_raise(rb_eArgError, hsprintf("Wrong number of arguments: %d for 2, 3, 5 or 6", argc).c_str());
		}
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		int x, y, w, h;
		hstr text;
		VALUE arg1, arg2, arg3, arg4, arg5, arg6;
		rb_scan_args(argc, argv, "24", &arg1, &arg2, &arg3, &arg4, &arg5, &arg6);
		if (NIL_P(arg4) && NIL_P(arg5) && NIL_P(arg6))
		{
			RB_CHECK_TYPE(arg1, rb_cRect);
			RB_VAR2CPP(arg1, Rect, rect);
			x = rect->x;
			y = rect->y;
			w = rect->width;
			h = rect->height;
			RB_CHECK_TYPE(arg2, rb_cString);
			text = hstr(StringValueCStr(arg2));
		}
		else
		{
			x = NUM2INT(arg1);
			y = NUM2INT(arg2);
			w = NUM2INT(arg3);
			h = NUM2INT(arg4);
			RB_CHECK_TYPE(arg5, rb_cString);
			text = hstr(StringValueCStr(arg5));
			arg3 = arg6;
		}
		int align = (NIL_P(arg3) ? 0 : NUM2INT(arg3));
		bitmap->_drawText(x, y, w, h, text, align);
		return Qnil;
	}

	VALUE Bitmap::rb_changeHue(VALUE self, VALUE hue)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		bitmap->texture->rotateHue(0, 0, bitmap->texture->getWidth(), bitmap->texture->getHeight(), (float)NUM2DBL(hue));
		return Qnil;
	}

	VALUE Bitmap::rb_textSize(VALUE self, VALUE string)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_CHECK_DISPOSED(bitmap);
		RB_CHECK_TYPE(string, rb_cString);
		hstr text = StringValueCStr(string);
		hstr fontName = bitmap->font->getAtresFontName();
		float w = atres::renderer->getTextWidth(fontName, text);
		float h = atres::renderer->getTextHeight(fontName, text, w + 2.0f);
		return Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX((int)ceil(w)), INT2FIX((int)ceil(h)));
	}

	VALUE Bitmap::rb_arcDump(VALUE self)
	{
		rb_raise(rb_eTypeError, "Can't arc-dump: Bitmap");
		return Qnil;
	}

}
