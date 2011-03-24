#include <ruby.h>

#include "RGSS/Audio.h"
#include "CodeSnippets.h"

namespace zer0
{
	namespace RGSS
	{
		void Audio::init()
		{
		}

		void Audio::createRubyInterface()
		{
			rb_mAudio = rb_define_module("Audio");
			rb_define_module_function(rb_mAudio, "bgm_play", RUBY_METHOD_FUNC(&Audio::bgm_play), 3);
			rb_define_module_function(rb_mAudio, "bgm_fade", RUBY_METHOD_FUNC(&Audio::bgm_fade), 1);
			rb_define_module_function(rb_mAudio, "bgm_stop", RUBY_METHOD_FUNC(&Audio::bgm_stop), 0);
			rb_define_module_function(rb_mAudio, "bgs_play", RUBY_METHOD_FUNC(&Audio::bgs_play), 3);
			rb_define_module_function(rb_mAudio, "bgs_fade", RUBY_METHOD_FUNC(&Audio::bgs_fade), 1);
			rb_define_module_function(rb_mAudio, "bgs_stop", RUBY_METHOD_FUNC(&Audio::bgs_stop), 0);
			rb_define_module_function(rb_mAudio, "me_play", RUBY_METHOD_FUNC(&Audio::me_play), 3);
			rb_define_module_function(rb_mAudio, "me_fade", RUBY_METHOD_FUNC(&Audio::me_fade), 1);
			rb_define_module_function(rb_mAudio, "me_stop", RUBY_METHOD_FUNC(&Audio::me_stop), 0);
			rb_define_module_function(rb_mAudio, "se_play", RUBY_METHOD_FUNC(&Audio::se_play), 3);
			rb_define_module_function(rb_mAudio, "se_stop", RUBY_METHOD_FUNC(&Audio::se_stop), 0);
		}

		VALUE Audio::bgm_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch)
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

		VALUE Audio::bgs_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch)
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

		VALUE Audio::me_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch)
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

		VALUE Audio::se_play(VALUE self, VALUE filename, VALUE volume, VALUE pitch)
		{
			return Qnil;
		}

		VALUE Audio::se_stop(VALUE self)
		{
			return Qnil;
		}
	
	}
}
