#ifndef RGSS_MSG_PACK_H
#define RGSS_MSG_PACK_H

#include <ruby.h>

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

	};
}
#endif
