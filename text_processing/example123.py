def multiline_input(text):
    print(text)
    multiline_input = ''

    while True:
        string = input()

        if string != '':
            multiline_input += string + '\n'
        else:
            break

    return multiline_input

print(multiline_input('Please enter your input: '))