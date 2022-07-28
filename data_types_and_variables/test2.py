number_of_eggs_first_player = int(input())
number_of_eggs_second_player = int(input())

while True:
    winner = input()

    if winner == 'End':
        print(f'Player one has {number_of_eggs_first_player} eggs left.')
        print(f'Player two has {number_of_eggs_second_player} eggs left.')
        break

    if winner == 'one':
        if number_of_eggs_second_player > 1:
            number_of_eggs_second_player -= 1
        else:
            print(f'Player two is out of eggs. Player one has {number_of_eggs_first_player} eggs left.')
            break

    elif winner == 'two':
        if number_of_eggs_first_player > 1:
            number_of_eggs_first_player -= 1
        else:
            print(f'Player one is out of eggs. Player two has {number_of_eggs_second_player} eggs left.')
            break