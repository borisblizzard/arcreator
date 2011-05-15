#ifndef RGSS_SPRITE_H
#define RGSS_SPRITE_H

#include <ruby.h>

#include "Zoomable.h"
#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cSprite;

	class Bitmap;
	class Rect;

	/// @brief Emulates RGSS's Sprite class.
	class rgssExport Sprite : public Zoomable
	{
	public:
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

		/// @brief Initializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Marks referenced values of sprite for garbage collection.
		/// @param[in] sprite Pointer to the Sprite to mark.
		static void gc_mark(Sprite* sprite);
		/// @brief Frees allocated memory.
		/// @param[in] sprite Pointer to the Sprite to free.
		static void gc_free(Sprite* sprite);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance, setting the viewport if provided.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[viewport]".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);

		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[viewport]"
		static VALUE create(int argc, VALUE* argv);

		/// @brief Sets the bitmap.
		/// @param[in] value The bitmap.
		static VALUE rb_setBitmap(VALUE self, VALUE value);
		/// @brief Gets the rotation angle.
		/// @return value The rotation angle.
		static VALUE rb_getAngle(VALUE self);
		/// @brief Sets the rotation angle.
		/// @param[in] value The rotation angle.
		static VALUE rb_setAngle(VALUE self, VALUE value);
		/// @brief Gets the mirror flag.
		/// @return value The mirror flag.
		static VALUE rb_getMirror(VALUE self);
		/// @brief Sets the mirror flag.
		/// @param[in] value The mirror flag.
		static VALUE rb_setMirror(VALUE self, VALUE value);
		/// @brief Gets the bush depth.
		/// @return value The bush depth.
		static VALUE rb_getBushDepth(VALUE self);
		/// @brief Sets the bush depth.
		/// @param[in] value The bush depth.
		static VALUE rb_setBushDepth(VALUE self, VALUE value);
		/// @brief Gets the source rectangle.
		/// @return value Returns the Sprite's source RGSS::Rect object.
		static VALUE rb_getSrcRect(VALUE self);
		/// @brief Sets the source rectangle.
		/// @param[in] value Sets the Sprite's source RGSS::Rect object.
		static VALUE rb_setSrcRect(VALUE self, VALUE value);

		/// @brief Mixes a color with the sprite for a short duration.
		/// @param[in] color Color component.
		/// @param[in] duration Number of frames.
		static VALUE rb_flash(VALUE self, VALUE color, VALUE duration);
		/// @brief Invokes the update method.
		static VALUE rb_update(VALUE self);

	protected:
		/// @brief Rotation angle.
		float angle;
		/// @brief Mirror flag.
		bool mirror;
		/// @brief Bush depth.
		int bushDepth;
		/// @brief Source rectangle.
		Rect* srcRect;
		/// @brief Ruby object of source rectangle.
		VALUE rb_srcRect;

		/// @brief Renders the actual texture.
		void _render();

	};

}
#endif
