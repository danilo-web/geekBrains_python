import random


def randomizer(input_list):
    if input_list:
        result = int(random.choice(input_list))
        return result
