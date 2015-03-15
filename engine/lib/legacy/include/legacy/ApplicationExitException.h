#ifndef LEGACY_APPLICATION_EXIT_EXCEPTION_H
#define LEGACY_APPLICATION_EXIT_EXCEPTION_H

#include <hltypes/hexception.h>

#include "legacyExport.h"

namespace legacy
{
	/// @brief Special exception that is thrown to terminate the game.
	class legacyExport ApplicationExitException : public hexception
	{
	public:
		/// @brief Constructor.
		ApplicationExitException();
		/// @brief Desstructor.
		~ApplicationExitException();

	};

}

#endif
