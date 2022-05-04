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

def sm_straight(dice_rolls):
    previous_num = dice_rolls[0] - 1
    straight_count = 0
    for i in range(5):
        if dice_rolls[i] == previous_num + 1:
            straight_count += 1
        previous_num = dice_rolls[i]
    # If there are 4 numbers in a sequence and it's not also a large straight, return 30 points
    if straight_count >= 4 and lg_straight(dice_rolls) == 0:
        return 30
    else:
        return 0

        

def lg_straight(dice_rolls):
    previous_num = dice_rolls[0] - 1
    straight_count = 0
    for i in range(5):
        if dice_rolls[i] == previous_num + 1:
            straight_count += 1
        previous_num = dice_rolls[i]
    if straight_count >= 5:
        return 40
    else:
        return 0








