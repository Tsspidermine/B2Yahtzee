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
        # if the count of number in dice_rolls is >= 3
        if dice_rolls.count(i) >= 3:
            # return chance(dice_rolls)
            return chance(dice_rolls)
    return 0

def four_of_kind(dice_rolls):
    # loop over each number 1 through 6
    for i in range(1,7):
        # if the count of number in dice_rolls is >= 3
        if dice_rolls.count(i) >= 4:
            # return chance(dice_rolls)
            return chance(dice_rolls)
    return 0

# TODO: Add a 100 point linear bonus for every yahtzee
def yahtzee(dice_rolls):
    for i in range(1,7):
        # if the count of the number in dice_rolls is >= 5
        if dice_rolls.count(i) >= 5:
            return 50 #+ (100 * yahtzee_count)
    return 0

def full_house(dice_rolls):
    three_house = False
    two_house = False
    for i in range(1,7):
        if dice_rolls.count(i) == 3:
            three_house = True
        if dice_rolls.count(i) == 2:
            two_house = True
        if three_house and two_house:
            return 25
    return 0

# TODO: I forgot to make sure it is a list from 1-6 (1,2,3,4,5,6), but forgot to account for
# cases like a full house, where it's (2,2,2,5,5)
def sm_straight(dice_rolls):
    sm_rolls = []
    sm_rolls.extend(dice_rolls)
    sm_rolls.pop()
    if sorted(sm_rolls) == sm_rolls:
        return 30
    return 0

# TODO: Refer to line 54
def lg_straight(dice_rolls):
    if sorted(dice_rolls) == dice_rolls:
        return 40
    return 0









