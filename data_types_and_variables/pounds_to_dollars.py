# pounds = int(input())
# dollars = pounds * 1.31
# print(f'{dollars:.3f}')

from forex_python.converter import CurrencyRates

amount = int(input('Enter the number of pounds: '))
c = CurrencyRates()
current_rate = c.get_rate('GBP', 'USD')
result = current_rate * amount
print(f'Your sum in dollars is: {result:.3f}')