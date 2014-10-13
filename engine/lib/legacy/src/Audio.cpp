#include <ruby.h>

#include <hltypes/exception.h>
#include <hltypes/harray.h>
#include <hltypes/hlog.h>
#include <hltypes/hltypesUtil.h>
#include <hltypes/hstring.h>
#include <xal/AudioManager.h>
#include <xal/Player.h>
#include <xal/Sound.h>

#include "Audio.h"
#include "CodeSnippets.h"
#include "legacy.h"

#define PATH_BGM "Audio/BGM/"
#define PATH_BGS "Audio/BGS/"
#define PATH_ME "Audio/ME/"
#define PATH_SE "Audio/SE/"
#define CATEGORY_BGM "BGM"
#define CATEGORY_BGS "BGS"
#define CATEGORY_ME "ME"
#define CATEGORY_SE "SE"

namespace legacy
{
	VALUE rb_mAudio;

	/****************************************************************************************
	 * Pure C++ code
	 ****************************************************************************************/

	xal::Player* bgmPlayer;
	int bgmPitch;
	xal::Player* bgsPlayer;
	int bgsPitch;
	xal::Player* mePlayer;
	harray<xal::Player*> sePlayers;
	
	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	void Audio::init()
	{
		xal::mgr->setIdlePlayerUnloadTime(300.0f);
		xal::mgr->createCategory(CATEGORY_BGM, xal::STREAMED, xal::DISK);
		xal::mgr->createSoundsFromPath(PATH_BGM, CATEGORY_BGM, PATH_BGM);
		xal::mgr->createCategory(CATEGORY_BGS, xal::STREAMED, xal::DISK);
		xal::mgr->createSoundsFromPath(PATH_BGS, CATEGORY_BGS, PATH_BGS);
		xal::mgr->createCategory(CATEGORY_ME, xal::MANAGED, xal::DISK);
		xal::mgr->createSoundsFromPath(PATH_ME, CATEGORY_ME, PATH_ME);
		xal::mgr->createCategory(CATEGORY_SE, xal::MANAGED, xal::DISK);
		xal::mgr->createSoundsFromPath(PATH_SE, CATEGORY_SE, PATH_SE);
		bgmPlayer = NULL;
		bgmPitch = 100;
		bgsPlayer = NULL;
		bgsPitch = 100;
		mePlayer = NULL;
	}

	void Audio::destroy()
	{
		rb_bgmStop(rb_mAudio);
		rb_bgsStop(rb_mAudio);
		rb_meStop(rb_mAudio);
		rb_seStop(rb_mAudio);
	}

