# this makes sure that Kernel#require and Kernel#load don't need (but still accept) a full path anymore
$:.clear
$:.push(Dir.getwd)

# wrapper for RMXP's Win32API class
class Win32API
  
  LIMIT_L = 4294967296
  LIMIT_S = 65536
  LIMIT_C = 256
  
  def initialize(dllname, func, import, export = "0", calltype = :stdcall)
    import = import.join('') if import.is_a?(Array)
    export = export.join('') if export.is_a?(Array)
    @export = export.clone
    import.upcase!
    export.upcase!
    @api = Win32::API.new(func, import, export, dllname)
  end

  def call(*args)
    result = @api.call(*args)
    result -= LIMIT_L if @export == 'l' && result >= LIMIT_L / 2
    result -= LIMIT_S if @export == 's' && result >= LIMIT_S / 2
    result -= LIMIT_C if @export == 'c' && result >= LIMIT_C / 2
    return result
  end

  alias Call call
  
end
