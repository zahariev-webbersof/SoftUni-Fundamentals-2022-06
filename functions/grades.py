
def type_of_grade(grade):
    result = ''
    if 2 <= grade <= 2.99:
        result ='Fail'
    elif 3 <= grade <= 3.49:
        result = 'Poor'
    elif 3.50 <= grade <= 4.49:
        result = 'Good'
    elif 4.50 <= grade <= 5.49:
        result = 'Very Good'
    elif 5.49 <= grade <= 6:
        result = 'Excellent'

    return result

score = float(input())
print(type_of_grade(score))
