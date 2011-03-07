def reflect(obj)
	io = open("./" + obj.class.to_s + ".txt", 'wb')
	io.write("Instance variables:\n")
	(obj.instance_variables - Object.new.instance_variables - 
	Class.instance_variables - Module.instance_variables).sort.each {|name|
		io.write("\t" + name.to_s + " => " + 
		obj.instance_variable_get(value).to_s + "\n")
	}
	io.write("Methods:\n")
	(obj.methods - Object.new.methods - Class.methods - Module.methods).sort.each {|name|
		io.write("\t" + name.to_s + "\n")
	}
	io.write("Public Methods:\n")
	(obj.public_methods(true) - Object.new.public_methods(true) - 
	Class.public_methods(true) - Module.public_methods(true)).sort.each {|name|
		io.write("\t" + name.to_s + "\n")
	}
	io.write("Private Methods:\n")
	(obj.private_methods(true) - Object.new.private_methods(true) - 
	Class.private_methods(true) - Module.private_methods(true)).sort.each {|name|
		io.write("\t" + name.to_s + "\n")
	}
	io.write("Protected Methods:\n")
	(obj.protected_methods(true) - Object.new.protected_methods(true) - 
	Class.protected_methods(true) - Module.protected_methods(true)).sort.each {|name|
		io.write("\t" + name.to_s + "\n")
	}
	io.write("Singleton Methods:\n")
	(obj.singleton_methods(true) - Object.new.singleton_methods(true) - 
	Class.singleton_methods(true) - Module.singleton_methods(true)).sort.each {|name|
		io.write("\t" + name.to_s + "\n")
	}
end

begin
  reflect(Bitmap.new(32, 32))
  reflect(Color.new(255, 255, 255, 255))
  reflect(Font.new())
  reflect(Plane.new())
  reflect(Rect.new(0, 0, 32, 32))
  reflect(Sprite.new())
  reflect(Table.new(10, 10, 10))
  reflect(Tilemap.new())
  reflect(Tone.new(255, 255, 255, 255))
  reflect(Viewport.new(0, 0, 640, 480))
  reflect(Window.new())
  reflect(RGSSEror.new())
end