	void Audio::createRubyInterface()
	{
		rb_mAudio = rb_define_module("Audio");
		rb_define_module_function(rb_mAudio, "bgm_play", RUBY_METHOD_FUNC(&Audio::rb_bgmPlay), -1);
		rb_define_module_function(rb_mAudio, "bgm_pause", RUBY_METHOD_FUNC(&Audio::rb_bgmPause), 0);
		rb_define_module_function(rb_mAudio, "bgm_resume", RUBY_METHOD_FUNC(&Audio::rb_bgmResume), 0);
		rb_define_module_function(rb_mAudio, "bgm_fade", RUBY_METHOD_FUNC(&Audio::rb_bgmFade), 1);
		rb_define_module_function(rb_mAudio, "bgm_stop", RUBY_METHOD_FUNC(&Audio::rb_bgmStop), 0);
		rb_define_module_function(rb_mAudio, "bgs_play", RUBY_METHOD_FUNC(&Audio::rb_bgsPlay), -1);
		rb_define_module_function(rb_mAudio, "bgs_pause", RUBY_METHOD_FUNC(&Audio::rb_bgsPause), 0);
		rb_define_module_function(rb_mAudio, "bgs_resume", RUBY_METHOD_FUNC(&Audio::rb_bgsResume), 0);
		rb_define_module_function(rb_mAudio, "bgs_fade", RUBY_METHOD_FUNC(&Audio::rb_bgsFade), 1);
		rb_define_module_function(rb_mAudio, "bgs_stop", RUBY_METHOD_FUNC(&Audio::rb_bgsStop), 0);
		rb_define_module_function(rb_mAudio, "me_play", RUBY_METHOD_FUNC(&Audio::rb_mePlay), -1);
		rb_define_module_function(rb_mAudio, "me_pause", RUBY_METHOD_FUNC(&Audio::rb_mePause), 0);
		rb_define_module_function(rb_mAudio, "me_resume", RUBY_METHOD_FUNC(&Audio::rb_meResume), 0);
		rb_define_module_function(rb_mAudio, "me_fade", RUBY_METHOD_FUNC(&Audio::rb_meFade), 1);
		rb_define_module_function(rb_mAudio, "me_stop", RUBY_METHOD_FUNC(&Audio::rb_meStop), 0);
		rb_define_module_function(rb_mAudio, "se_play", RUBY_METHOD_FUNC(&Audio::rb_sePlay), -1);
		rb_define_module_function(rb_mAudio, "se_stop", RUBY_METHOD_FUNC(&Audio::rb_seStop), 0);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Audio::rb_bgmPlay(int argc, VALUE* argv, VALUE self)
	{
		VALUE arg1, arg2, arg3;
		rb_scan_args(argc, argv, "12", &arg1, &arg2, &arg3);
		RB_CHECK_TYPE(arg1, rb_cString);
		hstr filename = StringValueCStr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150);
		try
		{
			if (bgmPlayer != NULL && (!bgmPlayer->isPlaying() ||
				bgmPlayer->getName() != filename || bgmPitch != pitch))
			{
				Audio::rb_bgmStop(self);
			}
			if (bgmPlayer == NULL && filename != "")
			{
				bgmPlayer = xal::mgr->createPlayer(filename);
				bgmPlayer->play(0.0f, true);
			}
			if (bgmPlayer != NULL)
			{
				bgmPlayer->setGain(volume / 100.0f);
				bgmPlayer->setPitch(pitch / 100.0f);
				bgmPitch = pitch;
			}
		}
		catch (hltypes::exception& e)
		{
			hlog::error(legacy::logTag, "File could not be played: " + filename);
			hlog::error(legacy::logTag, e.message());
		}
		return Qnil;
	}

	VALUE Audio::rb_bgmPause(VALUE self)
	{
		if (bgmPlayer != NULL && !bgmPlayer->isPaused())
		{
			bgmPlayer->pause();
		}
		return Qnil;
	}

	VALUE Audio::rb_bgmResume(VALUE self)
	{
		if (bgmPlayer != NULL && bgmPlayer->isPaused())
		{
			bgmPlayer->play();
		}
		return Qnil;
	}

	VALUE Audio::rb_bgmFade(VALUE self, VALUE time)
	{
		if (bgmPlayer != NULL)
		{
			bgmPlayer->stop((float)NUM2DBL(time) / 1000.f);
		}
		return Qnil;
	}

	VALUE Audio::rb_bgmStop(VALUE self)
	{
		if (bgmPlayer != NULL)
		{
			bgmPlayer->stop();
			xal::mgr->destroyPlayer(bgmPlayer);
			bgmPlayer = NULL;
		}
		return Qnil;
	}

