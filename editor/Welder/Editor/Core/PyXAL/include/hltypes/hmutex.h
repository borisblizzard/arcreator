/// @file
/// @version 2.3
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Provides functionality of a mutex for multithreading.

#ifndef HLTYPES_MUTEX_H
#define HLTYPES_MUTEX_H

#ifndef _WIN32
#include <pthread.h>
#endif

#include "hltypesExport.h"

namespace hltypes
{
	/// @brief Provides functionality of a Mutex for multithreading.
	/// @todo Finish the class and fix remaining problems.
	class hltypesExport Mutex
	{
	public:
		/// @brief Basic constructor.
		Mutex();
		/// @brief Destructor.
		~Mutex();
		/// @brief Locks the Mutex.
		/// @note If another thread has lock, the caller thread will wait until the previous thread unlocks it.
		void lock();
		/// @brief Unlocks the Mutex.
		/// @note Use this when you're done with thread-safe sections of your code.
		void unlock();
		
	protected:
		/// @brief Mutex OS handle.
		void* handle;
		
	};
}

/// @brief Alias for simpler code.
typedef hltypes::Mutex hmutex;

#endif
