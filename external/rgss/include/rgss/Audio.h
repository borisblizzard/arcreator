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
		/// @brief Starts BMG playback.
		/// @param[in] filename Filename of the BGM to play.
		/// @param[in] volume The volume of the BMG.
		/// @param[in] pitch The pitch of the BGM.
		static VALUE bgm_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch);
		/// @brief Starts BMG fadeout.
		/// @param[in] value The fadeout time in milliseconds.
		static VALUE bgm_fade(VALUE self, VALUE value);
		/// @brief Stops BGM playback.
		static VALUE bgm_stop(VALUE self);
		/// @brief Starts BGS playback.
		/// @param[in] filename Filename of the BGS to play.
		/// @param[in] volume The volume of the BGS.
		/// @param[in] pitch The pitch of the BGS.
		static VALUE bgs_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch);
		/// @brief Starts BGS fadeout.
		/// @param[in] value The fadeout time in milliseconds.
		static VALUE bgs_fade(VALUE self, VALUE value);
		/// @brief Stops BGS playback.
		static VALUE bgs_stop(VALUE self);
		/// @brief Starts ME playback.
		/// @param[in] filename Filename of the ME to play.
		/// @param[in] volume The volume of the ME.
		/// @param[in] pitch The pitch of the ME.
		static VALUE me_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch);
		/// @brief Starts ME fadeout.
		/// @param[in] value The fadeout time in milliseconds.
		static VALUE me_fade(VALUE self, VALUE value);
		/// @brief Stops ME playback.
		static VALUE me_stop(VALUE self);
		/// @brief Starts SE playback.
		/// @param[in] filename Filename of the SE to play.
		/// @param[in] volume The volume of the SE.
		/// @param[in] pitch The pitch of the SE.
		static VALUE se_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch);
		/// @brief Stops SE playback.
		static VALUE se_stop(VALUE self);
	};
}
#endif
