def printFn(n):
    value = 0
    if n == 2 :
       value = 2
    elif n == 1:
        value = 1
    elif n > 2: 
        value = printFn(n - 1) + printFn(n - 2)
    return value

for x in range(10):
    print(printFn(x), end=' ')


