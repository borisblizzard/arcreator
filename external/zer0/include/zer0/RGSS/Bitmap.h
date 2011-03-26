#ifndef ZER0_RGSS_BITMAP_H
#define ZER0_RGSS_BITMAP_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "RGSS/Color.h"
#include "RGSS/Font.h"
#include "RGSS/Rect.h"
#include "zer0Export.h"

namespace april
{
	class ImageSource;
	class Texture;
}

namespace zer0
{
	namespace RGSS
	{
		static VALUE rb_cBitmap;

		class zer0Export Bitmap
		{
		public:
			/// @todo Dummy, needs to be removed.
			Bitmap() { }
			/// @todo Dummy, needs to be removed.
			~Bitmap() { }

			/// @brief Gets the april::Texture.
			/// @return april::Texture used to draw.
			april::Texture* getTexture() { return this->texture; }
			/// @brief Gets the width.
			/// @return Width of april::Texture.
			int getWidth();
			/// @brief Gets the height.
			/// @return Height of april::Texture.
			int getHeight();
			/// @brief Updates the texture on the graphic card if necessary.
			void Bitmap::updateTexture();

			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Wraps this instance into a Ruby cobject.
			/// @return Ruby object.
			VALUE wrap();
			/// @brief Frees additional resources used by this instance.
			/// @param[in] bitmap Bitmap to free.
			static void gc_free(Bitmap* bitmap);
			/// @brief Ruby allocation of an instance.
			static VALUE rb_new(VALUE classe);
			/// @brief Sets the bitmap dimensions.
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			/// @note Arguments are "[filename]" or "[width, height]".
			static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
			/// @brief Used for clone and dup.
			/// @param[in] original The original Bitmap.
			static VALUE rb_initialize_copy(VALUE self, VALUE original);
			/// @brief Gets a string representation of the instance.
			/// @return String representation of the instance.
			static VALUE rb_inspect(VALUE self);
			/// @brief Disposes the object.
			static VALUE rb_dispose(VALUE self);

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

			/// @brief Checks whether bitmap is disposed.
			/// @return bool True if bitmap has been freed.
			static VALUE rb_isDisposed(VALUE self);
			/// @brief Blits src_rect from source bitmap to this one.
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			/// @note Arguments are "x, y, src_bitmap, src_rect[, opacity]"
			static VALUE rb_blt(int argc, VALUE* argv, VALUE self);
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
			/// @brief The Font used to draw text.
			Font font;
			/// @brief The bitmap's rectangle.
			Rect rect;

			/// @brief The underlying rednering system texture.
			april::Texture* texture;
			april::ImageSource* imageSource;
			//unsigned char* imageData;
			bool textureNeedsUpdate;

		};
	}
}
#endif

