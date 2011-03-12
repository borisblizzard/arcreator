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
			
		void Bitmap::Blit(int x, int y, Bitmap src_bitmap, Rect src_rect, int opacity)
		{
		}
			
		void Bitmap::Clear()
		{
		}
			
		void Bitmap::DrawText(int x, int y, int width, int height, hstr str, int align)
		{
		}
			
		void Bitmap::DrawText(Rect rect, hstr str, int align)
		{
		}
			
		void Bitmap::FillRect(int x, int y, int width, int height, Color color)
		{
		}
			
		void Bitmap::FillRect(Rect rect, Color color)
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
			
		void Bitmap::ChangeHue(int hue)
		{
		}
			
		void Bitmap::StretchBlt(Rect dest_rect, Bitmap src_bitmap, Rect src_rect, int opacity)
		{
		}
			
		Rect Bitmap::TextSize(hstr str)
		{
			// default implementations REPLACE
			return Rect(0, 0, 32, 32);
		}
	
	}
}
