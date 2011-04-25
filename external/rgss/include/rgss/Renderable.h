#ifndef RGSS_RENDERABLE_H
#define RGSS_RENDERABLE_H

#include <ruby.h>

#include "rgssExport.h"

namespace rgss
{
	class Color;
	class RenderQueue;
	class Tone;

	/// @brief Provides commonly used rendering functionality.
	class rgssExport Renderable
	{
	public:
		/// @brief Type enumarator because of Ruby.
		enum Type
		{
			TYPE_VIEWPORT,
			TYPE_PLANE,
			TYPE_SPRITE,
			TYPE_WINDOW,
			TYPE_TILEMAP
		};

		/// @brief Initializes the basic Renderable object.
		void initializeRenderable(RenderQueue* renderQueue);

		/// @brief Sets the visible flag.
		/// @param[in] value The visible flag.
		void setVisible(bool value) { this->visible = value; }
		/// @brief Gets the Z coordinate.
		/// @return The Z coordinate.
		int getZ() { return this->z; }
		/// @brief Sets the Z coordinate.
		/// @param[in] value The Z coordinate.
		void setZ(int value);
		/// @brief Sets the offset X coordinate.
		/// @param[in] value The offset X coordinate.
		void setOX(int value) { this->ox = value; }
		/// @brief Sets the offset Y coordinate.
		/// @param[in] value The offset Y coordinate.
		void setOY(int value) { this->oy = value; }
		/// @brief Gets the disposed flag.
		/// @return The disposed flag.
		bool isDisposed() { return this->disposed; }
		/// @brief Gets the counter ID.
		/// @return The counter ID.
		unsigned int getCounterId() { return this->counterId; }

		/// @brief Draws this renderable on the screen.
		void draw();
		/// @brief Disposed this renderable.
		void dispose();

		/// @brief Sprite counter.
		static unsigned int CounterProgress;

		/// @brief Marks referenced values of renderable for garbage collection.
		/// @param[in] renderable Renderable to mark.
		static void gc_mark(Renderable* renderable);
		/// @brief Frees allocated memory.
		/// @param[in] renderable Renderable to free.
		static void gc_free(Renderable* renderable);
		/// @brief Disposes the object.
		static VALUE rb_dispose(VALUE self);

		/// @brief Checks whether this renderable is disposed.
		/// @return True if renderable is disposed.
		static VALUE rb_isDisposed(VALUE self);
		/// @brief Gets the visibility.
		/// @return The visibility.
		static VALUE rb_getVisible(VALUE self);
		/// @brief Sets the visibility.
		/// @param[in] value Visibility.
		static VALUE rb_setVisible(VALUE self, VALUE value);
		/// @brief Gets the Z coordinate.
		/// @return The Z coordinate.
		static VALUE rb_getZ(VALUE self);
		/// @brief Sets the Z coordinate.
		/// @param[in] value Z coordinate.
		static VALUE rb_setZ(VALUE self, VALUE value);
		/// @brief Gets the offset X coordinate.
		/// @return Offset X coordinate.
		static VALUE rb_getOX(VALUE self);
		/// @brief Sets the offset X coordinate.
		/// @param[in] value Offset X coordinate.
		static VALUE rb_setOX(VALUE self, VALUE value);
		/// @brief Gets the offset Y coordinate.
		/// @return Offset Y coordinate.
		static VALUE rb_getOY(VALUE self);
		/// @brief Sets the offset Y coordinate.
		/// @param[in] value Offset Y coordinate.
		static VALUE rb_setOY(VALUE self, VALUE value);
		/// @brief Gets the color.
		/// @return value The color.
		static VALUE rb_getColor(VALUE self);
		/// @brief Sets the color.
		/// @param[in] value The color.
		static VALUE rb_setColor(VALUE self, VALUE value);
		/// @brief Gets the tone.
		/// @return Returns The tone.
		static VALUE rb_getTone(VALUE self);
		/// @brief Sets the tone.
		/// @param[in] value The tone.
		static VALUE rb_setTone(VALUE self, VALUE value);

	protected:
		/// @brief The RenderQueue this renderable belongs to.
		RenderQueue* renderQueue;
		/// @brief Disposed flag.
		bool disposed;
		/// @brief Visible flag.
		bool visible;
		/// @brief Z coordinate.
		int z;
		/// @brief Offset X coordinate.
		int ox;
		/// @brief Offset Y coordinate.
		int oy;
		/// @brief The color.
		Color* color;
		/// @brief Ruby object of the color.
		VALUE rb_color;
		/// @brief The tone.
		Tone* tone;
		/// @brief Ruby object of the tone.
		VALUE rb_tone;
		/// @brief Used for determining which Renderable subclass it actually is.
		/// @note This is a necessity because objects created through Ruby don't have a virtual function pointer table.
		Type type;
		/// @brief Renderable counter Id.
		unsigned int counterId;

	};

}
#endif
