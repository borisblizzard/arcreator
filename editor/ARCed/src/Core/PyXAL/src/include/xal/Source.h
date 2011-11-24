/// @file
/// @author  Boris Mikic
/// @version 2.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides an interface for audio sources.

#ifndef XAL_DECODER_H
#define XAL_DECODER_H

#include <hltypes/hstring.h>

#include "AudioManager.h"
#include "xalExport.h"

namespace xal
{
	class xalExport Source
	{
	public:
		Source(chstr filename);
		virtual ~Source();

		int getSize() { return this->size; }
		int getChunkSize() { return this->chunkSize; }
		int getChannels() { return this->channels; }
		int getSamplingRate() { return this->samplingRate; }
		int getBitsPerSample() { return this->bitsPerSample; }
		float getDuration() { return this->duration; }
		bool isOpen() { return this->streamOpen; }

		virtual bool open();
		virtual void close() { }
		virtual void rewind() { }
		virtual bool load(unsigned char* output);
		virtual int loadChunk(unsigned char* output, int size = STREAM_BUFFER_SIZE);
		
	protected:
		hstr filename;
		int size;
		int channels;
		int samplingRate;
		int bitsPerSample;
		float duration;
		int chunkSize;
		bool streamOpen;

	};

}

#endif
