#include <ruby.h>

#include "Audio.h"
#include "CodeSnippets.h"

namespace rgss
{
	/****************************************************************************************
	 * Ruby Interfacing, Creation, Destruction, Systematics
	 ****************************************************************************************/

	VALUE rb_mAudio;
	
	void Audio::init()
	{
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
		return Qnil;
	}

	VALUE Audio::bgm_fade(VALUE self, VALUE value)
	{
		return Qnil;
	}

	VALUE Audio::bgm_stop(VALUE self)
	{
		return Qnil;
	}

	VALUE Audio::bgs_play(int argc, VALUE* argv, VALUE self)
	{
		return Qnil;
	}

	VALUE Audio::bgs_fade(VALUE self, VALUE time)
	{
		return Qnil;
	}

	VALUE Audio::bgs_stop(VALUE self)
	{
		return Qnil;
	}

	VALUE Audio::me_play(int argc, VALUE* argv, VALUE self)
	{
		return Qnil;
	}

	VALUE Audio::me_fade(VALUE self, VALUE time)
	{
		return Qnil;
	}

	VALUE Audio::me_stop(VALUE self)
	{
		return Qnil;
	}

	VALUE Audio::se_play(int argc, VALUE* argv, VALUE self)
	{
		return Qnil;
	}

	VALUE Audio::se_stop(VALUE self)
	{
		return Qnil;
	}
	
}
