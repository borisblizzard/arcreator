#ifndef ZER0_RGSS_FONT_H
#define ZER0_RGSS_FONT_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		static VALUE rb_cFont;

		class Color;

		/// @brief Emulates RGSS's Font class.
		class zer0Export Font
		{
		public:
			/// @todo Dummy for now, needs to be removed later.
			Font() { }
			/// @todo Dummy for now, needs to be removed later.
			~Font() { }
			/*
			/// @brief Empty constructor.
			Font();
			/// @brief Basic constructor.
			/// @param[in] name Font name.
			Font(chstr name);
			/// @brief Basic constructor.
			/// @param[in] name Font name.
			/// @param[in] size Font size.
			Font(chstr name, int size);
			/// @brief Destructor
			~Font();
			*/

			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Wraps into Ruby cobject.
			/// @param[in] bitmap The bitmap to convert.
			VALUE wrap();
			/// @brief Ruby allocation of an instance.
			static VALUE rb_new(VALUE classe);
			/// @brief Sets the font parameters.
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
			/// @brief Gets a string representation of the instance.
			/// @return String representation of the instance.
			static VALUE rb_inspect(VALUE self);

			/// @brief Gets the font's bold value.
			/// @return Bool value of bold parameter.
			static VALUE rb_getBold(VALUE self);
			/// @brief Sets the font's bold value.
			/// @param[in] Bool value of bold parameter.
			static VALUE rb_setBold(VALUE self, VALUE value);
			/// @brief Gets the font's color.
			/// @return Color used for the font.
			static VALUE rb_getColor(VALUE self);
			/// @brief Sets the font's color.
			/// @param[in] Color used for the font.
			static VALUE rb_setColor(VALUE self, VALUE* value);
			/// @brief Gets the font's italic value.
			/// @return Bool value of italic parameter.
			static VALUE rb_getItalic(VALUE self);
			/// @brief Sets the font's italic value.
			/// @param[in] Bool value of italic parameter.
			static VALUE rb_setItalic(VALUE self, VALUE value);
			/// @brief Gets the font's name.
			/// @return Hstr name of the font.
			static VALUE rb_getName(VALUE self);
			/// @brief Sets the font's name.
			/// @param[in] Hstr name of the font.
			static VALUE rb_setName(VALUE self, VALUE value);
			/// @brief Gets the font's size.
			/// @return Integer value of the font's size.
			static VALUE rb_getSize(VALUE self);
			/// @brief Sets the font's size.
			/// @param[in] Integer value of the font's size.
			static VALUE rb_setSize(VALUE self, VALUE value);

		protected:
			/// @brief Font name.
			hstr name;
			/// @brief Font size.
			int size;
			/// @brief Bold flag.
			bool bold;
			/// @brief Italic flag.
			bool italic;
			/// @brief Font Color.
			Color color;
		};
	}
}
#endif
