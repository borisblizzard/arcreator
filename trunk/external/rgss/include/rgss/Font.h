#ifndef RGSS_FONT_H
#define RGSS_FONT_H

#include <ruby.h>

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
		/// @brief Default constructor.
		Font();
		/// @brief Destructor.
		~Font();

		/// @brief Default Font name.
		static hstr defaultName;
		/// @brief Default Font size.
		static int defaultSize;
		/// @brief Default Bold flag.
		static bool defaultBold;
		/// @brief Default Italic flag.
		static bool defaultItalic;
		/// @brief Default Font Color.
		/// @todo This will cause memory problems if changed via Ruby, needs to be refactored.
		static Color* defaultColor;
		/// @brief Default Font Color.
		static VALUE rb_defaultColor;


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

		/// @brief Intializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Wraps this instance into a Ruby cobject.
		/// @return Ruby object.
		VALUE wrap();
		/// @brief Marks referenced values of font for garbage collection.
		/// @param[in] Font Font to mark.
		static void gc_mark(Font* font);
		/// @brief Frees allocated memory.
		/// @param[in] font Font to free.
		static void gc_free(Font* font);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Sets the font parameters.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		static VALUE create(int argc, VALUE* argv);

		/// @brief Gets the font's name.
		/// @return Name of the font.
		static VALUE rb_getName(VALUE self);
		/// @brief Sets the font's name.
		/// @param[in] Name of the font.
		static VALUE rb_setName(VALUE self, VALUE value);
		/// @brief Gets the font's size.
		/// @return Value of the font's size.
		static VALUE rb_getSize(VALUE self);
		/// @brief Sets the font's size.
		/// @param[in] Value of the font's size.
		static VALUE rb_setSize(VALUE self, VALUE value);
		/// @brief Gets the font's bold value.
		/// @return Value of bold parameter.
		static VALUE rb_getBold(VALUE self);
		/// @brief Sets the font's bold value.
		/// @param[in] Value of bold parameter.
		static VALUE rb_setBold(VALUE self, VALUE value);
		/// @brief Gets the font's italic value.
		/// @return Value of italic parameter.
		static VALUE rb_getItalic(VALUE self);
		/// @brief Sets the font's italic value.
		/// @param[in] Value of italic parameter.
		static VALUE rb_setItalic(VALUE self, VALUE value);
		/// @brief Gets the font's color.
		/// @return Color used for the font.
		static VALUE rb_getColor(VALUE self);
		/// @brief Sets the font's color.
		/// @param[in] Color used for the font.
		static VALUE rb_setColor(VALUE self, VALUE value);

		/// @brief Gets the font's name.
		/// @return Default name of the font.
		static VALUE rb_getDefaultName(VALUE classe);
		/// @brief Sets the font's name.
		/// @param[in] Default name of the font.
		static VALUE rb_setDefaultName(VALUE classe, VALUE value);
		/// @brief Gets the font's size.
		/// @return Default value of the font's size.
		static VALUE rb_getDefaultSize(VALUE classe);
		/// @brief Sets the font's size.
		/// @param[in] Default value of the font's size.
		static VALUE rb_setDefaultSize(VALUE classe, VALUE value);
		/// @brief Gets the font's bold value.
		/// @return Default value of bold parameter.
		static VALUE rb_getDefaultBold(VALUE classe);
		/// @brief Sets the font's bold value.
		/// @param[in] Default value of bold parameter.
		static VALUE rb_setDefaultBold(VALUE classe, VALUE value);
		/// @brief Gets the font's italic value.
		/// @return Bool Default value of italic parameter.
		static VALUE rb_getDefaultItalic(VALUE classe);
		/// @brief Sets the font's italic value.
		/// @param[in] Bool Default value of italic parameter.
		static VALUE rb_setDefaultItalic(VALUE classe, VALUE value);
		/// @brief Gets the font's color.
		/// @return Default Color used for the font.
		static VALUE rb_getDefaultColor(VALUE classe);
		/// @brief Sets the font's color.
		/// @param[in] Default Color used for the font.
		static VALUE rb_setDefaultColor(VALUE classe, VALUE value);

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

	};

}
#endif
