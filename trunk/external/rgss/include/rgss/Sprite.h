#ifndef RGSS_SPRITE_H
#define RGSS_SPRITE_H

#include <ruby.h>

#include "Color.h"
#include "Rect.h"
#include "SourceRenderer.h"
#include "Tone.h"
#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cSprite;

	/// @brief Emulates RGSS's Sprite class.
	class rgssExport Sprite : public SourceRenderer
	{
	public:
		/*
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
		*/
		/// @brief Gets the source rectangle.
		/// @return Source Rectangle.
		Rect* getSrcRect() { return this->srcRect; }

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
		/// @brief Gets the angle.
		/// @return Angle.
		static VALUE rb_getAngle(VALUE self);
		/// @brief Sets the angle.
		/// @param[in] value Angle.
		static VALUE rb_setAngle(VALUE self, VALUE value);
		/// @brief Gets the source rectangle.
		/// @return Source rectangle.
		static VALUE rb_getSrcRect(VALUE self);
		/// @brief Sets the source rectangle.
		/// @param[in] value Source rectangle.
		static VALUE rb_setSrcRect(VALUE self, VALUE value);
		/// @brief Sets the bitmap.
		/// @param[in] value Bitmap.
		static VALUE rb_setBitmap(VALUE self, VALUE value);



		/// @brief Mixes a color with the sprite for a short duration.
		/// @param[in] color Color component.
		/// @param[in] duration Number of frames.
		static VALUE flash(VALUE self, VALUE color, VALUE duration);
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
		/// @brief Rotation angle.
		float angle;
		/// @brief Source rectangle.
		Rect* srcRect;
		/// @brief Ruby object of source rectangle.
		VALUE rb_srcRect;

		/// @brief Renders the actual texture.
		void _render();

	};

}
#endif
