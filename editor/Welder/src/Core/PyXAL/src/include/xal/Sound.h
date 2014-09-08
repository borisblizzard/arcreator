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
/// Represents a virtual entry of audio data in the sound system.

#ifndef XAL_SOUND_H
#define XAL_SOUND_H

#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>

#include "AudioManager.h"
#include "xalExport.h"

namespace xal
{
	class Buffer;
	class Category;

	/// @brief Provides audio data definition.
	class xalExport Sound
	{
	public:
		/// @brief Constructor.
		/// @param[in] filename Filename of the Sound.
		/// @param[in] category The Category where to register this Sound.
		/// @param[in] prefix Used to differentiate between Sounds that have the same filename (e.g. by using a directory path as prefix).
		Sound(chstr filename, Category* category, chstr prefix = "");
		/// @brief Destructor.
		~Sound();

		HL_DEFINE_GET(hstr, name, Name);
		HL_DEFINE_GET(hstr, filename, Filename);
		HL_DEFINE_GET(hstr, realFilename, RealFilename);
		HL_DEFINE_GET(Category*, category, Category);
		HL_DEFINE_GET(Buffer*, buffer, Buffer);

		/// @return Byte-size of the audio data.
		int getSize();
		/// @return Number of channels in the audio data.
		int getChannels();
		/// @return Sampling rate of the audio data.
		int getSamplingRate();
		/// @return Number of bits per sample in the audio data.
		int getBitsPerSample();
		/// @return Length of the audio data in seconds.
		float getDuration();
		/// @return File format of the underlying audio file.
		Format getFormat();
		/// @return True if the Sounds's Buffer accesses streamed data.
		bool isStreamed();

		/// @brief Reads the raw PCM data from the buffer.
		/// @param[in] size The byte-size of the data in the audio system.
		/// @param[out] output The buffer where to store the PCM data. It should be uninitialized. It will be set to NULL.
		/// @return The byte-size of the read data.
		/// @note If the underlying Source does not provide data as PCM, it will always be converted to PCM.
		int readPcmData(unsigned char** output);

	protected:
		/// @brief Name of the Sound.
		hstr name;
		/// @brief Logical filename of the Sound.
		hstr filename;
		/// @brief Actual filename of the Sound.
		/// @note This member includes the path as well as file extension.
		hstr realFilename;
		/// @brief Category to which the Sound is assigned.
		Category* category;
		/// @brief Buffer instance that handles
		Buffer* buffer;

		/// @return Finds the linked filename from an XLN file.
		/// @note TODO - will be possibly removed in the future
		hstr _findLinkedFile();

	};

}

#endif
