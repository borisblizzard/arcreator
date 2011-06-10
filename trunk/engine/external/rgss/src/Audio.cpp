#include <ruby.h>

#include <hltypes/exception.h>
#include <hltypes/util.h>
#include <xal/AudioManager.h>
#include <xal/Player.h>
#include <xal/Sound.h>

#include "Audio.h"
#include "CodeSnippets.h"
#include "rgss.h"

#define PATH_BGM "Audio/BGM/"
#define PATH_BGS "Audio/BGS/"
#define PATH_ME "Audio/ME/"
#define PATH_SE "Audio/SE/"
#define CATEGORY_BGM "BGM"
#define CATEGORY_BGS "BGS"
#define CATEGORY_ME "ME"
#define CATEGORY_SE "SE"

namespace rgss
{
	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	VALUE rb_mAudio;

	xal::Player* bgmPlayer;
	int bgmPitch;
	xal::Player* bgsPlayer;
	int bgsPitch;
	
	void Audio::init()
	{
		xal::mgr->createCategory(CATEGORY_BGM, xal::STREAMED, xal::STREAMED);
		xal::mgr->createSoundsFromPath(PATH_BGM, CATEGORY_BGM, PATH_BGM);
		xal::mgr->createCategory(CATEGORY_BGS, xal::STREAMED, xal::STREAMED);
		xal::mgr->createSoundsFromPath(PATH_BGS, CATEGORY_BGS, PATH_BGS);
		xal::mgr->createCategory(CATEGORY_ME, xal::LAZY, xal::LAZY);
		xal::mgr->createSoundsFromPath(PATH_ME, CATEGORY_ME, PATH_ME);
		xal::mgr->createCategory(CATEGORY_SE, xal::LAZY, xal::LAZY);
		xal::mgr->createSoundsFromPath(PATH_SE, CATEGORY_SE, PATH_SE);
		bgmPlayer = NULL;
		bgmPitch = 100;
		bgsPlayer = NULL;
		bgsPitch = 100;
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
		rb_define_module_function(rb_mAudio, "bgm_fade", RUBY_METHOD_FUNC(&Audio::rb_bgmFade), 1);
		rb_define_module_function(rb_mAudio, "bgm_stop", RUBY_METHOD_FUNC(&Audio::rb_bgmStop), 0);
		rb_define_module_function(rb_mAudio, "bgs_play", RUBY_METHOD_FUNC(&Audio::rb_bgsPlay), -1);
		rb_define_module_function(rb_mAudio, "bgs_fade", RUBY_METHOD_FUNC(&Audio::rb_bgsFade), 1);
		rb_define_module_function(rb_mAudio, "bgs_stop", RUBY_METHOD_FUNC(&Audio::rb_bgsStop), 0);
		rb_define_module_function(rb_mAudio, "me_play", RUBY_METHOD_FUNC(&Audio::rb_mePlay), -1);
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
		hstr filename = StringValuePtr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150); // unsupported now
		try
		{
			if (bgmPlayer != NULL && (!bgmPlayer->isPlaying() || bgmPlayer->getName() != filename))
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
			}
		}
		catch (hltypes::exception e)
		{
			rgss::log(hsprintf("file %s could not be played", filename.c_str()));
			rgss::log(e.message());
		}
		return Qnil;
	}

	VALUE Audio::rb_bgmFade(VALUE self, VALUE time)
	{
		xal::mgr->stopCategory(CATEGORY_BGM, (float)NUM2DBL(time) / 1000.f);
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
		hstr filename = StringValuePtr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150); // unsupported now
		try
		{
			if (bgsPlayer != NULL && (!bgsPlayer->isPlaying() || bgsPlayer->getName() != filename))
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
			}
		}
		catch (hltypes::exception e)
		{
			rgss::log(hsprintf("file %s could not be played", filename.c_str()));
			rgss::log(e.message());
		}
		return Qnil;
	}

	VALUE Audio::rb_bgsFade(VALUE self, VALUE time)
	{
		xal::mgr->stopCategory(CATEGORY_BGS, (float)NUM2DBL(time) / 1000.f);
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
		hstr filename = StringValuePtr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150); // unsupported now
		try
		{
			if (filename != "")
			{
				xal::mgr->play(filename, 0.0f, false, volume / 100.0f);
			}
		}
		catch (hltypes::exception e)
		{
			rgss::log(hsprintf("file %s could not be played", filename.c_str()));
			rgss::log(e.message());
		}
		return Qnil;
	}

	VALUE Audio::rb_meFade(VALUE self, VALUE time)
	{
		xal::mgr->stopCategory(CATEGORY_ME, (float)NUM2DBL(time) / 1000.f);
		return Qnil;
	}

	VALUE Audio::rb_meStop(VALUE self)
	{
		xal::mgr->stopCategory(CATEGORY_ME);
		return Qnil;
	}

	VALUE Audio::rb_sePlay(int argc, VALUE* argv, VALUE self)
	{
		VALUE arg1, arg2, arg3;
		rb_scan_args(argc, argv, "12", &arg1, &arg2, &arg3);
		hstr filename = StringValuePtr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150); // unsupported now
		try
		{
			if (filename != "")
			{
				xal::mgr->play(filename, 0.0f, false, volume / 100.0f);
			}
		}
		catch (hltypes::exception e)
		{
			rgss::log(hsprintf("file %s could not be played", filename.c_str()));
			rgss::log(e.message());
		}
		return Qnil;
	}

	VALUE Audio::rb_seStop(VALUE self)
	{
		xal::mgr->stopCategory(CATEGORY_SE);
		return Qnil;
	}
	
}
