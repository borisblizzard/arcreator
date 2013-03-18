#ifndef LEGACY_RUBY_OBJECT_H
#define LEGACY_RUBY_OBJECT_H

#include "legacyExport.h"

namespace legacy
{
	/// @brief Provides a base object for all RGSS classes.
	class legacyExport RubyObject
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
