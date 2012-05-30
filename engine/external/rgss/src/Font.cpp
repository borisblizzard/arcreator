#include <ruby.h>

#include <atres/Renderer.h>
#include <atresttf/FontResourceTtf.h>
#include <hltypes/harray.h>
#include <hltypes/hstring.h>

#include "CodeSnippets.h"
#include "Color.h"
#include "Constants.h"
#include "Font.h"
#include "rgss.h"

namespace rgss
{
	VALUE rb_cFont;

	/****************************************************************************************
	 * Construction/Destruction
	 ****************************************************************************************/

	hstr Font::defaultName;
	int Font::defaultSize;
	bool Font::defaultBold;
	bool Font::defaultItalic;
	Color* Font::defaultColor;
	VALUE Font::rb_defaultColor;
	harray<hstr> Font::_missingFonts;

	Font::Font() : RubyObject()
	{
		this->name = defaultName;
		this->size = defaultSize;
		this->bold = defaultBold;
		this->italic = defaultItalic;
		this->rb_color = Qnil;
		this->color = NULL;
	}
	
	Font::Font(chstr name) : RubyObject()
	{
		this->name = name;
		this->size = defaultSize;
		this->bold = defaultBold;
		this->italic = defaultItalic;
		this->rb_color = Qnil;
		this->color = new Color(*defaultColor);
	}

	Font::Font(chstr name, int size) : RubyObject()
	{
		this->name = name;
		this->size = size;
		this->bold = defaultBold;
		this->italic = defaultItalic;
		this->rb_color = Qnil;
		this->color = new Color(*defaultColor);
	}

	Font::~Font()
	{
		CPP_VAR_DELETE(color);
		this->rb_color = Qnil;
		this->color = NULL;
	}

	void Font::initialize(int argc, VALUE* argv)
	{
		VALUE name, size;
		rb_scan_args(argc, argv, "02", &name, &size);
		this->name = (!NIL_P(name) ? StringValueCStr(name) : defaultName);
		this->size = (!NIL_P(name) ? NUM2INT(size) : defaultSize);
		this->bold = defaultBold;
		this->italic = defaultItalic;
		this->rb_color = rb_obj_clone(rb_defaultColor);
		RB_VAR2CPP(this->rb_color, Color, color);
		this->color = color;
	}

	void Font::mark()
	{
		RubyObject::mark();
		RB_GC_MARK(color);
	}

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	void Font::generate(Font* font)
	{
		hstr fontName = font->_getAtresTtfName();
		if (!atres::renderer->hasFont(fontName) && !_missingFonts.contains(fontName))
		{
			float baseSize = (float)rgss::parameters.try_get_by_key(CFG_FONT_BASE_SIZE, "50");
			atresttf::FontResourceTtf* fontResource = new atresttf::FontResourceTtf("", fontName, baseSize, 1.0f);
			if (fontResource->isLoaded())
			{
				atres::renderer->registerFontResource(fontResource);
			}
			else // font file was not found
			{
				_missingFonts += fontName;
				delete fontResource;
			}
		}
	}

	hstr Font::getAtresFontName()
	{
		Font::generate(this);
		hstr result = this->_getAtresTtfName();
		if (!atres::renderer->hasFont(result))
		{
			return "";
		}
		float fontHeight = atres::renderer->getFontHeight(result);
		if (this->size != fontHeight)
		{
			result += hsprintf(":%f", this->size / fontHeight);
		}
		return result;
	}

	hstr Font::_getAtresTtfName()
	{
		hstr result = this->name;
		if (this->bold)
		{
			result += " Bold";
		}
		if (this->italic)
		{
			result += " Italic";
		}
		return result;
	}

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Font::init()
	{
		defaultName = "Arial";
		defaultSize = 22;
		defaultBold = false;
		defaultItalic = false;
		rb_defaultColor = Qnil;
		defaultColor = NULL;
		rb_gc_register_address(&rb_defaultColor);
		VALUE argv[3] = {INT2FIX(255), INT2FIX(255), INT2FIX(255)};
		Font::rb_setDefaultColor(rb_cFont, Color::create(3, argv));
	}

