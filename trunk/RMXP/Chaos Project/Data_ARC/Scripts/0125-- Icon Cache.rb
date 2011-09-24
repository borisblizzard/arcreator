if FINAL
files = []
Dir.foreach('Graphics/Icons') {|name|
    if name != '.' && name != '..'
      filename = "Graphics/Icons/#{name}"
      if FileTest.file?(filename)
        names = name.split('.')
        names.pop
        files.push(names.join('.'))
      end
    end}
w, h, rate = 480, 4, 16
sprite = Sprite.new
sprite.x, sprite.y = 320 - w / 2, 416 - h / 2
sprite.bitmap = Bitmap.new(w + 2, h + 34)
sprite.bitmap.font.name = 'Geometrix'
sprite.bitmap.font.size = 24
sprite.bitmap.font.color = Color.new(255, 255, 255)
sprite.bitmap.draw_text(0, 0, w + 2, 32, 'Caching Icons...', 1)
sprite.bitmap.fill_rect(0, 32, w + 2, h + 2, Color.new(240, 240, 240))
sprite.bitmap.fill_rect(1, 33, w, h, Color.new(0, 0, 0))
Graphics.update
r = -1
files.each_index {|i|
    RPG::Cache.icon(files[i])
    new_r = i * (w / rate) / (files.size - 1)
    if r != new_r
      r = new_r
      sprite.bitmap.fill_rect(1 + r * rate, 33, rate, h, Color.new(240, 0, 0))
      Graphics.update
    end}
sprite.dispose
Graphics.update
end
