import operator

def calculations(number_a, number_b, operation):
    operations_dict = {'multiply': operator.mul, 'divide': operator.truediv,
                       'add': operator.add, 'subtract': operator.sub}
    return int(operations_dict[operation](number_a, number_b))

type_of_operation = input()
first_numbers = int(input())
second_numbers = int(input())
print(calculations(first_numbers, second_numbers, type_of_operation))