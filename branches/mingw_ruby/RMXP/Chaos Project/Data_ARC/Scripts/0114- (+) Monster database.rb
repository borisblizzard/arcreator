#==============================================================================
# Monster
#==============================================================================

class Monster
  
  def database(id)
    @id = id
    case id
    when 1
      @name, @health, @power, @aggressive, @speed, @rate =
          'Doom Shroom', 192, 9, 9, 9, 3.5
    when 2
      @name, @health, @power, @aggressive, @speed, @rate =
          'Salomon', 213, 14, 8, 12, 2.1
    when 3
      @name, @health, @power, @aggressive, @speed, @rate =
          'Stinger', 193, 8, 15, 12, 1.8
    when 4
      @name, @health, @power, @aggressive, @speed, @rate =
          'Humphry', 244, 10, 12, 13, 1.4
    when 5
      @name, @health, @power, @aggressive, @speed, @rate =
          'P.I.C.K.', 243, 17, 13, 10, 1.3
    when 6
      @name, @health, @power, @aggressive, @speed, @rate =
          'Mickey', 306, 16, 13, 16, 1.1
    when 7
      @name, @health, @power, @aggressive, @speed, @rate =
          'Bowra', 300, 14, 19, 15, 4.3
    when 8
      @name, @health, @power, @aggressive, @speed, @rate =
          'Skelett', 267, 16, 20, 17, 3.6
    when 9
      @name, @health, @power, @aggressive, @speed, @rate =
          'HARRR', 308, 20, 23, 18, 2.9
    when 10
      @name, @health, @power, @aggressive, @speed, @rate =
          'Murray', 325, 24, 21, 14, 2.2
    when 11
      @name, @health, @power, @aggressive, @speed, @rate =
          'Timeshifter', 420, 26, 18, 20, 1.7
    when 12
      @name, @health, @power, @aggressive, @speed, @rate =
          'Lady Zii', 333, 28, 21, 24, 1.6
    when 13
      @name, @health, @power, @aggressive, @speed, @rate =
          'Mindhunger', 449, 29, 23, 21, 1.4
    when 14
      @name, @health, @power, @aggressive, @speed, @rate =
          'Grok', 447, 29, 25, 25, 1.2
    when 15
      @name, @health, @power, @aggressive, @speed, @rate =
          'Sunder', 502, 30, 26, 27, 1.1
    when 16
      @name, @health, @power, @aggressive, @speed, @rate =
          'Sphinx', 467, 28, 24, 23, 3.1
    when 17
      @name, @health, @power, @aggressive, @speed, @rate =
          'Cerbeclus', 508, 32, 25, 21, 2.3
    when 18
      @name, @health, @power, @aggressive, @speed, @rate =
          'Slinger', 558, 33, 23, 29, 2.1
    when 19
      @name, @health, @power, @aggressive, @speed, @rate =
          'Hobo', 859, 41, 20, 21, 1.8
    when 20
      @name, @health, @power, @aggressive, @speed, @rate =
          'Gnarly', 666, 34, 28, 33, 1.7
    when 21
      @name, @health, @power, @aggressive, @speed, @rate =
          'Dusa M.', 707, 41, 33, 35, 1.5
    when 22
      @name, @health, @power, @aggressive, @speed, @rate =
          'Lux', 743, 44, 39, 41, 1.3
    when 23
      @name, @health, @power, @aggressive, @speed, @rate =
          'Steve', 691, 40, 107, 55, 1.2
    when 24
      @name, @health, @power, @aggressive, @speed, @rate =
          'Boss Toss', 850, 50, 50, 50, 1.1
    when 25
      @name, @health, @power, @aggressive, @speed, @rate =
          'Pest', 761, 48, 47, 52, 3.9
    when 26
      @name, @health, @power, @aggressive, @speed, @rate =
          'Mutador', 871, 52, 45, 54, 3.4
    when 27
      @name, @health, @power, @aggressive, @speed, @rate =
          'Falc', 914, 56, 52, 61, 2.9
    when 28
      @name, @health, @power, @aggressive, @speed, @rate =
          'Ruin', 1440, 51, 53, 44, 2.3
    when 29
      @name, @health, @power, @aggressive, @speed, @rate =
          'Jungle Jack', 1263, 56, 58, 53, 1.9
    when 30
      @name, @health, @power, @aggressive, @speed, @rate =
          'Turega', 1189, 61, 57, 62, 1.7
    when 31
      @name, @health, @power, @aggressive, @speed, @rate =
          'Laplace', 1274, 63, 62, 63, 1.4
    when 32
      @name, @health, @power, @aggressive, @speed, @rate =
          'Pythonia', 1337, 60, 87, 61, 1.3
    when 33
      @name, @health, @power, @aggressive, @speed, @rate =
          'Ragna', 1500, 70, 70, 50, 1.1
    else
      @name, @health, @power, @aggressive, @speed, @rate =
          '', 200, 10, 10, 10, 1.0
    end
    @exp = 0
    @own = false
  end
  
end
