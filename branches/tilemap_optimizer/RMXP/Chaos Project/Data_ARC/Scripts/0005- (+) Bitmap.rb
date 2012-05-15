#==============================================================================
# Bitmap
#==============================================================================

class Bitmap
  
  def desaturate
    bitmap = Bitmap.new(width, height)
    (0...height).each {|y| (0...width).each {|x|
        c = get_pixel(x, y)
        if c.red > c.green
          if c.red > c.blue
            med = (c.red + (c.green > c.blue ? c.green : c.blue)) / 2
          else
            med = (c.blue + c.green) / 2
          end
        else
          if c.green > c.blue
            med = (c.green + (c.red > c.blue ? c.red : c.blue)) / 2
          else
            med = (c.blue + c.red) / 2
          end
        end
        bitmap.set_pixel(x, y, Color.new(med, med, med, c.alpha))}}
    return bitmap
  end
  
end

