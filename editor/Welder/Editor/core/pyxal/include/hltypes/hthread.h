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
/// Provides functionality of a thread for multithreading.

#ifndef HLTYPES_THREAD_H
#define HLTYPES_THREAD_H

#include "hltypesExport.h"
#include "hstring.h"

namespace hltypes
{
	/// @brief Provides functionality of a Thread for multithreading.
	class hltypesExport Thread
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] function Function pointer for the callback.
		/// @param[in] name Name for the thread.
		Thread(void (*function)(Thread*), const String& name = "");
		/// @brief Destructor.
		virtual ~Thread();
		/// @brief Sets function.
		/// @param[in] value New function.
		inline void setFunction(void (*value)(Thread*)) { this->function = value; }
		/// @brief Gets the thread name.
		/// @return Thread name.
		inline String getName() { return this->name; }
		/// @brief Gets whether the thread is running.
		/// @return True if the thread is running.
		inline bool isRunning() { return this->running; }
		/// @brief Starts the thread processing.
		void start();
		/// @brief Stops the thread processing.
		void stop();
		/// @brief Resumes the thread processing.
		void resume();
		/// @brief Pauses the thread processing.
		void pause();
		/// @brief Executes the thread's function.
		virtual void execute();
		/// @brief Joins thread.
		void join();
		/// @brief Puts current thread to sleep.
		/// @param[in] milliseconds How long to sleep in milliseconds.
		static void sleep(float milliseconds);
		
	protected:
		/// @brief The callback function of the thread.
		void (*function)(Thread*);
		/// @brief The internal OS handle ID for the thread.
		void* id;
		/// @brief Thread name.
		/// @note Usually used for debugging purposes.
		String name;
		/// @brief Flag that determines whether the thread is running or not.
		volatile bool running;
		
	private:
		/// @brief Copy constructor.
		/// @note Usage is not allowed and it will throw an exception.
		Thread(const Thread& other);
		/// @brief Assignment operator.
		/// @note Usage is not allowed and it will throw an exception.
		Thread& operator=(Thread& other);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::Thread hthread;

#endif
