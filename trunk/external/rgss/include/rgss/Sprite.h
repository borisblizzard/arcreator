#ifndef RGSS_SPRITE_H
#define RGSS_SPRITE_H

#include <ruby.h>

#include "Color.h"
#include "Rect.h"
#include "Tone.h"
#include "rgssExport.h"

namespace rgss
{
	static VALUE rb_cSprite;

	class Bitmap;
	class Viewport;

	/// @brief Emulates RGSS's Sprite class.
	class rgssExport Sprite
	{
	public:
		/// @todo Dummy, needs to be removed.
		Sprite() { }
		/// @todo Dummy, needs to be removed.
		~Sprite() { }

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
		/// @brief Gets the Z coordinate.
		/// @return The Z coordinate.
		int getZ() { return this->z; }
		/// @brief Sets the Z coordinate.
		/// @param[in] value The Z coordinate.
		void setZ(int value) { this->z = value; }

		/// @brief Draws this sprite on the screen.
		void draw();

		/// @brief Intializes the module.
		static void init();
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

	protected:
		/// @brief X coordinate.
		int x;
		/// @brief Y coordinate.
		int y;
		/// @brief Z coordinate.
		int z;
		/// @brief Disposed flag.
		bool disposed;
		/// @brief Bitmap drawing reference.
		Bitmap* bitmap;
		/// @brief Ruby object of bitmap drawing reference.
		VALUE rb_bitmap;

	};

}
#endif
