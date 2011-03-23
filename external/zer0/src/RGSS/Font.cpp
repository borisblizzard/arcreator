#include "RGSS/Color.h"
#include "RGSS/Font.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		//constructors
		Font::Font()
		{
			/*
			this->name = this->default_name;
			this->size = this->default_size;
			this->bold = this->default_bold;
			this->italic = this->default_italic;
			this->color = this->default_color;
			*/
		}

		Font::Font(chstr name)
		{
			/*
			this->name = name;
			this->size = this->default_size;
			this->bold = this->default_bold;
			this->italic = this->default_italic;
			this->color = this->default_color;
			*/
		}

		Font::Font(chstr name, int size)
		{
			/*
			this->name = name;
			this->size = size;
			this->bold = this->default_bold;
			this->italic = this->default_italic;
			this->color = this->default_color;
			*/
		}

		Font::~Font()
		{
		}

		void Font::createRubyInterface()
		{
			rb_cFont = rb_define_class("Font", rb_cObject);
			rb_define_alloc_func(rb_cFont, &Font::rb_new);
			// initialize
			rb_define_method(rb_cFont, "initialize", RUBY_METHOD_FUNC(&Font::rb_initialize), -1);
			// getters and setters
			rb_define_method(rb_cFont, "bold", RUBY_METHOD_FUNC(&Font::rb_getBold), 0);
			rb_define_method(rb_cFont, "bold=", RUBY_METHOD_FUNC(&Font::rb_setBold), 1);
			rb_define_method(rb_cFont, "color", RUBY_METHOD_FUNC(&Font::rb_getColor), 0);
			rb_define_method(rb_cFont, "color=", RUBY_METHOD_FUNC(&Font::rb_setColor), 1);
			rb_define_method(rb_cFont, "italic", RUBY_METHOD_FUNC(&Font::rb_getItalic), 0);
			rb_define_method(rb_cFont, "italic=", RUBY_METHOD_FUNC(&Font::rb_setItalic), 1);
			rb_define_method(rb_cFont, "name", RUBY_METHOD_FUNC(&Font::rb_getName), 0);
			rb_define_method(rb_cFont, "name=", RUBY_METHOD_FUNC(&Font::rb_setName), 1);
			rb_define_method(rb_cFont, "size", RUBY_METHOD_FUNC(&Font::rb_getSize), 0);
			rb_define_method(rb_cFont, "size=", RUBY_METHOD_FUNC(&Font::rb_setSize), 1);
		}

		VALUE Font::rb_new(VALUE classe)
		{
			return classe;
		}

		VALUE Font::rb_initialize(int argc, VALUE* argv, VALUE self)
		{
			return self;
		}

		VALUE Font::rb_inspect(VALUE self)
		{
			return self;
		}

		VALUE Font::rb_getBold(VALUE self)
		{
			return self;
		}

		VALUE Font::rb_setBold(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Font::rb_getColor(VALUE self)
		{
			return self;
		}

		VALUE Font::rb_setColor(VALUE self, VALUE* value)
		{
			return self;
		}

		VALUE Font::rb_getItalic(VALUE self)
		{
			return self;
		}

		VALUE Font::rb_setItalic(VALUE self, VALUE value)
		{
			return self;
		}

		VALUE Font::rb_getName(VALUE self)
		{
			return self;
		}

		VALUE Font::rb_setName(VALUE self, VALUE value)
		{
			return self;
		}

	    VALUE Font::rb_getSize(VALUE self)
		{
			return self;
		}

		VALUE Font::rb_setSize(VALUE self, VALUE value)
		{
			return self;
		}

		/*
		hstr Font::default_name = "Arial";
		int Font::default_size = 22;
		bool Font::default_bold = false;
		bool Font::default_italic = false;
		Color Font::default_color = Color(255.0f, 255.0f, 255.0f);
		*/

	}
}
