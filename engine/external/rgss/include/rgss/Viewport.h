#ifndef RGSS_VIEWPORT_H
#define RGSS_VIEWPORT_H

#include <ruby.h>

#include "Renderable.h"
#include "rgssExport.h"

namespace april
{
	class Texture;
}

namespace rgss
{
	extern VALUE rb_cViewport;

	class Rect;
	class RenderQueue;
	
	/// @brief Emulates RGSS's Viewport class.
	class rgssExport Viewport : public Renderable
	{
	public:
		RenderQueue* renderQueue;

		/// @brief Gets the Rect.
		/// @return The Rect.
		Rect* getRect() { return this->rect; }

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
		/// @brief Marks referenced values of Viewport for garbage collection.
		/// @param[in] viewport Pointer to the Viewport to mark.
		static void gc_mark(Viewport* viewport);
		/// @brief Frees allocated memory.
		/// @param[in] viewport Pointer to the Viewport to free.
		static void gc_free(Viewport* viewport);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "x, y, w, h" or "rect".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Used to prevent for cloning.
		/// @param[in] original The original.
		static VALUE rb_initialize_clone(VALUE self, VALUE original);
		/// @brief Used to prevent for duping.
		/// @param[in] original The original.
		static VALUE rb_initialize_dup(VALUE self, VALUE original);
		/// @brief Gets a string representation of the instance.
		/// @return The string representation of the instance.
		static VALUE rb_inspect(VALUE self);

		/// @brief Gets the display rectangle.
		/// @return The Viewport's RGSS::Rect object.
		static VALUE rb_getRect(VALUE self);
		/// @brief Sets the display rectangle.
		/// @param[in] value An RGSS::Rect object.
		static VALUE rb_setRect(VALUE self, VALUE value);

		/// @brief Invokes the update method.
		static VALUE rb_update(VALUE self);
		
	protected:
		/// @brief Display rectangle.
		Rect* rect;
		/// @brief Ruby object of display rectangle.
		VALUE rb_rect;

		/// @brief Renders everything in the viewport onto a texture first.
		void _renderToTexture();
		/// @brief Renders the actual texture.
		void _render();

	private:
		/// @brief Rendering texture.
		april::Texture* texture;

	};

}
#endif