	void Font::destroy()
	{
		rb_defaultColor = Qnil;
		defaultColor = NULL;
		rb_gc_unregister_address(&rb_defaultColor);
	}

	void Font::createRubyInterface()
	{
		rb_cFont = rb_define_class("Font", rb_cObject);
		rb_define_alloc_func(rb_cFont, &Font::rb_new);
		// initialize
		rb_define_method(rb_cFont, "initialize", RUBY_METHOD_FUNC(&Font::rb_initialize), -1);
		rb_define_method(rb_cFont, "initialize_copy", RUBY_METHOD_FUNC(&Font::rb_initialize_copy), 1);
		rb_define_method(rb_cFont, "_arc_dump", RUBY_METHOD_FUNC(&Font::rb_arcDump), 0);
		// getters and setters
		rb_define_method(rb_cFont, "name", RUBY_METHOD_FUNC(&Font::rb_getName), 0);
		rb_define_method(rb_cFont, "name=", RUBY_METHOD_FUNC(&Font::rb_setName), 1);
		rb_define_method(rb_cFont, "size", RUBY_METHOD_FUNC(&Font::rb_getSize), 0);
		rb_define_method(rb_cFont, "size=", RUBY_METHOD_FUNC(&Font::rb_setSize), 1);
		rb_define_method(rb_cFont, "bold", RUBY_METHOD_FUNC(&Font::rb_getBold), 0);
		rb_define_method(rb_cFont, "bold=", RUBY_METHOD_FUNC(&Font::rb_setBold), 1);
		rb_define_method(rb_cFont, "italic", RUBY_METHOD_FUNC(&Font::rb_getItalic), 0);
		rb_define_method(rb_cFont, "italic=", RUBY_METHOD_FUNC(&Font::rb_setItalic), 1);
		rb_define_method(rb_cFont, "color", RUBY_METHOD_FUNC(&Font::rb_getColor), 0);
		rb_define_method(rb_cFont, "color=", RUBY_METHOD_FUNC(&Font::rb_setColor), 1);
		// singleton getters and setters
		rb_define_singleton_method(rb_cFont, "default_name", RUBY_METHOD_FUNC(&Font::rb_getDefaultName), 0);
		rb_define_singleton_method(rb_cFont, "default_name=", RUBY_METHOD_FUNC(&Font::rb_setDefaultName), 1);
		rb_define_singleton_method(rb_cFont, "default_size", RUBY_METHOD_FUNC(&Font::rb_getDefaultSize), 0);
		rb_define_singleton_method(rb_cFont, "default_size=", RUBY_METHOD_FUNC(&Font::rb_setDefaultSize), 1);
		rb_define_singleton_method(rb_cFont, "default_bold", RUBY_METHOD_FUNC(&Font::rb_getDefaultBold), 0);
		rb_define_singleton_method(rb_cFont, "default_bold=", RUBY_METHOD_FUNC(&Font::rb_setDefaultBold), 1);
		rb_define_singleton_method(rb_cFont, "default_italic", RUBY_METHOD_FUNC(&Font::rb_getDefaultItalic), 0);
		rb_define_singleton_method(rb_cFont, "default_italic=", RUBY_METHOD_FUNC(&Font::rb_setDefaultItalic), 1);
		rb_define_singleton_method(rb_cFont, "default_color", RUBY_METHOD_FUNC(&Font::rb_getDefaultColor), 0);
		rb_define_singleton_method(rb_cFont, "default_color=", RUBY_METHOD_FUNC(&Font::rb_setDefaultColor), 1);
	}

	VALUE Font::rb_new(VALUE classe)
	{
		Font* font;
		return RB_OBJECT_NEW(classe, Font, font, &Font::gc_mark, &Font::gc_free);
	}

