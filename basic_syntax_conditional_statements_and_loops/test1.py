import random

questions = ['Кога е основана България?', 'Колко е 2 * 2?', 'Коя е най-голямата по площ държава в света?']
guess_counter = 0
answered_questions = []

for _ in range(10):
    current_question = random.choice(questions)
    if current_question not in answered_questions:
        answered_questions.append(current_question)
        print(current_question)
    else:
        continue

    if current_question == 'Кога е основана България?':
        answer = input('Моля въведете отговор: ')

        if answer == '681':
            print('Ти позна въпроса!\n')
            guess_counter += 1
        else:
            print('Грешен отговор!\n')

    elif current_question == 'Колко е 2 * 2?':
        answer = input('Моля въведете отговор: ')

        if answer == '4':
            print('Ти позна въпроса!\n')
            guess_counter += 1
        else:
            print('Грешен отговор!\n')

    elif current_question == 'Коя е най-голямата по площ държава в света?':
        answer = input('Моля въведете отговор: ')

        if answer == 'Русия':
            print('Ти позна въпроса!\n')
            guess_counter += 1
        else:
            print('Грешен отговор!\n')

    if guess_counter == 2:
        print('Ти спечели играта!')
        break