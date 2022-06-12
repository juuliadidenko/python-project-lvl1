import random


GOAL = 'What is the result of the expression?'


def calc(gen_number_1, operator, gen_number_2):
    if operator == '+':
        return gen_number_1 + gen_number_2
    elif operator == '-':
        return gen_number_1 - gen_number_2
    else:
        return gen_number_1 * gen_number_2


def generate_round_problem():
    operators = ['+', '-', '*']
    gen_number_1 = random.randint(1, 100)
    gen_number_2 = random.randint(1, 100)
    operator = random.choice(operators)
    question = f'{gen_number_1} {operator} {gen_number_2}'
    answer = calc(gen_number_1, operator, gen_number_2)
    return question, str(answer)