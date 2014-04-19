#ifndef LEGACY_SYSTEM_SPRITE_H
#define LEGACY_SYSTEM_SPRITE_H

#include <hltypes/hltypesUtil.h>

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

		HL_DEFINE_GETSET(int, x, X);
		HL_DEFINE_GETSET(int, y, Y);
		HL_DEFINE_GET(Rect*, srcRect, SrcRect);
		HL_DEFINE_SET(Bitmap*, bitmap, Bitmap);

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
