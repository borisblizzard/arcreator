#include <hltypes/util.h>

#include "RGSS/Window.h"
#include "RGSS/Bitmap.h"
#include "RGSS/Rect.h"
#include "RGSS/Viewport.h"

namespace zer0
{
	namespace RGSS
	{
	
		Window::Window()
		{
			this->viewport = new Viewport();
		}
		Window::Window(Viewport value)
		{
			this->viewport = value;
		}
		Window::~Window()
		{
			/// @todo Implement destructor
		}
	
		void Window::setBackOpacity(float value)
		{
			this->back_opacity = hclamp(value, 0.0f, 255.0f);
		}
		void Window::setContents(Bitmap value)
		{
			this->contents = value;
			/// @ todo Include RGSSError 
		}
		void Window::setContentsOpacity(float value)
		{
			this->contents_opacity = hclamp(value, 0.0f, 255.0f);
		}
		void Window::setOpacity(float value)
		{
			this->opacity = hclamp(value, 0.0f, 255.0f);
		}
		void Window::setWindowskin(Bitmap value)
		{
			this->windowskin = value;
			/// @ todo Include RGSSError 
		}

		void Window::dispose()
		{

		}
		bool Window::disposed()
		{

		}
		void Window::update()
		{

		}

	}
}
