import prompt
ROUND_COUNT = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GOAL)

    for round in range(ROUND_COUNT):
        question, answer = game.generate_round_problem()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is the wrong answer ;(. Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!") 
            return
    print(f'Congratulations, {name}!')