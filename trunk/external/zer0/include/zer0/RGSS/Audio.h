#ifndef ZER0_RGSS_AUDIO_H
#define ZER0_RGSS_AUDIO_H

#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class zer0Export Audio
		{
		public:
			// @brief starts BMG playback
			// @param[in] filename Filename of the BGM to play
			// @param[in] volume The volume of the BMG
			// @param[in] pitch The pitch of the BGM
			static void bgmPlay(hstr filename, int volume, int pitch);
			// @brief starts BMG fadeout
			// @param[in] time The Fadeout time in milliseconds
			static void bgmFade(int time);
			// @brief stops BGM playback
			static void bgmStop();
			// @brief starts BGS playback
			// @param[in] filename Filename of the BGS to play
			// @param[in] volume The volume of the BGS
			// @param[in] pitch The pitch of the BGS
			static void bgsPlay(hstr filename, int volume, int pitch);
			// @brief starts BGS fadeout
			// @param[in] time The fade out time in milliseconds
			static void bgsFade(int time);
			// @brief stops BGS playback
			static void bgsStop();
			// @brief starts ME playback
			// @param[in] filename Filename of the ME to play
			// @param[in] volume The volume of the ME
			// @param[in] pitch The pitch of the ME
			static void mePlay(hstr filename, int volume, int pitch);
			// @brief starts ME fadeout
			// @param[in] time The fade out time in milliseconds
			static void meFade(int time);
			// @brief stops ME playback
			static void meStop();
			// @brief starts SE playback
			// @param[in] filename Filename of the SE to play
			// @param[in] volume The volume of the SE
			// @param[in] pitch The pitch of the SE
			static void sePlay(hstr filename, int volume, int pitch);
			// @brief stops SE playback
			static void seStop();

		protected:
			Audio();
			~Audio();

		};
	
	}
}
#endif
