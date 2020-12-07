def create_combination(k, current_sum):
    if k == len(numbers):
        if goal_sum == current_sum:
            for index, number in enumerate(numbers):
                print(f'{symbols[index]} {number} ', end='')
            print()
    else:
        symbols[k] = '+'
        create_combination(k + 1, current_sum + numbers[k])
        symbols[k] = '-'
        create_combination(k + 1, current_sum - numbers[k])

numbers = [ 8, 4, 6, 2 ]
symbols = [ ' ' ] * len(numbers)
goal_sum = 8

create_combination(0, 0)