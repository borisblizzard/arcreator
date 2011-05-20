#include <ruby.h>

#include "CodeSnippets.h"
#include "Color.h"
#include "Font.h"

namespace rgss
{
	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	VALUE rb_cFont;

	hstr Font::defaultName;
	int Font::defaultSize;
	bool Font::defaultBold;
	bool Font::defaultItalic;
	Color* Font::defaultColor;
	VALUE Font::rb_defaultColor;

	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Font::init()
	{
		defaultName = "Arial";
		defaultSize = 22;
		defaultBold = false;
		defaultItalic = false;
		VALUE argv[3] = {INT2FIX(255), INT2FIX(255), INT2FIX(255)};
		Font::rb_setDefaultColor(rb_cFont, Color::create(3, argv));
	}

	void Font::createRubyInterface()
	{
		rb_cFont = rb_define_class("Font", rb_cObject);
		rb_define_alloc_func(rb_cFont, &Font::rb_new);
		// initialize
		rb_define_method(rb_cFont, "initialize", RUBY_METHOD_FUNC(&Font::rb_initialize), -1);
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

	void Font::gc_mark(Font* font)
	{
		if (!NIL_P(font->rb_color))
		{
			rb_gc_mark(font->rb_color);
		}
	}

	void Font::gc_free(Font* font)
	{
		font->rb_color = Qnil;
		font->color = NULL;
	}

	VALUE Font::rb_new(VALUE classe)
	{
		Font* font;
		return Data_Make_Struct(classe, Font, Font::gc_mark, Font::gc_free, font);
	}

	VALUE Font::rb_initialize(int argc, VALUE* argv, VALUE self)
	{
		VALUE name, size;
		rb_scan_args(argc, argv, "11", &name, &size);
		RB_SELF2CPP(Font, font);
		font->name = defaultName;
		font->size = defaultSize;
		font->bold = defaultBold;
		font->italic = defaultItalic;
		VALUE argv2[4] = {INT2FIX(defaultColor->red), INT2FIX(defaultColor->green),
			INT2FIX(defaultColor->blue), INT2FIX(defaultColor->alpha)};
		Font::rb_setColor(self, Color::create(4, argv2));
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
		font->name = StringValuePtr(value);
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
		font->bold = RTEST(value);
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
		font->italic = RTEST(value);
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
		defaultName = StringValuePtr(value);
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
		defaultBold = RTEST(value);
		return value;
	}

	VALUE Font::rb_getDefaultItalic(VALUE classe)
	{
		return (defaultItalic ? Qtrue : Qfalse);
	}

	VALUE Font::rb_setDefaultItalic(VALUE classe, VALUE value)
	{
		defaultItalic = RTEST(value);
		return value;
	}
	
	VALUE Font::rb_getDefaultColor(VALUE classe)
	{
		return rb_defaultColor;
	}

	VALUE Font::rb_setDefaultColor(VALUE classe, VALUE value)
	{
		RB_VAR2CPP(value, Color, color);
		defaultColor = color;
		return value;
	}
	
}
