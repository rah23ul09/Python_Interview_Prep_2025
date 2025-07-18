fib, a, b = 9, 0, 1

for i in range(0, fib+1):
    print(a, end=" ")
    a, b = b, a + b

