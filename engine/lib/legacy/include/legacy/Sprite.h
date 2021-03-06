#ifndef LEGACY_SPRITE_H
#define LEGACY_SPRITE_H

#include <ruby.h>

#include <hltypes/hltypesUtil.h>

#include "Blendable.h"
#include "legacyExport.h"

namespace legacy
{
	extern VALUE rb_cSprite;

	class Bitmap;
	class Rect;

	/// @brief Emulates RGSS's Sprite class.
	class legacyExport Sprite : public Blendable
	{
	public:
		/// @brief Constructor.
		Sprite();
		/// @brief Constructor.
		/// @param[in] viewport Viewport object.
		Sprite(Viewport* viewport);
		/// @brief Destructor.
		~Sprite();
		/// @brief Initializes the basic object.
		/// @param[in] rb_viewport Ruby Viewport object.
		void initialize(VALUE rb_viewport);
		/// @brief Disposes this object.
		void dispose();
		/// @brief Ruby garbage collector marking.
		void mark();

		HL_DEFINE_GETSET(int, x, X);
		HL_DEFINE_GETSET(int, y, Y);
		HL_DEFINE_GET(Rect*, srcRect, SrcRect);
		HL_DEFINE_GETSET(Bitmap*, bitmap, Bitmap);

		/// @brief Draws this sprite on the screen.
		void draw();

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance, setting the viewport if provided.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[viewport]".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Used to prevent for cloning.
		/// @param[in] original The original.
		static VALUE rb_initialize_clone(VALUE self, VALUE original);
		/// @brief Used to prevent for duping.
		/// @param[in] original The original.
		static VALUE rb_initialize_dup(VALUE self, VALUE original);

		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[viewport]"
		static VALUE create(int argc, VALUE* argv);

		/// @brief Sets the bitmap.
		/// @param[in] value The bitmap.
		static VALUE rb_setBitmap(VALUE self, VALUE value);
		/// @brief Gets the rotation angle.
		/// @return The rotation angle.
		static VALUE rb_getAngle(VALUE self);
		/// @brief Sets the rotation angle.
		/// @param[in] value The rotation angle.
		static VALUE rb_setAngle(VALUE self, VALUE value);
		/// @brief Gets the mirror flag.
		/// @return The mirror flag.
		static VALUE rb_getMirror(VALUE self);
		/// @brief Sets the mirror flag.
		/// @param[in] value The mirror flag.
		static VALUE rb_setMirror(VALUE self, VALUE value);
		/// @brief Gets the bush depth.
		/// @return The bush depth.
		static VALUE rb_getBushDepth(VALUE self);
		/// @brief Sets the bush depth.
		/// @param[in] value The bush depth.
		static VALUE rb_setBushDepth(VALUE self, VALUE value);
		/// @brief Gets the source rectangle.
		/// @return Returns the Sprite's source RGSS::Rect object.
		static VALUE rb_getSrcRect(VALUE self);
		/// @brief Sets the source rectangle.
		/// @param[in] value Sets the Sprite's source RGSS::Rect object.
		static VALUE rb_setSrcRect(VALUE self, VALUE value);

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

		/// @brief Checks if object is visible for rendering.
		/// @return True if object is visible for rendering.
		bool _canDraw();
		/// @brief Renders the actual texture.
		void _render();

	};

}
#endif
