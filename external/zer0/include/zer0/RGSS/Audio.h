#ifndef ZER0_RGSS_AUDIO_H
#define ZER0_RGSS_AUDIO_H

#include <ruby.h>

#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		static VALUE rb_mAudio;

		class zer0Export Audio
		{
		public:
			/// @brief Initializes the module.
			static void init();
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();

			// @brief starts BMG playback.
			// @param[in] filename Filename of the BGM to play.
			// @param[in] volume The volume of the BMG.
			// @param[in] pitch The pitch of the BGM.
			static VALUE bgm_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch);
			// @brief starts BMG fadeout.
			// @param[in] value The Fadeout time in milliseconds.
			static VALUE bgm_fade(VALUE self, VALUE value);
			// @brief stops BGM playback.
			static VALUE bgm_stop(VALUE self);
			// @brief starts BGS playback.
			// @param[in] filename Filename of the BGS to play.
			// @param[in] volume The volume of the BGS.
			// @param[in] pitch The pitch of the BGS.
			static VALUE bgs_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch);
			// @brief starts BGS fadeout.
			// @param[in] value The fade out time in milliseconds.
			static VALUE bgs_fade(VALUE self, VALUE value);
			// @brief stops BGS playback.
			static VALUE bgs_stop(VALUE self);
			// @brief starts ME playback.
			// @param[in] filename Filename of the ME to play.
			// @param[in] volume The volume of the ME.
			// @param[in] pitch The pitch of the ME.
			static VALUE me_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch);
			// @brief starts ME fadeout.
			// @param[in] value The fade out time in milliseconds.
			static VALUE me_fade(VALUE self, VALUE value);
			// @brief stops ME playback.
			static VALUE me_stop(VALUE self);
			// @brief starts SE playback.
			// @param[in] filename Filename of the SE to play.
			// @param[in] volume The volume of the SE.
			// @param[in] pitch The pitch of the SE.
			static VALUE se_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch);
			// @brief stops SE playback.
			static VALUE se_stop(VALUE self);

		};
	
	}
}
#endif
