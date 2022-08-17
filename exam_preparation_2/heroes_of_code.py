def create_heroes(heroes_dict, number):
    for _ in range(number):
        data = input().split(' ')
        hero_name = data[0]
        hit_points = int(data[1])
        mana_points = int(data[2])

        heroes_dict[hero_name] = [hit_points, mana_points]


def playing_game(heroes_dict):
    while True:
        command = input().split(' - ')

        if command[0] == 'End':
            break

        current_command = command[0]

        if current_command == 'CastSpell':
            hero_name = command[1]
            mp_needed = int(command[2])
            spell_name = command[3]
            available_mp = heroes_dict[hero_name][1]

            if available_mp >= mp_needed:
                heroes_dict[hero_name][1] -= mp_needed
                current_mp = heroes_dict[hero_name][1]
                print(f"{hero_name} has successfully cast {spell_name} and now has {current_mp} MP!")
            else:
                print(f"{hero_name} does not have enough MP to cast {spell_name}!")

        elif current_command == 'TakeDamage':
            hero_name = command[1]
            damage = int(command[2])
            attacker = command[3]
            available_hp = heroes_dict[hero_name][0]

            if available_hp - damage > 0:
                heroes_dict[hero_name][0] -= damage
                current_hp = heroes_dict[hero_name][0]

                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del heroes_dict[hero_name]
                print(f"{hero_name} has been killed by {attacker}!")

        elif current_command == 'Recharge':
            hero_name = command[1]
            amount = int(command[2])
            available_mp = heroes_dict[hero_name][1]

            if available_mp + amount > 200:
                amount = 200 - available_mp
                heroes_dict[hero_name][1] += amount
            else:
                heroes_dict[hero_name][1] += amount

            print(f"{hero_name} recharged for {amount} MP!")

        elif current_command == 'Heal':
            hero_name = command[1]
            amount = int(command[2])
            available_mp = heroes_dict[hero_name][0]

            if available_mp + amount > 100:
                amount = 100 - available_mp
                heroes_dict[hero_name][0] += amount
            else:
                heroes_dict[hero_name][0] += amount

            print(f"{hero_name} healed for {amount} HP!")

    return heroes_dict


def print_function(heroes_dict):
    for hero in heroes_dict:
        print(hero)
        print(f'  HP: {heroes_dict[hero][0]}')
        print(f'  MP: {heroes_dict[hero][1]}')


def heroes_of_code(number):
    # In heroes_dict we have list with two values:
    # HP - index 0, MP - index 1
    heroes_dict = {}

    create_heroes(heroes_dict, number)
    playing_game(heroes_dict)
    print_function(heroes_dict)

n = int(input())
heroes_of_code(n)