/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @version 1.4
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides functionality of a thread for multithreading.

#ifndef HLTYPES_THREAD_H
#define HLTYPES_THREAD_H

#ifndef _WIN32
#include <pthread.h>
#endif

#include "hltypesExport.h"

namespace hltypes
{
	/// @brief Provides functionality of a Thread for multithreading.
	/// @author Kresimir Spes
	/// @author Boris Mikic
	/// @todo Finish the class and fix remaining problems.
	class hltypesExport Thread
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] function Function pointer for the callback.
		Thread(void (*function)());
		/// @brief Destructor.
		~Thread();
		/// @brief Sets function.
		/// @param[in] value New function.
		void setFunction(void (*value)()) { this->function = value; }
		/// @brief Starts the thread processing.
		void start();
		/// @brief Stops the thread processing.
		void stop();
		/// @brief Resumes the thread processing.
		void resume();
		/// @brief Pauses the thread processing.
		void pause();
		/// @brief Enters a criticals section.
		void enterCritical();
		/// @brief Leaves a criticals section.
		void leaveCritical();
		/// @brief Executes the thread's function.
		virtual void execute();
		/// @brief Joins thread.
		void join();
		/// @brief Puts current thread to sleep.
		/// @param[in] miliseconds How long to sleep in miliseconds.
		static void sleep(float miliseconds);
		
		//static Thread* getCurrentThread();

	protected:
		/// @brief The callback function of the thread.
		void (*function)();
		/// @brief The internal OS handle ID for the thread.
#ifdef _WIN32
		void* id;
		/// @brief Void pointer to critical section.
		static void* criticalSection;
#else
		pthread_t id;
#endif
		/// @brief Flag that determines whether the thread is running or not.
		volatile bool running;
		
	};
}

/// @brief Alias for simpler code.
typedef hltypes::Thread hthread;

#endif
