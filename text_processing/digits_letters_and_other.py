def get_digits(data):
    return ''.join([str(ch) for ch in data if ch.isdigit()])

def get_letters(data):
    return ''.join([ch for ch in data if ch.isalpha()])

def get_other_signs(data):
    return ''.join([ch for ch in data if not ch.isalpha() and not ch.isdigit()])

data = input()
print(get_digits(data))
print(get_letters(data))
print(get_other_signs(data))
