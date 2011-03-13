#ifndef ZER0_RGSS_WINDOW_H
#define ZER0_RGSS_WINDOW_H

#include "RGSS/Rect.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class Bitmap;
		class Rect;
		class Viewport;

		class zer0Export Window
		{
		public:
			/// @brief Boolean flag to denote if window is active.
			bool active;
			/// @brief The opacity of the background windowskin.
			float back_opacity;
			/// @brief The bitmap that the skin and font is drawn on.
			Bitmap* contents;
			/// @brief The opacity of the window's contents.
			float contents_opacity;
			/// @brief A rect gotten from the cursor's rectangle.
			Rect cursor_rect;
			/// @brief The height, in pixels, of the window.
			int height;
			/// @brief The opacity if the window and its contents.
			float opacity;
			/// @brief The X-coordinate of the sprite's starting point.
			int ox;
			/// @brief The Y-coordinate of the sprite's starting point.
			int oy;
			/// @brief Boolean flag to draw the "waiting for input" arrow.
			bool pause;
			/// @brief Boolean value if the background bitmap should be stretched or tiled.
			bool stretch;
			/// @brief Boolean flag if window is visible.
			bool visible;
			/// @brief Width, in pixels, of the window.
			int width;
			/// @brief The bitmap graphic to use as the windowskin source.
			Bitmap* windowskin;
			/// @brief The X-coordinate of the window.
			int x;
			/// @brief The Y-coordinate of the window.
			int y;
			/// @brief The Z-coordinate of the window.
			int z;

			/// @brief Basic constructor.
			Window();
			/// @brief Constructor to initialize with viewport.
			/// @param[in] viewport Specifies the viewport to use for this sprite.
			Window(Viewport* value);
			/// @brief Basic Deconstructor.
			~Window();

			/// @brief Returns the viewport specified when the window was created.
			Viewport* getViewport() { return this->viewport; };
			/// @brief Set the back opacity, keeping in range (0 - 255).
			/// @param[in] Float value of the back opacity.
			void setBackOpacity(float value);
			/// @brief Set the bitmap to use for the window's contents.
			/// @param[in] value Bitmap used as contents.
			void setContents(Bitmap* value);
			/// @brief Set the window contents' opacity, keeping in range (0 - 255).
			/// @param[in] value Float value of the contents' opacity.
			void setContentsOpacity(float value);
			/// @brief Sets the opacity if the window, keeping in range (0 - 255).
			/// @param[in] value Float value of the window's opacity.
			void setOpacity(float value);
			/// @brief Sets the source bitmap of the windowskin.
			/// @param[in] value Bitmap source of the windowskin.
			void setWindowskin(Bitmap* value);

			/// @brief Frees the sprite.
			void dispose();
			/// @brief Boolean value if sprite has been disposed.
			/// @note This function is missing the "?" that the RGSS method uses. Not sure how to implement.
			bool disposed();
			/// @brief Calls the update method.
			void update();
			
		private:
			/// @brief The window's viewport.
			Viewport* viewport;

		};
	}
}
#endif
