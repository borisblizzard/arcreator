#ifndef RGSS_APPLICATION_EXIT_EXCEPTION_H
#define RGSS_APPLICATION_EXIT_EXCEPTION_H

#include <hltypes/exception.h>

#include "rgssExport.h"

namespace rgss
{
	/// @brief Special exception that is thrown to terminate the game.
	class rgssExport ApplicationExitException : public hltypes::exception
	{
	public:
		/// @brief Constructor.
		ApplicationExitException();
		/// @brief Desstructor.
		~ApplicationExitException();

	};

}

#endif
