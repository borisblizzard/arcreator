/// @file
/// @author  Boris Mikic
/// @version 2.5
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides a buffer for audio data.

#ifndef XAL_BUFFER_H
#define XAL_BUFFER_H

#include <hltypes/hstring.h>

#include "AudioManager.h"
#include "xalExport.h"

namespace xal
{
	class Source;

	class xalExport Buffer
	{
	public:
		Buffer(chstr filename, HandlingMode loadMode, HandlingMode decodeMode);
		~Buffer();

		chstr getFilename() { return this->filename; }
		int getFileSize() { return this->fileSize; }
		unsigned char* getStream() { return this->stream; }
		Source* getSource() { return this->source; }

		int getSize();
		int getChannels();
		int getSamplingRate();
		int getBitsPerSample();
		float getDuration();
		Format getFormat();
		bool isStreamed();
		bool setOffset(int value);

		void prepare();
		int load(bool looping, int size = STREAM_BUFFER_SIZE);
		void release();
		void free();
		void rewind();

		int convertToOutputSize(int size);
		int convertToInputSize(int size);

	protected:
		hstr filename;
		int fileSize;
		HandlingMode loadMode;
		HandlingMode decodeMode;
		bool loaded;
		bool decoded;
		unsigned char* stream;
		int streamSize;
		Source* source;

	};

}

#endif
