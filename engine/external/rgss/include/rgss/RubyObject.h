#ifndef RGSS_RUBY_OBJECT_H
#define RGSS_RUBY_OBJECT_H

#include "rgssExport.h"

namespace rgss
{
	/// @brief Provides a base object for all RGSS classes.
	class rgssExport RubyObject
	{
	public:
		/// @brief Constructor.
		RubyObject();
		/// @brief Destructor.
		virtual ~RubyObject();
		/// @brief Ruby garbage collector marking.
		virtual void mark();

		/// @brief Marks referenced values of the object for garbage collection.
		/// @param[in] rubyObject RubyObject to mark.
		static void gc_mark(RubyObject* rubyObject);
		/// @brief Frees allocated memory.
		/// @param[in] rubyObject RubyObject to free.
		static void gc_free(RubyObject* rubyObject);

	};

}
#endif
