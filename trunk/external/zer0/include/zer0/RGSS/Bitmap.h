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
		extern VALUE rb_cBitmap;

		class zer0Export Bitmap
		{
		public:
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();

			// @brief The Font used to draw text
			Font font;
			// @brief Bitmap Rect
			Rect rect;

			// @brief Constructor from filename
			// @param[in] filename Filename where the bitmap can be found
			Bitmap(hstr filename);
			// @brief Constructor From width and height
			// @param[in] width The width of the new bitmap
			// @param[in] height The height of the new bitmap
			Bitmap(int width, int height);
			// @brief Basic Deconstructor
			~Bitmap();

			// @brief Blits src_rect From source bitmap to this one
			// @param[in] x The x coordinate to place the bitmap
			// @param[in] y The y coordinate to place the bitmap
			// @param[in] src_bitmap The Bitmap to transfer from
			// @param[in] src_rect The rect to transfer from src_bitmap
			// @param[in] opacity The alpha blend of the blit operation
			void blit(int x, int y, Bitmap src_bitmap, Rect src_rect, int opacity);
			// @brief Clears the entire bitmap
			void clear();
			// @brief Draws text at position (x, y) using the Bitmap's Font
			// @param[in] x X position of the start of the text
			// @param[in] y Y Position of the start of the text
			// @param[in] width Width of the drawn text
			// @param[in] height Height of the drawn text
			// @param[in] str The text to draw
			// @param[in] align How to align the text 0:left 1:center 1:right
			void drawText(int x, int y, int width, int height, hstr str, int align);
			// @brief Draws text at inside rect using the Bitmap's Font
			// @param[in] rect The rect to draw the text inside
			// @param[in] str The text to draw
			// @param[in] align How to align the text 0:left 1:center 1:right
			void drawText(Rect rect, hstr str, int align);
			// @brief fill a rect with a solid color
			// @param[in] x X coordinate of the top left corner of the rect to fill
			// @param[in] y Y coordinate of the top left corner of the rect to fill
			// @param[in] width The width of the rect to fill
			// @param[in] height The height of the rect to fill
			// @param[in] color The color to fill the rect with
			void fillRect(int x, int y, int width, int height, Color color);
			// @brief fill a rec with a solid color
			// @param[in] rect The rect to fill with color
			// @param[in] color The color to fill the rect with
			void fillRect(Rect rect, Color color);
			// @brief get the color of a pixel at (x, y)
			// @param[in] x X coordinate
			// @param[in] y Y coordinate
			// @return Color the color of the pixel at (x, y)
			Color getPixel(int x, int y);
			// @brief set the color of a pixel at (x, y)
			// @param[in] x X coordinate
			// @param[in] y Y coordinate
			// @param[in] color The color to set the pixel to
			void setPixel(int x, int y, Color color);
			// @brief Changes the bitmap's hue within 360 degrees of displacement.
			// @param[in] hue Degrees to rotate the hue
			void changeHue(int hue);
			// @brief Blits src_rect from source bitmap to this one scaling the bitmap to fit inside dest_rect
			// @param[in] dest_rect The rect to fit the blit to
			// @param[in] src_bitmap The Bitmap to transfer from
			// @param[in] src_rect The rect to transfer from src_bitmap
			// @param[in] opacity The alpha blend of the blit operation
			void stretchBlt(Rect dest_rect, Bitmap src_bitmap, Rect src_rect, int opacity); 
			// @brief gets the rect needed to draw a string of text
			// @return Rect the rect needed to draw a string of text
			Rect textSize(hstr str);
			/*
			stretch_blt
			text_size
			*/

		};
	
	}
}
#endif
