#ifndef RGSS_MSG_PACK_H
#define RGSS_MSG_PACK_H

#include <ruby.h>

#include <hltypes/hmap.h>
#include <hltypes/harray.h>

#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_mMsgPack;

	class rgssExport MsgPack
	{
	public:
		/// @brief Initializes the module.
		static void init();
		/// @brief Destroys the module.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();

		/// @brief Dumps an object into a stream.
		/// @param[in] stream IO stream.
		/// @param[in] object Ruby object to dump.
		static VALUE rb_dump(VALUE self, VALUE stream, VALUE object);
		/// @brief Loads an object from a stream.
		/// @param[in] stream IO stream.
		/// @return Ruby object loaded from stream.
		static VALUE rb_load(VALUE self, VALUE stream);

	protected:
		/// @brief
		static VALUE io;
		/// @brief
		static hmap<VALUE, VALUE> symbols;
		/// @brief
		static hmap<VALUE, VALUE> strings;
		/// @brief
		static hmap<VALUE, VALUE> ids;
		/// @brief
		static harray<VALUE> stack;
		/// @brief
		static hmap<VALUE, VALUE> finaldump;
		/// @brief
		static int sym_count;
		/// @brief
		static harray<VALUE> pending_objects;
		/// @brief
		static harray<VALUE> post_load_objects;

		static void _build_object_table();
		static void _link_objects();
		static void _call_arc_post_load();
		static void _reset();
		static void _start_dump();
		static void _write_dump();
		static VALUE _queue_dump_object(VALUE obj);
		static void _dump_object(VALUE obj);
		static VALUE _dump_true_object(VALUE obj);
		static VALUE _dump_false_object(VALUE obj);
		static VALUE _dump_nil_object(VALUE obj);
		static VALUE _dump_numeric_object(VALUE obj);
		static VALUE _dump_string_object(VALUE obj);
		static VALUE _queue_dump_array_object(VALUE obj);
		static void _dump_array_object(VALUE obj);
		static VALUE _queue_dump_hash_object(VALUE obj);
		static void _dump_hash_object(VALUE obj);
		static VALUE _queue_dump_nonstandard_object(VALUE obj);
		static void _dump_nonstandard_object(VALUE obj);
		static VALUE _enter_obj(VALUE obj);

	};
}
#endif