	VALUE Font::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		RB_SELF2CPP(Font, font);
		font->initialize(argc, argv);
		return self;
	}

	VALUE Font::rb_initialize_copy(VALUE self, VALUE original)
	{
		RB_SELF2CPP(Font, font);
		RB_VAR2CPP(original, Font, other);
		font->name = other->name;
		font->size = other->size;
		font->bold = other->bold;
		font->italic = other->italic;
		Font::rb_setColor(self, rb_obj_clone(other->rb_color));
		return self;
	}

	VALUE Font::create(int argc, VALUE* argv)
	{
		VALUE object = Font::rb_new(rb_cFont);
		object = Font::rb_initialize(argc, argv, object);
		return object;
	}

	/****************************************************************************************
	 * Ruby Getters/Setters
	 ****************************************************************************************/

	VALUE Font::rb_getName(VALUE self)
	{
		RB_SELF2CPP(Font, font);
		return rb_str_new2(font->name.c_str());
	}

	VALUE Font::rb_setName(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Font, font);
		RB_CHECK_TYPE(value, rb_cString);
		font->name = StringValueCStr(value);
		return value;
	}

	VALUE Font::rb_getSize(VALUE self)
	{
		RB_SELF2CPP(Font, font);
		return INT2FIX(font->size);
	}

	VALUE Font::rb_setSize(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Font, font);
		font->size = NUM2INT(value);
		return value;
	}

	VALUE Font::rb_getBold(VALUE self)
	{
		RB_SELF2CPP(Font, font);
		return (font->bold ? Qtrue : Qfalse);
	}

	VALUE Font::rb_setBold(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Font, font);
		font->bold = (bool)RTEST(value);
		return value;
	}

	VALUE Font::rb_getItalic(VALUE self)
	{
		RB_SELF2CPP(Font, font);
		return (font->italic ? Qtrue : Qfalse);
	}

	VALUE Font::rb_setItalic(VALUE self, VALUE value)
	{
		RB_SELF2CPP(Font, font);
		font->italic = (bool)RTEST(value);
		return value;
	}

	VALUE Font::rb_getColor(VALUE self)
	{
		RB_SELF2CPP(Font, font);
		return font->rb_color;
	}

	VALUE Font::rb_setColor(VALUE self, VALUE value)
	{
		RB_GENERATE_SETTER(Font, font, Color, color);
		return value;
	}

	/****************************************************************************************
	 * Ruby Static Getters/Setters
	 ****************************************************************************************/

	VALUE Font::rb_getDefaultName(VALUE classe)
	{
		return rb_str_new2(defaultName.c_str());
	}

	VALUE Font::rb_setDefaultName(VALUE classe, VALUE value)
	{
		RB_CHECK_TYPE(value, rb_cString);
		defaultName = StringValueCStr(value);
		return value;
	}

	VALUE Font::rb_getDefaultSize(VALUE classe)
	{
		return INT2FIX(defaultSize);
	}

	VALUE Font::rb_setDefaultSize(VALUE classe, VALUE value)
	{
		defaultSize = NUM2INT(value);
		return value;
	}

	VALUE Font::rb_getDefaultBold(VALUE classe)
	{
		return (defaultBold ? Qtrue : Qfalse);
	}

	VALUE Font::rb_setDefaultBold(VALUE classe, VALUE value)
	{
		defaultBold = (bool)RTEST(value);
		return value;
	}

	VALUE Font::rb_getDefaultItalic(VALUE classe)
	{
		return (defaultItalic ? Qtrue : Qfalse);
	}

	VALUE Font::rb_setDefaultItalic(VALUE classe, VALUE value)
	{
		defaultItalic = (bool)RTEST(value);
		return value;
	}
	
	VALUE Font::rb_getDefaultColor(VALUE classe)
	{
		return rb_defaultColor;
	}

	VALUE Font::rb_setDefaultColor(VALUE classe, VALUE value)
	{
		rb_defaultColor = value;
		if (!NIL_P(value))
		{
			RB_CHECK_TYPE(value, rb_cColor);
			RB_VAR2CPP(value, Color, color);
			defaultColor = color;
		}
		else
		{
			defaultColor = NULL;
		}
		return value;
	}
	
	VALUE Font::rb_arcDump(VALUE self)
	{
		rb_raise(rb_eTypeError, "can't arc-dump Font");
		return Qnil;
	}

}
