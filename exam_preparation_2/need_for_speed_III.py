def store_cars_information(cars_dictionary, number):
    for _ in range(number):
        data = input().split('|')
        brand = data[0]
        mileage = int(data[1])
        fuel = int(data[2])

        cars_dictionary[brand] = [mileage, fuel]

    return cars_dictionary


def special_commands(cars_dictionary):
    
    while True:
        command = input()

        if command == 'Stop':
            break

        command = command.split(' : ')
        current_command = command[0]
        brand = command[1]

        if current_command == 'Drive':
            distance = int(command[2])
            fuel = int(command[3])
            available_fuel = cars_dictionary[brand][1]
            current_mileage = cars_dictionary[brand][0]

            if available_fuel < fuel:
                print("Not enough fuel to make that ride")
            else:
                cars_dictionary[brand][1] -= fuel
                cars_dictionary[brand][0] += distance
                print(f"{brand} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

            if cars_dictionary[brand][0] >= 100000:
                del cars_dictionary[brand]
                print(f"Time to sell the {brand}!")

        elif current_command == 'Refuel':
            fuel = int(command[2])
            available_fuel = cars_dictionary[brand][1]

            if fuel + available_fuel > 75:
                fuel = 75 - available_fuel

            cars_dictionary[brand][1] += fuel

            print(f"{brand} refueled with {fuel} liters")

        elif current_command == 'Revert':
            kilometers = int(command[2])
            current_mileage = cars_dictionary[brand][0]

            if current_mileage - kilometers < 10000:
                cars_dictionary[brand][0] = 10000
            else:
                cars_dictionary[brand][0] -= kilometers
                print(f"{brand} mileage decreased by {kilometers} kilometers")

    return cars_dictionary


def additional_print_function(cars_dictionary):
    for brand in cars_dictionary:
        mileage = cars_dictionary[brand][0]
        fuel = cars_dictionary[brand][1]

        print(f'{brand} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.')


def need_for_speed(number):
    # The current dictionary contains a list with two values
    # At index 0 we have mileage, and at index 1 we have fuel
    cars_dictionary = {}

    store_cars_information(cars_dictionary, number)
    special_commands(cars_dictionary)
    additional_print_function(cars_dictionary)


n = int(input())
need_for_speed(n)