/// @file
/// @version 3.0
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

#include "hltypesExport.h"
#include "hstring.h"

namespace hltypes
{
	/// @brief Provides functionality of a Mutex for multithreading.
	class hltypesExport Mutex
	{
	public:
		/// @brief Utility class for exception-safe Mutex-locking within a scope.
		class hltypesExport ScopeLock
		{
		public:
			/// @brief Basic constructor.
			/// @param[in] mutex The mutex to lock.
			/// @param[in] logUnhandledUnlocks Whether to log an automatic unlock when the ScopeLock is destroyed by going out of scope (usually on an exception).
			ScopeLock(Mutex* mutex = NULL, bool logUnhandledUnlocks = false);
			/// @brief Destructor.
			~ScopeLock();
			/// @brief Locks the Mutex.
			/// @param[in] mutex The mutex to lock.
			/// @return True if lock succeeded. False if there is already an assigned Mutex.
			bool acquire(Mutex* mutex);
			/// @brief Unlocks the Mutex.
			/// @return True if unlock succeeded. False if there is no assigned Mutex.
			bool release();

		protected:
			/// @brief The Mutex.
			Mutex* mutex;
			/// @brief Log-on-auto-unlock flag.
			bool logUnhandledUnlocks;

		};

		/// @brief Basic constructor.
		/// @param[in] name The internal name.
		Mutex(const String& name = "");
		/// @brief Destructor.
		~Mutex();
		/// @brief Returns the mutex name.
		/// @return The mutex name.
		inline String getName() { return this->name; }
		/// @brief Locks the Mutex.
		/// @note If another thread has lock, the caller thread will wait until the previous thread unlocks it.
		void lock();
		/// @brief Unlocks the Mutex.
		/// @note Use this when you're done with thread-safe sections of your code.
		void unlock();
		
	protected:
		/// @brief Mutex OS handle.
		void* handle;
		/// @brief Mutex name.
		String name;
		/// @brief Used internallly on Win32 so the much faster critical sections can be used instead of mutices and semaphores.
		bool locked;

	private:
		/// @brief Copy constructor.
		/// @note Usage is not allowed and it will throw an exception.
		Mutex(const Mutex& other);
		/// @brief Assignment operator.
		/// @note Usage is not allowed and it will throw an exception.
		Mutex& operator=(Mutex& other);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::Mutex hmutex;

#endif
