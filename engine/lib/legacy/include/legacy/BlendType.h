#ifndef LEGACY_BLEND_TYPE_H
#define LEGACY_BLEND_TYPE_H

#include "legacyExport.h"

namespace legacy
{
	/// @brief Provides commonly used rendering functionality using an existing bitmap source.
	enum legacyExport BlendType
	{
		/// @brief Normal alpha blending.
		Normal = 0,
		/// @brief Positive blending.
		Positive = 1,
		/// @brief Negative blending.
		Negative = 2
	};

}
#endif
