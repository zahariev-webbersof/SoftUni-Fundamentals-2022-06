energy = int(input())
won_battle_counter = 0

while True:
    command = input()

    if command == 'End of battle':
        print(f'Won battles: {won_battle_counter}. Energy left: {energy}')
        break

    distance = int(command)

    if energy >= distance:
        energy -= distance
        won_battle_counter += 1

        if won_battle_counter % 3 == 0:
            energy += won_battle_counter

    else:
        print(f'Not enough energy! Game ends with {won_battle_counter} won battles and {energy} energy')
        break