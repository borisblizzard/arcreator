/// @file
/// @version 3.4
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Provides a buffer for audio data.

#ifndef XAL_BUFFER_H
#define XAL_BUFFER_H

#include <hltypes/hltypesUtil.h>
#include <hltypes/hstream.h>
#include <hltypes/hstring.h>

#include "AudioManager.h"
#include "xalExport.h"

namespace xal
{
	class BufferAsync;
	class Player;
	class Sound;
	class Source;

	/// @brief Provides a mechanism for data access without requiring to understand the underlying buffering/streaming/reading system.
	class xalExport Buffer
	{
	public:
		friend class AudioManager;
		friend class BufferAsync;

		/// @brief Constructor.
		/// @param[in] sound Sound object for which to create the buffer.
		Buffer(Sound* sound);
		/// @brief Destructor.
		~Buffer();

		HL_DEFINE_GET(hstr, filename, Filename);
		HL_DEFINE_GET(int, fileSize, FileSize);
		inline hstream& getStream() { return this->stream; }
		HL_DEFINE_GET(Source*, source, Source);
		HL_DEFINE_GET(float, idleTime, IdleTime);

		int getSize();
		int getChannels();
		int getSamplingRate();
		int getBitsPerSample();
		float getDuration();
		Format getFormat();
		/// @return True if the Buffer's data is loaded.
		bool isLoaded();
		/// @return True if the Buffer's data is queued for asynchronous loading.
		bool isAsyncLoadQueued();
		/// @return True if the Buffer accesses streamed data.
		bool isStreamed();
		/// @return True if the Buffer's data is managed.
		bool isMemoryManaged();
		// TODO
		//bool setOffset(int value);

		/// @brief Prepares the Buffer by pre-loaded meta-data and getting Sources ready to provide audio data.
		void prepare();
		/// @brief Prepares the Buffer by pre-loaded meta-data and getting Sources ready to provide audio data asynchronously.
		/// @return True if the Buffer was queued successfully.
		bool prepareAsync();
		/// @brief Loads audio data from the Source.
		/// @param[in] looping Whether the data should be loaded in a looped manner.
		/// @param[in] size The maximum number of bytes to load.
		/// @return The number of bytes loaded.
		int load(bool looping, int size = STREAM_BUFFER_SIZE);
		/// @brief Attempts to bind a Player to this Buffer.
		/// @param[in] player The Player to bind.
		/// @param[in] playerPaused Whether the player is currently paused.
		void bind(Player* player, bool playerPaused);
		/// @brief Attempts to unbind a Player to this Buffer.
		/// @param[in] player The Player to bind.
		/// @param[in] playerPaused Whether the player is currently paused.
		/// @note Players are only truly unbound if they are not paused. This method also discards buffered data if no Players are bound to save memory (depends on the Buffer Mode).
		void unbind(Player* player, bool playerPaused);
		/// @brief Notifies the Buffer that it's being used.
		void keepLoaded();
		/// @brief Rewinds the Source to the beginning.
		/// @note This affects the underlying audio data, not the data provided by the Buffer.
		void rewind();

		/// @brief Calculates the byte-size to which the data will be converted in the underlying audio system.
		/// @param[in] size The byte-size of the actual data in this Buffer.
		/// @return The byte-size of the data in the audio system.
		/// @note This is only used by some audio systems.
		int calcOutputSize(int size);
		/// @brief Calculates the byte-size from which the data will be converted when getting data from the underlying audio system.
		/// @param[in] size The byte-size of the data in the audio system.
		/// @return The byte-size of the actual data in this Buffer.
		/// @note This is only used by some audio systems.
		int calcInputSize(int size);
		/// @brief Reads the raw PCM data from the buffer.
		/// @param[out] output The data stream where to store the PCM data.
		/// @note If the Source does not provide data as PCM, it will always be converted to PCM.
		void readPcmData(hstream& output);

	protected:
		/// @brief Filename of the source.
		hstr filename;
		/// @brief File size of the source.
		int fileSize;
		/// @brief Buffer Mode to use.
		BufferMode mode;
		/// @brief Whether the underlying source was loaded.
		bool loaded;
		/// @brief Current data provided by the buffer.
		hstream stream;
		/// @brief Flag for whether an asynchronous load was queued.
		bool asyncLoadQueued;
		/// @brief Flag for whether asynchronously loaded data should be discarded.
		bool asyncLoadDiscarded;
		/// @brief Mutex for access of asynchronously loaded data.
		hmutex asyncLoadMutex;
		/// @brief Connected Source from which data is read.
		Source* source;
		/// @brief Whether meta-data has been loaded.
		bool loadedMetaData;
		/// @brief Size of the Source's audio data.
		int size;
		/// @brief Number of channels of the Source's audio data.
		int channels;
		/// @brief Sampling rate of the Source's audio data.
		int samplingRate;
		/// @brief Number of bits per sample of the Source's audio data.
		int bitsPerSample;
		/// @brief Duration of the audio data in seconds.
		float duration;
		/// @brief List of bound Player instances.
		/// @note This is mainly needed for discarding unused Buffers/Sources.
		harray<Player*> boundPlayers;
		/// @brief How much time has passed since the last access of this buffer (in seconds).
		float idleTime;
		
		/// @brief Updates the Buffer.
		/// @param[in] timeDelta Time passed since the last update.
		void _update(float timeDelta);
		/// @brief Tries to load meta-data from the Source.
		void _tryLoadMetaData();
		/// @brief Tries to free up memory.
		/// @return True if any memory was freed.
		bool _tryClearMemory();

		/// @brief Loads the async data from the disk into a stream.
		/// @return True if there is a stream ready. False if loading was canceled in the meantime.
		bool _prepareAsyncStream();
		/// @brief Decodes the asynchronously loaded data.
		/// @param[in] stream The stream from which to decode the data.
		void _decodeFromAsyncStream();
		/// @brief Waits for the Buffer to load asynchronously.
		/// @param[in] timeout Max time to wait.
		/// @note A timeout value of 0.0 means indefinitely.
		void _waitForAsyncLoad(float timeout = 0.0f);

	};

}

#endif
