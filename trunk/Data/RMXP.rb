#require File.expand_path('dl.so') if File.exist?('dl.so')
=begin
class Win32API
  DLL = {}
  TYPEMAP = {"0" => DL::TYPE_VOID, "S" => DL::TYPE_VOIDP, "I" => DL::TYPE_LONG}

  def initialize(dllname, func, import, export = "0", calltype = :stdcall)
    @proto = [import].join.tr("VPpNnLlIi", "0SSI").sub(/^(.)0*$/, '\1')
    handle = DLL[dllname] ||= DL.dlopen(dllname)
    @func = DL::CFunc.new(handle[func], TYPEMAP[export.tr("VPpNnLlIi", "0SSI")], func, calltype)
  rescue DL::DLError => e
    raise LoadError, e.message, e.backtrace
  end

  def call(*args)
    import = @proto.split("")
    args.each_with_index do |x, i|
      args[i], = [x == 0 ? nil : x].pack("p").unpack("l!*") if import[i] == "S"
      args[i], = [x].pack("I").unpack("i") if import[i] == "I"
    end
    ret = @func.call(args)
    return ret || 0
  end

  alias Call call
end
=end

# this makes sure that Kernel#require and Kernel#load don't need (but still accept) a full path anymore
$:.clear
$:.push(Dir.getwd)

# RMXP's data loader from the RGSSAD archive
def load_data(filename)
	file = File.open(filename)
	data = Marshal.load(file)
	file.close()
	return data
end
