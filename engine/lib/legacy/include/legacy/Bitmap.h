#ifndef LEGACY_BITMAP_H
#define LEGACY_BITMAP_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "Color.h"
#include "Font.h"
#include "Rect.h"
#include "legacyExport.h"
#include "RubyObject.h"

namespace april
{
	class Texture;
}

namespace legacy
{
	class Tilemap;
	class Window;

	extern VALUE rb_cBitmap;

	class legacyExport Bitmap : public RubyObject
	{
	public:
		friend class Tilemap;
		friend class Window;

		/// @brief Constructor.
		Bitmap();
		/// @brief Constructor.
		/// @param[in] width The width.
		/// @param[in] height The height.
		Bitmap(int width, int height);
		/// @brief Constructor.
		/// @param[in] fullFilename The full filename.
		Bitmap(chstr fullFilename);
		/// @brief Destructor.
		~Bitmap();
		/// @brief Initializes the basic object.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		void initialize(int argc, VALUE* argv);
		/// @brief Disposes this object.
		void dispose();
		/// @brief Ruby garbage collector marking.
		void mark();

		/// @brief Gets the april::Texture.
		/// @return april::Texture used to draw.
		april::Texture* getTexture() { return this->texture; }
		/// @brief Sets the april::Texture.
		/// @param[in] value april::Texture used to draw.
		void setTexture(april::Texture* value) { this->texture = value; }
		/// @brief Gets the width.
		/// @return The width.
		int getWidth();
		/// @brief Gets the height.
		/// @return The height.
		int getHeight();
		/// @brief Gets the disposed flag.
		/// @return The disposed flag.
		bool isDisposed() { return this->disposed; }

		/// @brief Clears the entire bitmap.
		void clear();

		/// @brief Gets the full filename and checks whether it exists.
		/// @param[in] filename The filename, possibly without extension.
		/// @return The full filename.
		static hstr getFullFilename(chstr filename);

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Sets the bitmap dimensions.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[filename]" or "[width, height]".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Used for clone and dup.
		/// @param[in] original The original.
		static VALUE rb_initialize_copy(VALUE self, VALUE original);
		/// @brief Disposes the object.
		static VALUE rb_dispose(VALUE self);

		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[viewport]"
		static VALUE create(int argc, VALUE* argv);

		/// @brief Gets the height of the bitmap.
		/// @return Height of the bitmap.
		static VALUE rb_getHeight(VALUE self);
		/// @brief Gets the width of the bitmap.
		/// @return Width of the bitmap.
		static VALUE rb_getWidth(VALUE self);
		/// @brief Gets the size rectangle.
		/// @return The size rectangle.
		static VALUE rb_getRect(VALUE self);
		/// @brief Gets the font of the bitmap.
		/// @return Font of the bitmap.
		static VALUE rb_getFont(VALUE self);
		/// @brief Sets the font used for the bitmap.
		/// param[in] value The font to set for the bitmap.
		static VALUE rb_setFont(VALUE self, VALUE value);
		/// @brief Checks whether bitmap is disposed.
		/// @return bool True if bitmap has been freed.
		static VALUE rb_isDisposed(VALUE self);

		/// @brief Get the color of a pixel at (x, y).
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @return Color The color of the pixel at (x, y).
		static VALUE rb_getPixel(VALUE self, VALUE x, VALUE y);
		/// @brief Sets the color of a pixel at (x, y).
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @param[in] color The color to set the pixel to.
		static VALUE rb_setPixel(VALUE self, VALUE x, VALUE y, VALUE color);
		/// @brief Sets the color to the specified value.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[x, y, width, height, color]" or "[rect, color]".
		static VALUE rb_fillRect(int argc, VALUE* argv, VALUE self);
		/// @brief Clears the entire bitmap.
		static VALUE rb_clear(VALUE self);
		/// @brief Blits src_rect from source bitmap to this one.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "x, y, src_bitmap, src_rect[, opacity]"
		static VALUE rb_blt(int argc, VALUE* argv, VALUE self);
		/// @brief Stretch-blits src_rect from source bitmap to this dest_rect in this one.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "dest_rect, src_bitmap, src_rect[, opacity]"
		static VALUE rb_stretchBlt(int argc, VALUE* argv, VALUE self);
		/// @brief Sets the color to the specified value.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[x, y, width, height, string, align]" or "[rect, string, align]".
		static VALUE rb_drawText(int argc, VALUE* argv, VALUE self);
		/// @brief Changes the bitmap's hue within 360 degrees of displacement.
		/// @param[in] hue Degrees to rotate the hue
		static VALUE rb_changeHue(VALUE self, VALUE hue);
		/// @brief Gets the rect needed to draw a string of text.
		/// @return The rectangle needed to draw a string of text.
		static VALUE rb_textSize(VALUE self, VALUE string);

		/// @brief Mimics a dumping method to prevent dumping of this class.
		static VALUE rb_arcDump(VALUE self);

	protected:
		/// @brief Disposed flag.
		bool disposed;
		/// @brief Underlying rendering system texture.
		april::Texture* texture;
		/// @brief The Font used to draw text.
		Font* font;
		/// @brief Ruby object of the Font used to draw text.
		VALUE rb_font;
		/// @brief Used for error prints.
		hstr typeName;

		/// @brief Draws text onto this bitmap;
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @param[in] w Destination width.
		/// @param[in] h Destination height.
		/// @param[in] text Text to draw.
		/// @param[in] align Alignment.
		/// @note The alignments are: 0 = left; 1 = center; 1 = right
		void _drawText(int x, int y, int w, int h, chstr text, int align);
		/// @brief Loads a texture in the right bpp.
		/// @param[in] filename Filename of the texture to load.
		void _loadTexture(chstr filename);
		/// @brief Blits rect from source bitmap to this one.
		/// @param[in] sx Source X coordinate.
		/// @param[in] sy Source Y coordinate.
		/// @param[in] sw Source width.
		/// @param[in] sh Source height.
		/// @param[in] dx Destination X coordinate.
		/// @param[in] dy Destination Y coordinate.
		/// @param[in] source Source Texture.
		void _renderToTexture(int sx, int sy, int sw, int sh, int dx, int dy, april::Texture* source, unsigned char alpha = 255);
		/// @brief Blits rect from source bitmap to this one.
		/// @param[in] sx Source X coordinate.
		/// @param[in] sy Source Y coordinate.
		/// @param[in] sw Source width.
		/// @param[in] sh Source height.
		/// @param[in] dx Destination X coordinate.
		/// @param[in] dy Destination Y coordinate.
		/// @param[in] dw Destination width.
		/// @param[in] dh Destination height.
		/// @param[in] source Source Texture.
		void _renderToTexture(int sx, int sy, int sw, int sh, int dx, int dy, int dw, int dh, april::Texture* source, unsigned char alpha = 255);

	};

}
#endif

