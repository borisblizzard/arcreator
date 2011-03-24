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
		static VALUE rb_cSprite;

		class Bitmap;
		class Viewport;

		/// @brief Emulates RGSS's Sprite class.
		class zer0Export Sprite
		{
		public:
			/// @todo Dummy, needs to be removed.
			Sprite() { }
			/// @todo Dummy, needs to be removed.
			~Sprite() { }

			/// @brief Draws this sprite on the screen.
			void draw();

			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Wraps this instance into a Ruby cobject.
			/// @return Ruby object.
			VALUE wrap();
			/// @brief Marks referenced values of sprite for garbage collection.
			/// @param[in] sprite Sprite to mark.
			static void gc_mark(Sprite* sprite);
			/// @brief Frees allocated memory.
			/// @param[in] sprite Sprite to free.
			static void gc_free(Sprite* sprite);
			/// @brief Ruby allocation of an instance.
			static VALUE rb_new(VALUE classe);
			/// @brief Sets the color to the specified value.
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			/// @note Arguments are "[viewport]".
			static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
			/// @brief Disposes the object.
			static VALUE rb_dispose(VALUE self);

			/// @brief Gets the X coordinate.
			/// @return X coordinate.
			static VALUE rb_getX(VALUE self);
			/// @brief Sets the X coordinate.
			/// @param[in] value X coordinate.
			static VALUE rb_setX(VALUE self, VALUE value);
			/// @brief Gets the Y coordinate.
			/// @return Y coordinate.
			static VALUE rb_getY(VALUE self);
			/// @brief Sets the Y coordinate.
			/// @param[in] value Y coordinate.
			static VALUE rb_setY(VALUE self, VALUE value);
			/// @brief Gets the Z coordinate.
			/// @return Z coordinate.
			static VALUE rb_getZ(VALUE self);
			/// @brief Sets the Z coordinate.
			/// @param[in] value Z coordinate.
			static VALUE rb_setZ(VALUE self, VALUE value);
			/// @brief Gets the bitmap.
			/// @return Bitmap.
			static VALUE rb_getBitmap(VALUE self);
			/// @brief Sets the bitmap.
			/// @param[in] value Bitmap.
			static VALUE rb_setBitmap(VALUE self, VALUE value);
			/// @brief Checks whether sprite is disposed.
			/// @return True if sprite was disposed manually.
			static VALUE rb_isDisposed(VALUE self);

			/// @brief Mixes a color with the sprite for a short duration.
			/// @param[in] color Color component.
			/// @param[in] duration Number of frames.
			static VALUE flash(VALUE self, VALUE color, VALUE duration);
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

			/// @todo needs to be refactored
			int x;
			int y;
			int z;

		protected:
			bool disposed;
			Bitmap* bitmap;
			VALUE rb_bitmap;


		};
	}
}
#endif