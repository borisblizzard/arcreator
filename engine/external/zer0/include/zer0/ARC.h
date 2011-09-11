#ifndef ZER0_ARC_H
#define ZER0_ARC_H

#include <ruby.h>

#include <hltypes/harray.h>
#include <hltypes/hfile.h>
#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	extern VALUE rb_mARC;

	class zer0Export ARC
	{
	public:
		/// @brief Serializer version.
		static hstr Version;

		/// @brief Initializes the module.
		static void init();
		/// @brief Destroys the module.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();

		/// @brief Does nothing.
		/// @param[in] param Does nothing.
		static VALUE rb_test(VALUE self, VALUE param);

	};

}
#endif
