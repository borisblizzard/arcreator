#include <ruby.h>

#include <hltypes/util.h>

#include "RGSS/Window.h"
#include "RGSS/Bitmap.h"
#include "RGSS/Rect.h"
#include "RGSS/Viewport.h"

namespace zer0
{
	namespace RGSS
	{
		VALUE rb_cWindow;

		void Window::createRubyInterface()
		{
		}
	
		Window::Window()
		{
			this->viewport = new Viewport();
		}
		Window::Window(Viewport* value)
		{
			this->viewport = value;
		}
		/// @todo implement
		Window::~Window()
		{
		}
	
		void Window::setBackOpacity(float value)
		{
			this->back_opacity = hclamp(value, 0.0f, 255.0f);
		}
		/// @todo add RGSS Error calls
		void Window::setContents(Bitmap* value)
		{
			this->contents = value;
		}
		void Window::setContentsOpacity(float value)
		{
			this->contents_opacity = hclamp(value, 0.0f, 255.0f);
		}
		void Window::setOpacity(float value)
		{
			this->opacity = hclamp(value, 0.0f, 255.0f);
		}
		/// @todo add RGSS Error calls
		void Window::setWindowskin(Bitmap* value)
		{
			this->windowskin = value;
		}

		void Window::dispose()
		{

		}
		bool Window::disposed()
		{
			return true;
		}
		void Window::update()
		{

		}

	}
}
