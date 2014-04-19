#ifndef LEGACY_VIEWPORT_H
#define LEGACY_VIEWPORT_H

#include <ruby.h>

#include "Renderable.h"
#include "legacyExport.h"

namespace april
{
	class Texture;
}

namespace legacy
{
	extern VALUE rb_cViewport;

	class Rect;
	class RenderQueue;
	
	/// @brief Emulates RGSS's Viewport class.
	class legacyExport Viewport : public Renderable
	{
	public:
		/// @brief This viewport's RenderQueue.
		RenderQueue* renderQueue;

		/// @brief Constructor.
		Viewport();
		/// @brief Destructor.
		~Viewport();
		/// @brief Initializes the basic object.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		void initialize(int argc, VALUE* argv);
		/// @brief Disposes this object.
		void dispose();
		/// @brief Ruby garbage collector marking.
		void mark();

		/// @brief Gets the Rect.
		/// @return The Rect.
		Rect* getRect() { return this->rect; }

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
