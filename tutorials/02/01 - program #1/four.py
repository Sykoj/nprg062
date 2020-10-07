number = int(input())

while number > 1:
    if number % 4 == 0:
        number //= 4
    else:
        print(True)
        break
else:
    print(False)