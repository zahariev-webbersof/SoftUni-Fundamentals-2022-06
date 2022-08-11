# numbers = input().split(' ')
# abs_numbers = []
#
# for num in numbers:
#     abs_numbers.append(abs(float(num)))
#
# print(abs_numbers)

def abs_numbers(nums):
    result = [abs(num) for num in nums]
    return result

numbers = list(map(float, input().split(' ')))
print(abs_numbers(numbers))