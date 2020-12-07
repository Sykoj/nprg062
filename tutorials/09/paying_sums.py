
def pay(sum_to_pay, smallest, current_coins):
    if sum_to_pay == 0:
        print(current_coins)
    elif sum_to_pay >= 1:
        for coin in coins:
            if coin <= sum_to_pay and coin <= smallest:
                pay(sum_to_pay - coin, coin, current_coins + [ coin ])


goal_sum = 9
coins = [ 5, 2, 1 ]
pay(goal_sum, coins[0], [])
