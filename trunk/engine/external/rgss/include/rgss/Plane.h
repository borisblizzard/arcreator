#ifndef RGSS_PLANE_H
#define RGSS_PLANE_H

#include <ruby.h>

#include "Color.h"
#include "Rect.h"
#include "Tone.h"
#include "Blendable.h"
#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cPlane;

	class rgssExport Plane : public Blendable
	{
	public:
		/// @brief Draws this sprite on the screen.
		void draw();

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Marks referenced values of Plane for garbage collection.
		/// @param[in] plane Pointer to the Plane to mark.
		static void gc_mark(Plane* plane);
		/// @brief Frees allocated memory.
		/// @param[in] plane Pointer to the Plane to free.
		static void gc_free(Plane* plane);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance.
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
		
	protected:
		/// @brief Gets the render area rectangle.
		/// @return The render area rectangle.
		Rect _getRenderRect();
		/// @brief Renders the actual texture.
		void _render();

		/// @brief Color blended with plane
		Color color;
		/// @brief The plane's color tone
		Tone tone;

	};

}
#endif
