import random


GOAL = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(gen_number):
    return gen_number % 2 == 0


def generate_round_problem():
    gen_number = random.randint(1, 100)
    answer = 'yes' if is_even(gen_number) is True else 'no'
    return str(gen_number), answer