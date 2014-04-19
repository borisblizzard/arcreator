#ifndef REACTOR_ARC_H
#define REACTOR_ARC_H

#include <ruby.h>

#include <hltypes/harray.h>
#include <hltypes/hfile.h>
#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "reactorExport.h"

namespace reactor
{
	extern VALUE rb_mARC;

	class reactorExport ARC
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

		/// @brief Returns User System Path used for logs, save games, etc.
		/// @return System Path.
		static VALUE rb_getSystemPath(VALUE self);
		/// @brief Returns parameters from arc.cfg file.
		/// @return Parameters from arc.cfg file.
		static VALUE rb_getCfgParameters(VALUE self);
		/// @brief Returns the logical HWND for the window.
		/// @return Logical HWND for the window.
		static VALUE rb_getBackendId(VALUE self);

	};

}
#endif
