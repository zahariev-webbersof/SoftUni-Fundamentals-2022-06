from collections import defaultdict

words = input().split(' ')
counter_of_words = defaultdict(int)

for word in words:
    counter_of_words[word.lower()] += 1

print(' '.join([word for word, count in counter_of_words.items() if count % 2 != 0]))