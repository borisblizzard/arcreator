#ifndef ZER0_RGSS_PLANE_H
#define ZER0_RGSS_PLANE_H

#include <ruby.h>

#include "RGSS/Color.h"
#include "RGSS/Rect.h"
#include "RGSS/Tone.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		extern VALUE rb_cPlane;

		class Bitmap;
		class Viewport;

		class zer0Export Plane
		{
		public:
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();

			/// @brief The plane's bitmap
			Bitmap* bitmap;
			/// @brief Blend type used for the plane
			short blend_type;
			/// @brief Color blended with plane
			Color color;
			/// @brief The alpha value of the plane
			float opacity;
			/// @brief The X-coordinate of the plane's starting point
			int ox;
			/// @brief The Y-coordinate of the plane's starting point
			int oy;
			/// @brief The plane's color tone
			Tone tone;
			/// @brief The plane's visibility.
			bool visible;
			/// @brief The plane's Z-coordinate
			float z;
			/// @brief The plane's X-axis zoom level
			float zoomX;
			/// @brief The plane's Y-axis zoom level
			float zoomY;
			
			/// @brief Basic constructor
			Plane();
			/// @brief Constructor to initialize with viewport
			/// @param[in] viewport Specifies the viewport to use for this plane
			Plane(Viewport* value);
			/// @brief Basic Deconstructor
			~Plane();

			/// @brief Returns the viewport specified when initialized
			Viewport* getViewport() { return this->viewport; };
			/// @brief Sets the sprite's bitmap
			/// @param[in] bitmap Bitmap object to set
			void setBitmap(Bitmap* value);
			/// @brief Sets the alpha value of sprite
			/// param[in] Integer value of sprite opacity
			void setOpacity(float value);
			/// @brief Sets the sprite zoom on the x-axis
			/// param[in] Zoom value. 1.0 denotes actual pixel size
			void setZoomX(float value);
			/// @brief Sets the sprite zoom on the y-axis
			/// param[in] Zoom value. 1.0 denotes actual pixel size
			void setZoomY(float value);

			/// @brief Frees the sprite
			void dispose();
			/// @brief Boolean value if sprite has been disposed
			/// @note This function is missing the "?" that the RGSS method uses. Not sure how to implement.
			bool disposed();

		private:
			/// @brief Private value to store the viewport
			Viewport* viewport;

		};

	}
}
#endif
