#ifndef ZER0_RGSS_BITMAP_H
#define ZER0_RGSS_BITMAP_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "RGSS/Color.h"
#include "RGSS/Font.h"
#include "RGSS/Rect.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		static VALUE rb_cBitmap;

		class zer0Export Bitmap
		{
		public:

			// Constructors/Destructor
			/// @brief Constructor from filename
			/// @param[in] filename Filename where the bitmap can be found
			Bitmap(chstr filename);
			/// @brief Constructor From width and height
			/// @param[in] width The width of the new bitmap
			/// @param[in] height The height of the new bitmap
			Bitmap(int width, int height);
			/// @brief Basic Deconstructor
			~Bitmap();

			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Ruby allocation of an instance.
			static VALUE rb_new(VALUE classe);
			/// @brief Sets the bitmap dimensions
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			/// @note Arguments are "[filename]" or "[width, height]".
			static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
			/// @brief Gets a string representation of the instance.
			/// @return String representation of the instance.
			static VALUE rb_inspect(VALUE self);
			/// @brief Marks referenced values of bitmap for garbage collection.
			/// @param[in] bitmap Bitmap to mark.
			static void gc_mark(Bitmap* bitmap);
			/// @brief Frees the memory for the bitmap.
			static VALUE rb_dispose(VALUE self);

			// public getters/setters
			/// @brief Gets the height of the bitmap.
			static VALUE rb_getHeight(VALUE self);
			/// @brief Gets the width of the bitmap.
			static VALUE rb_getWidth(VALUE self);
			/// @brief Gets the font of the bitmap.
			static VALUE rb_getFont(VALUE self);
			/// @brief Sets the font used for the bitmap.
			/// param[in] value The font to set for the bitmap.
			static VALUE rb_setFont(VALUE self, VALUE value);
			/// @brief Gets the bitmap's rectangle.
			static VALUE rb_getRect(VALUE self);

			// public methods
			/// @brief Checks whether bitmap is disposed.
			/// @return bool True if bitmap has been freed.
			static VALUE rb_isDisposed(VALUE self);
			/// @brief Blits src_rect From source bitmap to this one.
			/// @param[in] x The x coordinate to place the bitmap.
			/// @param[in] y The y coordinate to place the bitmap.
			/// @param[in] src_bitmap The Bitmap to transfer from.
			/// @param[in] src_rect The rect to transfer from src_bitmap.
			/// @param[in] opacity The alpha blend of the blit operation.
			static VALUE rb_blckTran(VALUE self, VALUE x, VALUE y, VALUE src_bitmap, VALUE src_rect, VALUE opacity);
			/// @brief Clears the entire bitmap
			static VALUE rb_clear(VALUE self);
			/// @brief Sets the color to the specified value.
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			/// @note Arguments are "[x, y, width, height, string, align]" or "[rect, string, align]".
			static VALUE rb_drawText(int argc, VALUE* argv, VALUE self);
			/// @brief Sets the color to the specified value.
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			/// @note Arguments are "[x, y, width, height, color]" or "[rect, color]".
			static VALUE rb_fillRect(int argc, VALUE* argv, VALUE self);
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
			/// @brief Changes the bitmap's hue within 360 degrees of displacement.
			/// @param[in] hue Degrees to rotate the hue
			static VALUE rb_changeHue(VALUE self, VALUE hue);
			/// @brief Blits src_rect from source bitmap to this one scaling the bitmap to fit inside dest_rect
			/// @param[in] dest_rect The rect to fit the blit to
			/// @param[in] src_bitmap The Bitmap to transfer from
			/// @param[in] src_rect The rect to transfer from src_bitmap
			/// @param[in] opacity The alpha blend of the blit operation
			static VALUE rb_stretchBlt(VALUE self, VALUE dest_rect, VALUE src_bitmap, VALUE src_rect, VALUE opacity); 
			/// @brief Gets the rect needed to draw a string of text.
			/// @return value The rect needed to draw a string of text.
			static VALUE rb_textSize(VALUE self, VALUE value);

		protected:
			// Protected instance variables
			/// @brief The Font used to draw text.
			Font font;
			/// @brief The bitmap's rectangle.
			Rect rect;
		};
	}
}
#endif
