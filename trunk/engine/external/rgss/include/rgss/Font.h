#ifndef RGSS_FONT_H
#define RGSS_FONT_H

#include <ruby.h>

#include <hltypes/harray.h>
#include <hltypes/hstring.h>

#include "rgssExport.h"

namespace rgss
{
	class Color;

	extern VALUE rb_cFont;

	/// @brief Emulates RGSS's Font class.
	class rgssExport Font
	{
	public:
		/// @brief Gets the name.
		/// @return The name.
		hstr getName() { return this->name; }
		/// @brief Gets the size.
		/// @return The size.
		int getSize() { return this->size; }
		/// @brief Gets the bold flag.
		/// @return The bold flag.
		bool getBold() { return this->bold; }
		/// @brief Gets the bold flag.
		/// @return The bold flag.
		bool getItalic() { return this->italic; }
		/// @brief Gets the color.
		/// @return The color.
		Color* getColor() { return this->color; }

		/// @brief Generates a Font defintion for the current render.
		static void generate(chstr fontName);

		/// @brief Default Font name.
		static hstr defaultName;
		/// @brief Default Font size.
		static int defaultSize;
		/// @brief Default Bold flag.
		static bool defaultBold;
		/// @brief Default Italic flag.
		static bool defaultItalic;
		/// @brief Default Font Color.
		static Color* defaultColor;
		/// @brief Default Font Color.
		static VALUE rb_defaultColor;

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Marks referenced values of font for garbage collection.
		/// @param[in] font Pointer to the Font to mark.
		static void gc_mark(Font* font);
		/// @brief Frees allocated memory.
		/// @param[in] font Pointer to the Font to free.
		static void gc_free(Font* font);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Sets the font parameters.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Used for clone and dup.
		/// @param[in] original The original.
		static VALUE rb_initialize_copy(VALUE self, VALUE original);
		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		static VALUE create(int argc, VALUE* argv);

		/// @brief Gets the font's name.
		/// @return Name of the font.
		static VALUE rb_getName(VALUE self);
		/// @brief Sets the font's name.
		/// @param[in] value Name of the font.
		static VALUE rb_setName(VALUE self, VALUE value);
		/// @brief Gets the font's size.
		/// @return Value of the font's size.
		static VALUE rb_getSize(VALUE self);
		/// @brief Sets the font's size.
		/// @param[in] value Value of the font's size.
		static VALUE rb_setSize(VALUE self, VALUE value);
		/// @brief Gets the font's bold value.
		/// @return bool Value of bold parameter.
		static VALUE rb_getBold(VALUE self);
		/// @brief Sets the font's bold value.
		/// @param[in] bool Value of bold parameter.
		static VALUE rb_setBold(VALUE self, VALUE value);
		/// @brief Gets the font's italic value.
		/// @return bool Value of italic parameter.
		static VALUE rb_getItalic(VALUE self);
		/// @brief Sets the font's italic value.
		/// @param[in] bool Value of italic parameter.
		static VALUE rb_setItalic(VALUE self, VALUE value);
		/// @brief Gets the font's color.
		/// @return The Color value used for the font.
		static VALUE rb_getColor(VALUE self);
		/// @brief Sets the font's color.
		/// @param[in] value The Color used for the font.
		static VALUE rb_setColor(VALUE self, VALUE value);

		/// @brief Gets the font's name.
		/// @return Default name of the font.
		static VALUE rb_getDefaultName(VALUE classe);
		/// @brief Sets the font's name.
		/// @param[in] value Default name of the font.
		static VALUE rb_setDefaultName(VALUE classe, VALUE value);
		/// @brief Gets the font's size.
		/// @return Default value of the font's size.
		static VALUE rb_getDefaultSize(VALUE classe);
		/// @brief Sets the font's size.
		/// @param[in] value Default value of the font's size.
		static VALUE rb_setDefaultSize(VALUE classe, VALUE value);
		/// @brief Gets the font's bold value.
		/// @return Default value of bold parameter.
		static VALUE rb_getDefaultBold(VALUE classe);
		/// @brief Sets the font's bold value.
		/// @param[in] value Default value of bold parameter.
		static VALUE rb_setDefaultBold(VALUE classe, VALUE value);
		/// @brief Gets the font's italic value.
		/// @return bool Default value of italic parameter.
		static VALUE rb_getDefaultItalic(VALUE classe);
		/// @brief Sets the font's italic value.
		/// @param[in] value Default value of italic parameter.
		static VALUE rb_setDefaultItalic(VALUE classe, VALUE value);
		/// @brief Gets the font's color.
		/// @return Default Color used for the font.
		static VALUE rb_getDefaultColor(VALUE classe);
		/// @brief Sets the font's color.
		/// @param[in] value Default Color used for the font.
		static VALUE rb_setDefaultColor(VALUE classe, VALUE value);

		/// @brief Mimics a dumping method to prevent dumping of this class.
		static VALUE rb_arcDump(VALUE self);

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
		Color* color;
		/// @brief Ruby object of font Color.
		VALUE rb_color;

		/// @brief Keeps track of missing fonts so they aren't checked multiple times.
		static harray<hstr> _missingFonts;

	};

}
#endif