	VALUE Audio::rb_bgsPlay(int argc, VALUE* argv, VALUE self)
	{
		VALUE arg1, arg2, arg3;
		rb_scan_args(argc, argv, "12", &arg1, &arg2, &arg3);
		RB_CHECK_TYPE(arg1, rb_cString);
		hstr filename = StringValueCStr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150);
		try
		{
			if (bgsPlayer != NULL && (!bgsPlayer->isPlaying() ||
				bgsPlayer->getName() != filename || bgsPitch != pitch))
			{
				Audio::rb_bgsStop(self);
			}
			if (bgsPlayer == NULL && filename != "")
			{
				bgsPlayer = xal::mgr->createPlayer(filename);
				bgsPlayer->play(0.0f, true);
			}
			if (bgsPlayer != NULL)
			{
				bgsPlayer->setGain(volume / 100.0f);
				bgsPlayer->setPitch(pitch / 100.0f);
				bgsPitch = pitch;
			}
		}
		catch (hltypes::exception& e)
		{
			hlog::write(legacy::logTag, "File could not be played: " + filename);
			hlog::write(legacy::logTag, e.message());
		}
		return Qnil;
	}

	VALUE Audio::rb_bgsPause(VALUE self)
	{
		if (bgsPlayer != NULL && !bgsPlayer->isPaused())
		{
			bgsPlayer->pause();
		}
		return Qnil;
	}

	VALUE Audio::rb_bgsResume(VALUE self)
	{
		if (bgsPlayer != NULL && bgsPlayer->isPaused())
		{
			bgsPlayer->play();
		}
		return Qnil;
	}

	VALUE Audio::rb_bgsFade(VALUE self, VALUE time)
	{
		if (bgsPlayer != NULL)
		{
			bgsPlayer->stop((float)NUM2DBL(time) / 1000.f);
		}
		return Qnil;
	}

	VALUE Audio::rb_bgsStop(VALUE self)
	{
		if (bgsPlayer != NULL)
		{
			bgsPlayer->stop();
			xal::mgr->destroyPlayer(bgsPlayer);
			bgsPlayer = NULL;
		}
		return Qnil;
	}

	VALUE Audio::rb_mePlay(int argc, VALUE* argv, VALUE self)
	{
		VALUE arg1, arg2, arg3;
		rb_scan_args(argc, argv, "12", &arg1, &arg2, &arg3);
		RB_CHECK_TYPE(arg1, rb_cString);
		hstr filename = StringValueCStr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150);
		try
		{
			if (mePlayer != NULL && (!mePlayer->isPlaying() || mePlayer->getName() != filename))
			{
				Audio::rb_bgsStop(self);
			}
			if (mePlayer == NULL && filename != "")
			{
				mePlayer = xal::mgr->createPlayer(filename);
				mePlayer->play();
			}
			if (mePlayer != NULL)
			{
				mePlayer->setGain(volume / 100.0f);
				mePlayer->setPitch(pitch / 100.0f);
			}
		}
		catch (hltypes::exception& e)
		{
			hlog::write(legacy::logTag, "File could not be played: " + filename);
			hlog::write(legacy::logTag, e.message());
		}
		return Qnil;
	}

	VALUE Audio::rb_mePause(VALUE self)
	{
		if (mePlayer != NULL && !mePlayer->isPaused())
		{
			mePlayer->pause();
		}
		return Qnil;
	}

	VALUE Audio::rb_meResume(VALUE self)
	{
		if (mePlayer != NULL && mePlayer->isPaused())
		{
			mePlayer->play();
		}
		return Qnil;
	}

	VALUE Audio::rb_meFade(VALUE self, VALUE time)
	{
		if (mePlayer != NULL)
		{
			mePlayer->stop((float)NUM2DBL(time) / 1000.f);
		}
		return Qnil;
	}

	VALUE Audio::rb_meStop(VALUE self)
	{
		if (mePlayer != NULL)
		{
			mePlayer->stop();
			xal::mgr->destroyPlayer(mePlayer);
			mePlayer = NULL;
		}
		return Qnil;
	}

	VALUE Audio::rb_sePlay(int argc, VALUE* argv, VALUE self)
	{
		VALUE arg1, arg2, arg3;
		rb_scan_args(argc, argv, "12", &arg1, &arg2, &arg3);
		RB_CHECK_TYPE(arg1, rb_cString);
		hstr filename = StringValueCStr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150);
		// first remove inished players
		harray<xal::Player*> players = sePlayers;
		foreach (xal::Player*, it, players)
		{
			if (!(*it)->isPlaying())
			{
				xal::mgr->destroyPlayer(*it);
				sePlayers -= (*it);
			}
		}
		try
		{
			xal::Player* player = xal::mgr->createPlayer(filename);
			player->play();
			player->setGain(volume / 100.0f);
			player->setPitch(pitch / 100.0f);
			sePlayers += player;
		}
		catch (hltypes::exception& e)
		{
			hlog::write(legacy::logTag, "File could not be played: " + filename);
			hlog::write(legacy::logTag, e.message());
		}
		return Qnil;
	}

	VALUE Audio::rb_seStop(VALUE self)
	{
		foreach (xal::Player*, it, sePlayers)
		{
			(*it)->stop();
			xal::mgr->destroyPlayer(*it);
		}
		sePlayers.clear();
		return Qnil;
	}
	
}
