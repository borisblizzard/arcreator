#ifndef ZER0_RGSS_SPRITE_H
#define ZER0_RGSS_SPRITE_H

#include "RGSS/Color.h"
#include "RGSS/Rect.h"
#include "RGSS/Tone.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class Bitmap;
		class Viewport;

		/// @brief Emulates RGSS's Sprite class.
		class zer0Export Sprite
		{
		public:
			/// @brief The sprite's angle of rotation
			int angle;
			/// @brief The sprite's bitmap
			Bitmap* bitmap;
			/// @brief Blend type used for sprite
			short blend_type;
			/// @brief Bush depth used for sprite
			short bush_depth;
			/// @brief Color blended with sprite
			Color color;
			/// @brief Flag to have sprite drawn flipped
			bool mirror;
			/// @brief The alpha value of the sprite
			float opacity;
			/// @brief The X-coordinate of the sprite's starting point
			short ox;
			/// @brief The Y-coordinate of the sprite's starting point
			short oy;
			/// @brief The Rect taken from the sprite's bitmap.
			Rect src_rect;
			/// @brief The sprite's color tone
			Tone tone; 
			/// @brief The sprite's visibility.
			bool visible;
			/// @brief The sprite's X-coordinate
			short x;
			/// @brief The sprite's Y-coordinate
			short y;
			/// @brief The sprite's Z-coordinate
			short z; 
			/// @brief The sprite's X-axis zoom level
			float zoomX;
			/// @brief The sprite's Y-axis zoom level
			float zoomY;

			/// @brief Basic constructor
			Sprite();
			/// @brief Constructor to initialize with viewport
			/// @param[in] viewport Specifies the viewport to use for this sprite
			Sprite(Viewport* viewport);
			/// @brief Basic Deconstructor
			~Sprite();

			/// @brief Returns the viewport specified
			Viewport* getViewport() { return this->viewport; };
			/// @brief Sets the sprite's angle of rotation
			/// @param[in] value Value to set the angle
			void setAngle(int value);
			/// @brief Sets the sprite's bitmap
			/// @param[in] bitmap Bitmap object to set
			void setBitmap(Bitmap* value);
			/// @brief Sets the alpha value of sprite
			/// param[in] value Integer value of sprite opacity
			void setOpacity(float value);
			/// @brief Sets the sprite zoom on the x-axis
			/// param[in] value Zoom value. 1.0 denotes actual pixel size
			void setZoomX(float value);
			/// @brief Sets the sprite zoom on the y-axis
			/// param[in] value Zoom value. 1.0 denotes actual pixel size
			void setZoomY(float value);
			// Instance methods
			/// @brief Frees the sprite
			void dispose();
			/// @brief Boolean value if sprite has been disposed
			/// @note This function is missing the "?" that the RGSS method uses. Not sure how to implement.
			bool disposed();
			/// @brief Mixes a color with the sprite for a short duration
			/// @param[in] color Color to mix with the sprite during the flash
			/// @param[in] duration The number of frames that flash will last
			void flash(Color color, int duration);
			/// @brief Calls the update method
			void update();

		private:
			/// @brief The sprite's viewport
			Viewport* viewport;

			// Ideas
			// Add method to reset viewport (RMXP doesn't have by default)
			// Add rotate method, something like .rotate(rate, duration) and/or .rotate(degrees)
			// Add a "3-D" rotate (think rotating target arrow over character's head)
		};
	}
}
#endif
