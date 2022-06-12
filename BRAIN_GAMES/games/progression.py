import random

GOAL = 'What number is missing in the progression?'
progression_len = 10


def generate_progression(gen_number, step, progression_len):
    progression = [gen_number]
    count = 0
    while count < progression_len:
        gen_number += step
        progression.append(gen_number)
        count += 1
    return progression


def generate_round_problem():
    gen_number = random.randint(1, 100)
    step = random.randint(1, 10)
    progression = generate_progression(gen_number, step, progression_len)
    answer = random.choice(progression)
    question = f"{' '.join(generate_progression).replace(answer, '..')}"
    return question, answer

