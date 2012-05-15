#==============================================================================
# Card
#==============================================================================

class Card
  
  attr_reader :sign
  attr_reader :character
  attr_reader :color
  
  def initialize(sign, values, character, color)
    @sign, @values, @character, @color = sign, values, character, color
  end
  
  def values
    return @values.clone
  end
  
end

#==============================================================================
# Hand
#==============================================================================

class Hand
  
  attr_reader   :cards
  attr_accessor :stand
  
  def initialize
    clear
  end
  
  def clear
    @cards = []
    @stand = false
  end
  
  def score
    scores = []
    @cards.each {|card| scores.push(card.values)}
    score = 0
    loop do
      alternative = false
      scores.each {|values|
          score += values[0]
          if values.size > 1 && !alternative
            values.shift
            alternative = true
          end}
      break if score <= 21 || !alternative
      score = 0
    end
    return score
  end
  
  def blackjack?
    return (@cards.size == 2 && has_21?)
  end
  
  def busted?
    return (self.score > 21)
  end
  
  def full?
    return (@cards.size == 5)
  end
  
  def has_21?
    return (self.score == 21)
  end
  
  def <=>(other)
    return 0 if self.blackjack? && other.blackjack?
    return 1.5 if self.blackjack?
    return -1 if other.blackjack?
    return -1 if self.busted?
    return 1 if other.busted?
    return (self.score <=> other.score)
  end
  
end

#==============================================================================
# Roulette_Number
#==============================================================================

class Roulette_Number
  
  attr_reader :value
  attr_reader :color
  
  def initialize(value, color)
    @value, @color = value, color
  end
  
  def black?
    return (@color.red == 0 && @color.green == 0)
  end
  
  def red?
    return (!black? && @color.green == 0)
  end
  
  def even?
    return (@value % 2 == 0 && !is_0?)
  end
  
  def odd?
    return (@value % 2 == 1 && !is_0?)
  end
  
  def is_1_to_18?
    return (@value <= 18 && !is_0?)
  end
  
  def is_19_to_36?
    return (@value >= 19)
  end
  
  def is_1_to_12?
    return (@value <= 12 && !is_0?)
  end
  
  def is_13_to_24?
    return (@value >= 13 && @value <= 24)
  end
  
  def is_25_to_36?
    return (@value >= 25)
  end
  
  def column1?
    return (@value % 3 == 1)
  end
  
  def column2?
    return (@value % 3 == 2)
  end
  
  def column3?
    return (@value % 3 == 0 && !is_0?)
  end
  
  def is_0?
    return (@value == 0)
  end
  
end

#==============================================================================
# Roulette_Bet
#==============================================================================

class Roulette_Bet
  
  attr_reader :value
  attr_reader :numbers
  
  def initialize(value, numbers)
    @value = value
    @numbers = numbers
  end
  
  def payout
    return (@value * 36 / @numbers.size)
  end
  
  def won?(number)
    return (@numbers.size == [0]) if number == 0
    return (@numbers.include?(number))
  end
  
end
