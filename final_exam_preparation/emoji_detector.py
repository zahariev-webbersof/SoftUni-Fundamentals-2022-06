import re


def emoji_detector():
    data = input()
    pattern = r'[0-9]|(\:{2}[A-Z][a-z]{2,}\:{2})|(\*{2}[A-Z][a-z]{2,}\*{2})'
    result = re.finditer(pattern, data)
    words = {}
    cool_threshold = 1

    for res in result:
        word = res.group()

        if word.isdigit():
            cool_threshold *= int(word)
        else:
            words[word] = 0
            for ch in word:
                if ch != ':' and ch != '*':
                    words[word] += ord(ch)

    print(f'Cool threshold: {cool_threshold}')
    print(f'{len(words)} emojis found in the text. The cool ones are:')

    for current_word in words:
        if words[current_word] >= cool_threshold:
            print(current_word)

emoji_detector()