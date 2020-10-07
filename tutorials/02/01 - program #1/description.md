# Four

Máme program [four.py](four.py):

```python
number = int(input())

while number > 1:
    if number % 4 == 0:
        number //= 4
    else:
        print(True)
        break
else:
    print(False)
```


1. Pro jaká čísla (uvažujeme jenom přirozená) vypíše program `True`?
2. Nalezněte funkce vyjadřující počet porovnání v:
   
   ```python 
   while number > 1:
    ``` 
    1. v nejhorším případě
    2. v nejlepším případě
