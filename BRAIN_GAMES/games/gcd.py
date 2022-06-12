import math
import random


GOAL = 'Find the greatest common divisor of given numbers.'


def generate_round_problem():
    gen_number_1 = random.randint(1, 100)
    gen_number_2 = random.randint(1, 100)
    question = f'{gen_number_1} {gen_number_2}'
    answer = math.gcd(gen_number_1, gen_number_2)
    return question, str(answer)