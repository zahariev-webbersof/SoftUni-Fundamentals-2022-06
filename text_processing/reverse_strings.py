def reverse_func(data):
    for string in data:
        print(f'{string} = {string[::-1]}')

words = []

while True:
    word = input()

    if word == 'end':
        break
    words.append(word)

reverse_func(words)