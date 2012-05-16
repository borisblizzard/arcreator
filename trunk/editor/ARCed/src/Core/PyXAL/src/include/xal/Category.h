/// @file
/// @author  Boris Mikic
/// @version 2.6
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
		Category(chstr name, HandlingMode sourceMode = FULL, HandlingMode bufferMode = FULL, bool memoryManaged = false);
		~Category();
		
		hstr getName() { return this->name; }
		float getGain() { return this->gain; }
		void setGain(float value) { this->gain = value; }
		HandlingMode getSourceMode() { return this->sourceMode; }
		HandlingMode getBufferMode() { return this->bufferMode; }
		bool isMemoryManaged() { return this->memoryManaged; }
		bool isStreamed();
		
		DEPRECATED_ATTRIBUTE HandlingMode getLoadMode() { return this->getSourceMode(); }
		DEPRECATED_ATTRIBUTE HandlingMode getDecodeMode() { return this->getBufferMode(); }

	protected:
		hstr name;
		float gain;
		HandlingMode sourceMode;
		HandlingMode bufferMode;
		bool memoryManaged;
		
	};

}
#endif
