
number = int(input('Enter number:'))
binary_representation = ''
is_power_of_two = True

if number < 0:
    print('Higher power of two: 0')
    exit()
if number < 1:
    print('Higher power of two: 1')
    exit()

while number > 0:
    if number != 1 and number % 2 == 1:
        is_power_of_two = False
    
    binary_representation = str(number % 2) + binary_representation
    number //= 2

higher_power_of_two = int(binary_representation, 2) if is_power_of_two else 2 ** len(binary_representation)
print('Higher power of two: ' + str(higher_power_of_two))