/// @file
/// @author  Boris Mikic
/// @version 3.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Represents an audio category.

#ifndef XAL_CATEGORY_H
#define XAL_CATEGORY_H

#include <hltypes/hstring.h>

#include "AudioManager.h"
#include "xalExport.h"

namespace xal
{
	class xalExport Category
	{
	public:
		Category(chstr name, BufferMode bufferMode, SourceMode sourceMode);
		~Category();
		
		hstr getName() { return this->name; }
		float getGain() { return this->gain; }
		void setGain(float value) { this->gain = value; }
		BufferMode getBufferMode() { return this->bufferMode; }
		SourceMode getSourceMode() { return this->sourceMode; }
		bool isStreamed();
		bool isMemoryManaged();
		
	protected:
		hstr name;
		float gain;
		BufferMode bufferMode;
		SourceMode sourceMode;
		
	};

}
#endif
