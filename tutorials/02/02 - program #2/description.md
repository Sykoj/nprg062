# Sum

Máme program [sum.py](sum.py):

```python
number = int(input())

sum = 0
i = 1

while i < number:
    for j in range(i):
        sum += j
    i *= 2

print(i)
```

1. Asymptoticky odhadněte složitost programu.
2. Když změníme `range(i)` na `range(n)`, jak se změní odhad?
