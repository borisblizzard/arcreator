#ifndef LEGACY_AUDIO_H
#define LEGACY_AUDIO_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "legacyExport.h"

namespace legacy
{
	extern VALUE rb_mAudio;

	class legacyExport Audio
	{
	public:
		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Starts BGM playback.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "filename[, volume[, pitch]]".
		static VALUE rb_bgmPlay(int argc, VALUE* argv, VALUE self);
		/// @brief Pauses BGM playback.
		static VALUE rb_bgmPause(VALUE self);
		/// @brief Resumes paused BGM playback.
		/// @note Works only if a BGM has been paused previously.
		static VALUE rb_bgmResume(VALUE self);
		/// @brief Starts BGM fadeout.
		/// @param[in] time The fadeout time in miliseconds.
		static VALUE rb_bgmFade(VALUE self, VALUE time);
		/// @brief Stops BGM playback.
		static VALUE rb_bgmStop(VALUE self);
		/// @brief Starts BGS playback.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "filename[, volume[, pitch]]".
		static VALUE rb_bgsPlay(int argc, VALUE* argv, VALUE self);
		/// @brief Pauses BGS playback.
		static VALUE rb_bgsPause(VALUE self);
		/// @brief Resumes paused BGS playback.
		/// @note Works only if a BGS has been paused previously.
		static VALUE rb_bgsResume(VALUE self);
		/// @brief Starts BGS fadeout.
		/// @param[in] time The fadeout time in miliseconds.
		static VALUE rb_bgsFade(VALUE self, VALUE time);
		/// @brief Stops BGS playback.
		static VALUE rb_bgsStop(VALUE self);
		/// @brief Starts ME playback.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "filename[, volume[, pitch]]".
		static VALUE rb_mePlay(int argc, VALUE* argv, VALUE self);
		/// @brief Pauses ME playback.
		static VALUE rb_mePause(VALUE self);
		/// @brief Resumes paused ME playback.
		/// @note Works only if a ME has been paused previously.
		static VALUE rb_meResume(VALUE self);
		/// @brief Starts ME fadeout.
		/// @param[in] time The fadeout time in miliseconds.
		static VALUE rb_meFade(VALUE self, VALUE time);
		/// @brief Stops ME playback.
		static VALUE rb_meStop(VALUE self);
		/// @brief Starts SE playback.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "filename[, volume[, pitch]]".
		static VALUE rb_sePlay(int argc, VALUE* argv, VALUE self);
		/// @brief Stops SE playback.
		static VALUE rb_seStop(VALUE self);

	};

}
#endif
