# This file has Yahtzee scoring function
def chance(dice_rolls):
  """Given a list of dice rolls, return the sum of the dice"""
  return sum(dice_rolls)

def singles(dice_rolls,number):
  # declare a sum
  sum = 0
  # loop over every dice roll
  for roll in dice_rolls:
    # if the roll is a one, add 1 to the sum, if it's a two, add 2, etc.
    if roll == number:
      sum += number
  return sum

def three_of_kind(dice_rolls):
  # loop over each number 1 through 6
  for i in range(1,7):
    # if the ount of number in dice_rolls is >= 3
    if dice_rolls.count(i) >= 3:
      # return chance(dice_rolls)
      return chance(dice_rolls)
  return 0

