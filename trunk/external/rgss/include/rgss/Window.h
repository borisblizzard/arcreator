#ifndef RGSS_WINDOW_H
#define RGSS_WINDOW_H

#include <ruby.h>

#include "Rect.h"
#include "SourceRenderer.h"
#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cWindow;

	class Rect;

	class rgssExport Window : public SourceRenderer
	{
	public:
		/// @brief Draws this sprite on the screen.
		void draw();

		/// @brief Intializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Marks referenced values of window for garbage collection.
		/// @param[in] window Window to mark.
		static void gc_mark(Window* window);
		/// @brief Frees allocated memory.
		/// @param[in] window Window to free.
		static void gc_free(Window* window);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance.
		static VALUE rb_initialize(VALUE self);



		/// @brief Set the back opacity.
		/// @param[in] value Alpha component.
		/// @note The value will be clamped between -255 and 255.
		static VALUE setBackOpacity(VALUE self, VALUE value);
		/// @brief Set the window contents' opacity.
		/// @param[in] value Alpha component
		/// @note The value will be clamped between -255 and 255.
		static VALUE setContentsOpacity(VALUE self, VALUE value);
		/// @brief Sets the source bitmap of the windowskin.
		/// @param[in] value Bitmap component.
		static VALUE setWindowskin(VALUE self, VALUE* value);
		/// @brief Calls the update method.
		static VALUE update(VALUE self);

	protected:
		/// @brief X coordinate.
		int x;
		/// @brief Y coordinate.
		int y;
		/// @brief Width.
		int width;
		/// @brief Height.
		int height;

		/// @brief Renders the actual texture.
		void _render();

	};

}
#endif
