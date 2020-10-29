
binary = input('Enter binary number:')
power = 1
number = 0

for x in binary[::-1]:
    number += power * (1 if x == '1' else 0)
    power *= 2

print(number)