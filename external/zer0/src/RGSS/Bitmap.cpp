#include "RGSS/Bitmap.h"
#include "RGSS/Color.h"
#include "RGSS/Font.h"
#include "RGSS/Rect.h"

namespace zer0
{
	namespace RGSS
	{
	
		Bitmap::Bitmap(hstr filename)
		{
		}

		Bitmap::Bitmap(int width, int height)
		{
		}
	
		Bitmap::~Bitmap()
		{
		}
			
		void Bitmap::blit(int x, int y, Bitmap src_bitmap, Rect src_rect, int opacity)
		{
		}
			
		void Bitmap::clear()
		{
		}
			
		void Bitmap::drawText(int x, int y, int width, int height, hstr str, int align)
		{
		}
			
		void Bitmap::drawText(Rect rect, hstr str, int align)
		{
		}
			
		void Bitmap::fillRect(int x, int y, int width, int height, Color color)
		{
		}
			
		void Bitmap::fillRect(Rect rect, Color color)
		{
		}
			
		Color Bitmap::getPixel(int x, int y)
		{
			// default implementations REPLACE
			return Color();
		}
			
		void Bitmap::setPixel(int x, int y, Color color)
		{
		}
			
		void Bitmap::changeHue(int hue)
		{
		}
			
		void Bitmap::stretchBlt(Rect dest_rect, Bitmap src_bitmap, Rect src_rect, int opacity)
		{
		}
			
		Rect Bitmap::textSize(hstr str)
		{
			// default implementations REPLACE
			return Rect(0, 0, 32, 32);
		}
	
	}
}
