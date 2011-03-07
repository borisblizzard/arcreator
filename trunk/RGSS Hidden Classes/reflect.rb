def reflect(obj)
	io = open("./" + obj.class.to_s + ".txt", 'wb')
	io.write("Instence veribles:\n")
	obj.instance_variables.each {|name|
		io.write("\t" + name.to_s + " => " + 
		obj.instance_variable_get(value).to_s + "\n")
	}
	io.write("Methods:\n")
	obj.methods.each {|name|
		io.write("\t" + name.to_s + "\n")
	}
	io.write("Public Methods:\n")
	obj.public_methods(true).each {|name|
		io.write("\t" + name.to_s + "\n")
	}
	io.write("Private Methods:\n")
	obj.private_methods(true).each {|name|
		io.write("\t" + name.to_s + "\n")
	}
	io.write("Protected Methods:\n")
	obj.protected_methods(true).each {|name|
		io.write("\t" + name.to_s + "\n")
	}
	io.write("Singleton Methods:\n")
	obj.singleton_methods(true).each {|name|
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
