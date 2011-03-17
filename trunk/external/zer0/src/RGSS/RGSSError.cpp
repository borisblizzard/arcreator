#include <ruby.h>

#include <hltypes/hstring.h>

#include "RGSS/RGSSError.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void RGSSError::createRubyInterface()
		{
		}

		RGSSError::RGSSError(chstr message) : hltypes::exception(message, __FILE__, __LINE__)
		{
		}
	
	}
}
