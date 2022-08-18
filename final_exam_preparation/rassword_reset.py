def password_reset():
    data = input()

    while True:
        command = input().split(' ')
        print(command)
        current_command = command[0]

        if current_command == 'Done':
            print(f'Your password is: {data}')
            break

        elif current_command == 'TakeOdd':
            data = ''.join([data[i] for i in range(len(data)) if i % 2 != 0])
            print(data)

        elif current_command == 'Cut':
            index = int(command[1])
            length = int(command[2])
            data = ''.join([data[i] for i in range(len(data)) if i < index or i >= index + length])
            print(data)

        elif current_command == 'Substitute':
            substring = command[1]
            substitute = command[2]

            if substring in data:
                data = data.replace(substring, substitute)
                print(data)
            else:
                print("Nothing to replace!")

password_reset()