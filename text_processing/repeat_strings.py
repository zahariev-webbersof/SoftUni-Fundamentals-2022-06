class Example:
    def __init__(self, words):
        self.words = words

    def repeat_func(self):
        return ''.join(map(lambda x: x * len(x), self.words))

words: list = input().split(' ')
obj = Example(words)
print(obj.repeat_func())

