#==============================================================================
# Array
#------------------------------------------------------------------------------
#  This class handles array data structures. It was modified to support the
#  utility operations sum and squares.
#==============================================================================

class Array
  
  #----------------------------------------------------------------------------
  # sum
  #  Sums up all the numeric values of the array.
  #----------------------------------------------------------------------------
  def sum
    # initialize
    sum = 0
    # add each element that's a number to sum
    self.each {|i| sum += i if i.is_a?(Numeric)}
    # return sum as float
    return sum
  end
  
end
