#ifndef LEGACY_SYSTEM_SPRITE_H
#define LEGACY_SYSTEM_SPRITE_H

#include "SourceRenderer.h"
#include "legacyExport.h"

namespace legacy
{
	class Bitmap;
	class Rect;
	class Viewport;

	/// @brief A special lighter sprite class used internally for rendering.
	/// @note This class is not exposed to Ruby and can be created only in C++.
	class legacyExport SystemSprite : public SourceRenderer
	{
	public:
		/// @brief Constructor.
		/// @param[in] viewport Viewport object.
		SystemSprite(Viewport* viewport);
		/// @brief Destructor;
		~SystemSprite();
		/// @brief Disposes this object.
		void dispose();

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
		/// @brief Sets the Bitmap.
		/// @param[in] value The Bitmap.
		void setBitmap(Bitmap* value) { this->bitmap = value; }

		/// @brief Draws this sprite on the screen.
		void draw();

	protected:
		/// @brief Source rectangle.
		Rect* srcRect;

		/// @brief Checks if object is visible for rendering.
		/// @return True if object is visible for rendering.
		bool _canDraw();
		/// @brief Renders the actual texture.
		void _render();

	};

}
#endif
