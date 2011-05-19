# this makes sure that Kernel#require and Kernel#load don't need (but still accept) a full path anymore
$:.clear
$:.push(Dir.getwd)

# wrapper for RMXP's Win32API class
class Win32API
  
  def initialize(dllname, func, import, export = "0", calltype = :stdcall)
    import = import.join('') if import.is_a?(Array)
    export = export.join('') if export.is_a?(Array)
    import.upcase!
    export.upcase!
    @api = Win32::API.new(func, import, export, dllname)
  end

  def call(*args)
    return @api.call(*args)
  end

  alias Call call
  
end

# RMXP's data loader from the RGSSAD archive
def load_data(filename)
	file = File.open(filename, 'rb')
	data = Marshal.load(file)
	file.close()
	return data
end
