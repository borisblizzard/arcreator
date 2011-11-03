#ifndef RGSS_WINDOW_H
#define RGSS_WINDOW_H

#include <ruby.h>

#include "Rect.h"
#include "SourceRenderer.h"
#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cWindow;

	class Bitmap;
	class Rect;
	class Sprite;

	class rgssExport Window : public SourceRenderer
	{
	public:
		/// @brief Draws this sprite on the screen.
		void draw();
		/// @brief Disposed this instance.
		void dispose();

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Marks referenced values of window for garbage collection.
		/// @param[in] window Pointer to the Window to mark.
		static void gc_mark(Window* window);
		/// @brief Frees allocated memory.
		/// @param[in] window Pointer to the Window to free.
		static void gc_free(Window* window);
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

		/// @brief Sets the visible flag.
		/// @param[in] value The visible flag.
		static VALUE rb_setVisible(VALUE self, VALUE value);
		/// @brief Sets the bitmap.
		/// @param[in] value The bitmap.
		static VALUE rb_setBitmap(VALUE self, VALUE value);
		/// @brief Sets the Z coordinate.
		/// @param[in] value The Z coordinate.
		static VALUE rb_setZ(VALUE self, VALUE value);
		/// @brief Gets the width.
		/// @return The width.
		static VALUE rb_getWidth(VALUE self);
		/// @brief Sets the width.
		/// @param[in] value The width.
		static VALUE rb_setWidth(VALUE self, VALUE value);
		/// @brief Gets the height.
		/// @return The height.
		static VALUE rb_getHeight(VALUE self);
		/// @brief Sets the height.
		/// @param[in] value The height.
		static VALUE rb_setHeight(VALUE self, VALUE value);
		/// @brief Gets the Active flag.
		/// @return The Active flag.
		static VALUE rb_getActive(VALUE self);
		/// @brief Sets the Active flag.
		/// @param[in] value The Active flag.
		static VALUE rb_setActive(VALUE self, VALUE value);
		/// @brief Gets the Pause flag.
		/// @return The Pause flag.
		static VALUE rb_getPause(VALUE self);
		/// @brief Sets the Pause flag.
		/// @param[in] value The Pause flag.
		static VALUE rb_setPause(VALUE self, VALUE value);
		/// @brief Gets the Stretch flag.
		/// @return The Stretch flag.
		static VALUE rb_getStretch(VALUE self);
		/// @brief Sets the Stretch flag.
		/// @param[in] value The Stretch flag.
		static VALUE rb_setStretch(VALUE self, VALUE value);
		/// @brief Gets the backOpacity.
		/// @return The backOpacity.
		static VALUE rb_getBackOpacity(VALUE self);
		/// @brief Sets the backOpacity.
		/// @param[in] value The backOpacity.
		static VALUE rb_setBackOpacity(VALUE self, VALUE value);
		/// @brief Gets the contentsOpacity.
		/// @return The contentsOpacity.
		static VALUE rb_getContentsOpacity(VALUE self);
		/// @brief Sets the contentsOpacity.
		/// @param[in] value The contentsOpacity.
		static VALUE rb_setContentsOpacity(VALUE self, VALUE value);
		/// @brief Gets the cursor rectangle.
		/// @return The cursor rectangle.
		static VALUE rb_getCursorRect(VALUE self);
		/// @brief Sets the cursor rectangle.
		/// @param[in] value The cursor rectangle.
		static VALUE rb_setCursorRect(VALUE self, VALUE value);
		/// @brief Gets the windowskin bitmap.
		/// @return Windowskin bitmap.
		static VALUE rb_getWindowskin(VALUE self);
		/// @brief Sets the windowskin bitmap.
		/// @param[in] value Windowskin bitmap.
		static VALUE rb_setWindowskin(VALUE self, VALUE value);

		/// @brief Updates this instance.
		static VALUE rb_update(VALUE self);

	protected:
		/// @brief Window width.
		int width;
		/// @brief Window height.
		int height;
		/// @brief Background opacity.
		int backOpacity;
		/// @brief Contents opacity.
		int contentsOpacity;
		/// @brief Active flag.
		bool active;
		/// @brief Pause flag.
		bool pause;
		/// @brief Stretch flag.
		bool stretch;
		/// @brief Pause animation counter.
		int pauseCount;
		/// @brief Cursor animation counter.
		int cursorCount;
		/// @brief Cursor rectangle.
		Rect* cursorRect;
		/// @brief Ruby object of cursor rectangle.
		VALUE rb_cursorRect;
		/// @brief Windowskin bitmap.
		Bitmap* windowskin;
		/// @brief Ruby object of windowskin bitmap.
		VALUE rb_windowskin;

		/// @brief Windowskin background bitmap.
		Bitmap* windowskinBackground;
		/// @brief Windowskin horizontal borders bitmap.
		Bitmap* windowskinHorizontalBorders;
		/// @brief Windowskin vertical borders.
		Bitmap* windowskinVerticalBorders;
		/// @brief Windowskin corners bitmap.
		Bitmap* windowskinCorners;
		/// @brief Contents sprite.
		Sprite* contentsSprite;
		/// @brief Ruby object of contents sprite.
		VALUE rb_contentsSprite;
		/// @brief Windowskin cursor Sprite.
		Sprite* cursorSprite;
		/// @brief Ruby object of cursor sprite.
		VALUE rb_cursorSprite;
		/// @brief Pause sprite.
		Sprite* pauseSprite;
		/// @brief Ruby object of pause sprite.
		VALUE rb_pauseSprite;
		/// @brief Bitmap border sprites.
		Sprite* borderSprites[4];
		/// @brief Ruby objects of bitmap border sprites.
		VALUE rb_borderSprites[4];
		
		/// @brief Renders the actual texture.
		void _render();
		/// @brief Renders the background of the window with the windowskin.
		void _renderWindowskinBackground();
		/// @brief Renders the borders of the window with the windowskin.
		void _renderWindowskinBorders();
		/// @brief Renders the corners of the window with the windowskin.
		void _renderWindowskinCorners();
		/// @brief Updates all windowskin components.
		void _updateWindowskin();
		/// @brief Updates the contents sprite.
		void _updateContentsSprite();
		/// @brief Updates the cursor sprite.
		void _updateCursorSprite();
		/// @brief Updates the pause sprite.
		void _updatePauseSprite();
		/// @brief Updates the bitmap border sprites.
		void _updateBorderSprites();

	};

}
#endif
