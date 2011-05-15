#ifndef RGSS_AUDIO_H
#define RGSS_AUDIO_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_mAudio;

	class rgssExport Audio
	{
	public:
		/// @brief Initializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Starts BGM playback.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "filename[, volume[, pitch]]".
		static VALUE bgm_play(int argc, VALUE* argv, VALUE self);
		/// @brief Starts BGM fadeout.
		/// @param[in] time The fadeout time in miliseconds.
		static VALUE bgm_fade(VALUE self, VALUE time);
		/// @brief Stops BGM playback.
		static VALUE bgm_stop(VALUE self);
		/// @brief Starts BGS playback.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "filename[, volume[, pitch]]".
		static VALUE bgs_play(int argc, VALUE* argv, VALUE self);
		/// @brief Starts BGS fadeout.
		/// @param[in] time The fadeout time in miliseconds.
		static VALUE bgs_fade(VALUE self, VALUE time);
		/// @brief Stops BGS playback.
		static VALUE bgs_stop(VALUE self);
		/// @brief Starts ME playback.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "filename[, volume[, pitch]]".
		static VALUE me_play(int argc, VALUE* argv, VALUE self);
		/// @brief Starts ME fadeout.
		/// @param[in] time The fadeout time in miliseconds.
		static VALUE me_fade(VALUE self, VALUE time);
		/// @brief Stops ME playback.
		static VALUE me_stop(VALUE self);
		/// @brief Starts SE playback.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "filename[, volume[, pitch]]".
		static VALUE se_play(int argc, VALUE* argv, VALUE self);
		/// @brief Stops SE playback.
		static VALUE se_stop(VALUE self);

	};
}
#endif
