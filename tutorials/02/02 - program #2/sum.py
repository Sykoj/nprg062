number = int(input())

sum = 0
i = 1

while i < number:
    for j in range(i):
        sum += j
    i *= 2

print(i)