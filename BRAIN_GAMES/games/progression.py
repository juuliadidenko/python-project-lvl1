import random

GOAL = 'What number is missing in the progression?'
progression_len = 10


def generate_round_problem():
    gen_number = random.randint(0, 30)
    step = random.randint(1, 5)
    end = random.randint(40, 100)
    sequence = list(range(gen_number, end, step))
    answer = random.choice(sequence)
    question = ' '.join(
        '..' if number == answer else str(number) for number in sequence
    )
    return question, str(answer)
