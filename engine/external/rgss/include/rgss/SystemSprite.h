#ifndef RGSS_SYSTEM_SPRITE_H
#define RGSS_SYSTEM_SPRITE_H

#include "SourceRenderer.h"
#include "rgssExport.h"

namespace rgss
{
	class Bitmap;
	class Rect;

	/// @brief A special lighter sprite class used internally for rendering.
	class rgssExport SystemSprite : public SourceRenderer
	{
	public:
		/// @brief Constructor.
		SystemSprite(Viewport* viewport = NULL);
		/// @brief Destructor;
		~SystemSprite();
		/// @brief Gets the X coordinate.
		/// @return The X coordinate.
		int getX() { return this->x; }
		/// @brief Sets the X coordinate.
		/// @param[in] value The X coordinate.
		void setX(int value) { this->x = value; }
		/// @brief Gets the Y coordinate.
		/// @return The Y coordinate.
		int getY() { return this->y; }
		/// @brief Sets the Y coordinate.
		/// @param[in] value The Y coordinate.
		void setY(int value) { this->y = value; }
		/// @brief Gets the source rectangle.
		/// @return Source Rectangle.
		Rect* getSrcRect() { return this->srcRect; }
		/// @brief Gets the Bitmap.
		/// @return The Bitmap.
		Bitmap* getBitmap() { return this->bitmap; }
		/// @brief Sets the Bitmap.
		/// @param[in] value The Bitmap.
		void setBitmap(Bitmap* value) { this->bitmap = value; }

		/// @brief Draws this sprite on the screen.
		void draw();

	protected:
		/// @brief Source rectangle.
		Rect* srcRect;

		/// @brief Renders the actual texture.
		void _render();

	};

}
#endif
