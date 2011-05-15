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

	void Audio::createRubyInterface()
	{
		rb_mAudio = rb_define_module("Audio");
		rb_define_module_function(rb_mAudio, "bgm_play", RUBY_METHOD_FUNC(&Audio::bgm_play), -1);
		rb_define_module_function(rb_mAudio, "bgm_fade", RUBY_METHOD_FUNC(&Audio::bgm_fade), 1);
		rb_define_module_function(rb_mAudio, "bgm_stop", RUBY_METHOD_FUNC(&Audio::bgm_stop), 0);
		rb_define_module_function(rb_mAudio, "bgs_play", RUBY_METHOD_FUNC(&Audio::bgs_play), -1);
		rb_define_module_function(rb_mAudio, "bgs_fade", RUBY_METHOD_FUNC(&Audio::bgs_fade), 1);
		rb_define_module_function(rb_mAudio, "bgs_stop", RUBY_METHOD_FUNC(&Audio::bgs_stop), 0);
		rb_define_module_function(rb_mAudio, "me_play", RUBY_METHOD_FUNC(&Audio::me_play), -1);
		rb_define_module_function(rb_mAudio, "me_fade", RUBY_METHOD_FUNC(&Audio::me_fade), 1);
		rb_define_module_function(rb_mAudio, "me_stop", RUBY_METHOD_FUNC(&Audio::me_stop), 0);
		rb_define_module_function(rb_mAudio, "se_play", RUBY_METHOD_FUNC(&Audio::se_play), -1);
		rb_define_module_function(rb_mAudio, "se_stop", RUBY_METHOD_FUNC(&Audio::se_stop), 0);
	}

	/****************************************************************************************
	 * Ruby Methods
	 ****************************************************************************************/

	VALUE Audio::bgm_play(int argc, VALUE* argv, VALUE self)
	{
		VALUE arg1, arg2, arg3;
		rb_scan_args(argc, argv, "12", &arg1, &arg2, &arg3);
		hstr filename = StringValuePtr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150); // unsupported now
		try
		{
			if (bgmPlayer != NULL && !bgmPlayer->isPlaying())
			{
				Audio::bgm_stop(self);
			}
			if (bgmPlayer != NULL)
			{
				if (bgmPlayer->getName() != filename)
				{
					Audio::bgm_stop(self);
					if (filename != "")
					{
						bgmPlayer = xal::mgr->createPlayer(filename);
						bgmPlayer->play(0.0f, true);
					}
				}
				if (bgmPlayer != NULL)
				{
					bgmPlayer->setGain(volume / 100.0f);
				}
			}
		}
		catch (hltypes::exception e)
		{
			rgss::log(hsprintf("file %s could not be played", filename.c_str()));
		}
		return Qnil;
	}

	VALUE Audio::bgm_fade(VALUE self, VALUE time)
	{
		xal::mgr->stopCategory(CATEGORY_BGM, (float)NUM2DBL(time) / 1000.f);
		return Qnil;
	}

	VALUE Audio::bgm_stop(VALUE self)
	{
		if (bgmPlayer != NULL)
		{
			bgmPlayer->stop();
			xal::mgr->destroyPlayer(bgmPlayer);
			bgmPlayer = NULL;
		}
		return Qnil;
	}

	VALUE Audio::bgs_play(int argc, VALUE* argv, VALUE self)
	{
		VALUE arg1, arg2, arg3;
		rb_scan_args(argc, argv, "12", &arg1, &arg2, &arg3);
		hstr filename = StringValuePtr(arg1);
		int volume = hclamp((NIL_P(arg2) ? 100 : NUM2INT(arg2)), 0, 100);
		int pitch = hclamp((NIL_P(arg3) ? 100 : NUM2INT(arg3)), 50, 150); // unsupported now
		try
		{
			if (bgsPlayer != NULL && !bgsPlayer->isPlaying())
			{
				Audio::bgs_stop(self);
			}
			if (bgsPlayer != NULL)
			{
				if (bgsPlayer->getName() != filename)
				{
					Audio::bgs_stop(self);
					if (filename != "")
					{
						bgsPlayer = xal::mgr->createPlayer(filename);
						bgsPlayer->play(0.0f, true);
					}
				}
				if (bgsPlayer != NULL)
				{
					bgsPlayer->setGain(volume / 100.0f);
				}
			}
		}
		catch (hltypes::exception e)
		{
			rgss::log(hsprintf("file %s could not be played", filename.c_str()));
		}
		return Qnil;
	}

	VALUE Audio::bgs_fade(VALUE self, VALUE time)
	{
		xal::mgr->stopCategory(CATEGORY_BGS, (float)NUM2DBL(time) / 1000.f);
		return Qnil;
	}

	VALUE Audio::bgs_stop(VALUE self)
	{
		if (bgsPlayer != NULL)
		{
			bgsPlayer->stop();
			xal::mgr->destroyPlayer(bgsPlayer);
			bgsPlayer = NULL;
		}
		return Qnil;
	}

	VALUE Audio::me_play(int argc, VALUE* argv, VALUE self)
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
		}
		return Qnil;
	}

	VALUE Audio::me_fade(VALUE self, VALUE time)
	{
		xal::mgr->stopCategory(CATEGORY_ME, (float)NUM2DBL(time) / 1000.f);
		return Qnil;
	}

	VALUE Audio::me_stop(VALUE self)
	{
		xal::mgr->stopCategory(CATEGORY_ME);
		return Qnil;
	}

	VALUE Audio::se_play(int argc, VALUE* argv, VALUE self)
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
		}
		return Qnil;
	}

	VALUE Audio::se_stop(VALUE self)
	{
		xal::mgr->stopCategory(CATEGORY_SE);
		return Qnil;
	}
	
}
