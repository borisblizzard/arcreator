#ifndef RGSS_BLEND_TYPE_H
#define RGSS_BLEND_TYPE_H

#include "rgssExport.h"

namespace rgss
{
	/// @brief Provides commonly used rendering functionality using an existing bitmap source.
	enum rgssExport BlendType
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
