/// @file
/// @version 3.2
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Represents an audio category.

#ifndef XAL_CATEGORY_H
#define XAL_CATEGORY_H

#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#include "AudioManager.h"
#include "xalExport.h"

namespace xal
{
	/// @brief Defines an audio category which makes audio file organization easier.
	class xalExport Category
	{
	public:
		/// @brief Constructor.
		/// @param[in] name Category name.
		/// @param[in] bufferMode How to handle the intermediate Buffer of the Sound.
		/// @param[in] sourceMode How to handle the Source of the Sound.
		Category(chstr name, BufferMode bufferMode, SourceMode sourceMode);
		/// @brief Destructor.
		~Category();
		
		HL_DEFINE_GET(hstr, name, Name);
		HL_DEFINE_GET(float, gain, Gain);
		void setGain(float value);
		HL_DEFINE_GET(BufferMode, bufferMode, BufferMode);
		HL_DEFINE_GET(SourceMode, sourceMode, SourceMode);
		/// @return True if Sounds in this Category are streamed.
		bool isStreamed();
		/// @return True if Sounds in this Category have their data managed by the system.
		bool isMemoryManaged();
		
	protected:
		/// @brief Category name.
		hstr name;
		/// @brief Category gain.
		float gain;
		/// @brief How to handle the intermediate Buffer of the Sound.
		BufferMode bufferMode;
		/// @brief sourceMode How to handle the Source of the Sound.
		SourceMode sourceMode;
		
	};

}
#endif
