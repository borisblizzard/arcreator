#ifndef ZER0_RGSS_SPRITE_H
#define ZER0_RGSS_SPRITE_H

#include <ruby.h>

#include "RGSS/Color.h"
#include "RGSS/Rect.h"
#include "RGSS/Tone.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		extern VALUE rb_cSprite;

		class Bitmap;
		class Viewport;

		/// @brief Emulates RGSS's Sprite class.
		class zer0Export Sprite
		{
		public:
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Frees the sprite.
			static VALUE dispose(VALUE self);
			/// @brief Mixes a color with the sprite for a short duration.
			/// @param[in] color Color component.
			/// @param[in] duration Number of frames.
			static VALUE flash(VALUE self, VALUE color, VALUE duration);
			/// @brief Basic constructor.
			/// @param[in] value Viewport component.
			static VALUE initialize(int argc, VALUE *argv, VALUE self);
			/// @brief Gets truth value if sprite has been disposed.
			static VALUE isDisposed(VALUE self);
			/// @brief Sets the sprite's angle of rotation.
			/// @param[in] value Angle value.
			/// @note Uses modulus operation to keep value between 0 and 360.
			static VALUE setAngle(VALUE self, VALUE value);
			/// @brief Sets the sprite's bitmap.
			/// @param[in] value Bitmap component.
			static VALUE setBitmap(VALUE self, VALUE* value);
			/// @brief Sets the alpha value of sprite.
			/// param[in] value Alpha component.
			static VALUE setOpacity(VALUE self, VALUE value);
			/// @brief Sets the sprite zoom on the x-axis.
			/// param[in] value X-axis zoom value.
			static VALUE setZoomX(VALUE self, VALUE value);
			/// @brief Sets the sprite zoom on the y-axis.
			/// param[in] value Y-axis zoom value.
			static VALUE setZoomY(VALUE self, VALUE value);
			/// @brief Invokes the sprites update method.
			static VALUE update(VALUE self);
		};
	}
}
#endif
