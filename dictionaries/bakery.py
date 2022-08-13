data = input().split(' ')

# for loop
# for i in range(0, len(data), 2):
#     products_dict[data[i]] = int(data[i + 1])

# dict comprehension
products_dict = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}

print(products_dict)