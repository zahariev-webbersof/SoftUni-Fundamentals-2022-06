number_of_stars = int(input())

for i in range(1, number_of_stars + 1):
    print(i * '*')

for i in range(number_of_stars -1, 0, -1):
    print(i * '*')