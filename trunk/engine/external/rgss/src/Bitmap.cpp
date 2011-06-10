#include <ruby.h>

#include <april/ImageSource.h>
#include <april/RenderSystem.h>
#include <april/Texture.h>
#include <atres/atres.h>
#include <atres/Font.h>
#include <gtypes/Rectangle.h>
#include <gtypes/Vector2.h>
#include <hltypes/exception.h>
#include <hltypes/harray.h>
#include <hltypes/hfile.h>
#include <hltypes/util.h>

#include "CodeSnippets.h"
#include "Bitmap.h"
#include "Color.h"
#include "Font.h"
#include "Rect.h"
#include "RGSSError.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/
	
	VALUE rb_cBitmap;
	hmap<hstr, Bitmap*> fontCache;
	hmap<hstr, atres::CacheEntry> characterCache;

	Bitmap::Bitmap(int width, int height) : texture(NULL)
	{
		this->imageSource = april::createEmptyImage(width, height);
		this->textureNeedsUpdate = true;
		this->disposed = false;
	}

	Bitmap::Bitmap(chstr filename) : texture(NULL)
	{
		hstr fullFilename = april::rendersys->findTextureFile(filename);
		if (fullFilename == "")
		{
			/// @todo Has to throw Errno::ENOENT without using eval()
			//rb_raise(rb_eENOENT, ("No such file or directory - " + filename).c_str());
			hstr evalString = "raise Errno::ENOENT.new(\"" + filename + "\")";
			rb_eval_string(evalString.c_str());
		}
		this->imageSource = april::loadImage(fullFilename);
		if (this->imageSource->bpp != 4)
		{
			april::ImageSource* imageSource = this->imageSource;
			this->imageSource = april::createEmptyImage(imageSource->w, imageSource->h);
			this->imageSource->copyImage(imageSource, 4);
		}
		this->textureNeedsUpdate = true;
		this->disposed = false;
	}

	Bitmap::~Bitmap()
	{
		if (!this->disposed)
		{
			if (this->texture != NULL)
			{
				delete this->texture;
				this->texture = NULL;
			}
			if (this->imageSource != NULL)
			{
				delete this->imageSource;
				this->imageSource = NULL;
			}
			this->disposed = true;
		}
	}

	int Bitmap::getWidth()
	{
		return this->imageSource->w;
	}

	int Bitmap::getHeight()
	{
		return this->imageSource->h;
	}

	void Bitmap::blt(int x, int y, Bitmap* source, int sx, int sy, int sw, int sh)
	{
		this->imageSource->blit(x, y, source->imageSource, sx, sy, sw, sh);
		this->textureNeedsUpdate = true;
	}

	void Bitmap::stretchBlt(int x, int y, int w, int h, Bitmap* source, int sx, int sy, int sw, int sh)
	{
		this->imageSource->stretch_blit(x, y, w, h, source->imageSource, sx, sy, sw, sh);
		this->textureNeedsUpdate = true;
	}

	void Bitmap::_drawText(int x, int y, int w, int h, chstr text, int align)
	{
		atres::Alignment horizontal;
		switch (align)
		{
		case 1:
			horizontal = atres::CENTER;
			break;
		case 2:
			horizontal = atres::RIGHT;
			break;
		default:
			horizontal = atres::LEFT;
			break;
		}
		atres::Alignment vertical = atres::CENTER;
		grect rect((float)x, (float)y, (float)w, (float)h);
		april::Color color = this->font->getColor()->toAColor();
		hstr fontName = this->_getAFontName();

		// pure Atres code
		bool needCache = !characterCache.has_key(text);
		atres::CacheEntry entry;
		grect drawRect = grect(0.0f, 0.0f, rect.getSize());
		harray<atres::RenderSequence> sequences;
		if (!needCache)
		{
			entry = characterCache[text];
			needCache = (entry.fontName != fontName || entry.size.x != drawRect.w || entry.size.y != drawRect.h);
			sequences = entry.sequences;
		}
		if (needCache)
		{
			harray<atres::FormatTag> tags;
			atres::FormatTag tag;
			tag.type = atres::FORMAT_COLOR;
			tag.data = color.hex();
			tags.push_front(tag);
			tag.type = atres::FORMAT_FONT;
			tag.data = fontName;
			tags.push_front(tag);
			/// @todo Possibly to be added later.
			/*
			if (this->font->getBold())
			{
				tag.type = atres::FORMAT_BOLD;
				tag.data = this->_getAFontName();
				tags += tag;
			}
			if (this->font->getItalic())
			{
				tag.type = atres::FORMAT_ITALIC;
				tag.data = this->_getAFontName();
				tags += tag;
			}
			*/
			harray<atres::RenderLine> lines = atres::createRenderLines(drawRect, text, tags, horizontal, vertical);
			sequences = atres::createRenderSequences(drawRect, lines, tags);
			if (text.size() <= 1)
			{
				entry.fontName = fontName;
				entry.size = rect.getSize();
				entry.sequences = sequences;
				characterCache[text] = entry;
			}
		}
		/// @todo This works but is very slow, improve it
		//*
		hstr name = this->font->getName();
		if (!atres::hasFont(name))
		{
			name = atres::getFont("")->getName(); // default font
		}
		name = "Graphics/Fonts/" + name;
		// creating a bitmap to blit from
		Bitmap* bitmap;
		if (fontCache.has_key(name))
		{
			bitmap = fontCache[name];
		}
		else
		{
			bitmap = new Bitmap(name);
			fontCache[name] = bitmap;
		}
		// blit every character manually
		foreach (atres::RenderSequence, it, sequences)
		{
			if ((*it).rectangles.size() > 0)
			{
				foreach (atres::RenderRectangle, it2, (*it).rectangles)
				{
					this->stretchBlt((int)((*it2).dest.x + rect.x), (int)((*it2).dest.y + rect.y),
						(int)(*it2).dest.w, (int)(*it2).dest.h, bitmap, (int)(*it2).src.x,
						(int)(*it2).src.y, (int)(*it2).src.w, (int)(*it2).src.h);
				}
			}
		}
		//*/
		this->textureNeedsUpdate = true;
	}

	hstr Bitmap::_getAFontName()
	{
		hstr result = this->font->getName();
		int h = this->font->getSize();
		if (!atres::hasFont(result))
		{
			result = atres::getFont("")->getName(); // default font
		}
		float fontHeight = atres::getFontHeight(result);
		if (h != fontHeight)
		{
			result += hsprintf(":%f", h / fontHeight);
		}
		return result;
	}

	void Bitmap::updateTexture()
	{
		if (this->textureNeedsUpdate)
		{
			this->textureNeedsUpdate = false;
			if (this->texture != NULL)
			{
				delete this->texture;
			}
			this->texture = april::rendersys->createTextureFromMemory(
				this->imageSource->data, this->imageSource->w, this->imageSource->h);
		}
	}

	void Bitmap::dispose()
	{
		if (!this->disposed)
		{
			if (this->texture != NULL)
			{
				delete this->texture;
				this->texture = NULL;
			}
			if (this->imageSource != NULL)
			{
				delete this->imageSource;
				this->imageSource = NULL;
			}
			this->disposed = true;
		}
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/
	
	void Bitmap::init()
	{
		fontCache = hmap<hstr, Bitmap*>();
	}

	void Bitmap::destroy()
	{
		foreach_m (Bitmap*, it, fontCache)
		{
			delete it->second;
		}
		fontCache.clear();
	}

	void Bitmap::createRubyInterface()
	{
		rb_cBitmap = rb_define_class("Bitmap", rb_cObject);
		rb_define_alloc_func(rb_cBitmap, &Bitmap::rb_new);
		// initialize
		rb_define_method(rb_cBitmap, "initialize", RUBY_METHOD_FUNC(&Bitmap::rb_initialize), -1);
		rb_define_method(rb_cBitmap, "initialize_copy", RUBY_METHOD_FUNC(&Bitmap::rb_initialize_copy), 1);
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
		// not implemented yet
			
		rb_define_method(rb_cBitmap, "dispose", RUBY_METHOD_FUNC(&Bitmap::rb_dispose), 0); 
		rb_define_method(rb_cBitmap, "disposed?", RUBY_METHOD_FUNC(&Bitmap::rb_isDisposed), 0); 
		rb_define_method(rb_cBitmap, "draw_text", RUBY_METHOD_FUNC(&Bitmap::rb_drawText), -1); 
		rb_define_method(rb_cBitmap, "hue_change", RUBY_METHOD_FUNC(&Bitmap::rb_changeHue), 1); 
		rb_define_method(rb_cBitmap, "text_size", RUBY_METHOD_FUNC(&Bitmap::rb_textSize), 1); 
	}
	
	void Bitmap::gc_mark(Bitmap* bitmap)
	{
		if (!NIL_P(bitmap->rb_font))
		{
			rb_gc_mark(bitmap->rb_font);
		}
	}

	void Bitmap::gc_free(Bitmap* bitmap)
	{
		bitmap->dispose();
	}

	VALUE Bitmap::rb_new(VALUE classe) 
	{
		Bitmap* bitmap;
		VALUE result = Data_Make_Struct(classe, Bitmap, Bitmap::gc_mark, Bitmap::gc_free, bitmap);
		bitmap->disposed = true;
		return result;
	}

	VALUE Bitmap::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		bitmap->disposed = false;
		VALUE arg1, arg2;
		rb_scan_args(argc, argv, "11", &arg1, &arg2);
		if (NIL_P(arg2))
		{
			hstr filename = StringValuePtr(arg1);
			hstr fullFilename = april::rendersys->findTextureFile(filename);
			if (fullFilename == "")
			{
				/// @todo Has to throw Errno::ENOENT without using eval()
				//rb_raise(rb_eENOENT, ("No such file or directory - " + filename).c_str());
				hstr evalString = "raise Errno::ENOENT.new(\"" + filename + "\")";
				rb_eval_string(evalString.c_str());
			}
			bitmap->imageSource = april::loadImage(fullFilename);
			if (bitmap->imageSource->bpp != 4)
			{
				april::ImageSource* imageSource = bitmap->imageSource;
				bitmap->imageSource = april::createEmptyImage(imageSource->w, imageSource->h);
				bitmap->imageSource->copyImage(imageSource, 4);
			}
		}
		else
		{
			int w = NUM2INT(arg1);
			int h = NUM2INT(arg2);
			if (w < 1 || h < 1)
			{
				rb_raise(rb_eRGSSError, "failed to create bitmap");
			}
			bitmap->imageSource = april::createEmptyImage(w, h);
		}
		Bitmap::rb_setFont(self, Font::create(0, NULL));
		bitmap->textureNeedsUpdate = true;
		return self;
	}

	VALUE Bitmap::rb_initialize_copy(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		RB_VAR2CPP(original, Bitmap, other);
		bitmap->disposed = false;
		bitmap->imageSource = april::createEmptyImage(other->imageSource->w, other->imageSource->h);
		bitmap->imageSource->copyImage(other->imageSource);
		// TODO - should be changed to call an actual clone method for convenience
		Bitmap::rb_setFont(self, rb_funcall(other->rb_font, rb_intern("clone"), 0, NULL));
		bitmap->textureNeedsUpdate = true;
		return self;
	}

	VALUE Bitmap::rb_dispose(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		if (!bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
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
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		return INT2FIX(bitmap->getWidth());
	}

	VALUE Bitmap::rb_getHeight(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		return INT2FIX(bitmap->getHeight());
	}

	VALUE Bitmap::rb_getRect(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		return Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX(bitmap->getWidth()), INT2FIX(bitmap->getHeight()));
	}

	VALUE Bitmap::rb_getFont(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		return bitmap->rb_font;
	}

	VALUE Bitmap::rb_setFont(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Bitmap, bitmap, Font, font);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
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
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		april::Color color = bitmap->imageSource->getPixel(NUM2INT(x), NUM2INT(y));
		VALUE argv[4] = {INT2FIX(color.r), INT2FIX(color.g), INT2FIX(color.b), INT2FIX(color.a)};
		return Color::create(4, argv);
	}

	VALUE Bitmap::rb_setPixel(VALUE self, VALUE x, VALUE y, VALUE color)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		RB_VAR2CPP(color, Color, cColor);
		bitmap->imageSource->setPixel(NUM2INT(x), NUM2INT(y), cColor->toAColor());
		bitmap->textureNeedsUpdate = true;
		return Qnil;
	}

	VALUE Bitmap::rb_fillRect(int argc, VALUE* argv, VALUE self)
	{
		if (argc != 2 && argc != 5)
		{
			hstr message = hsprintf("wrong number of arguments (%d for 2 or 5)", argc);
			rb_raise(rb_eArgError, message.c_str());
		}
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		int x, y, w, h;
		VALUE arg1, arg2, arg3, arg4, color;
		rb_scan_args(argc, argv, "23", &arg1, &arg2, &arg3, &arg4, &color);
		if (NIL_P(arg3) && NIL_P(arg4) && NIL_P(color))
		{
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
		RB_VAR2CPP(color, Color, cColor);
		bitmap->imageSource->setPixels(x, y, w, h, cColor->toAColor());
		bitmap->textureNeedsUpdate = true;
		return Qnil;
	}

	VALUE Bitmap::rb_clear(VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		bitmap->imageSource->clear();
		bitmap->textureNeedsUpdate = true;
		return Qnil;
	}

	VALUE Bitmap::rb_blt(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		VALUE arg1, arg2, arg3, arg4, arg5;
		rb_scan_args(argc, argv, "41", &arg1, &arg2, &arg3, &arg4, &arg5);
		int x = NUM2INT(arg1);
		int y = NUM2INT(arg2);
		RB_VAR2CPP(arg3, Bitmap, source);
		RB_VAR2CPP(arg4, Rect, rect);
		if (NIL_P(arg5))
		{
			bitmap->imageSource->blit(x, y, source->imageSource, rect->x, rect->y, rect->width, rect->height);
		}
		else
		{
			bitmap->imageSource->blit(x, y, source->imageSource, rect->x, rect->y, rect->width, rect->height,
				(unsigned char)NUM2INT(arg5));
		}
		bitmap->textureNeedsUpdate = true;
		return Qnil;
	}

	VALUE Bitmap::rb_stretchBlt(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		VALUE arg1, arg2, arg3, arg4;
		rb_scan_args(argc, argv, "31", &arg1, &arg2, &arg3, &arg4);
		RB_VAR2CPP(arg1, Rect, dest_rect);
		RB_VAR2CPP(arg2, Bitmap, source);
		RB_VAR2CPP(arg3, Rect, src_rect);
		if (NIL_P(arg4))
		{
			bitmap->imageSource->stretch_blit(dest_rect->x, dest_rect->y, dest_rect->width, dest_rect->height,
				source->imageSource, src_rect->x, src_rect->y, src_rect->width, src_rect->height);
		}
		else
		{
			bitmap->imageSource->stretch_blit(dest_rect->x, dest_rect->y, dest_rect->width, dest_rect->height,
				source->imageSource, src_rect->x, src_rect->y, src_rect->width, src_rect->height,
				(unsigned char)NUM2INT(arg4));
		}
		bitmap->textureNeedsUpdate = true;
		return Qnil;
	}

	/****************************************************************************************
	 * TODO
	 ****************************************************************************************/

	VALUE Bitmap::rb_drawText(int argc, VALUE* argv, VALUE self)
	{
		if (argc != 2 && argc != 3 && argc != 5 && argc != 6)
		{
			hstr message = hsprintf("wrong number of arguments (%d for 2, 3, 5 or 6)", argc);
			rb_raise(rb_eArgError, message.c_str());
		}
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		int x, y, w, h;
		hstr text;
		VALUE arg1, arg2, arg3, arg4, arg5, arg6;
		rb_scan_args(argc, argv, "24", &arg1, &arg2, &arg3, &arg4, &arg5, &arg6);
		if (NIL_P(arg4) && NIL_P(arg5) && NIL_P(arg6))
		{
			RB_VAR2CPP(arg1, Rect, rect);
			x = rect->x;
			y = rect->y;
			w = rect->width;
			h = rect->height;
			text = hstr(StringValuePtr(arg2));
		}
		else
		{
			x = NUM2INT(arg1);
			y = NUM2INT(arg2);
			w = NUM2INT(arg3);
			h = NUM2INT(arg4);
			text = hstr(StringValuePtr(arg5));
			arg3 = arg6;
		}
		int align = (NIL_P(arg3) ? 0 : NUM2INT(arg3));
		bitmap->_drawText(x, y, w, h, text, align);
		bitmap->textureNeedsUpdate = true;
		return Qnil;
	}

	VALUE Bitmap::rb_changeHue(VALUE self, VALUE hue)
	{
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		return Qnil;
	}

	VALUE Bitmap::rb_textSize(VALUE self, VALUE string)
	{
		/// @todo Test this.
		RB_SELF2CPP(Bitmap, bitmap);
		if (bitmap->disposed)
		{
			//rb_raise(rb_eRGSSError, "disposed bitmap");
		}
		hstr text = StringValuePtr(string);
		hstr fontName = bitmap->_getAFontName();
		float w = atres::getTextWidthUnformatted(fontName, text);
		int h = bitmap->getHeight();
		return Rect::create(INT2FIX(0), INT2FIX(0), INT2FIX((int)ceil(w)), INT2FIX(h));
	}

}
