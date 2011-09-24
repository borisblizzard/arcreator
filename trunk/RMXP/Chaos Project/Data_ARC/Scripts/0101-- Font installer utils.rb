# 
# = fileutils.rb
# 
# Copyright (c) 2000-2005 Minero Aoki <aamine@loveruby.net>
# 
# This program is free software.
# You can distribute/modify this program under the same terms of ruby.
# 
# == module FileUtils
#

module FileUtils

  def self.private_module_function(name)   #:nodoc:
    module_function name
    private_class_method name
  end

  OPT_TABLE = {}   #:nodoc: internal use only
  
  def copy(src, dest, options = {})
    fu_check_options options, :preserve, :noop, :verbose
    fu_output_message "cp#{options[:preserve] ? ' -p' : ''} #{[src,dest].flatten.join ' '}" if options[:verbose]
    return if options[:noop]
    fu_each_src_dest(src, dest) do |s, d|
      copy_file s, d, options[:preserve]
    end
  end
  module_function :copy

  OPT_TABLE['copy'] = %w( noop verbose preserve )

  def fu_check_options(options, *optdecl)   #:nodoc:
    h = options.dup
    optdecl.each do |name|
      h.delete name
    end
    raise ArgumentError, "no such option: #{h.keys.join(' ')}" unless h.empty?
  end
  private_module_function :fu_check_options
  
  def fu_each_src_dest(src, dest)   #:nodoc:
    fu_each_src_dest0(src, dest) do |s, d|
      raise ArgumentError, "same file: #{s} and #{d}" if fu_same?(s, d)
      yield s, d
    end
  end
  private_module_function :fu_each_src_dest

  def fu_each_src_dest0(src, dest)   #:nodoc:
    if src.is_a?(Array)
      src.each do |s|
        s = s.to_str
        yield s, File.join(dest, File.basename(s))
      end
    else
      src = src.to_str
      if File.directory?(dest)
        yield src, File.join(dest, File.basename(src))
      else
        yield src, dest.to_str
      end
    end
  end
  private_module_function :fu_each_src_dest0

  def fu_same?(a, b)   #:nodoc:
    if fu_have_st_ino?
      st1 = File.stat(a)
      st2 = File.stat(b)
      st1.dev == st2.dev && st1.ino == st2.ino
    else
      File.expand_path(a) == File.expand_path(b)
    end
  rescue Errno::ENOENT
    return false
  end
  private_module_function :fu_same?

  def fu_have_st_ino?   #:nodoc:
    !fu_windows?
  end
  private_module_function :fu_have_st_ino?

  def copy_file(src, dest, preserve = false, dereference = true)
    ent = Entry_.new(src, nil, dereference)
    ent.copy_file dest
    ent.copy_metadata dest if preserve
  end
  module_function :copy_file

  module StreamUtils_
  
    private
    
    def fu_windows?
      /mswin|mingw|bccwin|wince|emx/ =~ RUBY_PLATFORM
    end
  
    def fu_copy_stream0(src, dest, blksize)   #:nodoc:
      # FIXME: readpartial?
      while s = src.read(blksize)
        dest.write s
      end
    end

    def fu_blksize(st)
      s = st.blksize
      return nil unless s
      return nil if s == 0
      s
    end

    def fu_default_blksize
      1024
    end

  end

  include StreamUtils_
  extend StreamUtils_

  class Entry_   #:nodoc: internal use only
    include StreamUtils_

    def initialize(a, b = nil, deref = false)
      @prefix = @rel = @path = nil
      if b
        @prefix = a
        @rel = b
      else
        @path = a
      end
      @deref = deref
      @stat = nil
      @lstat = nil
    end
    
    def copy_file(dest)
      st = stat()
      File.open(path(),  'rb') {|r|
        File.open(dest, 'wb', st.mode) {|w|
          fu_copy_stream0 r, w, (fu_blksize(st) || fu_default_blksize())
        }
      }
    end

    def copy_metadata(path)
      st = lstat()
      File.utime st.atime, st.mtime, path
      begin
        File.chown st.uid, st.gid, path
      rescue Errno::EPERM
        # clear setuid/setgid
        File.chmod st.mode & 01777, path
      else
        File.chmod st.mode, path
      end
    end
  
    def stat
      return @stat if @stat
      if lstat() && lstat().symlink?
        @stat = File.stat(path())
      else
        @stat = lstat()
      end
      @stat
    end
    
    def lstat
      if dereference?
        @lstat ||= File.stat(path())
      else
        @lstat ||= File.lstat(path())
      end
    end

    def dereference?
      @deref
    end
   
    def path
      if @path
        @path.to_str
      else
        join(@prefix, @rel)
      end
    end

  end

end
