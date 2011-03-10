#include "RGSS/Font.h"

namespace zer0
{
	namespace RGSS
	{
	
		hstr Font::default_name = "MS PGothic";
		int Font::default_size = 22;
		bool Font::default_bold = false;
		bool Font::default_italic = false;
		Color Font::default_color = Color(255.0f, 255.0f, 255.0f, 255.0f);

		//constructers
		Font::Font()
		{
			this->name = this->default_name;
			this->size = this->default_size;
			this->bold = this->default_bold;
			this->italic = this->default_italic;
			this->color = this->default_color;
		}
		Font::Font(hstr name)
		{
			this->name = name;
			this->size = this->default_size;
			this->bold = this->default_bold;
			this->italic = this->default_italic;
			this->color = this->default_color;
		}
		Font::Font(hstr name, int size)
		{
			this->name = name;
			this->size = size;
			this->bold = this->default_bold;
			this->italic = this->default_italic;
			this->color = this->default_color;
		}

		// deconstructer
		Font::~Font()
		{
		}

		//getters and setters
		hstr Font::get_name()
		{
			return this->name;
		}
		void Font::set_name(hstr name)
		{
			this->name = name;
		}
		int Font::get_size()
		{
			return this->size;
		}
		void Font::set_size(int size)
		{
			this->size = size;
		}
		bool Font::get_bold()
		{
			return this->bold;
		}
		void Font::set_bold(bool state)
		{
			this->bold = bold;
		}
		bool Font::get_italic()
		{
			return this->italic;
		}
		void Font::set_italic(bool state)
		{
			this->italic = italic;
		}
		Color Font::get_color()
		{
			return this->color;
		}
		void Font::set_color(Color &color)
		{
			this->color = color;
		}
	
	}
}
