def create_combination(k, current_symbols, current_sum):
    if k == len(numbers):
        if goal_sum == current_sum:
            for index, number in enumerate(numbers):
                print(f'{current_symbols[index]} {number} ', end='')
            print()
    else:
        create_combination(k + 1, current_symbols + [ '+' ], current_sum + numbers[k], numbers, goal_sum)
        create_combination(k + 1, current_symbols + [ '-' ], current_sum - numbers[k], numbers, goal_sum)

numbers = [ 8, 4, 6, 2 ]
goal_sum = 8

create_combination(0, [], 0)