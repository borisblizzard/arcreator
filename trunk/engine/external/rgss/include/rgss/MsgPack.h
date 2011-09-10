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

		static unsigned char* stream;

		static unsigned char __read_stream();
		static unsigned char* __read_stream(unsigned int bytes);
		static unsigned char __read_uint8();
		static unsigned short __read_uint16();
		static unsigned int __read_uint32();
		static unsigned long __read_uint64();

		static VALUE _unpack(unsigned char* data);
		static VALUE _unpack_object();

		static VALUE _unpack_pint8(unsigned char data);
		static VALUE _unpack_nint8(unsigned char data);
		static VALUE _unpack_uint8();
		static VALUE _unpack_uint16();
		static VALUE _unpack_uint32();
		static VALUE _unpack_uint64();
		static VALUE _unpack_int8();
		static VALUE _unpack_int16();
		static VALUE _unpack_int32();
		static VALUE _unpack_int64();
		static VALUE _unpack_nil();
		static VALUE _unpack_true();
		static VALUE _unpack_false();
		static VALUE _unpack_float();
		static VALUE _unpack_double();
		static VALUE _unpack_raw(unsigned int size);
		static VALUE _unpack_array(unsigned int size);
		static VALUE _unpack_map(unsigned int size);


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
