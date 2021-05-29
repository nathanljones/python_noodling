import random
from collections import namedtuple

dice_count = namedtuple('dice_count', ['total_score', 'number_of_times'])
max_dice_score = 50
#dice_rolls = [[] for i in range(max_dice_score)]
dice_rolls = [dice_count(0, 0) for i in range(max_dice_score)]


def overall():
    for target_score in range(1, max_dice_score):
        play_turn(target_score)
    for dice_roll in dice_rolls:
        print(dice_roll.total_score)


def play_turn(target_score):
    die_sides = 6
    loosing_number = 1
    total_score = 0
    ok_to_play = True
    roll_count = 0

    while ok_to_play == True:
        roll_count += 1
        die_roll = random.randint(1, die_sides)
        if die_roll == loosing_number:
            break
        total_score += die_roll
        if total_score >= target_score:
            dice_roll = dice_count(
                total_score=total_score, number_of_times=roll_count)
            dice_rolls[target_score] = dice_roll
            print('Maximum score of ' + str(total_score) +
                  ' in ' + str(roll_count) + ' rolls' + ' I was aiming for ' + str(target_score))
            break
    total_score = 0
    roll_count = 0


if __name__ == "__main__":
    overall()
