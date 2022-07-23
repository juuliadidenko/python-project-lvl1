import random

GOAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(gen_number):
    if gen_number == 1:
        return False
    k = 0
    for i in range(2, gen_number // 2 + 1):
        if (gen_number % i == 0):
            k += 1
    if (k <= 0):
        return True
    else:
        return False


def generate_round_problem():
    gen_number = random.randint(1, 100)
    answer = 'yes' if is_prime(gen_number) else 'no'
    return str(gen_number), answer
