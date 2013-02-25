#ifndef LEGACY_APPLICATION_EXIT_EXCEPTION_H
#define LEGACY_APPLICATION_EXIT_EXCEPTION_H

#include <hltypes/exception.h>

#include "legacyExport.h"

namespace legacy
{
	/// @brief Special exception that is thrown to terminate the game.
	class legacyExport ApplicationExitException : public hltypes::exception
	{
	public:
		/// @brief Constructor.
		ApplicationExitException();
		/// @brief Desstructor.
		~ApplicationExitException();

	};

}

#endif
