/// @file
/// @author  Boris Mikic
/// @version 2.62
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides an interface for audio sources.

#ifndef XAL_SOURCE_H
#define XAL_SOURCE_H

#include <hltypes/hsbase.h>
#include <hltypes/hstring.h>

#include "AudioManager.h"
#include "xalExport.h"

namespace xal
{
	class Category;

	class xalExport Source
	{
	public:
		Source(chstr filename, Category* category);
		virtual ~Source();

		hstr getFilename() { return this->filename; }
		SourceMode getMode() { return this->mode; }
		bool isOpen() { return this->streamOpen; }
		int getSize() { return this->size; }
		int getChunkSize() { return this->chunkSize; }
		int getChannels() { return this->channels; }
		int getSamplingRate() { return this->samplingRate; }
		int getBitsPerSample() { return this->bitsPerSample; }
		float getDuration() { return this->duration; }

		virtual bool open();
		virtual void close();
		virtual void rewind();
		virtual bool load(unsigned char* output);
		virtual int loadChunk(unsigned char* output, int size = STREAM_BUFFER_SIZE);
		
	protected:
		hstr filename;
		SourceMode mode;
		bool streamOpen;
		int size;
		int channels;
		int samplingRate;
		int bitsPerSample;
		float duration;
		int chunkSize;
		hsbase* stream;

	};

}

#endif
