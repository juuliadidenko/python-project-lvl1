#!/usr/bin/env python3

import prompt
import random


rounds_count = 3

def is_even(gen_number):
    return gen_number %2 == 0


def even_check(): 
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    
    for game_round in range(rounds_count):
        gen_number = random.randint(1, 100)
        answer = 'yes' if is_even(gen_number) is True else 'no'
        print(f'Question: {gen_number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is the wrong answer ;(. Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!") 
            return
    print(f'Congratulations, {name}!')


def main():
    even_check()


if __name__ == '__main__':
    main()