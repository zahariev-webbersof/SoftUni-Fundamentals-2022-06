tail = input()
body = input()
head = input()

animal = [tail, body, head]
animal[0], animal[-1] = animal[-1], animal[0]
print(animal)