#include "RGSS/Color.h"
#include "RGSS/Font.h"

namespace zer0
{
	namespace RGSS
	{
		/*
		hstr Font::default_name = "Arial";
		int Font::default_size = 22;
		bool Font::default_bold = false;
		bool Font::default_italic = false;
		Color Font::default_color = Color(255.0f, 255.0f, 255.0f);
		*/

		//constructers
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

		// deconstructer
		Font::~Font()
		{
		}

	}
}
